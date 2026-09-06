# 100 Finais — estudo de finais de xadrez em português

Página de estudo com posições de finais navegáveis lance a lance. O capítulo 1
está pronto: 9 finais, 23 posições.

**A página publicada é o `index.html`.** Ele é autocontido: todo o CSS, o
JavaScript, os dados das posições e os desenhos das peças estão dentro do
arquivo. A única coisa externa são as fontes do Google.

## Como o projeto está organizado

| arquivo | o que é |
|---|---|
| `dados.py` | **O conteúdo.** Textos, posições em FEN, linhas de lances, notas, referências aos diagramas. É o arquivo que representa o trabalho. |
| `gerar.py` | Transforma `dados.py` na página. Pré-calcula todas as posições intermediárias, monta sumário, seções e tabuleiros. |
| `pecas.py` | Carrega o conjunto de peças e isola os `id` de cada SVG. |
| `medir_pecas.py` | Mede a caixa da união das 12 peças e grava a `viewBox` comum em `pecas.py`. Rodar só se o conjunto de peças mudar. |
| `verificar.py` | Passa cada posição e cada lance pelo Stockfish. |
| `sets/merida/` | As 12 peças, em SVG. |
| `index.html` | A página pronta, gerada. **É o que o GitHub Pages publica.** |
| `finais.html` | Mesmo conteúdo sem o invólucro `<html>`, para publicar como Artifact do Claude. |

## Como atualizar

1. O conteúdo novo entra no `dados.py`.
2. `python verificar.py` — confere cada posição e cada lance com o Stockfish.
3. `python gerar.py` — regenera `index.html` e `finais.html`.
4. `git add . && git commit && git push` — o GitHub Pages publica sozinho.

Na prática, os passos 1 a 3 são feitos pelo Claude; o passo 4 é seu.

## Para rodar os scripts localmente (opcional)

Não é necessário para atualizar a página, mas se quiser rodar:

```
pip install chess
python gerar.py
```

Para a verificação também é preciso o Stockfish instalado, e o caminho do
binário ajustado na constante `SF` do `verificar.py` (no Windows, algo como
`C:/Stockfish/stockfish.exe`).

## Verificação

Cada posição é avaliada pelo Stockfish em profundidade 34, e **cada lance das
linhas principais é reavaliado individualmente** para confirmar que o resultado
objetivo não muda no caminho. Nos finais de rei e peão contra rei o Stockfish
consulta a sua bitbase interna de KPK, que é exaustiva.

Esse processo encontrou e corrigiu quatro erros no capítulo 1: dois lances
ilegais transcritos dos diagramas, um lance de torre que era de rei, e uma
posição que só é legal com as pretas a jogar.

## Sobre a origem do material

O roteiro de quais finais estudar segue *Los 100 finales que hay que saber*, de
Jesús de la Villa. **Este repositório não contém o livro nem tradução dele.**
As posições e os lances são fatos, não protegidos por direito autoral; os
textos explicativos foram escritos do zero para esta página.

O PDF do livro não deve ser adicionado ao repositório.

## Créditos e licenças

**Peças:** conjunto *Merida*, de Armando Hernandez Marroquin, sob
[GPLv2+](https://www.gnu.org/licenses/gpl-2.0.txt). Os arquivos em
`sets/merida/` vieram do repositório do Lichess
(`lichess-org/lila`, `public/piece/merida`) e mantêm a licença original.

**Fontes:** Zilla Slab, Spectral e IBM Plex Mono, via Google Fonts.
