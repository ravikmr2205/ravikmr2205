"""Build the standalone GitHub Pages copy of the invitation into ../docs.

The claude.ai artifact (index.html here) is a page fragment; GitHub Pages
needs a full HTML document, so this wraps it and copies the photos.
Run from the repository root:  python3 wedding-invitation/build_site.py
"""
import pathlib, shutil

src = pathlib.Path(__file__).parent
out = src.parent / "docs"
out.mkdir(exist_ok=True)
page = (src / "index.html").read_text(encoding="utf-8")
cut = page.index("<style>")
meta, body = page[:cut], page[cut:]  # title, meta and font links go in <head>
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        + meta + '</head>\n<body>\n')
(out / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
shutil.copytree(src / "images", out / "images", dirs_exist_ok=True)
(out / ".nojekyll").write_text("")
print("Built", out / "index.html")
