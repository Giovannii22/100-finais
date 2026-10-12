# -*- coding: utf-8 -*-
"""Gera a página HTML do livro (múltiplos capítulos) a partir de dados.py.
Todas as sequências de lances são pré-calculadas aqui (python-chess),
então a página não precisa de nenhuma biblioteca de xadrez no navegador.
"""
import sys, os, json, html, re, urllib.parse
import chess

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from dados import CAPITULOS, DIAGRAMAS
from pecas import symbols as pecas_symbols, CREDITO as PECAS_CREDITO

# Versao publicada (git tag correspondente). Atualizar manualmente a cada release.
VERSAO = "v1.0.6"


def expandir(pos):
    b = chess.Board(pos["fen"])
    fens, sans = [b.fen()], []
    for san in pos.get("linha", []):
        mv = b.parse_san(san)
        sans.append(b.san(mv))
        b.push(mv)
        fens.append(b.fen())
    fim = ""
    if b.is_checkmate():
        fim = "mate"
    elif b.is_stalemate():
        fim = "afogamento"
    return fens, sans, fim


def expandir_alt(fen, linha):
    b = chess.Board(fen)
    fens, sans = [b.fen()], []
    for san in linha:
        mv = b.parse_san(san)
        sans.append(b.san(mv))
        b.push(mv)
        fens.append(b.fen())
    fim = "afogamento" if b.is_stalemate() else ("mate" if b.is_checkmate() else "")
    return fens, sans, fim


def md(t):
    """**x** -> negrito, *x* -> itálico. O negrito vem primeiro, senão o
    asterisco simples consumiria metade do par duplo."""
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    if "*" in t:
        raise ValueError(f"asterisco solto sobrou no texto: {t[:90]}")
    return t


def cap_anchor(cap):
    return f"cap-{cap['numero']}"


def sec_anchor(cap, sec):
    return f"sec-{cap['numero']}-{sec['id']}"


def build_positions():
    """Percorre TODOS os capítulos, na ordem de CAPITULOS, e prepara cada
    posição para renderização. A ordem de visita tem que bater exatamente
    com a ordem de DIAGRAMAS (lista única, compartilhada entre capítulos)."""
    dados = []
    ordem = []
    for cap in CAPITULOS:
        for sec in cap["secoes"]:
            for fin in sec["finais"]:
                grupos = [(fin["posicoes"], None)]
                ep = fin.get("exemplo_pratico")
                if ep:
                    grupos.append((ep["posicoes"], ep))
                for lista, _ in grupos:
                    for pos in lista:
                        fens, sans, fim = expandir(pos)
                        pos["_fens"], pos["_sans"], pos["_fim"] = fens, sans, fim
                        for alt in pos.get("alternativas", []):
                            af, asn, afim = expandir_alt(pos["fen"], alt["linha"])
                            alt["_fens"], alt["_sans"], alt["_fim"] = af, asn, afim
                        ordem.append(pos)
    if len(ordem) != len(DIAGRAMAS):
        raise ValueError(
            f"{len(ordem)} posições mas {len(DIAGRAMAS)} referências de diagrama")
    for pos, ref in zip(ordem, DIAGRAMAS):
        pos["_diag"] = ref
    return dados


def contar_totais():
    """Totais globais (todos os capítulos) para os chips e o rodapé."""
    n_finais = 0
    n_posicoes = 0
    for cap in CAPITULOS:
        for sec in cap["secoes"]:
            for fin in sec["finais"]:
                n_finais += 1
                n_posicoes += len(fin["posicoes"])
                ep = fin.get("exemplo_pratico")
                if ep:
                    n_posicoes += len(ep["posicoes"])
    return n_finais, n_posicoes


PID = [0]


def pos_payload(pos):
    PID[0] += 1
    pid = f"p{PID[0]}"
    payload = {
        "id": pid,
        "fens": pos["_fens"],
        "sans": pos["_sans"],
        "fim": pos["_fim"],
        "notas": {str(k): md(v) for k, v in pos.get("notas", {}).items()},
        "marcas": pos.get("marcas", {}),
        "marcasDesde": pos.get("marcas_desde", 0),
        "marcasAte": pos.get("marcas_ate", 999),
        "alts": [
            {"titulo": a["titulo"], "fens": a["_fens"], "sans": a["_sans"],
             "fim": a["_fim"], "nota": md(a.get("nota", ""))}
            for a in pos.get("alternativas", [])
        ],
    }
    return pid, payload


def render_pos(pos, payload_store):
    pid, payload = pos_payload(pos)
    payload_store[pid] = payload
    res = pos["resultado"]
    marca = {"Brancas ganham": "1–0", "Pretas ganham": "0–1",
             "Empate": "½–½", "Empate teórico": "½–½"}.get(res, "")
    cls = "res-win" if "ganham" in res else "res-draw"
    legenda = pos.get("legenda_marcas", "")
    destaque = pos.get("regra_destaque", "")

    out = [f'<figure class="board-block" id="{pid}" data-pos="{pid}">']
    out.append('<figcaption class="board-head">')
    out.append('<span class="head-left">')
    ref = pos.get("_diag")
    if ref:
        pref = "Diagrama " if not ref.startswith("análise") else "Diagrama de "
        out.append(f'<span class="diag-ref" title="Referência ao diagrama do livro">'
                   f'{pref}{html.escape(ref)}</span>')
    out.append(f'<span class="board-label">{html.escape(pos["rotulo"])}</span>')
    out.append('</span>')
    out.append(f'<span class="result {cls}"><span class="res-mark">{marca}</span>{html.escape(res)}</span>')
    out.append('</figcaption>')
    out.append('<div class="board-body">')
    out.append('<div class="board-col">')
    out.append(f'<div class="board" role="img" aria-label="Diagrama de xadrez"></div>')
    if legenda:
        out.append(f'<p class="board-legend">{html.escape(legenda)}</p>')
    out.append('</div>')
    out.append('<div class="play-col">')
    out.append('<div class="controls">'
               '<button type="button" class="ctl" data-act="start" aria-label="Posição inicial">⏮</button>'
               '<button type="button" class="ctl" data-act="prev" aria-label="Lance anterior">◀</button>'
               '<button type="button" class="ctl" data-act="next" aria-label="Próximo lance">▶</button>'
               '<button type="button" class="ctl" data-act="end" aria-label="Posição final">⏭</button>'
               '</div>')
    out.append('<ol class="moves"></ol>')
    out.append('<p class="note"></p>')
    out.append('</div></div>')
    if destaque:
        out.append(f'<p class="rule-inline">{md(destaque)}</p>')
    out.append('</figure>')
    return "\n".join(out)


# Seta discreta usada tanto no sumário ("ir até o capítulo/tema") quanto como
# marcador customizado de abrir/fechar dos <details> (girar via CSS).
_CHEVRON = ('<svg class="chev" viewBox="0 0 24 24" width="13" height="13" fill="none" '
            'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true" focusable="false">'
            '<path d="M9 5l7 7-7 7"/></svg>')


def render():
    build_positions()
    store = {}
    body = []

    # ---------------------------------------------------------------- sumário
    body.append('<nav class="toc" aria-label="Sumário">')
    body.append('<h2 class="toc-title">Sumário</h2>')
    body.append('<div class="search-box">'
                '<input type="search" id="busca" aria-label="Buscar nos finais" '
                'placeholder="Buscar nos finais… (ex.: cavalo, afogamento)">'
                '<p class="search-info" id="busca-info" hidden></p>'
                '</div>')
    for cap in CAPITULOS:
        body.append(f'<details class="toc-cap">')
        body.append(f'<summary class="toc-cap-head">{_CHEVRON}'
                    f'<span class="toc-cap-title">Capítulo {cap["numero"]} · '
                    f'{html.escape(cap["titulo"])}</span>'
                    f'<a class="toc-goto" href="#{cap_anchor(cap)}" '
                    f'aria-label="Ir até o Capítulo {cap["numero"]}">Ir até ↳</a></summary>')
        body.append('<div class="toc-cap-body">')
        for sec in cap["secoes"]:
            body.append(f'<details class="toc-sec">')
            body.append(f'<summary class="toc-sec-head">{_CHEVRON}'
                        f'<span class="toc-sec-title">{html.escape(sec["titulo"])}</span>'
                        f'<a class="toc-goto" href="#{sec_anchor(cap, sec)}" '
                        f'aria-label="Ir até {html.escape(sec["titulo"])}">Ir até ↳</a></summary>')
            body.append('<ol class="toc-list">')
            for fin in sec["finais"]:
                body.append(f'<li><a href="#final-{fin["n"]}"><span class="toc-n">{fin["n"]:02d}</span>'
                            f'<span class="toc-t">{html.escape(fin["titulo"])}</span>'
                            f'<span class="toc-c">{html.escape(fin["conceito"])}</span></a></li>')
            body.append('</ol>')
            body.append('</details>')
        body.append('</div>')
        body.append('</details>')
    body.append('</nav>')

    # --------------------------------------------------------- capítulos/seções
    for cap in CAPITULOS:
        body.append(f'<details class="cap" id="{cap_anchor(cap)}">')
        body.append(f'<summary class="cap-head">{_CHEVRON}<div class="cap-head-txt">'
                    f'<h2>Capítulo {cap["numero"]} · {html.escape(cap["titulo"])}</h2>'
                    f'<p class="cap-intro">{html.escape(cap["intro"])}</p></div></summary>')
        body.append('<div class="cap-body">')
        for sec in cap["secoes"]:
            body.append(f'<details class="sec" id="{sec_anchor(cap, sec)}">')
            body.append(f'<summary class="sec-head">{_CHEVRON}<div class="sec-head-txt">'
                        f'<h3>{html.escape(sec["titulo"])}</h3>'
                        f'<p class="sec-resumo">{html.escape(sec["resumo"])}</p></div></summary>')
            body.append('<div class="sec-body">')
            for fin in sec["finais"]:
                body.append(f'<article class="final" id="final-{fin["n"]}">')
                body.append(f'<h4 class="final-h"><span class="final-n">Final {fin["n"]:02d}</span>'
                            f'<span class="final-t">{html.escape(fin["titulo"])}</span></h4>')
                body.append(f'<p class="final-c">{html.escape(fin["conceito"])}</p>')
                for p in fin["texto"]:
                    body.append(f'<p>{md(p)}</p>')
                for pos in fin["posicoes"]:
                    body.append(render_pos(pos, store))
                body.append('<div class="regras"><h5>Para memorizar</h5><ul>')
                for r in fin["regras"]:
                    body.append(f'<li>{md(r)}</li>')
                body.append('</ul></div>')
                ep = fin.get("exemplo_pratico")
                if ep:
                    body.append(f'<div class="exemplo"><h5>{html.escape(ep["titulo"])}</h5>')
                    for p in ep["texto"]:
                        body.append(f'<p>{md(p)}</p>')
                    for pos in ep["posicoes"]:
                        body.append(render_pos(pos, store))
                    body.append(f'<p class="exemplo-fecho">{md(ep["fecho"])}</p>')
                    body.append('</div>')
                body.append('</article>')
            body.append('</div>')
            body.append('</details>')
        body.append('</div>')
        body.append('</details>')

    return "\n".join(body), store


# Favicon: peão sobre o verde do tabuleiro, em SVG embutido como data URI —
# sem arquivo externo e nítido em qualquer resolução. O SVG é percent-encoded
# porque "#" numa data URI seria lido como início de âncora.
_FAV_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
    '<rect width="32" height="32" rx="6.5" fill="#6f8a70"/>'
    '<circle cx="16" cy="9.6" r="4.6" fill="#f4f2ea"/>'
    '<path d="M12.4 13.8h7.2l-1.1 3.6c2.8 1.7 4.6 4.5 4.6 7.6H8.9'
    'c0-3.1 1.8-5.9 4.6-7.6z" fill="#f4f2ea"/>'
    '<rect x="8.1" y="24.3" width="15.8" height="3.7" rx="1.7" fill="#f4f2ea"/>'
    '</svg>'
)
FAVICON = "data:image/svg+xml," + urllib.parse.quote(_FAV_SVG, safe="")

HTML_TOP = f"""<title>100 Finais de Xadrez</title>
<link rel="icon" href="{FAVICON}">""" + """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@500;600;700&family=Spectral:ital,wght@0,300;0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500;600&family=Noto+Sans+Symbols+2&display=swap">
<style>
:root{
  --ink:#171b1e; --ink-2:#3c464b; --ink-3:#6b767c;
  --paper:#f3f3f0; --paper-2:#e9e9e4; --paper-3:#dcdcd5;
  --line:#c9cac2; --line-soft:#e0e0d9;
  --accent:#2f4b7c; --accent-soft:#e4e9f2;
  --ochre:#b3801f; --ochre-soft:#f0e4c8;
  --sq-l:#eeeade; --sq-d:#84a083;
  --pc-w:#fbfbf8; --pc-w-edge:#20262a; --pc-b:#181c1f; --pc-b-edge:#e8e8e0;
  --ok:#2f6b4f;
  --mark:#efd27a; --mark-ink:#171b1e;
  --shadow:0 1px 2px rgba(23,27,30,.06),0 8px 24px -12px rgba(23,27,30,.22);
  --f-disp:"Zilla Slab",Georgia,serif;
  --f-body:"Spectral",Georgia,"Times New Roman",serif;
  --f-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
  --f-sym:"Noto Sans Symbols 2","Segoe UI Symbol","DejaVu Sans",serif;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ink:#e6e7e2; --ink-2:#b3b8b6; --ink-3:#868d8c;
    --paper:#14181b; --paper-2:#1c2126; --paper-3:#232a2f;
    --line:#333c42; --line-soft:#252c31;
    --accent:#8fb0e0; --accent-soft:#1e2836;
    --ochre:#d9ac52; --ochre-soft:#332a15;
    --sq-l:#d9d5c8; --sq-d:#6f8a70;
    --pc-w:#fbfbf6; --pc-w-edge:#15191c; --pc-b:#15191c; --pc-b-edge:#d8d8cc;
    --ok:#6fb894;
    --mark:#8a6f22; --mark-ink:#f3f3f0;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -14px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --ink:#e6e7e2; --ink-2:#b3b8b6; --ink-3:#868d8c;
  --paper:#14181b; --paper-2:#1c2126; --paper-3:#232a2f;
  --line:#333c42; --line-soft:#252c31;
  --accent:#8fb0e0; --accent-soft:#1e2836;
  --ochre:#d9ac52; --ochre-soft:#332a15;
  --sq-l:#d9d5c8; --sq-d:#6f8a70;
  --pc-w:#fbfbf6; --pc-w-edge:#15191c; --pc-b:#15191c; --pc-b-edge:#d8d8cc;
  --ok:#6fb894;
  --mark:#8a6f22; --mark-ink:#f3f3f0;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -14px rgba(0,0,0,.7);
}
/* Escolha explícita do leitor no botão da página — vence tudo acima.
   Declarado por último, então ganha por ordem em igualdade de especificidade. */
:root[data-user-theme="light"]{
  color-scheme:light;
  --ink:#171b1e; --ink-2:#3c464b; --ink-3:#6b767c;
  --paper:#f3f3f0; --paper-2:#e9e9e4; --paper-3:#dcdcd5;
  --line:#c9cac2; --line-soft:#e0e0d9;
  --accent:#2f4b7c; --accent-soft:#e4e9f2;
  --ochre:#b3801f; --ochre-soft:#f0e4c8;
  --sq-l:#eeeade; --sq-d:#84a083;
  --pc-w:#fbfbf8; --pc-w-edge:#20262a; --pc-b:#181c1f; --pc-b-edge:#e8e8e0;
  --ok:#2f6b4f;
  --mark:#efd27a; --mark-ink:#171b1e;
  --shadow:0 1px 2px rgba(23,27,30,.06),0 8px 24px -12px rgba(23,27,30,.22);
}
:root[data-user-theme="dark"]{
  color-scheme:dark;
  --ink:#e6e7e2; --ink-2:#b3b8b6; --ink-3:#868d8c;
  --paper:#14181b; --paper-2:#1c2126; --paper-3:#232a2f;
  --line:#333c42; --line-soft:#252c31;
  --accent:#8fb0e0; --accent-soft:#1e2836;
  --ochre:#d9ac52; --ochre-soft:#332a15;
  --sq-l:#d9d5c8; --sq-d:#6f8a70;
  --pc-w:#fbfbf6; --pc-w-edge:#15191c; --pc-b:#15191c; --pc-b-edge:#d8d8cc;
  --ok:#6fb894;
  --mark:#8a6f22; --mark-ink:#f3f3f0;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -14px rgba(0,0,0,.7);
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:var(--f-body);font-size:17px;line-height:1.62;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:52rem;margin:0 auto;padding:0 1.5rem 6rem}
p{margin:0 0 1.05em}
/* texto corrido justificado, com hifenização para evitar rios de espaço */
.dek,.cap-intro,.sec-resumo,.final>p,.exemplo>p,.exemplo-fecho,.regras li,.foot p,.rule-inline,.note{
  text-align:justify;text-justify:inter-word;
  hyphens:auto;-webkit-hyphens:auto;hyphenate-limit-chars:6 3 3}
/* a nota fica numa coluna estreita: hifeniza mais cedo para não abrir vãos */
.note{hyphenate-limit-chars:5 2 2}
/* títulos, subtítulos e rótulos também justificados, mas sem hifenizar —
   quebrar palavra em título fica ruim. Em título de uma linha só a
   justificação não muda nada: o CSS nunca estica a última linha. */
h1,.eyebrow,.cap-head h2,.sec-head h3,.final-c,.toc-title,.toc-cap-title,.toc-sec-title,.toc-c,
.regras h5,.exemplo h5,.foot h4,.board-label{
  text-align:justify;text-justify:inter-word;hyphens:manual;-webkit-hyphens:manual}
strong{font-weight:600;color:var(--ink)}
em{font-style:italic}
a{color:var(--accent)}
mark{background:var(--mark);color:var(--mark-ink);border-radius:1px;padding:0 .05em}

/* ---------- topo ---------- */
.masthead{border-bottom:1px solid var(--line);background:var(--paper-2)}
.masthead-in{max-width:52rem;margin:0 auto;padding:2.6rem 1.5rem 2rem;
  display:flex;flex-direction:column;gap:1rem}
.eyebrow{font-family:var(--f-mono);font-size:.7rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--ink-3);margin:0}
h1{font-family:var(--f-disp);font-weight:700;font-size:clamp(2rem,5.2vw,2.9rem);
  line-height:1.08;letter-spacing:-.015em;margin:0}
.dek{margin:0;color:var(--ink-2);font-size:1.06rem}
.meta{display:flex;flex-wrap:wrap;gap:.5rem .45rem;align-items:center;margin-top:.2rem}
.chip{font-family:var(--f-mono);font-size:.68rem;letter-spacing:.06em;
  text-transform:uppercase;padding:.3rem .55rem;border:1px solid var(--line);
  border-radius:2px;color:var(--ink-2);background:var(--paper)}
.chip-ok{color:var(--ok);border-color:color-mix(in srgb,var(--ok) 45%,var(--line))}
.meta-controls{margin-left:auto;display:flex;flex-wrap:wrap;gap:.5rem 1.1rem;align-items:center}
.seg-group{display:flex;align-items:center;gap:.4rem}
.seg-group>span:first-child{font-family:var(--f-mono);font-size:.68rem;letter-spacing:.06em;
  text-transform:uppercase;color:var(--ink-3)}
.toggle{display:inline-flex;border:1px solid var(--line);border-radius:2px;overflow:hidden}
.toggle button{font-family:var(--f-mono);font-size:.7rem;font-weight:500;
  padding:.3rem .55rem;border:0;background:var(--paper);color:var(--ink-2);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--accent);color:var(--paper)}
.toggle button:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.toggle button.icon{display:inline-flex;align-items:center;justify-content:center;
  padding:.28rem .48rem;line-height:0}
.toggle button.icon svg{display:block}

/* ---------- details/summary genéricos ---------- */
/* Base para todo <details> retrátil do projeto (sumário e conteúdo):
   marcador nativo escondido, usamos a seta própria (.chev), que gira ao abrir. */
details>summary{cursor:pointer;list-style:none}
details>summary::-webkit-details-marker{display:none}
details>summary::marker{content:""}
details>summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.chev{flex:none;color:var(--ink-3);transition:transform .15s}
details[open]>summary .chev{transform:rotate(90deg)}
.toc-goto{font-family:var(--f-mono);font-size:.72rem;letter-spacing:.03em;
  color:var(--ink-3);text-decoration:none;white-space:nowrap;padding:.15rem .4rem;
  border-radius:2px;flex:none;margin-left:auto}
.toc-goto:hover{color:var(--accent);background:var(--accent-soft)}
.toc-goto:focus-visible{outline:2px solid var(--accent);outline-offset:1px}

/* ---------- sumário ---------- */
.toc{margin:2.6rem 0 3.4rem;border-top:2px solid var(--ink);padding-top:1.1rem}
.toc-title{font-family:var(--f-mono);font-size:.7rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--ink-3);margin:0 0 1rem;font-weight:500}
.search-box{margin-bottom:1.4rem}
.search-box input{width:100%;font-family:var(--f-body);font-size:.96rem;
  padding:.55rem .75rem;border:1px solid var(--line);border-radius:2px;
  background:var(--paper);color:var(--ink)}
.search-box input::placeholder{color:var(--ink-3)}
.search-box input:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.search-info{margin:.5rem 0 0;font-family:var(--f-mono);font-size:.74rem;color:var(--ink-3)}
.toc-cap{border-bottom:1px solid var(--line-soft);padding-bottom:.9rem;margin-bottom:.9rem}
.toc-cap-head{display:flex;align-items:baseline;gap:.55rem;padding:.3rem 0}
.toc-cap-title{font-family:var(--f-disp);font-weight:700;font-size:1.1rem;color:var(--ink)}
.toc-cap-body{padding:.4rem 0 0 1.25rem;display:flex;flex-direction:column;gap:.6rem}
.toc-sec-head{display:flex;align-items:baseline;gap:.5rem;padding:.3rem 0;
  border-bottom:1px solid var(--line-soft)}
.toc-sec-title{font-family:var(--f-disp);font-weight:600;font-size:1rem;color:var(--ink)}
.toc-list{list-style:none;margin:.3rem 0 .6rem;padding:0;display:flex;flex-direction:column}
.toc-list a{display:grid;grid-template-columns:2.6rem 1fr;gap:0 .6rem;
  padding:.42rem 0;text-decoration:none;color:var(--ink);
  border-bottom:1px solid var(--line-soft)}
.toc-list li:last-child a{border-bottom:0}
.toc-list a:hover{color:var(--accent)}
.toc-n{font-family:var(--f-mono);font-size:.78rem;color:var(--ink-3);
  font-variant-numeric:tabular-nums;padding-top:.15rem}
.toc-t{font-weight:600;font-size:.98rem}
.toc-c{grid-column:2;font-size:.86rem;color:var(--ink-3);line-height:1.4}

/* ---------- capítulos/seções (conteúdo) ---------- */
.cap{margin-top:3.4rem}
.cap-head{display:flex;align-items:flex-start;gap:.6rem;border-top:3px double var(--ink);
  padding-top:1.1rem}
.cap-head h2{font-family:var(--f-disp);font-weight:700;font-size:2rem;
  margin:0 0 .4rem;letter-spacing:-.01em}
.cap-intro{color:var(--ink-2);margin:0}
.cap-head .chev{margin-top:.35rem}
.cap-body{padding-left:0}
.sec{margin-top:3rem}
.sec-head{display:flex;align-items:flex-start;gap:.55rem;border-top:2px solid var(--ink);
  padding-top:1rem;margin-bottom:0}
.sec-head h3{font-family:var(--f-disp);font-weight:700;font-size:1.75rem;
  margin:0 0 .5rem;letter-spacing:-.01em}
.sec-resumo{color:var(--ink-2);margin:0}
.sec-head .chev{margin-top:.3rem}
.sec-body{padding-top:2.2rem}
.final{margin:0 0 3.6rem;padding-top:.5rem}
.final-h{display:flex;flex-wrap:wrap;align-items:baseline;gap:.65rem;margin:2.4rem 0 .25rem}
.final-n{font-family:var(--f-mono);font-size:.72rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--paper);background:var(--ink);
  padding:.2rem .45rem;border-radius:2px}
.final-t{font-family:var(--f-disp);font-weight:700;font-size:1.4rem;letter-spacing:-.01em}
.final-c{font-family:var(--f-mono);font-size:.78rem;color:var(--ink-3);
  margin:0 0 1.3rem;letter-spacing:.01em}

/* ---------- tabuleiro ---------- */
.board-block{margin:1.8rem 0;padding:0;border:1px solid var(--line);
  border-radius:3px;background:var(--paper-2);box-shadow:var(--shadow);overflow:hidden}
.board-head{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;
  justify-content:space-between;padding:.65rem .9rem;
  border-bottom:1px solid var(--line);background:var(--paper-3)}
.head-left{display:flex;flex-wrap:wrap;align-items:center;gap:.45rem;min-width:0}
.diag-ref{font-family:var(--f-mono);font-size:.67rem;letter-spacing:.05em;
  color:var(--ink-3);border:1px solid var(--line);border-radius:2px;
  padding:.14rem .38rem;white-space:nowrap}
.board-label{font-family:var(--f-mono);font-size:.76rem;letter-spacing:.02em;color:var(--ink-2)}
.result{display:inline-flex;align-items:center;gap:.45rem;font-family:var(--f-mono);
  font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
.res-mark{font-weight:600;font-size:.8rem;letter-spacing:0;padding:.12rem .35rem;
  border-radius:2px;font-variant-numeric:tabular-nums}
.res-win .res-mark{background:var(--accent);color:var(--paper)}
.res-draw .res-mark{background:var(--paper);color:var(--ink-2);border:1px solid var(--line)}
.board-body{display:grid;grid-template-columns:minmax(0,1fr);gap:1.1rem;padding:1.1rem}
@media(min-width:41rem){.board-body{grid-template-columns:minmax(0,20rem) minmax(0,1fr);gap:1.3rem}}
.board-col{display:flex;flex-direction:column;gap:.55rem}
/* linhas E colunas em 1fr: sem isso a fila com a peça mais alta estica
   e as casas deixam de ser quadradas */
/* minmax(0,1fr) é obrigatório: com 1fr puro o mínimo da pista é o conteúdo,
   e uma peça maior que a casa faz a fila crescer — o tabuleiro deixa de ser
   quadrado. overflow:hidden garante que a proporção 1:1 seja respeitada. */
.board{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));
  grid-template-rows:repeat(8,minmax(0,1fr));
  width:100%;aspect-ratio:1;overflow:hidden;
  border:1px solid var(--pc-w-edge);background:var(--sq-l);
  user-select:none;container-type:inline-size}
.sq{position:relative;display:flex;align-items:center;justify-content:center;
  min-width:0;min-height:0;overflow:hidden}
.sq.d{background:var(--sq-d)}
/* Peças em vetor desenhadas para esta página, no padrão Staunton de diagrama.
   Cada símbolo tem a viewBox ajustada à caixa real do seu desenho, medida na
   geração — então centralizar o <svg> na casa centraliza a peça, sem depender
   de nenhuma métrica de fonte. As alturas relativas vêm do próprio desenho:
   o peão é naturalmente mais baixo que o rei. */
/* Peças do conjunto Merida (ver crédito no rodapé). As cores vêm do próprio
   desenho, então não há fill/stroke aqui. As doze compartilham a mesma
   viewBox — a caixa da união, medida na geração — o que centraliza o conjunto
   na casa e preserva as proporções que o autor definiu entre as peças. */
.pc{width:82%;height:82%;display:block}
.sq.mk::after{content:"";position:absolute;inset:0;
  box-shadow:inset 0 0 0 3px var(--ochre);pointer-events:none}
.sq.mk-critica::before{content:"";position:absolute;width:26%;aspect-ratio:1;
  border-radius:50%;background:var(--ochre);opacity:.85}
.sq.mk-critica .pc{position:relative}
.sq.from,.sq.to{background-image:linear-gradient(color-mix(in srgb,var(--accent) 26%,transparent),
  color-mix(in srgb,var(--accent) 26%,transparent))}
.sq .coord{position:absolute;font-family:var(--f-mono);font-size:.55rem;
  color:rgba(20,24,26,.5);letter-spacing:0;line-height:1;pointer-events:none}
.sq.d .coord{color:rgba(255,255,255,.72)}
.sq .coord.f{right:3px;bottom:2px}
.sq .coord.r{left:3px;top:2px}
.board-legend{margin:0;font-family:var(--f-mono);font-size:.68rem;color:var(--ink-3);
  display:flex;align-items:center;gap:.4rem}
.board-legend::before{content:"";width:.6rem;height:.6rem;border-radius:50%;
  background:var(--ochre);flex:none}

/* ---------- controles e lances ---------- */
.play-col{display:flex;flex-direction:column;gap:.75rem;min-width:0}
/* quatro colunas iguais: os botões têm exatamente a mesma largura */
.controls{display:grid;grid-template-columns:repeat(4,1fr);gap:.3rem}
.ctl{font-family:var(--f-sym);font-size:.85rem;padding:.45rem .3rem;
  background:var(--paper);color:var(--ink-2);border:1px solid var(--line);
  border-radius:2px;cursor:pointer;transition:background .12s,color .12s}
.ctl:hover:not(:disabled){background:var(--accent);color:var(--paper);border-color:var(--accent)}
.ctl:disabled{opacity:.35;cursor:default}
.ctl:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.moves{list-style:none;margin:0;padding:.55rem .6rem;display:flex;flex-wrap:wrap;
  gap:.15rem .3rem;background:var(--paper);border:1px solid var(--line-soft);
  border-radius:2px;font-family:var(--f-mono);font-size:.82rem;min-height:2.6rem;
  align-content:flex-start;max-height:11rem;overflow-y:auto}
.mv-n{color:var(--ink-3);font-variant-numeric:tabular-nums;padding:.1rem 0 .1rem .18rem}
.mv{cursor:pointer;padding:.1rem .28rem;border-radius:2px;color:var(--ink);
  background:none;border:0;font:inherit}
.mv:hover{background:var(--accent-soft)}
.mv[aria-current="true"]{background:var(--accent);color:var(--paper);font-weight:500}
.mv:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.mv-end{font-family:var(--f-mono);font-size:.72rem;color:var(--ink-3);
  padding:.1rem .28rem;letter-spacing:.04em}
.note{margin:0;font-size:.94rem;line-height:1.55;color:var(--ink-2);min-height:1.4em}
.note:empty::before{content:"Use ▶ para percorrer a solução.";color:var(--ink-3);font-style:italic}
.alt-wrap{display:flex;flex-direction:column;gap:.3rem;margin-top:.1rem}
.alt-btn{font-family:var(--f-mono);font-size:.7rem;text-align:left;padding:.35rem .5rem;
  background:var(--paper);border:1px dashed var(--ink-3);border-radius:2px;color:var(--ink);cursor:pointer}
.alt-btn:hover{border-color:var(--accent);color:var(--accent)}
.alt-btn[aria-pressed="true"]{background:var(--accent);border-style:solid;border-color:var(--accent);color:var(--paper)}
.alt-btn:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.rule-inline{margin:0;padding:.75rem .9rem;border-top:1px solid var(--line);
  background:var(--ochre-soft);font-size:.93rem;color:var(--ink)}

/* ---------- regras / exemplo ---------- */
.regras{margin:1.6rem 0 0;padding:1.1rem 1.2rem;background:var(--paper-2);
  border-left:3px solid var(--ochre);border-radius:0 3px 3px 0}
.regras h5{font-family:var(--f-mono);font-size:.68rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-3);margin:0 0 .6rem;font-weight:500}
.regras ul{margin:0;padding-left:1.1rem;display:flex;flex-direction:column;gap:.4rem}
.regras li{font-size:.96rem;line-height:1.5}
.exemplo{margin-top:2rem;padding-top:1.4rem;border-top:1px solid var(--line)}
.exemplo h5{font-family:var(--f-disp);font-size:1.1rem;margin:0 0 .8rem;font-weight:600}
.exemplo-fecho{font-size:.95rem;color:var(--ink-2)}

/* ---------- rodapé ---------- */
.foot{max-width:52rem;margin:0 auto;padding:2rem 1.5rem 3rem;border-top:1px solid var(--line);
  font-size:.88rem;color:var(--ink-3)}
.foot h4{font-family:var(--f-mono);font-size:.68rem;letter-spacing:.14em;
  text-transform:uppercase;margin:0 0 .6rem;font-weight:500;color:var(--ink-2)}
.foot p{margin:0 0 .7rem}
.foot code{font-family:var(--f-mono);font-size:.82em;background:var(--paper-2);
  padding:.1rem .3rem;border-radius:2px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style>
<script>
/* Aplica o tema antes do resto da página desenhar, para não piscar.
   Padrão: escuro. */
(function () {
  var t = null;
  try { t = localStorage.getItem("tema"); } catch (e) {}
  if (t !== "claro" && t !== "escuro") t = "escuro";
  document.documentElement.setAttribute("data-user-theme", t === "escuro" ? "dark" : "light");
})();
</script>
"""


def main():
    body, store = render()
    n_finais, n_posicoes = contar_totais()
    n_caps = len(CAPITULOS)
    desc_cap = (f"Capítulo {CAPITULOS[0]['numero']}" if n_caps == 1
                else f"Capítulos {CAPITULOS[0]['numero']}–{CAPITULOS[-1]['numero']}")
    top = f"""{pecas_symbols()}
<header class="masthead" lang="pt-BR"><div class="masthead-in">
<p class="eyebrow">{desc_cap} · Estudo de finais</p>
<h1>100 Finais de Xadrez</h1>
<p class="dek">Posições interativas de finais de xadrez, verificadas por engine, com análise
escrita em português.</p>
<div class="meta">
<span class="chip">{n_finais} finais</span>
<span class="chip">{n_posicoes} posições</span>
<span class="chip chip-ok">Verificado por Stockfish&nbsp;19</span>
<span class="meta-controls">
<span class="seg-group"><span>Notação</span>
<span class="toggle" role="group" aria-label="Notação">
<button type="button" data-nota="pt" aria-pressed="true">PT</button>
<button type="button" data-nota="en" aria-pressed="false">EN</button>
</span></span>
<span class="seg-group">
<span class="toggle" role="group" aria-label="Tema da página">
<button type="button" class="icon" data-tema="claro" aria-pressed="false" title="Tema claro" aria-label="Tema claro">
<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1"/><path d="M12 2.3v2.5M12 19.2v2.5M4.4 4.4l1.8 1.8M17.8 17.8l1.8 1.8M2.3 12h2.5M19.2 12h2.5M4.4 19.6l1.8-1.8M17.8 6.2l1.8-1.8"/></svg>
</button>
<button type="button" class="icon" data-tema="escuro" aria-pressed="true" title="Tema escuro" aria-label="Tema escuro">
<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M20.4 14.7A8.7 8.7 0 0 1 9.3 3.6 8.7 8.7 0 1 0 20.4 14.7Z"/></svg>
</button>
</span></span>
</span>
</div>
</div></header>
<main class="wrap" lang="pt-BR">
{body}
</main>
<footer class="foot" lang="pt-BR">
<h4>Como conferir</h4>
<p>Cada tabuleiro traz o número do diagrama correspondente no livro <em>Los 100 finales que hay
que saber</em>, de Jesús de la Villa García, para conferência lado a lado. Onde há dois números,
o segundo é uma posição que aparece dentro da mesma linha de lances — avance os lances para
chegar nela.</p>
<p>As posições vieram dos diagramas do livro; os textos e as linhas de análise foram escritos
para esta página. Cada uma das {n_posicoes} posições foi avaliada pelo Stockfish 19 em
profundidade 20, e cada lance das linhas principais foi reavaliado individualmente para
confirmar que o resultado objetivo não muda no caminho. Nos finais de rei e peão contra rei o
Stockfish consulta a sua bitbase interna de KPK, que é exaustiva — não é estimativa.</p>
<h4>Créditos</h4>
<p>Este estudo é inspirado no livro <em>Los 100 finales que hay que saber</em>, de Jesús de la
Villa García (2ª edición revisada, Esfera Editorial, 2008) — as posições seguem sua seleção e
numeração, mas os textos e análises desta página são originais. Este é um trabalho sem fins
comerciais, feito exclusivamente para fins de estudo pessoal.</p>
<p>{PECAS_CREDITO} O texto da licença está em
<a href="https://www.gnu.org/licenses/gpl-2.0.txt">gnu.org/licenses/gpl-2.0.txt</a>.</p>
<p><code>{VERSAO}</code></p>
</footer>
<script>
const DADOS = {json.dumps(store, ensure_ascii=False)};
const SVGNS = "http://www.w3.org/2000/svg";
const PT = {{K:"R",Q:"D",R:"T",B:"B",N:"C"}};
let notacao = "pt";
try {{ const s = localStorage.getItem("notacao"); if (s === "pt" || s === "en") notacao = s; }} catch (e) {{}}

function traduzir(san) {{
  if (notacao === "en") return san;
  let out = san;
  const c = out[0];
  if (PT[c] && c === c.toUpperCase() && /[KQRBN]/.test(c)) out = PT[c] + out.slice(1);
  return out.replace(/=([QRBN])/, (m, p) => "=" + PT[p]);
}}

function parseFen(fen) {{
  const board = {{}};
  const rows = fen.split(" ")[0].split("/");
  for (let r = 0; r < 8; r++) {{
    let file = 0;
    for (const ch of rows[r]) {{
      if (/\\d/.test(ch)) {{ file += parseInt(ch, 10); continue; }}
      const sq = "abcdefgh"[file] + (8 - r);
      board[sq] = ch;
      file++;
    }}
  }}
  return board;
}}

function diffSquares(a, b) {{
  if (!a || !b) return [];
  const A = parseFen(a), B = parseFen(b), out = [];
  for (const sq of new Set([...Object.keys(A), ...Object.keys(B)])) {{
    if (A[sq] !== B[sq]) out.push(sq);
  }}
  return out;
}}

function drawBoard(el, fen, marks, prevFen) {{
  const board = parseFen(fen);
  const moved = diffSquares(prevFen, fen);
  el.textContent = "";
  const frag = document.createDocumentFragment();
  for (let r = 8; r >= 1; r--) {{
    for (let f = 0; f < 8; f++) {{
      const file = "abcdefgh"[f];
      const sq = file + r;
      const cell = document.createElement("div");
      cell.className = "sq" + ((f + r) % 2 === 1 ? " d" : "");
      if (marks && marks[sq]) cell.classList.add("mk", "mk-" + marks[sq]);
      if (moved.includes(sq)) cell.classList.add("to");
      if (r === 1) {{
        const c = document.createElement("span");
        c.className = "coord f"; c.textContent = file; cell.appendChild(c);
      }}
      if (f === 0) {{
        const c = document.createElement("span");
        c.className = "coord r"; c.textContent = r; cell.appendChild(c);
      }}
      const pc = board[sq];
      if (pc) {{
        const tipo = pc.toUpperCase();
        const svg = document.createElementNS(SVGNS, "svg");
        svg.setAttribute("class", "pc");
        svg.setAttribute("aria-hidden", "true");
        svg.setAttribute("focusable", "false");
        const uso = document.createElementNS(SVGNS, "use");
        uso.setAttribute("href", "#pc-" + (pc === tipo ? "w" : "b") + tipo);
        svg.appendChild(uso);
        cell.appendChild(svg);
      }}
      frag.appendChild(cell);
    }}
  }}
  el.appendChild(frag);
}}

class Viewer {{
  constructor(root, data) {{
    this.root = root; this.data = data;
    this.line = {{ fens: data.fens, sans: data.sans, fim: data.fim, notas: data.notas }};
    this.altIndex = -1;
    this.i = 0;
    this.boardEl = root.querySelector(".board");
    this.movesEl = root.querySelector(".moves");
    this.noteEl = root.querySelector(".note");
    root.querySelectorAll(".ctl").forEach(b =>
      b.addEventListener("click", () => this.act(b.dataset.act)));
    if (data.alts && data.alts.length) {{
      const wrap = document.createElement("div");
      wrap.className = "alt-wrap";
      data.alts.forEach((alt, k) => {{
        const b = document.createElement("button");
        b.type = "button"; b.className = "alt-btn"; b.setAttribute("aria-pressed", "false");
        b.textContent = data.alts.length > 1 ? `Lance alternativo ${{k + 1}}` : "Lance alternativo";
        b.addEventListener("click", () => this.toggleAlt(k, b));
        wrap.appendChild(b);
      }});
      root.querySelector(".play-col").appendChild(wrap);
    }}
    root.tabIndex = 0;
    root.addEventListener("keydown", e => {{
      if (e.key === "ArrowRight") {{ e.preventDefault(); this.act("next"); }}
      if (e.key === "ArrowLeft") {{ e.preventDefault(); this.act("prev"); }}
    }});
    this.render();
  }}
  toggleAlt(k, btn) {{
    this.root.querySelectorAll(".alt-btn").forEach(b => b.setAttribute("aria-pressed", "false"));
    if (this.altIndex === k) {{
      this.altIndex = -1;
      this.line = {{ fens: this.data.fens, sans: this.data.sans, fim: this.data.fim, notas: this.data.notas }};
    }} else {{
      this.altIndex = k; btn.setAttribute("aria-pressed", "true");
      const a = this.data.alts[k];
      this.line = {{ fens: a.fens, sans: a.sans, fim: a.fim, notas: {{ "0": a.nota }} }};
    }}
    this.i = 0; this.render();
  }}
  act(a) {{
    const n = this.line.fens.length - 1;
    if (a === "start") this.i = 0;
    if (a === "prev") this.i = Math.max(0, this.i - 1);
    if (a === "next") this.i = Math.min(n, this.i + 1);
    if (a === "end") this.i = n;
    this.render();
  }}
  render() {{
    const marks = (this.altIndex === -1
      && this.i >= (this.data.marcasDesde || 0)
      && this.i <= (this.data.marcasAte === undefined ? 999 : this.data.marcasAte))
      ? this.data.marcas : null;
    drawBoard(this.boardEl, this.line.fens[this.i], marks, this.i > 0 ? this.line.fens[this.i - 1] : null);
    this.movesEl.textContent = "";
    const frag = document.createDocumentFragment();
    this.line.sans.forEach((san, k) => {{
      if (k % 2 === 0) {{
        const n = document.createElement("span");
        n.className = "mv-n"; n.textContent = (k / 2 + 1) + ".";
        frag.appendChild(n);
      }}
      const b = document.createElement("button");
      b.type = "button"; b.className = "mv"; b.textContent = traduzir(san);
      if (k + 1 === this.i) b.setAttribute("aria-current", "true");
      b.addEventListener("click", () => {{ this.i = k + 1; this.render(); }});
      frag.appendChild(b);
    }});
    if (this.line.fim) {{
      const e = document.createElement("span");
      e.className = "mv-end";
      e.textContent = this.line.fim === "mate" ? "— mate" : "— afogamento";
      frag.appendChild(e);
    }}
    this.movesEl.appendChild(frag);
    const nota = this.line.notas[String(this.i)];
    this.noteEl.innerHTML = nota || "";
    const n = this.line.fens.length - 1;
    this.root.querySelector('[data-act="start"]').disabled = this.i === 0;
    this.root.querySelector('[data-act="prev"]').disabled = this.i === 0;
    this.root.querySelector('[data-act="next"]').disabled = this.i === n;
    this.root.querySelector('[data-act="end"]').disabled = this.i === n;
  }}
}}

/* Centra a TINTA do glifo na casa, não a caixa de texto. Os símbolos de xadrez
   do Unicode não ocupam o eixo vertical do em de forma simétrica, e cada fonte
   de fallback faz diferente — então medimos a fonte que realmente carregou. */
const viewers = [];
document.querySelectorAll("[data-pos]").forEach(el => {{
  viewers.push(new Viewer(el, DADOS[el.dataset.pos]));
}});

document.querySelectorAll("[data-nota]").forEach(b => {{
  b.setAttribute("aria-pressed", String(b.dataset.nota === notacao));
  b.addEventListener("click", () => {{
    notacao = b.dataset.nota;
    try {{ localStorage.setItem("notacao", notacao); }} catch (e) {{}}
    document.querySelectorAll("[data-nota]").forEach(x =>
      x.setAttribute("aria-pressed", String(x.dataset.nota === notacao)));
    viewers.forEach(v => v.render());
  }});
}});

let tema = document.documentElement.getAttribute("data-user-theme") === "light" ? "claro" : "escuro";
function aplicarTema() {{
  document.documentElement.setAttribute("data-user-theme", tema === "escuro" ? "dark" : "light");
  document.querySelectorAll("[data-tema]").forEach(x =>
    x.setAttribute("aria-pressed", String(x.dataset.tema === tema)));
}}
document.querySelectorAll("[data-tema]").forEach(b => {{
  b.addEventListener("click", () => {{
    tema = b.dataset.tema;
    try {{ localStorage.setItem("tema", tema); }} catch (e) {{}}
    aplicarTema();
  }});
}});
aplicarTema();

/* ---------- sumário: título expande/retrai; botão "ir até" navega direto ---------- */
/* O link "ir até" mora dentro do <summary>; por padrão clicar nele também
   alternaria o retrátil (o clique sobe até o summary). stopPropagation()
   no clique do link evita essa alternância, deixando só a navegação nativa.
   Além disso, quando o alvo é o PRÓPRIO <details> do capítulo/tema (não um
   final lá dentro), o navegador não precisa abri-lo para revelá-lo — o
   <summary> já está visível mesmo fechado — então forçamos a abertura na
   mão, para "ir até" realmente mostrar o conteúdo, não só rolar até o
   cabeçalho fechado. (Links para um final específico não precisam disso:
   aí o alvo fica escondido dentro de <details> fechados, e o navegador já
   abre os ancestrais sozinho ao navegar para a âncora.) */
document.querySelectorAll(".toc-goto").forEach(a => {{
  a.addEventListener("click", e => {{
    e.stopPropagation();
    const alvo = document.querySelector(a.getAttribute("href"));
    if (alvo && alvo.tagName === "DETAILS") alvo.open = true;
  }});
}});

/* ---------- busca ---------- */
/* Normaliza para comparação: minúsculas e sem diacríticos (cavalo = Cavalo = cavaló). */
function normalizar(s) {{
  return (s || "").normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase();
}}
/* Para destacar o trecho encontrado no texto ORIGINAL (com acento), cada letra
   do termo vira uma classe que aceita qualquer acentuação comum em português —
   assim "cavalo" encontra e marca "Cavaló" como o mesmo trecho visualmente. */
const _ACC = {{
  a: "aàáâãä", e: "eèéêë", i: "iìíîï", o: "oòóôõö", u: "uùúûü", c: "cç", n: "nñ"
}};
function regexAcentos(termo) {{
  const esc = termo.replace(/[.*+?^${{}}()|[\\]\\\\]/g, "\\\\$&");
  const pat = esc.replace(/[aeiouÇcn]/gi, ch => {{
    const l = ch.toLowerCase();
    const classe = _ACC[l];
    return classe ? "[" + classe + classe.toUpperCase() + "]" : ch;
  }});
  return new RegExp(pat, "gi");
}}

const BUSCA_INPUT = document.getElementById("busca");
const BUSCA_INFO = document.getElementById("busca-info");
const BUSCA_CAMPOS = [".final-t", ".final-c", "p", "li"];

/* Índice: para cada final, o texto visível (título, conceito, parágrafos,
   regras) + as notas de lance (vêm de DADOS, não aparecem estáticas no HTML). */
const buscaIndex = [];
document.querySelectorAll("article.final").forEach(finalEl => {{
  let texto = finalEl.textContent;
  finalEl.querySelectorAll("[data-pos]").forEach(board => {{
    const d = DADOS[board.dataset.pos];
    if (!d) return;
    Object.values(d.notas || {{}}).forEach(n => {{ texto += " " + n.replace(/<[^>]+>/g, ""); }});
    (d.alts || []).forEach(a => {{ texto += " " + (a.nota || "").replace(/<[^>]+>/g, ""); }});
  }});
  buscaIndex.push({{
    final: finalEl,
    sec: finalEl.closest("details.sec"),
    cap: finalEl.closest("details.cap"),
    n: finalEl.id.replace("final-", ""),
    texto: normalizar(texto),
  }});
}});

/* Marca/desmarca os <li> do sumário que apontam para finais sem match. */
const tocItens = Array.from(document.querySelectorAll(".toc-list li")).map(li => ({{
  li, n: li.querySelector("a").getAttribute("href").replace("#final-", ""),
}}));

function limparDestaque(raiz) {{
  raiz.querySelectorAll("mark.busca-mk").forEach(m => {{
    m.replaceWith(document.createTextNode(m.textContent));
  }});
}}

function destacar(finalEl, termo) {{
  // Uma instância de regex NOVA a cada teste/substituição: regex com /g guarda
  // posição interna (lastIndex) entre chamadas de .test(), e reaproveitar a
  // mesma instância entre elementos diferentes faz o "cursor" vazar de um
  // texto pro outro, pulando destaques por engano.
  finalEl.querySelectorAll(".final-t, .final-c, p, li").forEach(el => {{
    if (el.closest(".moves, .note")) return; // texto dinâmico do tabuleiro, não tocar
    if (!regexAcentos(termo).test(el.textContent)) return;
    el.innerHTML = el.innerHTML.replace(regexAcentos(termo), m => `<mark class="busca-mk">${{m}}</mark>`);
  }});
}}

function buscar() {{
  const termoBruto = BUSCA_INPUT.value.trim();
  document.querySelectorAll("article.final").forEach(f => limparDestaque(f));
  if (!termoBruto) {{
    document.querySelectorAll("article.final, details.sec, details.cap").forEach(el => {{
      el.style.display = "";
    }});
    tocItens.forEach(({{ li }}) => {{ li.style.display = ""; }});
    BUSCA_INFO.hidden = true;
    return;
  }}
  const termo = normalizar(termoBruto);
  const finaisOk = new Set(), secsOk = new Set(), capsOk = new Set();
  buscaIndex.forEach(item => {{
    if (item.texto.includes(termo)) {{
      finaisOk.add(item.final);
      if (item.sec) secsOk.add(item.sec);
      if (item.cap) capsOk.add(item.cap);
    }}
  }});
  document.querySelectorAll("article.final").forEach(f => {{
    const ok = finaisOk.has(f);
    f.style.display = ok ? "" : "none";
    if (ok) destacar(f, termoBruto);
  }});
  document.querySelectorAll("details.sec").forEach(s => {{
    const ok = secsOk.has(s);
    s.style.display = ok ? "" : "none";
    if (ok) s.open = true;
  }});
  document.querySelectorAll("details.cap").forEach(c => {{
    const ok = capsOk.has(c);
    c.style.display = ok ? "" : "none";
    if (ok) c.open = true;
  }});
  tocItens.forEach(({{ li, n }}) => {{
    const match = buscaIndex.find(it => it.n === n);
    li.style.display = match && finaisOk.has(match.final) ? "" : "none";
  }});
  BUSCA_INFO.hidden = false;
  const plural = finaisOk.size !== 1;
  BUSCA_INFO.textContent = finaisOk.size === 0
    ? "Nenhum final encontrado."
    : `${{finaisOk.size}} ${{plural ? "finais" : "final"}} encontrado${{plural ? "s" : ""}}.`;
}}
if (BUSCA_INPUT) BUSCA_INPUT.addEventListener("input", buscar);
</script>
"""
    out = HTML_TOP + top

    # finais.html — só o conteúdo (não publicado em lugar nenhum atualmente;
    # mantido por simplicidade do gerador).
    with open(os.path.join(BASE, "finais.html"), "w", encoding="utf-8") as f:
        f.write(out)

    # index.html — documento completo, para hospedar em qualquer lugar
    # (GitHub Pages, por exemplo). Mesmo conteúdo, com o invólucro incluído.
    completo = (
        '<!doctype html>\n<html lang="pt-BR">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<meta name="description" content="Estudo de finais de '
        'xadrez em português, com posições interativas verificadas por engine.">\n'
        + out.replace("</style>", "</style>\n</head>\n<body>", 1)
        + "\n</body>\n</html>\n"
    )
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(completo)

    print("gerado:", len(out), "bytes (finais.html) /",
          len(completo), "bytes (index.html) /", len(store), "tabuleiros")


if __name__ == "__main__":
    main()
