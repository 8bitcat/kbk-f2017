"""Bygger index.html (fristående sida) från artefakt-källan på Skrivbordet.
Kör:  python bygg.py   (från D:\GamesProjects\kbk-f2017)
"""
import pathlib
SRC = pathlib.Path(r"C:/Users/palss/Desktop/KBK F2017 stödmedlem/index.html")
OUT = pathlib.Path(__file__).with_name("index.html")
BASE = "https://8bitcat.github.io/kbk-f2017/"
body = SRC.read_text(encoding="utf8").replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
assert 'content="bilder/lagposter.jpg"' in body
body = body.replace('content="bilder/lagposter.jpg"', 'content="' + BASE + 'bilder/lagposter.jpg"')
body = body.replace('<meta property="og:type" content="website">',
    '<meta property="og:type" content="website">\n<meta property="og:url" content="' + BASE + '">\n<meta name="twitter:card" content="summary_large_image">')
i = body.index('<header class="hero">')
head = ('<!doctype html>\n<html lang="sv">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
out = (head + body[:i] + '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
       + body[i:] + '\n</body>\n</html>\n')
OUT.write_text(out, encoding="utf8", newline="\n")
print("skrev", OUT, len(out), "bytes")
