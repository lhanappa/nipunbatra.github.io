import sys

notebook_file = sys.argv[1]

from nbconvert import HTMLExporter
import nbformat

html_exporter = HTMLExporter()
#html_exporter.template_file = 'basic'

nb = nbformat.reads(open(notebook_file, 'r').read(), as_version=4)

(body, resources) = html_exporter.from_notebook_node(nb)

read_navbar = open("navbar.txt", 'r').read()
read_disqus = open("disqus.txt", 'r').read()
read_css = open("bootstrap_css.txt", 'r').read()
read_ga = open("google_analytics.txt","r").read()

if read_navbar not in body:
	body = body.replace("<body>", "<body>\n" + read_navbar)

if read_ga not in body:
	body = body.replace("</body>", read_ga + "\n</body>")

if read_disqus not in body:
	body = body.replace("</body>", read_disqus + "\n</body>")

if read_css not in body:
	body = body.replace("</title>", "</title>\n" + read_css)
	body = body.replace("</body>", read_css + "\n</body>")

#body = body.replace(" rendered_html", "")
body = body.replace(".rendered_html{overflow-x:auto" , ".rendered_html{overflow-x:auto;overflow-y: hidden;")
body = body.replace("#notebook{font-size:14px;line-height:20px;", "#notebook{font-size:20px;line-height:29px;")
body = body.replace("div.text_cell_render{outline:0;resize:none;width:inherit;border-style:none;padding:.5em .5em .5em .4em;color:#000;",
                    "div.text_cell_render{outline:0;resize:none;width:inherit;border-style:none;padding:.5em .5em .5em .4em;color:#777;")

html_file = notebook_file.replace(".ipynb", ".html")
html_file_writer = open(html_file, 'w')
html_file_writer.write(body)
html_file_writer.close()
