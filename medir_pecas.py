# -*- coding: utf-8 -*-
"""Mede a caixa da UNIÃO das doze peças e reescreve VIEWBOX em pecas.py.

A união, e não peça a peça: o conjunto já vem com as proporções e a linha de
base coerentes entre as peças, e reenquadrar cada uma isoladamente destruiria
isso. Medindo a união e aplicando a mesma viewBox a todas, o conjunto inteiro
fica centrado na casa e as relações internas ficam intactas.
"""
import importlib, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import pecas
importlib.reload(pecas)
from playwright.sync_api import sync_playwright

FOLGA = 0.6   # respiro em unidades da viewBox original


def main():
    doc = "<!doctype html><html><body>" + pecas.symbols("0 0 50 50")
    for n in pecas.nomes():
        doc += (f'<svg width="300" height="300" viewBox="0 0 50 50">'
                f'<g id="g{n}"><use href="#pc-{n}"/></g></svg>')
    doc += "</body></html>"
    tmp = pathlib.Path(__file__).parent / "_bbox.html"
    tmp.write_text(doc, encoding="utf-8")

    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = b.new_page()
        pg.goto("file://" + str(tmp.resolve()))
        pg.wait_for_timeout(600)
        bb = pg.evaluate("""(ns) => Object.fromEntries(ns.map(n => {
            const g = document.getElementById('g'+n).getBBox();
            return [n, {x:g.x, y:g.y, w:g.width, h:g.height}];
        }))""", pecas.nomes())
        b.close()
    tmp.unlink()

    x0 = min(g["x"] for g in bb.values())
    y0 = min(g["y"] for g in bb.values())
    x1 = max(g["x"] + g["w"] for g in bb.values())
    y1 = max(g["y"] + g["h"] for g in bb.values())
    for n in pecas.nomes():
        g = bb[n]
        print(f"  {n}: {g['w']:5.2f} x {g['h']:5.2f}")
    print(f"união: x {x0:.2f}..{x1:.2f}   y {y0:.2f}..{y1:.2f}")

    lado = max(x1 - x0, y1 - y0) + 2 * FOLGA
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = f"{cx-lado/2:.3f} {cy-lado/2:.3f} {lado:.3f} {lado:.3f}"
    print("viewBox comum:", vb)

    src = pathlib.Path(pecas.__file__).read_text(encoding="utf-8")
    src = re.sub(r'VIEWBOX = "[^"]*"', f'VIEWBOX = "{vb}"', src)
    pathlib.Path(pecas.__file__).write_text(src, encoding="utf-8")
    print("VIEWBOX atualizado em pecas.py")


if __name__ == "__main__":
    main()
