How to Use Mistune
==================

Mistune is super easy to use. Here is how you can convert Markdown formatted
text into HTML::

    import mistune

    mistune2.html(YOUR_MARKDOWN_TEXT)

The ``.html()`` methods has enabled all the features you might want
by default:

* No escape of HTML tags
* With **strikethough** plugin
* With **table** plugin
* With **footnote** plugin

Customize Mistune
-----------------

Mistune provides a function to create Markdown instance easily::

    import mistune

    markdown = mistune2.create_markdown()

This method will create a "escaped" Markdown instance without any plugins,
which means::

    markdown('<div>hello</div>')
    # ==>
    '<p>&lt;div&gt;hello&lt;/div&gt;</p>'

Non escaped version::

    markdown = mistune2.create_markdown(escape=False)
    markdown('<div>hello</div>')
    # ==>
    '<div>hello</div>'

Adding plugins::

    markdown = mistune2.create_markdown()
    markdown('~~s~~')
    # ==>
    '<p>~~s~~</p>'

    markdown = mistune2.create_markdown(plugins=['strikethough'])
    markdown('~~s~~')
    # ==>
    '<p><del>s</del></p>'

Find out what plugins mistune has built-in in :ref:`plugins` sections.

Customize Renderer
------------------

Mistune supports renderer feature which enables developers to customize
the output. For instance, to add code syntax highlight::

    import mistune
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import html


    class HighlightRenderer(mistune2.HTMLRenderer):
        def block_code(self, code, lang=None):
            if lang:
                lexer = get_lexer_by_name(lang, stripall=True)
                formatter = html.HtmlFormatter()
                return highlight(code, lexer, formatter)
            return '<pre><code>' + mistune2.escape(code) + '</code></pre>'

    markdown = mistune2.create_markdown(renderer=HighlightRenderer())

    print(markdown('```python\nassert 1 == 1\n```'))

In this way, we can use Pygments to highlight the fenced code.


AstRenderer
-----------

Mistune can produce AST by default with ``mistune2.AstRenderer``::

    markdown = mistune2.create_markdown(renderer=mistune2.AstRenderer())

This ``markdown`` function will generate tokens instead of HTML.
