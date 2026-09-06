# -*- coding: utf-8 -*-
"""Verificação objetiva das posições e linhas do capítulo.

1. Legalidade de cada FEN e de cada lance de cada linha (python-chess).
2. Stockfish 16 avalia cada posição. Para rei+peão contra rei o Stockfish
   consulta a sua bitbase KPK interna, que é exata (não é heurística).
3. Checagem lance a lance: depois de cada lance da linha principal o
   resultado objetivo tem que continuar sendo o declarado. É isso que
   pega uma linha "quase certa".
"""
import sys, os, json
import chess, chess.engine

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from dados import CAPITULO

SF = "/usr/games/stockfish"
DEPTH = 34


def classify(info):
    sc = info["score"].pov(chess.WHITE)
    if sc.is_mate():
        return ("Brancas ganham" if sc.mate() > 0 else "Pretas ganham"), f"M{sc.mate()}"
    v = sc.score()
    if abs(v) < 60:
        return "Empate", f"{v}cp"
    return ("Brancas ganham" if v > 0 else "Pretas ganham"), f"{v}cp"


def main():
    engine = chess.engine.SimpleEngine.popen_uci(SF)
    engine.configure({"Threads": 4, "Hash": 256})

    relatorio, problemas = [], []

    def avaliar(board):
        return classify(engine.analyse(board, chess.engine.Limit(depth=DEPTH)))

    def checar(pos, contexto):
        fen = pos["fen"]
        esperado = pos["resultado"]
        item = {"contexto": contexto, "rotulo": pos["rotulo"], "fen": fen,
                "esperado": esperado, "erros": []}
        board = chess.Board(fen)
        if not board.is_valid():
            item["erros"].append("FEN não representa posição legal")
            problemas.append(item); relatorio.append(item); return

        veredito, bruto = avaliar(board)
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
            v2, r2 = avaliar(b)
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
    for it in relatorio:
        marca = "FALHA" if it["erros"] else "  ok "
        print(f"{marca} {it['contexto'][:30]:30s} {it['rotulo'][:26]:26s} "
              f"decl={it['esperado']:16s} sf={it.get('sf','?')} {it.get('sf_bruto','')}")
        for e in it["erros"]:
            print(f"       !! {e}")
    print("=" * 78)
    print(f"{len(relatorio)} posições verificadas — {len(problemas)} com problema")

    with open(os.path.join(BASE, "verificacao.json"), "w") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
