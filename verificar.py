# -*- coding: utf-8 -*-
"""Verificação objetiva das posições e linhas do capítulo.

1. Legalidade de cada FEN e de cada lance de cada linha (python-chess).
2. Stockfish 19 avalia cada posição (profundidade padrão 20, ver DEPTH
   abaixo). Para rei+peão contra rei o Stockfish consulta a sua bitbase
   KPK interna, que é exata (não é heurística).
3. Checagem lance a lance: depois de cada lance da linha principal o
   resultado objetivo tem que continuar sendo o declarado. É isso que
   pega uma linha "quase certa".
"""
import sys, os, json, shutil
import chess, chess.engine

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from dados import CAPITULO


def localizar_stockfish():
    """Acha o binário do Stockfish sem precisar editar este arquivo a cada
    máquina. Ordem de busca: variável de ambiente STOCKFISH_PATH -> PATH do
    sistema -> alguns caminhos comuns no Windows/Linux."""
    env = os.environ.get("STOCKFISH_PATH")
    if env and os.path.isfile(env):
        return env
    achado = shutil.which("stockfish") or shutil.which("stockfish.exe")
    if achado:
        return achado
    candidatos = [
        r"C:\Stockfish\stockfish.exe",
        r"C:\Program Files\Stockfish\stockfish.exe",
        "/usr/games/stockfish",
        "/usr/local/bin/stockfish",
    ]
    for c in candidatos:
        if os.path.isfile(c):
            return c
    raise FileNotFoundError(
        "Stockfish não encontrado. Instale e garanta que 'stockfish' esteja "
        "no PATH, ou defina a variável de ambiente STOCKFISH_PATH apontando "
        "para o executável (ex.: set STOCKFISH_PATH=C:\\Stockfish\\stockfish.exe "
        "no Windows)."
    )


SF = localizar_stockfish()

# Profundidade padrão: 20 já é sobra para estes finais (poucas peças, sem
# meio-jogo complexo; K+P vs K é resolvido de forma exata pela bitbase KPK
# interna do Stockfish independente da profundidade). Para uma posição
# específica que pareça "em cima do muro", aumente só ali, adicionando
# "profundidade": 40 (ou o valor que quiser) no dicionário da posição em
# dados.py — não precisa mexer aqui nem afetar as outras posições.
DEPTH = 20


def classify(info):
    sc = info["score"].pov(chess.WHITE)
    if sc.is_mate():
        return ("Brancas ganham" if sc.mate() > 0 else "Pretas ganham"), f"M{sc.mate()}"
    v = sc.score()
    if abs(v) < 60:
        return "Empate", f"{v}cp"
    return ("Brancas ganham" if v > 0 else "Pretas ganham"), f"{v}cp"


def contar_posicoes():
    total = 0
    for sec in CAPITULO["secoes"]:
        for fin in sec["finais"]:
            total += len(fin["posicoes"])
            ep = fin.get("exemplo_pratico")
            if ep:
                total += len(ep["posicoes"])
    return total


def main():
    total = contar_posicoes()
    print(f"Verificando {total} posições com Stockfish (profundidade padrão {DEPTH},"
          f" pode variar por posição) — cada linha aparece assim que termina;"
          f" pode levar alguns minutos no total.")
    print(f"Motor: {SF}")
    engine = chess.engine.SimpleEngine.popen_uci(SF)
    engine.configure({"Threads": 4, "Hash": 256})

    relatorio, problemas = [], []
    contador = [0]

    def avaliar(board, profundidade=DEPTH):
        return classify(engine.analyse(board, chess.engine.Limit(depth=profundidade)))

    def imprimir_item(it):
        marca = "FALHA" if it["erros"] else "  ok "
        prof = f" (d={it['profundidade']})" if "profundidade" in it else ""
        print(f"{marca} [{contador[0]}/{total}] {it['contexto'][:30]:30s} "
              f"{it['rotulo'][:26]:26s} decl={it['esperado']:16s} "
              f"sf={it.get('sf','?')} {it.get('sf_bruto','')}{prof}", flush=True)
        for e in it["erros"]:
            print(f"       !! {e}", flush=True)

    def checar(pos, contexto):
        contador[0] += 1
        fen = pos["fen"]
        esperado = pos["resultado"]
        profundidade = pos.get("profundidade", DEPTH)
        item = {"contexto": contexto, "rotulo": pos["rotulo"], "fen": fen,
                "esperado": esperado, "erros": []}
        if profundidade != DEPTH:
            item["profundidade"] = profundidade
        board = chess.Board(fen)
        if not board.is_valid():
            item["erros"].append("FEN não representa posição legal")
            problemas.append(item); relatorio.append(item); imprimir_item(item); return

        veredito, bruto = avaliar(board, profundidade)
        item["sf"] = veredito
        item["sf_bruto"] = bruto
        alvo = "Empate" if esperado == "Empate teórico" else esperado
        if veredito != alvo:
            item["erros"].append(f"Stockfish diz '{veredito}' ({bruto}), declarado '{esperado}'")

        b = chess.Board(fen)
        fens = [b.fen()]
        sans = []
        for i, san in enumerate(pos.get("linha", [])):
            try:
                mv = b.parse_san(san)
            except Exception as e:
                item["erros"].append(f"lance {i+1} '{san}' ILEGAL ({e})")
                break
            sans.append(b.san(mv))
            b.push(mv)
            fens.append(b.fen())
            if b.is_game_over():
                break
            v2, r2 = avaliar(b, profundidade)
            if v2 != alvo:
                item["erros"].append(f"após {i+1}.{san} o resultado vira '{v2}' ({r2})")
        item["fens"] = fens
        item["sans"] = sans
        item["final"] = ("mate" if b.is_checkmate() else
                         "afogamento" if b.is_stalemate() else
                         "promocao" if len(sans) and sans[-1].find("=") >= 0 else "")

        for alt in pos.get("alternativas", []):
            b2 = chess.Board(fen)
            afens, asans = [b2.fen()], []
            for i, san in enumerate(alt["linha"]):
                try:
                    mv = b2.parse_san(san)
                except Exception as e:
                    item["erros"].append(f"[alternativa] lance {i+1} '{san}' ILEGAL ({e})")
                    break
                asans.append(b2.san(mv)); b2.push(mv); afens.append(b2.fen())
            alt["fens"] = afens
            alt["sans"] = asans
            alt["final"] = "afogamento" if b2.is_stalemate() else ("mate" if b2.is_checkmate() else "")

        if item["erros"]:
            problemas.append(item)
        relatorio.append(item)
        imprimir_item(item)

    print("=" * 78, flush=True)
    for sec in CAPITULO["secoes"]:
        for fin in sec["finais"]:
            for pos in fin["posicoes"]:
                checar(pos, f"F{fin['n']} {fin['titulo']}")
            ep = fin.get("exemplo_pratico")
            if ep:
                for pos in ep["posicoes"]:
                    checar(pos, f"F{fin['n']} {ep['titulo']}")

    engine.quit()

    print("=" * 78)
    print(f"{len(relatorio)} posições verificadas — {len(problemas)} com problema")

    with open(os.path.join(BASE, "verificacao.json"), "w") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
