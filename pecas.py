# -*- coding: utf-8 -*-
"""Conjunto de peças Merida, embutido na página.

Merida, de Armando Hernandez Marroquin, sob GPLv2+. Os arquivos vieram do
repositório do Lichess (public/piece/merida). A licença exige crédito e que a
mesma licença acompanhe a obra — a página traz os dois no rodapé.

Duas coisas precisam ser tratadas ao juntar os doze arquivos num documento só:

1. IDs. Cada SVG declara gradientes com ids curtos ("a", "b"...). Juntos, os
   ids colidem e uma peça passa a usar o gradiente de outra. Por isso cada
   arquivo recebe um prefixo próprio nos ids e nas referências url(#...).

2. Escala. NÃO renormalizo peça por peça: o autor já desenhou as doze num
   mesmo sistema de coordenadas, com as alturas relativas e a linha de base
   coerentes entre si. Reenquadrar cada uma destruiria isso. Em vez disso
   meço a caixa da UNIÃO das doze e aplico a MESMA viewBox a todas, o que
   centraliza o conjunto inteiro preservando as proporções originais.
"""
import pathlib
import re

BASE = pathlib.Path(__file__).parent / "sets" / "merida"

ORDEM = ["K", "Q", "R", "B", "N", "P"]
CORES = ["w", "b"]

CREDITO = ("Peças: conjunto <em>Merida</em>, de Armando Hernandez Marroquin, "
           "sob licença GPLv2+.")

# viewBox comum às doze peças, medida da união das caixas reais.
# Recalcular com medir_pecas.py se o conjunto mudar.
VIEWBOX = "1.430 1.746 47.089 47.089"


def _corpo(nome):
    """Conteúdo interno do SVG, com os ids isolados por um prefixo."""
    txt = (BASE / f"{nome}.svg").read_text(encoding="utf-8")
    txt = re.sub(r"^.*?<svg[^>]*>", "", txt, count=1, flags=re.S)
    txt = re.sub(r"</svg>\s*$", "", txt, flags=re.S)
    ids = set(re.findall(r'\bid="([^"]+)"', txt))
    for i in sorted(ids, key=len, reverse=True):
        txt = txt.replace(f'id="{i}"', f'id="{nome}-{i}"')
        txt = txt.replace(f"url(#{i})", f"url(#{nome}-{i})")
        txt = txt.replace(f'href="#{i}"', f'href="#{nome}-{i}"')
    return txt


def nomes():
    return [c + k for k in ORDEM for c in CORES]


def symbols(viewbox=None):
    vb = viewbox or VIEWBOX
    out = ['<svg width="0" height="0" style="position:absolute" '
           'aria-hidden="true" focusable="false">']
    for n in nomes():
        out.append(f'<symbol id="pc-{n}" viewBox="{vb}">{_corpo(n)}</symbol>')
    out.append("</svg>")
    return "".join(out)
