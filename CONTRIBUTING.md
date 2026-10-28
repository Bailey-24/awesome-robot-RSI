# Contributing

This collection follows robot recursive self-improvement: execution feedback must lead to a persistent change in policies, code, reusable skills, memory, curricula, or agent harnesses. A one-off robot demonstration or a general agent that never retains improvements is not enough for the methods list.

## Add or update a paper

Edit `data/catalogue.json`, the single source for the README and website. Include:

- Exact title and **first public release date** from the paper's submission history. July–October 2026 is the initial focus. Later revisions do not change the first release date. The two explicitly requested June seed papers have `foundational: true`.
- A short original summary, an explicit feedback → update → evaluation loop, experimental setting, and a concise evidence/limitation statement. Distinguish simulation from physical experiments and author-reported results from independent reproduction.
- Verified official Paper and, when released, Code links. Add Data and Models only for real corresponding releases, not project pages or promises. Omit missing links.
- A real main method or overview figure, saved under `assets/papers/`, with descriptive alt text, original source URL, and author credit. Use the original figure rather than a PDF cover, a generated illustration, or an unrelated robot photo. Preserve its license and attribution.
- Primary sources for dates, methods, and results. Keep summaries concise; do not copy abstracts.

The build presents Paper and Code first, then available Data and Models, followed by Project. Avoid collapsible summaries or “Details & sources” text.

## Leaderboard snapshots

Record the benchmark, track, ordering metric, check date, official update date, and source with every snapshot. RoboDojo Score and Success Rate are separate metrics. Preserve official names and values; do not infer a research paper or RSI mechanism from a high leaderboard rank. Keep baseline/system rows distinct from the paper collection.

## Validate and build

From the repository root:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 website/build.py
git diff --check
```

Commit the generated README along with the JSON and assets. `website/dist/` is generated and is deployed by GitHub Actions; do not commit it.

## Attribution

This collection was initially curated from [Awesome-Robot-Use-Agent](https://github.com/kairunwen/Awesome-Robot-Use-Agent), by Kairun Wen, then checked against primary sources. Its MIT license is retained in `LICENSE`. Paper figures remain attributed to their original authors and retain their original licenses; the repository's MIT license does not relicense those figures.
