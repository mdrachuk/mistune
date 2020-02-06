import mistune2
from unittest import TestCase


class TestMiscCases(TestCase):
    def test_none(self):
        self.assertEqual(mistune2.html(None), '')

    def test_before_parse_hooks(self):
        def _add_name(md, s, state):
            state['name'] = 'test'
            return s, state

        md = mistune2.create_markdown()
        md.before_parse_hooks.append(_add_name)
        state = {}
        md.parse('', state)
        self.assertEqual(state['name'], 'test')

    def test_escape_html(self):
        md = mistune2.create_markdown(escape=True)
        result = md('<div>1</div>')
        expected = '<p>&lt;div&gt;1&lt;/div&gt;</p>'
        self.assertEqual(result.strip(), expected)

        result = md('<em>1</em>')
        expected = '<p>&lt;em&gt;1&lt;/em&gt;</p>'
        self.assertEqual(result.strip(), expected)

    def test_emphasis(self):
        md = mistune2.create_markdown(escape=True)
        result = md('_em_ **strong**')
        expected = '<p><em>em</em> <strong>strong</strong></p>'
        self.assertEqual(result.strip(), expected)

    def test_allow_harmful_protocols(self):
        renderer = mistune2.HTMLRenderer(allow_harmful_protocols=True)
        md = mistune2.Markdown(renderer)
        result = md('[h](javascript:alert)')
        expected = '<p><a href="javascript:alert">h</a></p>'
        self.assertEqual(result.strip(), expected)

    def test_allow_data_protocols(self):
        renderer = mistune2.HTMLRenderer(allow_harmful_protocols=['data:'])
        md = mistune2.Markdown(renderer)
        result = md('[h](data:alert)')
        expected = '<p><a href="data:alert">h</a></p>'
        self.assertEqual(result.strip(), expected)

    def test_use_plugin(self):
        from mistune2.plugins import plugin_url
        md = mistune2.Markdown(mistune2.HTMLRenderer())
        md.use(plugin_url)
