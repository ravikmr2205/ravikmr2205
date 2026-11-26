"""Build the standalone GitHub Pages copy of the invitation into ../docs.

The claude.ai artifacts (index.html, classic.html here) are page fragments;
GitHub Pages needs full HTML documents, so this wraps them, copies the photos
and music, and writes the four #pyaarkaPR invitation links as their own pages.
Run from the repository root:  python3 wedding-invitation/build_site.py
To build the pyaarkapr.github.io site:  python3 wedding-invitation/build_site.py pyaarkapr <path to its checkout>
"""
import pathlib, shutil, sys

src = pathlib.Path(__file__).parent
PYAARKAPR = len(sys.argv) > 1 and sys.argv[1] == "pyaarkapr"
if PYAARKAPR:
    SITE = "https://pyaarkapr.github.io/"
    out = pathlib.Path(sys.argv[2])
else:
    SITE = "https://ravikmr2205.github.io/ravikmr2205/"
    out = src.parent / "docs"
out.mkdir(exist_ok=True)

# The four guest links: folder name -> (side, functions shown, page title)
PFX = "" if PYAARKAPR else "pyaarkaPR-"
LINKS = {
    PFX + "groom":         ("groom", "all",   "Ravi & Priyanshi Shubh Vivah"),
    PFX + "groom-shaadi":  ("groom", "shadi", "Ravi & Priyanshi Shubh Vivah"),
    PFX + "bride":         ("bride", "all",   "Priyanshi & Ravi Shubh Vivah"),
    PFX + "bride-shaadi":  ("bride", "shadi", "Priyanshi & Ravi Shubh Vivah"),
}


def wrap(page, extra_head=""):
    cut = page.index("<style>")
    meta, body = page[:cut], page[cut:]  # title, meta and font links go in <head>
    head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
            + extra_head + meta + '</head>\n<body>\n')
    return head + body + "\n</body>\n</html>\n"


if PYAARKAPR:  # the bare address shows the groom-side invitation
    (out / "index.html").write_text(wrap((src / "classic.html").read_text(encoding="utf-8")), encoding="utf-8")
else:
    for name in ("index.html", "classic.html"):
        (out / name).write_text(wrap((src / name).read_text(encoding="utf-8")), encoding="utf-8")

classic = (src / "classic.html").read_text(encoding="utf-8")
for folder, (side, mode, title) in LINKS.items():
    names = "Priyanshi & Ravi" if side == "bride" else "Ravi & Priyanshi"
    dates = "Wednesday, 24 February 2027" if mode == "shadi" else "23 & 24 February 2027"
    head = (f'<base href="../">\n'
            f'<script>window.INVITE = {{ side: "{side}", mode: "{mode}" }};</script>\n'
            f'<meta property="og:title" content="{names} · #pyaarkaPR">\n'
            f'<meta property="og:description" content="You are invited · {dates} · Vasundhara, Ghaziabad">\n'
            f'<meta property="og:image" content="{SITE}images/couple-waist.jpg">\n'
            f'<meta property="og:url" content="{SITE}{folder}/">\n'
            f'<meta property="og:type" content="website">\n')
    page = classic.replace("<title>Ravi & Priyanshi Shubh Vivah</title>", f"<title>{title}</title>", 1)
    d = out / folder
    d.mkdir(exist_ok=True)
    (d / "index.html").write_text(wrap(page, head), encoding="utf-8")

if PYAARKAPR:  # only the files the classic invitation uses
    (out / "images").mkdir(exist_ok=True)
    for f in ("couple-waist.jpg", "ganesh-gold.png"):
        shutil.copy(src / "images" / f, out / "images" / f)
else:
    shutil.copytree(src / "images", out / "images", dirs_exist_ok=True)
shutil.copytree(src / "music", out / "music", dirs_exist_ok=True)
(out / ".nojekyll").write_text("")
print("Built", out, ":", ", ".join([f + "/" for f in LINKS]))
