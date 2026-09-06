# -*- coding: utf-8 -*-
"""Dados do Capítulo 1 — Finais básicos.
Posições retiradas dos diagramas do livro (posições e lances não são
protegidos por direito autoral); textos didáticos escritos do zero.
"""

# Referência ao diagrama de origem no livro, na ordem em que as posições
# aparecem no capítulo. O gerador confere se a contagem bate com o número de
# posições e falha se alguém acrescentar uma posição sem registrar a referência.
DIAGRAMAS = [
    "1.1–1.2",        # Final 1 — regra do quadrado (1.2 é a posição após 1.a4)
    "1.3",            # Final 1 — interposição
    "1.4",            # Final 2 — brancas jogam
    "1.4–1.5",        # Final 2 — mesma posição com as pretas a jogar (1.5 após 1...Rg8)
    "1.6",            # Final 2 — oposição na borda
    "1.7",            # Final 2 — a oposição pode ser perdida
    "1.8",            # Final 2 — peão de cavalo
    "1.9",            # Final 3 — rei em casa crítica
    "1.10",           # Final 3 — peão de cavalo
    "1.11",           # Final 3 — peão atrás da quinta
    "1.12",           # Final 3 — oposição distante
    "1.13",           # Final 3 — tempo de reserva
    "1.14",           # Final 4 — peão de torre
    "1.15",           # Final 4 — seis peões de torre
    "1.16",           # Final 5 — confinamento do rei forte
    "1.17",           # Final 6 — canto ruim
    "1.18",           # Final 7 — canto bom
    "1.19",           # Final 8 — rei e cavalo na borda
    "análise 1.20",   # Final 8 — diagrama de análise
    "1.21",           # Final 9 — cavalo no canto
    "1.22",           # Final 9 — rei no canto
    "1.23",           # Final 9 — casa boba do cavalo
    "1.24",           # Final 9 — Kamsky–Bacrot
]

CAPITULO = {
    "numero": 1,
    "titulo": "Finais básicos",
    "intro": (
        "Este capítulo cobre o que precisa estar automático antes de qualquer coisa: "
        "rei e peão contra rei, e as duas defesas de peça menor contra torre. "
        "São finais que aparecem o tempo todo e onde o erro custa o ponto inteiro — "
        "não há compensação posicional que salve quem não sabe a regra."
    ),
    "secoes": [
        {
            "id": "rei-peao",
            "titulo": "Rei e peão contra rei",
            "resumo": (
                "Cinco finais que respondem a uma única pergunta: o peão promove ou não? "
                "As ferramentas são a regra do quadrado, a oposição e as casas críticas — "
                "nessa ordem de utilidade."
            ),
            "finais": [
                {
                    "n": 1,
                    "titulo": "A regra do quadrado",
                    "conceito": "O peão promove sozinho?",
                    "texto": [
                        "Quando o rei do lado forte está longe demais para ajudar, a corrida é entre "
                        "o peão e o rei adversário. A regra do quadrado responde isso de olho, sem contar lances.",
                        "**Regra do quadrado:** trace o quadrado que tem como lado a distância do peão até a casa de promoção. "
                        "Se, no seu lance, o rei defensor **entrar** nesse quadrado, ele alcança o peão. Se não entrar, o peão promove.",
                        "Não importa se o rei já estava dentro antes de jogar ou se entra agora, nem se ele persegue o peão "
                        "por trás ou pelo lado — o que vale é o resultado depois do lance dele.",
                        "**A sutileza que decide esta posição:** com o peão ainda na casa de origem, conte o quadrado "
                        "a partir da terceira fila, porque o passo duplo vale um tempo. É exatamente esse tempo que ganha aqui.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Posição inicial — brancas jogam",
                            "fen": "6k1/8/8/8/8/8/P7/7K w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["a4", "Kf7", "a5", "Ke6", "a6", "Kd6", "a7", "Kc7", "a8=Q"],
                            "notas": {
                                0: "O passo duplo é o lance decisivo. O quadrado passa a ser a4-a8-e8-e4, e o rei preto, em g8, está fora dele.",
                                1: "Nem f7 nem qualquer outra casa alcançável entra no quadrado. A corrida está perdida.",
                                9: "O peão promove com tempo de sobra.",
                            },
                            "marcas": {"a4": "quadrado", "b4": "quadrado", "c4": "quadrado", "d4": "quadrado", "e4": "quadrado",
                                       "a5": "quadrado", "e5": "quadrado", "a6": "quadrado", "e6": "quadrado",
                                       "a7": "quadrado", "e7": "quadrado", "a8": "quadrado", "b8": "quadrado",
                                       "c8": "quadrado", "d8": "quadrado", "e8": "quadrado"},
                            "marcas_desde": 1,
                            "marcas_ate": 2,
                            "legenda_marcas": "Quadrado do peão depois de 1.a4 (lances 1 e 2)",
                        },
                        {
                            "rotulo": "Quando o rei precisa ajudar — a interposição",
                            "fen": "8/4k3/2K5/8/8/8/1P6/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["Kc7", "Ke6", "b4", "Kd5", "b5", "Kc5", "b6", "Kc4", "b7"],
                            "notas": {
                                0: "Aqui o rei preto está dentro do quadrado, então o peão sozinho não vale nada — ele precisa do rei. "
                                   "A forma mais eficiente de ajudar é **se interpor**: ocupar as casas por onde o rei adversário entraria na frente do peão.",
                                1: "De c7 o rei branco cobre b8, c8 e d8 de uma vez. O rei preto nunca mais consegue se colocar à frente do peão, "
                                   "e ainda por cima o rei branco já está apoiando os três últimos passos.",
                                2: "Sem poder bloquear, o rei preto tenta atacar o peão antes que ele chegue à zona protegida (b6-b7-b8).",
                                6: "O peão avança protegido pelo rei. O ataque preto chegou tarde.",
                                9: "Sem bloqueio nem captura possível, as pretas não têm defesa.",
                            },
                        },
                    ],
                    "regras": [
                        "Se o rei defensor entra no quadrado do peão, captura-o; se não entra, o peão promove.",
                        "Com o peão na casa de origem, conte o quadrado a partir da terceira fila.",
                        "Se o rei defensor está dentro do quadrado, o peão só promove com a ajuda do próprio rei — e o método é a interposição.",
                    ],
                },
                {
                    "n": 2,
                    "titulo": "O peão na sexta e a oposição",
                    "conceito": "Com o peão na sexta, quem tem a oposição decide",
                    "texto": [
                        "Esta é a primeira imagem que precisa ficar gravada. Com o peão na sexta fila e o rei defensor "
                        "conseguindo se colocar à frente dele, tudo depende da posição relativa dos reis.",
                        "**Oposição:** os reis estão em oposição quando ficam na mesma coluna, fila ou diagonal com um número "
                        "ímpar de casas entre eles. Quem *toma* a oposição leva vantagem; quem *precisa jogar* estando em oposição, leva desvantagem.",
                        "A oposição tem fama exagerada — ela não serve para tudo. Mas no final de rei e peão contra rei, "
                        "com o peão na sexta, ela é literalmente o resultado da partida.",
                        "**O erro que essa posição ensina:** avançar o peão cedo demais. O peão na sexta atrapalha as manobras do próprio rei. "
                        "Só avance para a sexta quando (a) o caminho até a promoção estiver limpo, ou (b) o avanço lhe der a oposição — "
                        "e isso normalmente só acontece se o rei chegou à sexta antes do peão.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Brancas jogam — ganham",
                            "fen": "5k2/8/5PK1/8/8/8/8/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["f7+", "Ke7", "Kg7"],
                            "notas": {
                                0: "As brancas jogam e o peão dá os dois últimos passos quase automaticamente.",
                                1: "O peão avança com xeque e o rei preto é obrigado a sair da casa de promoção.",
                                2: "O rei branco apoia o último passo. O peão promove no lance seguinte.",
                            },
                        },
                        {
                            "rotulo": "Mesma posição, pretas jogam — empate",
                            "fen": "5k2/8/5PK1/8/8/8/8/8 b - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Kg8", "f7+", "Kf8", "Kf6"],
                            "notas": {
                                0: "Mesma posição, resultado oposto. O rei preto toma a oposição e o peão nunca promove.",
                                1: "Agora os reis estão em oposição direta (g6 contra g8), e é a vez das brancas.",
                                3: "**Afogamento.** O peão em sétima, defendido pelo rei, não tem como progredir.",
                            },
                            "alternativas": [
                                {
                                    "titulo": "A defesa alternativa: oscilar à frente do peão",
                                    "linha": ["Kg8", "Kg5", "Kf7", "Kf5", "Kf8", "Kf4", "Kf7", "Kf5", "Kf8", "Ke6", "Ke8", "f7+", "Kf8", "Kf6"],
                                    "nota": "Manter-se sempre à frente do peão, oscilando entre as duas casas, é um método de defesa "
                                            "que não pode ser quebrado. Quando o rei branco finalmente sai da coluna do peão, aí sim se toma a oposição.",
                                },
                            ],
                        },
                        {
                            "rotulo": "Tomando a oposição na borda",
                            "fen": "k7/8/2P5/K7/8/8/8/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["Ka6", "Kb8", "Kb6", "Kc8", "c7", "Kd7", "Kb7"],
                            "notas": {
                                0: "Com o peão na sexta e os reis fora da coluna do peão, as manobras continuam guiadas pela oposição.",
                                1: "Tomando a oposição. O lance natural **1.Rb6?? Rb8!** entrega a oposição ao rei preto e empata.",
                                5: "Agora o peão avança com o caminho garantido.",
                                6: "O rei apoia a promoção.",
                            },
                        },
                        {
                            "rotulo": "A oposição pode ser perdida",
                            "fen": "8/6k1/4P3/6K1/8/8/8/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["Kf5", "Kg8", "Kg6", "Kf8", "Kf6", "Ke8", "e7", "Kd7", "Kf7"],
                            "notas": {
                                0: "Uma das posições que mais provoca erro. Os reis estão em oposição e é a vez das brancas — "
                                   "parecia ruim para elas, mas a oposição preta é **provisória**.",
                                1: "O motivo: o peão em e6 controla f7 e d7. O rei preto não tem como manter a oposição, "
                                   "porque as casas de que ele precisaria estão inacessíveis.",
                                4: "As brancas conquistaram a oposição na sexta — a situação-chave.",
                                8: "O peão promove.",
                            },
                            "regra_destaque": "A oposição já conquistada pode ser perdida, se alguma das casas necessárias para mantê-la for inacessível.",
                        },
                        {
                            "rotulo": "A exceção do peão de cavalo",
                            "fen": "8/8/8/8/8/5kp1/7K/8 w - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Kh1", "Kf2"],
                            "notas": {
                                0: "Aqui as **pretas** têm o peão. O rei branco deve jogar e não pode tomar a oposição. "
                                   "Com um peão central esta posição estaria perdida — mas o peão de cavalo, tão perto da borda, tem seus caprichos.",
                                1: "A oposição diagonal (h1 contra f3) normalmente não serve de muito, mas aqui funciona.",
                                2: "**Afogamento.** Contra outros lances o rei branco simplesmente volta ao bloqueio à frente do peão: 1...Rg4 2.Rg2! e é inexpugnável.",
                            },
                        },
                    ],
                    "regras": [
                        "Com o peão na sexta, a oposição dos reis decide o final.",
                        "Não se precipite em avançar o peão: o peão na sexta atrapalha o próprio rei.",
                        "A oposição pode ser perdida se as casas necessárias para mantê-la estiverem controladas pelo peão.",
                        "Peão de cavalo é exceção: o afogamento na borda pode salvar o defensor.",
                    ],
                },
                {
                    "n": 3,
                    "titulo": "As casas críticas",
                    "conceito": "Onde o rei precisa chegar para o peão promover",
                    "texto": [
                        "Com o peão antes da sexta fila os cálculos ficam mais longos, mas existe uma regra que resolve "
                        "praticamente tudo — e é a regra mais útil de todo o capítulo.",
                        "**Casas críticas:** se o rei do lado forte ocupa uma das casas críticas, o peão promove — não importa de quem é a vez.",
                        "Onde ficam elas: para o peão na **quinta** fila, são as três casas imediatamente à frente. "
                        "Para o peão na **segunda, terceira ou quarta**, são as três casas **duas filas à frente**. "
                        "Na prática, isso faz com que peão na quarta e peão na quinta tenham as mesmas casas críticas.",
                        "Toda a manobra prévia do rei passa a ter um objetivo concreto: alcançar uma dessas três casas. "
                        "E a oposição volta como ferramenta — o papel dela é justamente **impedir** o rei adversário de chegar lá.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "O rei já está numa casa crítica",
                            "fen": "5k2/8/4K3/5P2/8/8/8/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["Kf6", "Ke8", "Kg7", "Ke7", "f6+", "Ke6", "f7"],
                            "notas": {
                                0: "Peão na quinta: as casas críticas são e6, f6 e g6. O rei branco já ocupa uma delas, então as brancas ganham.",
                                1: "Não **1.f6?? Re8!** tomando a oposição, com empate. Como já foi dito: não se precipite em avançar o peão — "
                                   "primeiro o rei abre caminho.",
                                2: "O rei preto se afastou das casas por onde o peão precisa passar.",
                                3: "Agora o caminho está livre e o peão promove em três lances.",
                            },
                            "marcas": {"e6": "critica", "f6": "critica", "g6": "critica"},
                            "legenda_marcas": "Casas críticas do peão em f5",
                        },
                        {
                            "rotulo": "Casas críticas com o peão de cavalo",
                            "fen": "7k/5K2/8/6P1/8/8/8/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["Kg6", "Kg8", "Kh6", "Kh8", "g6", "Kg8", "g7", "Kf7", "Kh7"],
                            "notas": {
                                0: "A regra continua valendo com o peão de cavalo, mas é preciso um cuidado a mais.",
                                1: "O rei tem que passar para o outro lado, para evitar os truques de afogamento. "
                                   "**1.g6? é afogamento imediato.**",
                                4: "Deste lado o peão avança com tranquilidade.",
                                8: "O peão promove no próximo lance.",
                            },
                        },
                        {
                            "rotulo": "Peão atrás da quinta fila",
                            "fen": "5k2/8/8/8/3PK3/8/8/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["Kd5", "Ke7", "Kc6", "Kd8", "Kd6", "Kc8", "Ke7", "Kc7", "d5", "Kc8", "d6", "Kb7", "d7"],
                            "notas": {
                                0: "Peão na quarta: as casas críticas estão duas filas à frente — c6, d6 e e6.",
                                1: "Rumo à casa crítica c6. **1.Re5?? seria ruim por 1...Re7!** — a oposição impede o rei branco de avançar, "
                                   "que é o uso mais típico dela.",
                                3: "Casa crítica alcançada. Daqui em diante o procedimento já é conhecido.",
                            },
                            "marcas": {"c6": "critica", "d6": "critica", "e6": "critica"},
                            "legenda_marcas": "Casas críticas do peão em d4",
                        },
                        {
                            "rotulo": "A oposição distante",
                            "fen": "8/8/8/1kp5/8/8/8/K7 w - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Kb1", "Kb4", "Kb2", "c4", "Kc2", "c3", "Kc1", "Kb3", "Kb1", "c2+", "Kc1", "Kc3"],
                            "notas": {
                                0: "Agora as **pretas** têm o peão, e a disputa pelas casas críticas (b3, c3 e d3) é mais acirrada.",
                                1: "**Oposição distante:** reis na mesma coluna com número ímpar de casas entre eles (3 ou 5). "
                                   "É um método eficaz para limitar o avanço do rei adversário.",
                                3: "Tomando de imediato a oposição direta e impedindo o rei de chegar às casas críticas.",
                                11: "Afogamento na sequência — empate.",
                            },
                            "marcas": {"b3": "critica", "c3": "critica", "d3": "critica"},
                            "legenda_marcas": "Casas críticas do peão em c5 (visto pelas pretas)",
                        },
                        {
                            "rotulo": "O tempo de reserva do peão",
                            "fen": "8/6k1/8/6K1/8/6P1/8/8 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["g4", "Kh7", "Kf6", "Kh8", "Kg6", "Kg8", "g5", "Kh8", "Kf7", "Kh7", "g6+", "Kh6", "g7"],
                            "notas": {
                                0: "Peão na terceira: casas críticas em f5, g5 e h5. O rei branco já está numa delas — "
                                   "mas como superar a oposição do rei adversário para continuar avançando?",
                                1: "Justamente com o **tempo de reserva do peão**. Como os reis estão em oposição, o peão avança "
                                   "e devolve o turno ao adversário.",
                                2: "Agora o rei alcança as novas casas críticas.",
                                6: "O tempo de reserva é usado uma segunda vez, pelo mesmo motivo.",
                            },
                            "marcas": {"f5": "critica", "g5": "critica", "h5": "critica"},
                            "legenda_marcas": "Casas críticas do peão em g3",
                        },
                    ],
                    "regras": [
                        "Se o rei do lado forte ocupa uma casa crítica, o peão promove — independentemente de quem joga.",
                        "Peão na quinta: casas críticas são as três casas imediatamente à frente.",
                        "Peão na segunda, terceira ou quarta: casas críticas são as três casas duas filas à frente.",
                        "A função da oposição é impedir o rei adversário de alcançar as casas críticas.",
                        "Com peão atrasado, o tempo de reserva do peão quebra a oposição.",
                    ],
                },
                {
                    "n": 4,
                    "titulo": "O peão de torre",
                    "conceito": "Rei defensor à frente do peão: empate sempre",
                    "texto": [
                        "Tudo o que foi dito até aqui vale para todos os peões, **menos o de torre**. Ele precisa de estudo separado.",
                        "O peão de torre é o mais difícil de promover, e a única forma de conseguir é com o caminho inteiro livre. "
                        "O motivo é simples: há afogamento assim que o peão chega à sétima defendido pelo rei, venha ele de onde vier.",
                        "Isso torna inúteis, para o peão de torre, todas as regras anteriores — chegada, oposição e casas críticas.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Empate com qualquer lado a jogar",
                            "fen": "8/8/8/8/8/6kp/8/6K1 w - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Kh1", "h2"],
                            "notas": {
                                0: "Não importa de quem é a vez: é sempre empate.",
                                1: "As brancas perdem a oposição, e não faz a menor diferença — há afogamento de qualquer maneira.",
                                2: "**Afogamento.**",
                            },
                        },
                        {
                            "rotulo": "Ter mais peões não ajuda",
                            "fen": "8/7p/7p/7p/7p/6kp/7p/6K1 w - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Kh1", "Kf3", "Kxh2", "Kg4", "Kh1", "Kg3", "Kg1", "h2+", "Kh1", "Kg4", "Kxh2", "h3", "Kh1", "Kg3", "Kg1"],
                            "notas": {
                                0: "Excepcionalmente, um diagrama com vários peões — para deixar claro o tamanho da limitação.",
                                1: "Com o rei defensor à frente, **nem com seis peões de torre** se ganha.",
                                7: "E de novo é preciso entregar o peão avançado para evitar o afogamento. "
                                   "Assim até perder todos, ou nunca avançá-los.",
                            },
                        },
                    ],
                    "regras": [
                        "Com peão de torre, se o rei defensor se coloca à frente do peão, é empate.",
                        "O peão de torre só promove com o caminho inteiramente livre.",
                        "O número de peões de torre é irrelevante: o afogamento não muda.",
                    ],
                },
                {
                    "n": 5,
                    "titulo": "O confinamento do rei forte",
                    "conceito": "A segunda forma de empatar contra o peão de torre",
                    "texto": [
                        "Colocar-se à frente do peão não é a única forma de empatar contra o peão de torre. "
                        "A proximidade da borda também restringe dramaticamente a mobilidade do rei do lado forte — "
                        "a ponto de ele mesmo ficar encerrado.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Brancas jogam e empatam",
                            "fen": "8/8/8/p7/8/1k6/3K4/8 w - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Kc1", "Ka2", "Kc2", "a4", "Kc1", "a3", "Kc2", "Ka1", "Kc1"],
                            "notas": {
                                0: "As pretas ameaçam ...Rb2, liberando o caminho do peão até o fim. Mas jogam as brancas.",
                                1: "Impedindo ...Rb2 e ameaçando Rb1. Contra **1...a4 2.Rb1 a3 3.Ra1** chega-se ao empate já conhecido.",
                                2: "Única forma de evitar que o rei branco se coloque à frente do peão — mas agora o rei preto perde a mobilidade "
                                   "e não conseguirá dar passagem ao próprio peão.",
                                3: "Agora as brancas não deixam o rei preto sair do canto. O resto é simples.",
                                8: "Não há o que fazer: o rei não sai, e se o peão avança, é ele que fica afogado.",
                            },
                            "marcas": {"c1": "critica", "c2": "critica"},
                            "legenda_marcas": "As duas casas que também garantem o empate",
                        },
                    ],
                    "regras": [
                        "Para empatar contra o peão de torre basta pôr o rei à frente dele...",
                        "...mas também basta ocupar uma das duas casas da coluna de bispo mais próxima (aqui, c1 ou c2).",
                        "Nessa configuração, peões de torre dobrados também não ajudam.",
                    ],
                },
            ],
        },
        {
            "id": "torre-bispo",
            "titulo": "Torre contra bispo",
            "resumo": (
                "Quase sempre empate. O que o lado do bispo precisa saber é qual canto evitar — "
                "e por que o outro canto é completamente seguro."
            ),
            "finais": [
                {
                    "n": 6,
                    "titulo": "Torre contra bispo: o canto ruim",
                    "conceito": "O canto da cor do bispo perde",
                    "texto": [
                        "A luta de torre contra bispo costuma terminar em empate, mas o lado fraco precisa tomar cuidado "
                        "com algumas posições quando o rei fica confinado à borda.",
                        "**O canto ruim é o da cor do bispo.** Levar o rei para lá é especialmente perigoso — e nesta posição, perde.",
                        "O método de ataque: obrigar o bispo a sair do esconderijo atrás do rei, para depois ameaçar mate na oitava fila "
                        "com ganho de tempo.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Brancas jogam e ganham",
                            "fen": "6k1/5R2/6K1/8/8/8/8/6b1 w - - 0 1",
                            "resultado": "Brancas ganham",
                            "linha": ["Rf1", "Bh2", "Rh1", "Bg3", "Rg1", "Bh2", "Rg2", "Bd6", "Rd2", "Be7", "Rc2", "Kf8", "Rc8+"],
                            "notas": {
                                0: "O rei preto não consegue se afastar do canto e perde, independentemente de onde esteja o bispo. "
                                   "O bispo está em g1 — casa escura — e h8, o canto para onde o rei foi empurrado, também é escura.",
                                1: "Atacando o bispo para forçá-lo a sair. Erro grave seria **1.Tb7??** ameaçando mate, "
                                   "porque após **1...Rf8** o rei preto não poderá mais ser obrigado a voltar ao canto ruim.",
                                6: "A torre toma duas das casas seguras, e o rei branco descoberto impede o acesso à terceira. "
                                   "O bispo é obrigado a sair para a zona onde a torre ganha o tempo decisivo.",
                                12: "E as pretas recebem mate.",
                            },
                        },
                    ],
                    "regras": [
                        "No final de torre contra bispo, o canto ruim é o da cor do bispo.",
                        "O método é forçar o bispo a sair de trás do rei, ganhando o tempo para o mate na oitava.",
                        "Cuidado com lances de ameaça precipitados que liberam a fuga do rei do canto ruim.",
                    ],
                },
                {
                    "n": 7,
                    "titulo": "Torre contra bispo: o canto bom",
                    "conceito": "O canto de cor oposta é seguro",
                    "texto": [
                        "No outro canto acontece exatamente o contrário. A defesa é tão fácil que é perfeitamente razoável "
                        "dirigir-se para lá desde o início.",
                        "O rei se instala no canto e o bispo fica pronto para cobri-lo em caso de xeque. "
                        "O atacante então precisa afrouxar a pressão para evitar o afogamento, e a posição se repete.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Empate — a defesa se repete",
                            "fen": "7k/R7/6K1/8/8/1b6/8/8 w - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Ra8+", "Bg8", "Ra7", "Bb3", "Ra8+", "Bg8", "Ra7", "Bc4"],
                            "notas": {
                                0: "O rei preto está no canto claro e o bispo é de casas claras — canto bom. Não há tentativa séria de ganho.",
                                1: "O bispo cobre o xeque.",
                                2: "Agora a torre ou o rei precisam afrouxar a pressão, para não afogar o adversário.",
                            },
                            "regra_destaque": "A única precaução do lado do bispo é mantê-lo a distância suficiente para dar xeque na diagonal b1-h7 quando necessário.",
                        },
                    ],
                    "regras": [
                        "O canto de cor oposta à do bispo é totalmente seguro.",
                        "O afogamento é o recurso que sustenta a defesa: o atacante sempre precisa afrouxar.",
                        "Mantenha o bispo a distância suficiente na diagonal para poder dar xeque quando necessário.",
                    ],
                },
            ],
        },
        {
            "id": "torre-cavalo",
            "titulo": "Torre contra cavalo",
            "resumo": (
                "Também empate na maioria das posições, com duas exceções que o lado do cavalo precisa "
                "conhecer de cor: separar o cavalo do rei, e ir para o canto."
            ),
            "finais": [
                {
                    "n": 8,
                    "titulo": "Torre contra cavalo: rei e cavalo na borda",
                    "conceito": "Mantenha o cavalo junto do rei",
                    "texto": [
                        "Contra a torre, o cavalo passa por dificuldades um pouco maiores que o bispo, embora a maioria das posições "
                        "seja empate. A recomendação é simples e vale quase sempre: **mantenha o cavalo perto do rei**. "
                        "Se o cavalo se afasta, costuma se perder.",
                        "Não há perigo em ter as duas peças rechaçadas para a borda — desde que não seja para o canto. "
                        "E esta posição tem importância teórica extra: ela aparece com frequência como resultado da luta de torre contra peão.",
                        "Com rei e cavalo juntos na borda, os lances costumam ser únicos — o que na prática ajuda, porque há menos chance de errar.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Brancas jogam e empatam",
                            "fen": "8/8/8/8/8/3k4/r7/3NK3 w - - 0 1",
                            "resultado": "Empate",
                            "linha": ["Nf2+", "Ke3", "Nd1+", "Kf3", "Nc3", "Rc2", "Nd1", "Re2+", "Kf1", "Rh2", "Ke1", "Rc2", "Kf1"],
                            "notas": {
                                0: "O primeiro lance é claramente único.",
                                1: "O segundo também, seguindo o critério de manter cavalo e rei unidos — embora aqui o xeque em g4 não perca.",
                                4: "Para o terceiro lance há duas opções que levam à mesma posição alguns lances depois. "
                                   "**3.Rf1 Re2 4.Cc3** é a alternativa, e é o único momento em que rei e cavalo se separam momentaneamente.",
                                7: "Única forma de afastar o rei do cavalo — mas só por um instante.",
                                10: "O rei volta imediatamente. A posição se repete e o empate está garantido.",
                            },
                        },
                        {
                            "rotulo": "Diagrama de análise: o que acontece se o cavalo se afasta",
                            "fen": "8/8/8/3N4/8/5k2/2r5/4K3 b - - 0 1",
                            "resultado": "Pretas ganham",
                            "linha": ["Rc4", "Nb6", "Rb4", "Nc8", "Rb7", "Kd2", "Kf4", "Ke2", "Ke5"],
                            "notas": {
                                0: "Esta posição vem de **4.Cd5??**, saindo a cavalgar pelo campo aberto. Uma vez afastado do rei, "
                                   "o cavalo provavelmente se perde — embora o processo de capturá-lo seja taticamente difícil.",
                                1: "Evitando o regresso por b4. O cavalo precisa ir ainda mais longe.",
                                2: "Se **5.Cf6 Rd4** corta quase todas as casas do cavalo.",
                                4: "Não dá para voltar: **6.Cd5 Te4+ 7.Rf1 Td4 8.Cc3 Td3** e as pretas ganham.",
                                5: "Todos os lances de cavalo estão direta ou indiretamente controlados.",
                                8: "E o rei preto vai capturá-lo. O importante não é decorar a análise — é saber que a separação deve ser evitada.",
                            },
                        },
                    ],
                    "regras": [
                        "Mantenha sempre o cavalo perto do rei.",
                        "Rei e cavalo na borda (fora do canto) é empate — e os lances costumam ser únicos.",
                        "O lado forte restringe o cavalo e usa xeques duplos e cravadas para fechar o cerco.",
                    ],
                },
                {
                    "n": 9,
                    "titulo": "Rei e cavalo no canto",
                    "conceito": "No canto, perde-se de imediato",
                    "texto": [
                        "Tudo muda se rei e cavalo estão no canto do tabuleiro — e não importa qual dos dois ocupa a casa da esquina. "
                        "A mobilidade das duas peças cai a tal ponto que a perda é imediata.",
                        "Há ainda um caso à parte: a casa **g2** (e suas simétricas) é especialmente desgraçada para o cavalo. "
                        "Com o cavalo ali, perde-se em muitas posições na borda — mesmo sem estar no canto. "
                        "É a primeira aparição da chamada **casa boba do cavalo**, e não será a última.",
                    ],
                    "posicoes": [
                        {
                            "rotulo": "Cavalo no canto",
                            "fen": "8/8/8/8/8/6k1/r7/6KN b - - 0 1",
                            "resultado": "Pretas ganham",
                            "linha": [],
                            "notas": {0: "Não é preciso análise nenhuma: as brancas perdem o cavalo imediatamente. "
                                         "(No diagrama do livro o cavalo em h1 já dá xeque ao rei em g3, então quem joga aqui são as pretas.)"},
                        },
                        {
                            "rotulo": "Rei no canto",
                            "fen": "8/8/8/8/8/6k1/r7/6NK w - - 0 1",
                            "resultado": "Pretas ganham",
                            "linha": [],
                            "notas": {0: "Mesma coisa com as peças trocadas de lugar. Não importa qual das duas ocupa a esquina."},
                        },
                        {
                            "rotulo": "A casa boba do cavalo (g2)",
                            "fen": "r7/8/8/8/8/6k1/6N1/7K w - - 0 1",
                            "resultado": "Pretas ganham",
                            "linha": [],
                            "notas": {0: "O caso mais chamativo: o cavalo se perde **apesar de não estar sequer na borda**. "
                                         "A casa g2 basta para condená-lo."},
                        },
                    ],
                    "regras": [
                        "Na luta de cavalo contra torre, o lado do cavalo deve evitar duas situações: separar o cavalo do rei, e ter ambas as peças no canto.",
                        "O cavalo na casa g2 (ou simétricas) já é suficiente para perder em muitas posições de borda.",
                    ],
                    "exemplo_pratico": {
                        "titulo": "Kamsky – Bacrot, Sófia 2006",
                        "texto": [
                            "Um final entre dois jogadores de elite que mistura as ideias dos dois últimos finais e mostra "
                            "como essa fase pode ser difícil na prática.",
                            "As pretas acabaram de promover a cavalo — que, como se verá adiante, é a forma típica de salvar essas posições — "
                            "e chegaram a um final teoricamente de empate. Mas há uma circunstância especial: "
                            "**o cavalo está a um pulo da sua casa boba (g2), e o rei está do lado do cavalo próximo a essa casa.** "
                            "Nesse caso a defesa é bem mais difícil.",
                        ],
                        "posicoes": [
                            {
                                "rotulo": "Posição do diagrama — brancas jogam",
                                "fen": "8/8/8/8/8/5K2/7R/4nk2 w - - 0 1",
                                "resultado": "Empate teórico",
                                "linha": ["Kg3", "Nd3", "Rd2", "Ne1", "Rf2+", "Kg1", "Rf8", "Ng2"],
                                "notas": {
                                    0: "Até aqui tudo é forçado.",
                                    7: "Agora aparece o primeiro incômodo: o cavalo tem que ir para a casa boba ou se afastar do rei. "
                                       "A mais intuitiva, **4...Cd3?**, perde por 5.Rf3 Ce1+ 6.Re2. Já **4...Cc2** empata e é a forma mais simples, "
                                       "embora afastar tanto o cavalo cause desconforto.",
                                },
                            },
                        ],
                        "fecho": "Na partida seguiu-se 5.Rf3 Rf1?, o lance realmente perdedor — com o cavalo naquela casa, perde-se quase sempre. "
                                 "A defesa correta, muito estreita, era 5...Ch4+ 6.Re3 Rg2 7.Tg8+ Rh3 8.Rf2 Rh2, repetindo a posição inicial na prática.",
                    },
                },
            ],
        },
    ],
}
