"""Check the shared catalogue and visible resource/figure contracts."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('catalogue_build', ROOT / 'website/build.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def fixture():
    return {
        'title': 'awesome-robot-RSI', 'description': 'Robot self-improvement research.',
        'updated_at': '2026-10-28', 'cutoff': '2026-07-01',
        'repository': 'https://github.com/researcher/awesome-robot-RSI',
        'papers': [{
            'id': 'test-paper', 'title': 'Test <method>', 'date': '2026-10-20',
            'category': 'Code & harness evolution', 'summary': 'Diagnose & retain useful revisions.',
            'loop': 'Execute → revise → evaluate', 'setting': 'Simulation',
            'evidence': 'Author-reported results.',
            'links': {'paper': 'https://example.org/paper', 'code': 'https://example.org/code'},
            'figure': {'path': 'assets/papers/test.svg', 'alt': 'Method diagram',
                       'source': 'https://example.org/figure', 'credit': 'Test paper authors'},
            'sources': ['https://example.org/paper'],
        }],
    }


class RendererTests(unittest.TestCase):
    def test_resources_have_explicit_rows_and_missing_links_are_omitted(self):
        data = fixture()
        card = builder.render_paper(data['papers'][0])
        self.assertIn('primary-resources', card)
        self.assertNotIn('secondary-resources', card)
        self.assertNotIn('>Data<', card)
        self.assertNotIn('>Models<', card)
        self.assertLess(card.index('>Paper<'), card.index('>Code<'))
        data['papers'][0]['links'].update(data='https://example.org/data', models='https://example.org/models')
        card = builder.render_paper(data['papers'][0])
        self.assertLess(card.index('primary-resources'), card.index('secondary-resources'))
        self.assertLess(card.index('>Code<'), card.index('>Data<'))
        self.assertLess(card.index('>Data<'), card.index('>Models<'))

    def test_plain_visible_summary_figure_credit_and_escaping(self):
        data = fixture()
        page = builder.render_html(data)
        readme = builder.render_readme(data)
        self.assertNotIn('<details', page)
        self.assertNotIn('Details &amp; sources', page)
        self.assertNotIn('>Citation<', page)
        self.assertIn('Test &lt;method&gt;', page)
        self.assertIn('Diagnose &amp; retain', page)
        self.assertIn('assets/papers/test.svg', page)
        self.assertIn('Test paper authors', readme)
        self.assertIn('https://researcher.github.io/awesome-robot-RSI/', readme)
        self.assertEqual(page.count('class="paper-card"'), readme.count('### Test <method>'))
        self.assertNotIn('↗', page)
        data['papers'][0]['date_note'] = 'Technical report date; the project was announced on 2026-10-17.'
        page = builder.render_html(data)
        readme = builder.render_readme(data)
        self.assertIn('Report released 2026-10-20', page)
        self.assertIn('**Report released:** 2026-10-20', readme)
        self.assertIn(data['papers'][0]['date_note'], page)
        self.assertIn(data['papers'][0]['date_note'], readme)

    def test_schema_rejects_unsafe_figures_duplicates_links_and_unmarked_old_dates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'assets/papers').mkdir(parents=True)
            (root / 'assets/papers/test.svg').write_text('<svg/>')
            builder.validate_catalogue(fixture(), root)
            for mutate in (
                lambda d: d['papers'][0]['figure'].update(path='../outside.svg'),
                lambda d: d['papers'][0]['links'].update(code='javascript:alert(1)'),
                lambda d: d['papers'][0].update(date='2026-06-18'),
                lambda d: d['papers'][0].update(date='2026-02-30'),
                lambda d: d['papers'][0].update(date='2026-11-01'),
                lambda d: d['papers'].append(copy.deepcopy(d['papers'][0])),
            ):
                with self.subTest(mutate=mutate):
                    data = fixture()
                    mutate(data)
                    with self.assertRaises(ValueError):
                        builder.validate_catalogue(data, root)
            data = fixture()
            data['papers'][0].update(date='2026-06-18', foundational=True, updated='2026-09-20')
            builder.validate_catalogue(data, root)
            self.assertIn('Revised 2026-09-20', builder.render_html(data))

    def test_leaderboard_keeps_metrics_numeric_and_ranks_distinct(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'assets/papers').mkdir(parents=True)
            (root / 'assets/papers/test.svg').write_text('<svg/>')
            data = fixture()
            data['leaderboard'] = {
                'source': 'https://example.org/board', 'checked_at': '2026-10-28',
                'rows': [{'rank': 1, 'name': 'Agent', 'score': 61.9, 'success_rate': 56.42}],
            }
            builder.validate_catalogue(data, root)
            for metric in ('score', 'success_rate'):
                for invalid in ('61.9%', 101, -1, True):
                    broken = copy.deepcopy(data)
                    broken['leaderboard']['rows'][0][metric] = invalid
                    with self.assertRaises(ValueError):
                        builder.validate_catalogue(broken, root)
            data['leaderboard']['rows'].append(copy.deepcopy(data['leaderboard']['rows'][0]))
            with self.assertRaises(ValueError):
                builder.validate_catalogue(data, root)

    def test_repository_catalogue_has_figures_and_matching_generated_content(self):
        path = ROOT / 'data/catalogue.json'
        if not path.exists():
            self.skipTest('Catalogue research is not yet present')
        data = builder.validate_catalogue(json.loads(path.read_text(encoding='utf-8')), ROOT)
        page = builder.render_html(data)
        readme = builder.render_readme(data)
        self.assertEqual(len(data['papers']), page.count('class="paper-card"'))
        for paper in data['papers']:
            self.assertIn(f'### {paper["title"]}', readme)
            self.assertIn(paper['figure']['path'], page)
            self.assertIn(paper['figure']['path'], readme)
            self.assertIn(paper['links']['paper'], readme)
        self.assertNotIn('<details', page)


if __name__ == '__main__':
    unittest.main()
