# -*- coding: utf-8 -*-
"""Gera a página HTML do capítulo a partir de dados.py.
Todas as sequências de lances são pré-calculadas aqui (python-chess),
então a página não precisa de nenhuma biblioteca de xadrez no navegador.
"""
import sys, os, json, html, re, urllib.parse
import chess

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from dados import CAPITULO, DIAGRAMAS
from pecas import symbols as pecas_symbols, CREDITO as PECAS_CREDITO


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


def build_positions():
    dados = []
    ordem = []
    for sec in CAPITULO["secoes"]:
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


def render():
    build_positions()
    store = {}
    body = []

    # ---------------------------------------------------------------- sumário
    body.append('<nav class="toc" aria-label="Sumário">')
    body.append('<h2 class="toc-title">Sumário</h2>')
    for sec in CAPITULO["secoes"]:
        body.append(f'<div class="toc-sec"><a class="toc-sec-link" href="#{sec["id"]}">{html.escape(sec["titulo"])}</a><ol class="toc-list">')
        for fin in sec["finais"]:
            body.append(f'<li><a href="#final-{fin["n"]}"><span class="toc-n">{fin["n"]:02d}</span>'
                        f'<span class="toc-t">{html.escape(fin["titulo"])}</span>'
                        f'<span class="toc-c">{html.escape(fin["conceito"])}</span></a></li>')
        body.append('</ol></div>')
    body.append('</nav>')

    # ---------------------------------------------------------------- seções
    for sec in CAPITULO["secoes"]:
        body.append(f'<section class="sec" id="{sec["id"]}">')
        body.append(f'<header class="sec-head"><h2>{html.escape(sec["titulo"])}</h2>'
                    f'<p class="sec-resumo">{html.escape(sec["resumo"])}</p></header>')
        for fin in sec["finais"]:
            body.append(f'<article class="final" id="final-{fin["n"]}">')
            body.append(f'<h3 class="final-h"><span class="final-n">Final {fin["n"]:02d}</span>'
                        f'<span class="final-t">{html.escape(fin["titulo"])}</span></h3>')
            body.append(f'<p class="final-c">{html.escape(fin["conceito"])}</p>')
            for p in fin["texto"]:
                body.append(f'<p>{md(p)}</p>')
            for pos in fin["posicoes"]:
                body.append(render_pos(pos, store))
            body.append('<div class="regras"><h4>Para memorizar</h4><ul>')
            for r in fin["regras"]:
                body.append(f'<li>{md(r)}</li>')
            body.append('</ul></div>')
            ep = fin.get("exemplo_pratico")
            if ep:
                body.append(f'<div class="exemplo"><h4>{html.escape(ep["titulo"])}</h4>')
                for p in ep["texto"]:
                    body.append(f'<p>{md(p)}</p>')
                for pos in ep["posicoes"]:
                    body.append(render_pos(pos, store))
                body.append(f'<p class="exemplo-fecho">{md(ep["fecho"])}</p>')
                body.append('</div>')
            body.append('</article>')
        body.append('</section>')

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
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -14px rgba(0,0,0,.7);
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:var(--f-body);font-size:17px;line-height:1.62;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:52rem;margin:0 auto;padding:0 1.5rem 6rem}
p{margin:0 0 1.05em}
/* texto corrido justificado, com hifenização para evitar rios de espaço */
.dek,.sec-resumo,.final>p,.exemplo>p,.exemplo-fecho,.regras li,.foot p,.rule-inline,.note{
  text-align:justify;text-justify:inter-word;
  hyphens:auto;-webkit-hyphens:auto;hyphenate-limit-chars:6 3 3}
/* a nota fica numa coluna estreita: hifeniza mais cedo para não abrir vãos */
.note{hyphenate-limit-chars:5 2 2}
/* títulos, subtítulos e rótulos também justificados, mas sem hifenizar —
   quebrar palavra em título fica ruim. Em título de uma linha só a
   justificação não muda nada: o CSS nunca estica a última linha. */
h1,.eyebrow,.sec-head h2,.final-c,.toc-title,.toc-sec-link,.toc-c,
.regras h4,.exemplo h4,.foot h4,.board-label{
  text-align:justify;text-justify:inter-word;hyphens:manual;-webkit-hyphens:manual}
strong{font-weight:600;color:var(--ink)}
em{font-style:italic}
a{color:var(--accent)}

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

/* ---------- sumário ---------- */
.toc{margin:2.6rem 0 3.4rem;border-top:2px solid var(--ink);padding-top:1.1rem}
.toc-title{font-family:var(--f-mono);font-size:.7rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--ink-3);margin:0 0 1.2rem;font-weight:500}
.toc-sec{margin-bottom:1.5rem}
.toc-sec-link{display:block;font-family:var(--f-disp);font-weight:600;font-size:1rem;
  color:var(--ink);text-decoration:none;padding-bottom:.4rem;border-bottom:1px solid var(--line-soft)}
.toc-sec-link:hover{color:var(--accent)}
.toc-list{list-style:none;margin:.5rem 0 0;padding:0;display:flex;flex-direction:column}
.toc-list a{display:grid;grid-template-columns:2.6rem 1fr;gap:0 .6rem;
  padding:.42rem 0;text-decoration:none;color:var(--ink);
  border-bottom:1px solid var(--line-soft)}
.toc-list li:last-child a{border-bottom:0}
.toc-list a:hover{color:var(--accent)}
.toc-n{font-family:var(--f-mono);font-size:.78rem;color:var(--ink-3);
  font-variant-numeric:tabular-nums;padding-top:.15rem}
.toc-t{font-weight:600;font-size:.98rem}
.toc-c{grid-column:2;font-size:.86rem;color:var(--ink-3);line-height:1.4}

/* ---------- seções ---------- */
.sec{margin-top:4rem}
.sec-head{border-top:2px solid var(--ink);padding-top:1rem;margin-bottom:2.2rem}
.sec-head h2{font-family:var(--f-disp);font-weight:700;font-size:1.75rem;
  margin:0 0 .5rem;letter-spacing:-.01em}
.sec-resumo{color:var(--ink-2);margin:0}
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
  background:none;border:1px dashed var(--line);border-radius:2px;color:var(--ink-2);cursor:pointer}
.alt-btn[aria-pressed="true"]{background:var(--accent-soft);border-style:solid;color:var(--ink)}
.alt-btn:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.rule-inline{margin:0;padding:.75rem .9rem;border-top:1px solid var(--line);
  background:var(--ochre-soft);font-size:.93rem;color:var(--ink)}

/* ---------- regras / exemplo ---------- */
.regras{margin:1.6rem 0 0;padding:1.1rem 1.2rem;background:var(--paper-2);
  border-left:3px solid var(--ochre);border-radius:0 3px 3px 0}
.regras h4{font-family:var(--f-mono);font-size:.68rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-3);margin:0 0 .6rem;font-weight:500}
.regras ul{margin:0;padding-left:1.1rem;display:flex;flex-direction:column;gap:.4rem}
.regras li{font-size:.96rem;line-height:1.5}
.exemplo{margin-top:2rem;padding-top:1.4rem;border-top:1px solid var(--line)}
.exemplo h4{font-family:var(--f-disp);font-size:1.1rem;margin:0 0 .8rem;font-weight:600}
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
    top = f"""{pecas_symbols()}
<header class="masthead" lang="pt-BR"><div class="masthead-in">
<p class="eyebrow">Capítulo {CAPITULO['numero']} · Estudo de finais</p>
<h1>{html.escape(CAPITULO['titulo'])}</h1>
<p class="dek">{html.escape(CAPITULO['intro'])}</p>
<div class="meta">
<span class="chip">9 finais</span>
<span class="chip">23 posições</span>
<span class="chip chip-ok">Verificado por Stockfish&nbsp;16</span>
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
<p>Cada tabuleiro traz o número do diagrama correspondente no livro, para conferência lado a lado.
Onde há dois números, o segundo é uma posição que aparece dentro da mesma linha de lances — avance
os lances para chegar nela.</p>
<p>As posições vieram dos diagramas do capítulo; os textos e as linhas de análise foram escritos
para esta página. Cada uma das 23 posições foi avaliada pelo Stockfish 16 em profundidade 34, e
cada lance das linhas principais foi reavaliado individualmente para confirmar que o resultado
objetivo não muda no caminho. Nos finais de rei e peão contra rei o Stockfish consulta a sua
bitbase interna de KPK, que é exaustiva — não é estimativa.</p>
<p>Quatro erros foram encontrados e corrigidos nesse processo: dois lances ilegais transcritos dos
diagramas, um lance de torre que na verdade era de rei, e uma posição que só é legal com as pretas
a jogar. Nenhum deles sobreviveu à checagem.</p>
<h4>Créditos</h4>
<p>{PECAS_CREDITO} O texto da licença está em
<a href="https://www.gnu.org/licenses/gpl-2.0.txt">gnu.org/licenses/gpl-2.0.txt</a>.</p>
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
        b.textContent = alt.titulo;
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
</script>
"""
    out = HTML_TOP + top

    # finais.html — só o conteúdo, para publicar como Artifact (a plataforma
    # acrescenta o invólucro <html>/<head>/<body> na publicação).
    with open(os.path.join(BASE, "finais.html"), "w", encoding="utf-8") as f:
        f.write(out)

    # index.html — documento completo, para hospedar em qualquer lugar
    # (GitHub Pages, por exemplo). Mesmo conteúdo, com o invólucro incluído.
    completo = (
        '<!doctype html>\n<html lang="pt-BR">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<meta name="description" content="Capítulo 1 de um estudo de finais de '
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
