"""Build the README and dependency-free website from the same verified catalogue."""
from __future__ import annotations

import argparse
from datetime import date
import html
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_NAMES = {"paper": "Paper", "code": "Code", "project": "Project", "data": "Data", "models": "Models"}


def esc(value):
    return html.escape(str(value), quote=True)


def text(value):
    """Research fields may contain several short evidence statements."""
    return "; ".join(str(item) for item in value) if isinstance(value, list) else str(value or "")


def valid_url(value):
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username


def validate_catalogue(data, root=ROOT):
    for field in ("title", "description", "updated_at", "cutoff", "repository", "papers"):
        if not data.get(field):
            raise ValueError(f"Missing catalogue field: {field}")
    if not valid_url(data["repository"]):
        raise ValueError("Repository must be an HTTPS URL")
    checked_date = date.fromisoformat(data['updated_at'])
    cutoff = date.fromisoformat(data['cutoff'])
    seen = set()
    excluded = {item['id'] for item in data.get('excluded_papers', [])}
    for paper in data["papers"]:
        for field in ("id", "title", "date", "category", "summary", "loop", "setting", "evidence", "links", "figure"):
            if not paper.get(field):
                raise ValueError(f"Missing {field} for {paper.get('id', 'paper')}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", paper["id"]) or paper["id"] in seen:
            raise ValueError("Paper IDs must be unique URL-safe slugs")
        if paper['id'] in excluded:
            raise ValueError(f"Paper explicitly excluded by curator: {paper['id']}")
        seen.add(paper["id"])
        if not re.fullmatch(r"\d{4}-\d{2}(?:-\d{2})?", paper["date"]):
            raise ValueError(f"Invalid release date: {paper['date']}")
        released = date.fromisoformat(paper['date'] + ('-01' if len(paper['date']) == 7 else ''))
        if released > checked_date:
            raise ValueError(f"Release date is after the catalogue check: {paper['id']}")
        if paper.get('updated'):
            revised = date.fromisoformat(paper['updated'])
            if revised < released or revised > checked_date:
                raise ValueError(f"Revision date is outside the checked release interval: {paper['id']}")
        if released < cutoff and not paper.get("foundational"):
            raise ValueError(f"Pre-cutoff paper must be marked foundational: {paper['id']}")
        if not paper["links"].get("paper"):
            raise ValueError(f"Paper URL required: {paper['id']}")
        for url in paper["links"].values():
            if url and not valid_url(url):
                raise ValueError(f"Invalid resource URL: {paper['id']}")
        figure = paper["figure"]
        if not all(figure.get(key) for key in ("path", "alt", "source", "credit")):
            raise ValueError(f"Figure needs path, alt, source and credit: {paper['id']}")
        relative = Path(figure["path"])
        target = (root / relative).resolve()
        if relative.is_absolute() or not target.is_relative_to(root.resolve()) or not target.is_file():
            raise ValueError(f"Missing or unsafe figure: {figure['path']}")
        if not valid_url(figure["source"]):
            raise ValueError(f"Figure source must be HTTPS: {paper['id']}")
    board = data.get("leaderboard", {})
    if board.get("rows") and (not board.get("source") or not board.get("checked_at")):
        raise ValueError("Leaderboard needs a source and checked date")
    if board.get('rows'):
        if not valid_url(board['source']) or date.fromisoformat(board['checked_at']) > checked_date:
            raise ValueError('Leaderboard source or check date is invalid')
        ranks = set()
        for row in board['rows']:
            rank = row.get('rank')
            if type(rank) is not int or rank < 1 or rank in ranks:
                raise ValueError('Leaderboard ranks must be unique positive integers')
            ranks.add(rank)
            for metric in ('score', 'success_rate'):
                value = row.get(metric)
                if type(value) not in (int, float) or not 0 <= value <= 100:
                    raise ValueError(f'Leaderboard {metric} must be numeric in [0, 100]')
            if not row.get('name') or any(not valid_url(url) for url in row.get('links', {}).values() if url):
                raise ValueError('Leaderboard name or resource link is invalid')
    return data


def ordered_papers(data):
    return sorted(data["papers"], key=lambda paper: paper["date"], reverse=True)


def release_label(paper):
    return 'Report released' if 'report date' in paper.get('date_note', '').lower() else 'First release'


def resource_links(links, keys, css=""):
    return "".join(f'<a class="resource {css}" href="{esc(links[key])}"><span>{RESOURCE_NAMES[key]}</span><span aria-hidden="true">→</span></a>'
                   for key in keys if links.get(key))


def leaderboard_note(paper, board):
    for row in (board or {}).get('rows', []):
        if row.get('links', {}).get('paper') == paper['links'].get('paper'):
            return f"RoboDojo-Sim Agent #{row['rank']} · Score {row['score']:.2f} · Success {row['success_rate']:.2f}% ({board['checked_at']})."
    return ''


def render_paper(paper, board=None):
    figure = paper["figure"]
    note = leaderboard_note(paper, board)
    rank_html = f' <a class="inline-ranking" href="{esc(board["source"])}">{esc(note)}</a>' if note else ''
    foundational = '<span class="tag foundation">Foundation</span>' if paper.get("foundational") else ""
    primary = resource_links(paper["links"], ("paper", "code"), "primary-resource")
    secondary = resource_links(paper["links"], ("data", "models"))
    project = f'<a class="project-link" href="{esc(paper["links"]["project"])}">Project page →</a>' if paper["links"].get("project") else ""
    revised = f'<span class="revision">Revised {esc(paper["updated"])}</span>' if paper.get('updated') else ''
    date_note = f'<p class="date-note">{esc(paper["date_note"])}</p>' if paper.get('date_note') else ''
    date_text = f'{release_label(paper)} {paper["date"]}' if paper.get('date_note') else paper['date']
    return f'''<article class="paper-card" id="{esc(paper['id'])}" data-category="{esc(paper['category'])}" data-date="{esc(paper['date'])}" data-code="{'true' if paper['links'].get('code') else 'false'}">
  <figure class="paper-figure"><a href="{esc(figure['source'])}" aria-label="View original figure for {esc(paper['title'])}"><img src="{esc(figure['path'])}" alt="{esc(figure['alt'])}" loading="lazy" decoding="async"></a><figcaption>{esc(figure['credit'])} · <a href="{esc(figure['source'])}">Figure source →</a></figcaption></figure>
  <div class="paper-content"><div class="paper-meta"><time datetime="{esc(paper['date'])}">{esc(date_text)}</time>{revised}<span class="tag">{esc(paper['category'])}</span>{foundational}</div>{date_note}
  <h3><a href="{esc(paper['links']['paper'])}">{esc(paper['title'])}</a></h3><p class="paper-summary">{esc(paper['summary'])}{rank_html}</p>
  <nav class="resources" aria-label="Resources for {esc(paper['title'])}"><div class="primary-resources">{primary}</div>{f'<div class="secondary-resources">{secondary}</div>' if secondary else ''}{project}</nav></div>
</article>'''


def render_html(data):
    papers = ordered_papers(data)
    categories = list(dict.fromkeys(paper["category"] for paper in papers))
    h2_count = sum(not paper.get("foundational") for paper in papers)
    nav = ''.join(f'<button type="button" data-category="{esc(category)}" aria-pressed="false"><span>{esc(category)}</span><span>{sum(p["category"] == category for p in papers)}</span></button>' for category in categories)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{esc(data['description'])}"><meta name="color-scheme" content="light"><title>{esc(data['title'])} · Robot Recursive Self-Improvement</title><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='24' fill='%23e45735'/%3E%3Ctext x='50' y='66' text-anchor='middle' font-family='monospace' font-size='50' fill='white'%3E↻%3C/text%3E%3C/svg%3E"><link rel="stylesheet" href="style.css"><script src="app.js" defer></script></head>
<body><a class="skip-link" href="#papers">Skip to papers</a><header class="topbar shell"><a class="brand" href="#top"><span class="brand-icon" aria-hidden="true">↻</span> awesome-robot-RSI</a><nav aria-label="Main navigation"><a href="#papers">Papers</a><a href="https://robodojo-benchmark.com/leaderboard?bench=sim#agent">RoboDojo →</a><a href="{esc(data['repository'])}">GitHub →</a></nav></header>
<main id="top"><section class="hero shell"><p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> A focused reading list · Updated {esc(data['updated_at'])}</p><h1>Robots that learn<br>to <em>improve themselves.</em></h1><p class="hero-description">{esc(data['description'])}</p><div class="hero-bottom"><p><strong>{len(papers)}</strong> selected works <span>·</span> <strong>{h2_count}</strong> from H2 2026 <span>·</span> Paper → experiment → improvement</p><a class="hero-link" href="#papers">Explore the collection <span aria-hidden="true">↓</span></a></div><div class="loop-strip" aria-label="The self-improvement cycle"><span><b>01</b> Act &amp; observe</span><span aria-hidden="true">→</span><span><b>02</b> Diagnose &amp; revise</span><span aria-hidden="true">→</span><span><b>03</b> Evaluate &amp; retain</span><span class="loop-return" aria-hidden="true">↻</span></div></section>
<div class="catalogue shell" id="papers"><aside class="sidebar"><div class="sidebar-inner"><p class="eyebrow">The collection</p><h2>Follow the loop.</h2><p class="scope-note">Recent papers, newest first.</p><nav class="category-nav enhanced-control" aria-label="Filter by research area" hidden><button type="button" data-category="all" aria-pressed="true"><span>All papers</span><span>{len(papers)}</span></button>{nav}</nav><a class="sidebar-source" href="{esc(data['repository'])}/blob/main/CONTRIBUTING.md">Suggest a paper →</a></div></aside>
<section class="paper-list" aria-label="Selected papers"><div class="search-controls enhanced-control" hidden><label class="search-field"><span aria-hidden="true">⌕</span><span class="sr-only">Search papers</span><input id="search" type="search" maxlength="300" placeholder="Search papers, methods, settings…" autocomplete="off"><kbd>/</kbd></label><div class="filter-row"><label class="code-toggle"><input type="checkbox" id="code-only"> Code available</label><label class="sort-label">Sort <select id="sort"><option value="newest">Newest first</option><option value="oldest">Oldest first</option></select></label><button class="reset-button" id="reset" type="button">Reset</button></div></div><p class="results-count" id="result-count" role="status" aria-live="polite">{len(papers)} papers · all research areas</p><noscript><p class="notice">All papers are readable below. Enable JavaScript to search and filter.</p></noscript><p class="empty-state" id="empty" hidden>No papers match these filters. Try another term or reset the collection.</p><div id="paper-cards">{''.join(render_paper(paper, data.get('leaderboard')) for paper in papers)}</div></section></div>
</main>
<footer><div class="shell footer-inner"><div><a class="footer-brand" href="#top">awesome-robot-RSI <span aria-hidden="true">↻</span></a><p>A living reading list for robot recursive self-improvement.</p></div><nav aria-label="Footer"><a href="{esc(data['repository'])}">Source &amp; contributions →</a><a href="https://github.com/kairunwen/Awesome-Robot-Use-Agent">Original collection →</a><a href="#top">Back to top ↑</a></nav></div><p class="shell credits">Curated from Awesome Robot Use Agent and verified primary sources. Code: MIT. Paper figures retain their authors’ rights.</p></footer></body></html>'''


def md_escape(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_readme(data):
    papers = ordered_papers(data)
    owner, repository = urlparse(data['repository']).path.strip('/').split('/')[:2]
    pages_url = f'https://{owner}.github.io/{repository}/'
    out = [f'# {data["title"]}', '', data['description'], '',
           f'[Website]({pages_url}) · [Contributing](CONTRIBUTING.md)', '', '## Papers', '']
    for paper in papers:
        figure = paper['figure']
        out += [f'### {paper["title"]}', '', f'**{release_label(paper)}:** {paper["date"]}', '']
        if paper.get('date_note'):
            out += [paper['date_note'], '']
        out += [f'![{figure["alt"]}]({figure["path"]})', '',
                f'*{figure["credit"].rstrip(".")}. [Figure source]({figure["source"]}).*', '', paper['summary'], '']
        note = leaderboard_note(paper, data.get('leaderboard'))
        if note:
            out[-2] += f" [{note}]({data['leaderboard']['source']})"
        links = paper['links']
        out += [' · '.join(f'[{RESOURCE_NAMES[key]}]({links[key]})' for key in ('paper', 'code') if links.get(key)), '']
        extras = ' · '.join(f'[{RESOURCE_NAMES[key]}]({links[key]})' for key in ('data', 'models', 'project') if links.get(key))
        if extras:
            out += [extras, '']
    out += ['', '## Development', '',
            'See [build and deployment instructions](docs/使用与部署.md). Edit `data/catalogue.json`, then run `python3 website/build.py` to update the README and website.', '',
            '## Attribution', '',
            'Based on [Awesome Robot Use Agent](https://github.com/kairunwen/Awesome-Robot-Use-Agent) by Kairun Wen. [MIT license](LICENSE). Figures retain their original licenses; see [credits](assets/ATTRIBUTION.md).', '',
            '<!-- Generated by website/build.py from data/catalogue.json. -->', '']
    return '\n'.join(out)


def build(root=ROOT):
    data = validate_catalogue(json.loads((root / 'data/catalogue.json').read_text(encoding='utf-8')), root)
    output = root / 'website/dist'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'index.html').write_text(render_html(data), encoding='utf-8')
    (root / 'README.md').write_text(render_readme(data), encoding='utf-8')
    for name in ('app.js', 'style.css'):
        shutil.copy2(root / 'website' / name, output / name)
    if (output / 'assets').exists():
        shutil.rmtree(output / 'assets')
    shutil.copytree(root / 'assets', output / 'assets')
    (output / '.nojekyll').touch()
    print(f'Built {len(data["papers"])} papers → {output / "index.html"} and README.md')
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    build()
