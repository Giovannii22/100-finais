# 100 Finais — estudo de finais de xadrez em português

Página de estudo com posições de finais navegáveis lance a lance, baseada no
roteiro de *Los 100 finales que hay que saber* (Jesús de la Villa García).

**A página publicada é o `index.html`, servido pelo GitHub Pages.** Ele é
100% autocontido: todo o CSS, o JavaScript, os dados de todas as posições
(em FEN) e os desenhos vetoriais das 12 peças estão dentro do próprio
arquivo. A única coisa carregada de fora são as fontes do Google.

## Sumário

- [Stack](#stack)
- [Tecnologias e linguagens](#tecnologias-e-linguagens)
- [Arquitetura e fluxo de dados](#arquitetura-e-fluxo-de-dados)
- [Estrutura de arquivos](#estrutura-de-arquivos)
- [Estrutura de dados (`dados.py`)](#estrutura-de-dados-dadospy)
- [Como o HTML é montado (`gerar.py`)](#como-o-html-é-montado-gerarpy)
- [Lógica no navegador (JavaScript)](#lógica-no-navegador-javascript)
- [Tema, notação e acessibilidade](#tema-notação-e-acessibilidade)
- [Peças do tabuleiro](#peças-do-tabuleiro)
- [Verificação com Stockfish](#verificação-com-stockfish)
- [Como atualizar o conteúdo](#como-atualizar-o-conteúdo)
- [Rodando localmente](#rodando-localmente)
- [Versionamento e branches](#versionamento-e-branches)
- [Deploy](#deploy)
- [Sobre a origem do material](#sobre-a-origem-do-material)
- [Créditos e licenças](#créditos-e-licenças)

## Stack

Site estático, **sem backend, sem banco de dados, sem API e sem build step
de frontend**. Um script Python lê todo o conteúdo de um módulo Python
(`dados.py`), pré-calcula com `python-chess` cada posição intermediária de
cada linha de lances, e escreve um único arquivo HTML já pronto para
publicar. Não existe bundler (Webpack/Vite), não existe transpiler, não
existe `npm install` para rodar a página — o HTML gerado **é** o artefato
final, exatamente como vai para o ar.

Consequência direta disso: **o navegador do usuário final não executa
nenhuma lógica de xadrez**. Ele só recebe listas de posições (FEN) e lances
(SAN) já calculados e resolvidos, e alterna entre eles conforme o clique.
Não há parsing de regras, não há validação de lance, não há motor de xadrez
rodando em JS — tudo isso já foi feito em Python, uma vez, na hora de gerar
a página. Isso mantém o runtime da página trivial (só DOM e alguns objetos
JS) e elimina uma classe inteira de bugs de sincronização entre "o que a
página mostra" e "o que é de fato uma posição/lance legal".

## Tecnologias e linguagens

| Camada | Tecnologia | Observação |
|---|---|---|
| Geração/validação | Python 3 | Roda só no ambiente de desenvolvimento, nunca no navegador |
| Motor de regras de xadrez | [`python-chess`](https://pypi.org/project/chess/) | Parsing de FEN/SAN, validação de lances, detecção de xeque-mate/afogamento |
| Verificação objetiva | Stockfish 19 (binário externo) | Só para conferir se os lances não pioram o resultado teórico |
| Estrutura da página | HTML5 semântico | `<figure>`, `<nav>`, `<section>`, `<article>`, `role="img"`, `aria-*` |
| Estilo | CSS puro | Grid, custom properties (design tokens), `color-mix()`, `container-type`, `aspect-ratio`, `@media (prefers-color-scheme)` |
| Interatividade | JavaScript vanilla (ES6+) | Sem frameworks — nenhum React/Vue/Angular, nenhuma dependência de runtime |
| Peças do tabuleiro | SVG inline (`<symbol>`/`<use>`) | Conjunto Merida, embutido como sprite sheet no próprio HTML |
| Tipografia | Google Fonts via CDN | Zilla Slab (títulos), Spectral (corpo), IBM Plex Mono (rótulos/lances), Noto Sans Symbols 2 (fallback de símbolos) |

Não há `package.json`, `webpack.config`, `tsconfig` ou qualquer coisa do
ecossistema Node — o único ambiente de desenvolvimento é Python + a
biblioteca `chess`.

## Arquitetura e fluxo de dados

```
dados.py (conteúdo: textos, FENs, linhas de lances) ──┐
                                                        ├──► gerar.py ──► index.html  (publicado no GitHub Pages)
pecas.py (SVG das 12 peças, sprite sheet)  ────────────┤              └► finais.html (gerado, mas hoje não é publicado em lugar nenhum)
                                                        │
verificar.py (audita dados.py com Stockfish) ──────────┘
```

O pipeline é de mão única: **todo o conteúdo mora em `dados.py`**, um
dicionário Python puro (nada de YAML/JSON externo). `gerar.py` importa esse
dicionário, expande cada linha de lances em uma sequência de posições FEN
usando `python-chess`, serializa esses dados prontos como um objeto
JavaScript (`const DADOS = {...}`) dentro do HTML, e renderiza o HTML/CSS
ao redor. `verificar.py` é uma ferramenta de QA independente: lê o mesmo
`dados.py` e usa o Stockfish para confirmar que cada posição é legal e que
nenhum lance da linha principal muda o resultado objetivo do final.

`finais.html` é gerado com o mesmo conteúdo de `index.html`, mas sem o
wrapper de documento (sem `<!doctype>`/`<html>`/`<head>`/`<body>`) — foi
pensado originalmente para colar em uma plataforma que adiciona seu próprio
invólucro. **Esse destino foi abandonado**: hoje o projeto publica só via
GitHub Pages, e `finais.html` continua sendo gerado apenas por simplicidade
do script (não há necessidade de removê-lo, mas ele não é publicado em
lugar nenhum).

## Estrutura de arquivos

| Arquivo / pasta | Papel |
|---|---|
| `dados.py` | **O conteúdo do livro.** Dicionário `CAPITULO` (títulos, textos, posições em FEN, linhas de lances, notas por lance, marcações de casas) e lista `DIAGRAMAS` (referência cruzada com a numeração de diagramas do livro de origem). Este é o arquivo que muda a cada novo final adicionado. |
| `gerar.py` | O gerador. Importa `dados.py` e `pecas.py`, expande todas as sequências de lances com `python-chess`, monta o HTML (sumário, seções, tabuleiros) e escreve `index.html` / `finais.html`. Contém também todo o CSS e o JavaScript da página, como strings Python (f-strings). |
| `pecas.py` | Lê os 12 arquivos SVG de `sets/merida/`, isola os `id`s internos de cada um (gradientes, principalmente) para não colidirem quando embutidos juntos, e envolve cada peça em um `<symbol>` com uma `viewBox` comum. |
| `medir_pecas.py` | Utilitário que roda com Playwright: abre as 12 peças no navegador, mede a caixa delimitadora da **união** das doze e grava essa `viewBox` comum em `pecas.py`. Só precisa rodar de novo se o conjunto de peças for trocado. |
| `verificar.py` | Ferramenta de QA. Para cada posição e cada lance de `dados.py`, consulta o Stockfish 19 em profundidade 20 (com override por posição via `"profundidade"`, e a bitbase interna KPK do próprio Stockfish nos finais de rei e peão) para confirmar que o resultado teórico não muda ao longo da linha. |
| `sets/merida/*.svg` | As 12 peças originais do conjunto Merida (wK, bK, wQ, bQ, wR, bR, wB, bB, wN, bN, wP, bP), sem modificação. |
| `sets/merida/LICENSE.txt` | Licença original do conjunto Merida (GPLv2+), mantida junto aos arquivos por exigência da licença. |
| `index.html` | **Saída publicada no GitHub Pages.** HTML completo, com `<!doctype>`/`<html>`/`<head>`/`<body>`. É o único artefato realmente "em produção". |
| `finais.html` | Mesma saída sem o invólucro de documento. Gerado, mas atualmente não publicado em nenhuma plataforma (ver seção Deploy). |
| `README.md` | Este arquivo. |
| `.gitignore` | Ignora `__pycache__/`, `venv/`, `verificacao.json`, `*.pyc`. |

## Estrutura de dados (`dados.py`)

Todo o conteúdo do capítulo é um único dicionário Python, sem nenhum
formato de serialização intermediário:

```python
DIAGRAMAS = [
    "1.1–1.2",   # referência ao diagrama do livro, na ordem de aparição na página
    "1.3",
    ...
]

CAPITULO = {
    "numero": 1,
    "titulo": "Finais básicos",
    "intro": "...",
    "secoes": [
        {
            "id": "rei-peao",                       # âncora da seção no sumário
            "titulo": "Rei e peão contra rei",
            "resumo": "...",
            "finais": [
                {
                    "n": 1,
                    "titulo": "A regra do quadrado",
                    "conceito": "...",               # subtítulo curto, aparece no sumário
                    "texto": ["parágrafo 1", "parágrafo 2"],   # markdown simplificado (** e *)
                    "regras": ["regra para memorizar 1", "..."],
                    "posicoes": [
                        {
                            "fen": "6k1/8/8/8/8/8/P7/7K w - - 0 1",
                            "rotulo": "Brancas jogam e ganham",
                            "resultado": "Brancas ganham",     # ou "Pretas ganham" / "Empate" / "Empate teórico"
                            "linha": ["a4", "Kf7", "a5", ...], # lances em SAN, linha principal
                            "notas": {0: "texto na posição inicial", 3: "texto após o 3º lance"},
                            "marcas": {"a5": "critica"},        # casas destacadas no tabuleiro
                            "marcas_desde": 0, "marcas_ate": 3, # janela de lances em que as marcas aparecem
                            "legenda_marcas": "● casa crítica",
                            "regra_destaque": "texto em caixa de destaque, opcional",
                            "alternativas": [                   # linhas alternativas opcionais
                                {
                                    "titulo": "...",             # não é mais mostrado como rótulo do botão — ver gerar.py
                                    "linha": ["Kg8", "Kg5", ...],
                                    "nota": "explicação da linha alternativa",
                                },
                            ],
                        },
                    ],
                    "exemplo_pratico": {                        # opcional, ao final de um final
                        "titulo": "...",
                        "texto": ["..."],
                        "posicoes": [ ... ],                     # mesma forma de "posicoes" acima
                        "fecho": "parágrafo de fechamento",
                    },
                },
            ],
        },
    ],
}
```

Pontos importantes sobre esse formato:

- **`len(DIAGRAMAS)` precisa bater exatamente com o número total de
  posições** em todo o capítulo (contando `posicoes` de cada final e de
  cada `exemplo_pratico`). O gerador (`build_positions()` em `gerar.py`)
  falha com um erro explícito se alguém adicionar uma posição sem registrar
  a referência de diagrama correspondente, na ordem certa — isso existe
  para impedir que a numeração dos diagramas fique dessincronizada do
  conteúdo.
- Textos aceitam um **markdown simplificado**: `**negrito**` e `*itálico*`
  (função `md()` em `gerar.py`). Um asterisco que sobra sem par vira erro
  na geração, de propósito — evita negrito/itálico quebrado silenciosamente.
- `notas` é um dicionário `índice do lance → texto`, mostrado abaixo do
  tabuleiro conforme o usuário avança/retrocede pelos lances daquela linha.
- `marcas` destaca casas específicas do tabuleiro (usado para indicar a
  "casa crítica" de uma regra, por exemplo), só dentro da janela de lances
  `marcas_desde`–`marcas_ate`.
- `alternativas` permite anexar uma ou mais linhas alternativas a uma
  posição, exibidas como botões abaixo da lista de lances principal (ver
  próxima seção).

## Como o HTML é montado (`gerar.py`)

O gerador funciona em etapas, todas dentro de `gerar.py`:

1. **`build_positions()`** percorre `CAPITULO` inteiro, e para cada posição
   chama `expandir()`, que usa `python-chess` para tocar a linha de lances a
   partir do FEN inicial e gravar a lista completa de FENs intermediários
   (`_fens`), os lances já normalizados em SAN (`_sans`) e se a linha termina
   em xeque-mate ou afogamento (`_fim`). O mesmo é feito para cada
   `alternativa`, via `expandir_alt()`. Isso confere `len(DIAGRAMAS)` contra
   o total de posições encontradas.
2. **`pos_payload()`** empacota cada posição processada num dicionário JSON
   simples (`fens`, `sans`, `fim`, `notas`, `marcas`, `alts`, ...) — é
   exatamente esse dicionário que vira dado no navegador.
3. **`render_pos()` / `render()`** montam o HTML: sumário navegável, uma
   seção por grupo temático, um `<article>` por final, e dentro dele um
   `<figure class="board-block">` por posição/diagrama (com div vazia para o
   tabuleiro e `<ol class="moves">` vazia — o conteúdo real é preenchido em
   JavaScript a partir de `DADOS`, no carregamento da página).
4. **`main()`** monta o documento completo: injeta o *sprite sheet* de peças
   SVG (`pecas_symbols()`), o cabeçalho (`<header class="masthead">`, com os
   controles de tema e notação), o corpo (`render()`), o rodapé com créditos
   e a versão publicada, e por fim o `<script>` com `const DADOS = {...}`
   (todas as posições já calculadas, serializadas via `json.dumps`) seguido
   da classe `Viewer` que efetivamente desenha e controla cada tabuleiro.
5. **`gerar()`** escreve o resultado em `index.html` (com wrapper de
   documento completo) e `finais.html` (mesmo conteúdo, sem wrapper).

Todo o CSS e todo o JavaScript vivem como strings dentro de `gerar.py` —
não há arquivos `.css`/`.js` separados. Isso é intencional: o objetivo é um
único arquivo autocontido na saída, e manter tudo junto na fonte evita
desincronização entre o gerador e os assets.

## Lógica no navegador (JavaScript)

O JavaScript embutido no HTML gerado é pequeno e sem dependências. As
peças principais:

- **`const DADOS = {...}`** — objeto com todas as posições pré-calculadas
  (uma entrada por `id` de tabuleiro: `p1`, `p2`, ...). Nenhuma lógica de
  xadrez roda a partir daqui; é só consulta a listas prontas.
- **`drawBoard(el, fen, marks, fenAnterior)`** — lê um FEN e desenha as 64
  casas e as peças (via `<use href="#pc-...">`, referenciando o sprite
  sheet SVG), aplicando coordenadas, marcações de casas e destaque da
  última jogada (`.sq.from`/`.sq.to`).
- **`class Viewer`** — uma instância por tabuleiro (`data-pos="pN"` no
  HTML). Controla:
  - navegação pela linha de lances (`act("start"|"prev"|"next"|"end")`,
    além das setas do teclado quando o tabuleiro está focado);
  - clique direto em qualquer lance da lista (`.mv`) para pular até ele;
  - alternância entre a linha principal e uma **linha alternativa**
    (`toggleAlt`), quando a posição tem `alts`. Os botões de alternativa
    (`.alt-btn`) são criados dinamicamente e rotulados de forma padronizada
    como **"Lance alternativo"** (ou "Lance alternativo 1", "2", ... quando
    há mais de uma linha alternativa na mesma posição) — o campo `titulo`
    de cada alternativa em `dados.py` não é mais usado como texto visível,
    só como documentação interna;
  - exibição da nota (`notas[i]`) correspondente ao lance atual.
- **Notação PT/EN** (`traduzir()`) — troca as iniciais das peças (R/D/T/B/C
  ↔ K/Q/R/B/N) na hora de exibir os lances, sem alterar os dados; a escolha
  é lembrada em `localStorage` (`notacao`).
- **Tema claro/escuro** — aplicado antes do primeiro paint (script inline no
  `<head>`, para não piscar), com preferência salva em `localStorage`
  (`tema`) e fallback para `prefers-color-scheme` quando não há preferência
  salva.

Não há build step nem minificação — o JS é servido exatamente como está no
gerador.

## Tema, notação e acessibilidade

- Toda a paleta de cores é definida como **custom properties CSS**
  (`--ink`, `--paper`, `--accent`, `--line`, ...), redefinidas para o tema
  escuro tanto via `@media (prefers-color-scheme: dark)` quanto via
  `:root[data-user-theme="dark"]` (escolha explícita do usuário, que tem
  prioridade). O tema padrão da página é **escuro**.
- Botões de controle usam `aria-pressed`/`aria-current` para estado, têm
  `aria-label` descritivo e outline visível em `:focus-visible`.
- `@media (prefers-reduced-motion: reduce)` desliga todas as transições.
- O tabuleiro é `role="img"` com `aria-label`, e as peças SVG são
  `aria-hidden` (o conteúdo relevante para leitor de tela é a lista de
  lances em texto, não o desenho).

## Peças do tabuleiro

Usa o conjunto **Merida**, de Armando Hernandez Marroquin, sob **GPLv2+**,
obtido originalmente do repositório público do Lichess
(`lichess-org/lila`, `public/piece/merida`). Os 12 SVGs individuais e o
`LICENSE.txt` da licença completa estão versionados em `sets/merida/`.

Duas decisões técnicas relevantes ao embutir um conjunto de peças de
terceiros:

1. **Isolar os `id`s internos de cada SVG** (gradientes chamados `a`, `b`,
   etc. em arquivos diferentes) antes de juntá-los num único documento —
   sem isso, os `id`s colidem e uma peça acaba usando o gradiente de outra.
   Isso é feito em `pecas.py`.
2. **Não reenquadrar peça por peça.** O autor do conjunto já desenhou as
   doze peças com proporções e linha de base coerentes entre si. Em vez de
   ajustar a `viewBox` individualmente, `medir_pecas.py` mede a caixa
   delimitadora da **união** das doze e aplica essa mesma `viewBox` a
   todas — preservando as proporções relativas que o autor definiu (por
   exemplo, o peão é naturalmente mais baixo que o rei).

Se um dia for necessário trocar de conjunto, candidatos livres do
repositório do Lichess incluem: rhosgfx (CC0), chessnut (Apache),
fantasy/spatial/celtic (MIT), cburnett (GPLv2+, similar ao Merida). Evitar
os conjuntos sob CC BY-**NC**-SA (staunty, maestro, california, anarcandy
etc.) por causa da cláusula de uso não comercial.

## Verificação com Stockfish

`verificar.py` audita `dados.py` independentemente do gerador: para cada
posição e cada lance de cada linha (principal e alternativas), consulta o
Stockfish 19 em **profundidade 20** (padrão) para confirmar que o resultado
objetivo do final (vitória de brancas/pretas ou empate) não muda em nenhum
ponto da linha. Em finais de rei e peão contra rei, o Stockfish consulta sua
bitbase interna de KPK (exaustiva, não é estimativa). Se uma posição
específica exigir mais rigor, é possível aumentar a profundidade só para
ela com o campo opcional `"profundidade"` no dicionário da posição em
`dados.py` — não afeta as demais.

Esse processo já encontrou e corrigiu quatro erros de transcrição no
capítulo 1: dois lances ilegais, um lance de torre que na verdade era de
rei, e uma posição que só é legal com as pretas a jogar.

`verificar.py` localiza o binário do Stockfish automaticamente
(`localizar_stockfish()`): tenta a variável de ambiente `STOCKFISH_PATH`,
depois o `PATH` do sistema, depois alguns caminhos comuns no Windows/Linux.
Não é preciso editar o script por máquina — basta ter o Stockfish instalado
e no PATH, ou definir `STOCKFISH_PATH` apontando para o executável.

## Como atualizar o conteúdo

1. Editar `dados.py` — adicionar ou corrigir posições, textos, linhas de
   lances, notas.
2. `python verificar.py` — confirma que toda posição é legal e que nenhum
   lance da linha principal muda o resultado objetivo do final.
3. `python gerar.py` — regenera `index.html` e `finais.html` a partir do
   `dados.py` atualizado.
4. Abrir `index.html` diretamente no navegador para conferir visualmente.
5. `git add` → `git commit` → `git push` — o GitHub Pages publica sozinho a
   cada push na `main`.

## Rodando localmente

```bash
# 1. Clonar o repositório
git clone https://github.com/Giovannii22/100-finais.git
cd 100-finais

# 2. Instalar a dependência Python (parsing/validação de xadrez)
pip install chess

# 3. Instalar o Stockfish (só necessário para rodar verificar.py)
#    Windows: baixar o binário e apontar o caminho em verificar.py
#    Linux/WSL: apt-get install stockfish

# 4. Editar dados.py, depois:
python verificar.py   # valida posições e lances
python gerar.py       # gera index.html / finais.html

# 5. Abrir index.html direto no navegador para conferir
```

Não há dependências de Node/JavaScript para desenvolvimento — só Python.

## Versionamento e branches

- **Branch principal:** `main` — sempre publicável, reflete o que está em
  produção no GitHub Pages.
- **Branches de trabalho:** uma por capítulo, nomeadas `capitulo-N-descricao`
  (ex.: `capitulo-2-finais-10-19`), mescladas em `main` quando o capítulo
  está completo e verificado.
- **Tags Git, seguindo versionamento semântico:**
  - `vX.0` — novo capítulo completo adicionado.
  - `vX.Y.Z` — correção ou ajuste pequeno, sem conteúdo novo (patch).
  - `vX+1.0` — mudança estrutural grande.
  - Uma tag já publicada **nunca é movida** — uma correção depois da
    publicação vira uma nova tag patch.
- **Tags publicadas até agora:**
  - `v1.0` — primeira publicação do capítulo 1 (9 finais, 23 posições).
  - `v1.0.1` — correções de título, favicon, créditos ao livro de
    referência, indicador de versão no rodapé e infraestrutura de SVGs
    versionada em `sets/`.

## Deploy

**Único destino de publicação: GitHub Pages.**

| Destino | O que serve | Como atualiza |
|---|---|---|
| **GitHub Pages** | `index.html` (raiz do repositório) | Automático a cada `git push` na `main` |

Não há CI/CD automatizado — `gerar.py` precisa ser rodado localmente antes
de cada push. Um destino anterior (publicação manual de `finais.html` como
Claude Artifact) foi descontinuado; o arquivo `finais.html` continua sendo
gerado, mas não é publicado em nenhuma plataforma atualmente.

## Sobre a origem do material

O roteiro de quais finais estudar, a seleção e a numeração das posições
seguem *Los 100 finales que hay que saber*, de Jesús de la Villa García (2ª
edición revisada, Esfera Editorial, 2008). **Este repositório não contém o
livro nem tradução dele.** As posições e os lances são fatos objetivos, não
protegidos por direito autoral; todos os textos explicativos e análises
foram escritos do zero, em português, especificamente para esta página.
Trabalho sem fins comerciais, feito exclusivamente para estudo pessoal.

O PDF do livro não deve ser adicionado a este repositório em nenhuma
circunstância.

## Créditos e licenças

**Peças do tabuleiro:** conjunto *Merida*, de Armando Hernandez Marroquin,
sob [GPLv2+](https://www.gnu.org/licenses/gpl-2.0.txt). Os arquivos em
`sets/merida/` vieram do repositório do Lichess (`lichess-org/lila`,
`public/piece/merida`) e mantêm a licença original, exibida no rodapé de
toda página gerada conforme exigido pela licença.

**Fontes:** Zilla Slab, Spectral, IBM Plex Mono e Noto Sans Symbols 2, via
Google Fonts.
