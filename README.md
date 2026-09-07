# 100 Finais — estudo de finais de xadrez em português

Página de estudo com posições de finais navegáveis lance a lance. O capítulo 1
está pronto e versionado (`v1.0.1`): 9 finais, 23 posições. O capítulo 2 está
em desenvolvimento numa branch separada.

**A página publicada é o `index.html`.** Ele é autocontido: todo o CSS, o
JavaScript, os dados das posições e os desenhos das peças estão dentro do
arquivo. A única coisa externa são as fontes do Google.

## Arquitetura

Site estático, **sem backend, sem banco de dados, sem API**. Um script Python
lê os dados de todas as posições, pré-calcula todas as sequências de lances
com a biblioteca `python-chess`, e gera um único HTML autocontido.

O navegador do usuário final não executa nenhuma lógica de xadrez — só
percorre listas de posições (FEN) já calculadas. Não há bundler, transpiler
ou build step de frontend: o HTML gerado já é o artefato final.

```
dados.py (conteúdo) ──┐
                       ├──► gerar.py ──► index.html (GitHub Pages)
pecas.py (peças SVG) ──┤              └─► finais.html (Claude Artifact)
                       │
verificar.py ──────────┘ (valida dados.py com Stockfish)
```

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Geração/validação | Python 3 |
| Estrutura da página | HTML5 |
| Estilo | CSS puro (Grid, custom properties, `color-mix`, `container-type`) |
| Interatividade | JavaScript vanilla — sem frameworks |
| Peças do tabuleiro | SVG inline (`<symbol>`/`<use>`), conjunto Merida |
| Tipografia | Google Fonts via CDN: Zilla Slab, Spectral, IBM Plex Mono, Noto Sans Symbols 2 |

## Como o projeto está organizado

| arquivo | o que é |
|---|---|
| `dados.py` | **O conteúdo.** Textos, posições em FEN, linhas de lances, notas, referências aos diagramas. É o arquivo que representa o trabalho. |
| `gerar.py` | Transforma `dados.py` na página. Pré-calcula todas as posições intermediárias, monta sumário, seções e tabuleiros. |
| `pecas.py` | Carrega o conjunto de peças e isola os `id` de cada SVG. |
| `medir_pecas.py` | Mede a caixa da união das 12 peças e grava a `viewBox` comum em `pecas.py`. Rodar só se o conjunto de peças mudar. |
| `verificar.py` | Passa cada posição e cada lance pelo Stockfish. |
| `sets/merida/` | As 12 peças, em SVG, com `LICENSE.txt` próprio. |
| `index.html` | A página pronta, gerada. **É o que o GitHub Pages publica.** |
| `finais.html` | Mesmo conteúdo sem o invólucro `<html>`, para publicar como Artifact do Claude. |

## Estrutura de dados (`dados.py`)

```python
DIAGRAMAS = [
    "1.1–1.2",   # referência ao diagrama do livro, na ordem de aparição
    ...
]

CAPITULO = {
    "numero": 1,
    "titulo": "Finais básicos",
    "intro": "...",
    "secoes": [
        {
            "id": "rei-peao",
            "titulo": "Rei e peão contra rei",
            "resumo": "...",
            "finais": [
                {
                    "n": 1,
                    "titulo": "A regra do quadrado",
                    "conceito": "...",
                    "texto": ["parágrafo 1", "parágrafo 2"],
                    "posicoes": [
                        {"fen": "...", "resultado": "Brancas ganham", "linha": ["a4", "Kf7", ...]},
                    ],
                },
            ],
        },
    ],
}
```

O gerador confere se `len(DIAGRAMAS)` bate com o número total de posições e
falha se alguém adicionar uma posição sem registrar a referência.

## Como atualizar

1. O conteúdo novo entra no `dados.py`.
2. `python verificar.py` — confere cada posição e cada lance com o Stockfish.
3. `python gerar.py` — regenera `index.html` e `finais.html`.
4. `git add . && git commit && git push` — o GitHub Pages publica sozinho.
5. Republicar o Claude Artifact com o novo `finais.html` (processo manual).

Na prática, os passos 1 a 3 são feitos pelo Claude; os passos 4 e 5 são seus.

## Versionamento e branches

Cada capítulo é desenvolvido numa branch própria (`capitulo-N-descricao`),
criada a partir da `main`, e só é mesclado de volta quando o capítulo está
verificado e completo. A branch `main` reflete sempre o que está publicado.

Releases são marcadas com tags Git seguindo versionamento semântico:

- `vX.0` — novo capítulo completo adicionado
- `vX.Y.Z` — correção ou ajuste pequeno, sem conteúdo novo (patch)
- `vX+1.0` — mudança estrutural grande

Uma tag já publicada não é movida — uma correção depois da publicação vira uma
nova tag patch. Tags publicadas até agora: `v1.0` (primeira versão do
capítulo 1) e `v1.0.1` (correções de título, favicon, créditos e SVGs
versionados).

## Deploy

Dois destinos independentes, sincronizados manualmente a cada mudança:

| Destino | O que serve | Como atualiza |
|---|---|---|
| **GitHub Pages** | `index.html` (raiz do repositório) | Automático a cada `git push` na `main` |
| **Claude Artifact** | Conteúdo de `finais.html` | Manual — não tem versionamento próprio, reflete só o último conteúdo publicado |

Não há CI/CD automatizado.

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

O roteiro de quais finais estudar segue *Los 100 finales que hay que saber*,
de Jesús de la Villa García (2ª edición revisada, Esfera Editorial, 2008).
**Este repositório não contém o livro nem tradução dele.** As posições e os
lances são fatos, não protegidos por direito autoral; os textos explicativos
foram escritos do zero para esta página. Trabalho sem fins comerciais, feito
exclusivamente para estudo pessoal.

O PDF do livro não deve ser adicionado ao repositório.

## Créditos e licenças

**Peças:** conjunto *Merida*, de Armando Hernandez Marroquin, sob
[GPLv2+](https://www.gnu.org/licenses/gpl-2.0.txt). Os arquivos em
`sets/merida/` vieram do repositório do Lichess
(`lichess-org/lila`, `public/piece/merida`) e mantêm a licença original.

**Fontes:** Zilla Slab, Spectral e IBM Plex Mono, via Google Fonts.
