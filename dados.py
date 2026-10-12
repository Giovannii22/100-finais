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
    "1.24",           # Final 9 — Kamsky–Bacrot (posição do diagrama)
    "1.24.1",         # Final 9 — Kamsky–Bacrot, defesa correta depois de 5.Rf3 (derivada, não é do livro)
    "3.1",  # Capitulo 2
    "3.2",  # Capitulo 2
    "3.3",  # Capitulo 2
    "3.4",  # Capitulo 2
    "3.5–3.6",  # Capitulo 2
    "3.7",  # Capitulo 2
    "3.9",  # Capitulo 2
    "3.10",  # Capitulo 2
    "4.1",  # Capitulo 2
    "4.2",  # Capitulo 2
    "4.3",  # Capitulo 2
    "4.4",  # Capitulo 2
    "4.6",  # Capitulo 2
    "4.7",  # Capitulo 2
    "4.8",  # Capitulo 2
    "4.9",  # Capitulo 2
    "4.10–4.11",  # Capitulo 2
    "4.12",  # Capitulo 2
    "4.13",  # Capitulo 2
    "5.1",  # Capitulo 3
    "5.1 (pretas)",  # Capitulo 3
    "5.3",  # Capitulo 3
    "análise 5.3.1",  # Capitulo 3
    "análise 5.3.2",  # Capitulo 3
    "análise 5.3.3",  # Capitulo 3
    "5.4",  # Capitulo 3
    "5.5",  # Capitulo 3
    "5.5 (pretas)",  # Capitulo 3
    "análise 5.5.1",  # Capitulo 3
    "análise 5.5.2",  # Capitulo 3
    "análise 5.5.3",  # Capitulo 3
    "5.6",  # Capitulo 3
    "5.7",  # Capitulo 3
    "5.8",  # Capitulo 3
    "5.9",  # Capitulo 3
    "análise 5.10",  # Capitulo 3
    "5.11",  # Capitulo 3
    "5.12",  # Capitulo 3
    "5.13",  # Capitulo 3
    "5.14",  # Capitulo 3
    "análise 5.14.1",  # Capitulo 3
    "análise 5.14.2",  # Capitulo 3
    "análise 5.14.3",  # Capitulo 3
    "5.15",  # Capitulo 3
    "exemplo prático",  # Capitulo 3
]

CAPITULO_1 = {
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
                            "tempo_max": 60,  # cavalo x torre: sem bitbase e rico em xeques, pode precisar de mais que o padrao
                            "notas": {
                                0: "O primeiro lance é claramente único.",
                                1: "O segundo também, seguindo o critério de manter cavalo e rei unidos — embora aqui o xeque em g4 não perca.",
                                4: "Para o terceiro lance há duas opções que levam à mesma posição alguns lances depois — veja a linha alternativa abaixo.",
                                7: "Única forma de afastar o rei do cavalo — mas só por um instante.",
                                10: "O rei volta imediatamente. A posição se repete e o empate está garantido.",
                            },
                            "alternativas": [
                                {
                                    "titulo": "A separação momentânea do rei e do cavalo",
                                    "linha": ["Nf2+", "Ke3", "Nd1+", "Kf3", "Kf1", "Re2", "Nc3"],
                                    "nota": "Em vez de reagrupar na hora (3.Cc3), as brancas podem adiar um lance: 3.Rf1 obriga "
                                            "a torre preta a ir para e2, e só então o cavalo vai para c3. É o único momento em que "
                                            "rei e cavalo ficam temporariamente separados — mas c3 continua uma casa segura, e a "
                                            "posição volta a cair no mesmo tipo de fortaleza.",
                                },
                            ],
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
                                       "**4...Cd3?** perde por 5.Rf3 Ce1+ 6.Re2. A linha principal segue com o cavalo indo mesmo "
                                       "para a casa boba — veja a posição seguinte para o que aconteceu depois disso na partida.",
                                },
                                "alternativas": [
                                    {
                                        "titulo": "A defesa mais simples: cavalo para c2",
                                        "linha": ["Kg3", "Nd3", "Rd2", "Ne1", "Rf2+", "Kg1", "Rf8", "Nc2"],
                                        "nota": "Mais simples do que ir para a casa boba: afastar bastante o cavalo também empata, "
                                                "embora separar tanto as duas peças cause desconforto.",
                                    },
                                ],
                            },
                            {
                                "rotulo": "A defesa correta depois de 5.Rf3",
                                "fen": "5R2/8/8/8/8/6K1/6n1/6k1 w - - 8 5",
                                "resultado": "Empate teórico",
                                "linha": ["Kf3", "Nh4+", "Ke3", "Kg2", "Rg8+", "Kh3", "Kf2", "Kh2"],
                                "tempo_max": 60,  # mesmo material do Final 8: sem bitbase, pode precisar de mais tempo
                                "notas": {
                                    0: "Na partida, as brancas aproximaram o rei do cavalo na casa boba.",
                                    1: "A defesa correta e estreita: o cavalo dá xeque e ganha o tempo necessário para escapar de g2. "
                                       "Na partida real, as pretas erraram aqui com **5...Rf1??** — e com o cavalo na casa boba, "
                                       "esse erro quase sempre perde.",
                                    3: "O rei preto também precisa fugir da zona perigosa.",
                                    4: "A torre troca de coluna para dar o xeque que faltava.",
                                    7: "Posição-tipo de novo: cavalo e rei pretos lado a lado, perto da borda mas fora do canto — o mesmo padrão do Final 8.",
                                },
                                "profundidade": 30,
                            },
                        ],
                        "fecho": "Na partida seguiu-se 5.Rf3 Rf1??, o lance realmente perdedor — com o cavalo na casa boba, "
                                 "esse erro quase sempre perde. A defesa correta está na posição interativa acima.",
                    },
                },
            ],
        },
    ],
}

CAPITULO_2 = {   'numero': 2,
    'titulo': 'Cavalo e dama contra peão',
    'intro': 'Este capítulo cobre o duelo mais simples de peça menor contra peão passado — o '
             'cavalo — e o mais comum de todos os finais de dama — a dama contra peão, que costuma '
             'aparecer como desfecho natural de uma corrida de peões. São posições de cálculo '
             'preciso, cheias de regras curtas e memorizáveis, mas também de armadilhas conhecidas '
             'que continuam decidindo partidas de jogadores experientes.',
    'secoes': [   {   'id': 'cavalo-peao',
                      'titulo': 'Cavalo contra peão',
                      'resumo': 'Seis finais que ensinam quando um cavalo sozinho segura um peão '
                                'passado — incluindo as exceções perigosas dos peões de torre e de '
                                'cavalo, perto da borda.',
                      'finais': [   {   'n': 10,
                                        'titulo': 'Cavalo contra peão na sétima',
                                        'conceito': 'O cavalo sozinho consegue parar um peão que '
                                                    'já chegou à sétima fila?',
                                        'texto': [   'Este é o alicerce de todo o capítulo: se '
                                                     'dominarmos bem o duelo de cavalo contra '
                                                     'peão, depois será muito mais fácil calcular '
                                                     'finais parecidos com mais peças no '
                                                     "tabuleiro, e também 'sentir' com confiança "
                                                     'quando uma posição complexa se reduz a um '
                                                     'empate conhecido.',
                                                     'A ideia central é simples de enunciar: o '
                                                     'cavalo quer se colocar **à frente do peão**. '
                                                     'Uma vez ali, ele consegue manobrar para os '
                                                     'dois lados e nunca fica preso. Isso vale '
                                                     'para qualquer peão das quatro colunas '
                                                     'centrais (c, d, e, f), mesmo que ele já '
                                                     'esteja na sétima fila.',
                                                     'Mas nem sempre o cavalo chega a tempo de '
                                                     'bloquear o peão. A segunda posição deste '
                                                     'final mostra o que fazer quando isso não é '
                                                     'possível: em vez de ficar na frente, o '
                                                     'cavalo controla a casa de coroação **pelo '
                                                     'lado** — uma ideia menos intuitiva, mas '
                                                     'igualmente eficaz.'],
                                        'posicoes': [   {   'rotulo': 'O cavalo bloqueia o peão',
                                                            'fen': '8/K7/8/8/8/1k6/1N1p4/8 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': [   'Nd1',
                                                                         'Kc2',
                                                                         'Nf2',
                                                                         'Kc3',
                                                                         'Ka6',
                                                                         'Kd4',
                                                                         'Kb5',
                                                                         'Ke3',
                                                                         'Nd1+',
                                                                         'Ke2',
                                                                         'Nb2'],
                                                            'notas': {   0: 'O único lance, mas '
                                                                            'também o certo: o '
                                                                            'cavalo ocupa a casa '
                                                                            'de coroação. À frente '
                                                                            'do peão ele pode '
                                                                            'manobrar pelos dois '
                                                                            'lados e as pretas não '
                                                                            'conseguem criar '
                                                                            'problemas.',
                                                                         1: 'O rei preto ataca o '
                                                                            'cavalo — começa a '
                                                                            'única tentativa de '
                                                                            'progresso das pretas.',
                                                                         2: 'A forma mais simples '
                                                                            'de fugir: o cavalo se '
                                                                            'afasta do rei '
                                                                            'adversário. **2.Ne3** '
                                                                            'também empatava.',
                                                                         3: 'Sem conseguir nada em '
                                                                            'c3, o rei preto '
                                                                            'precisa iniciar uma '
                                                                            'longa caminhada até o '
                                                                            'outro lado para '
                                                                            'atacar o cavalo de '
                                                                            'novo.',
                                                                         4: 'Lances de espera do '
                                                                            'rei branco: o cavalo '
                                                                            'em f2 já controla d1 '
                                                                            "'pelo lado' (a mesma "
                                                                            'ideia da próxima '
                                                                            'posição), então o '
                                                                            'peão não pode coroar '
                                                                            'enquanto o rei preto '
                                                                            'não chega perto o '
                                                                            'bastante.',
                                                                         8: 'Quando o rei preto '
                                                                            'finalmente ameaça o '
                                                                            'cavalo em f2, ele '
                                                                            'volta à casa de '
                                                                            'coroação — e ainda dá '
                                                                            'xeque de quebra.',
                                                                         10: 'A posição do lance 2 '
                                                                             'se reproduz, agora '
                                                                             'do lado oposto. '
                                                                             'Empate evidente: as '
                                                                             'pretas podem repetir '
                                                                             'a caminhada para o '
                                                                             'outro lado, mas o '
                                                                             'resultado nunca '
                                                                             'muda.'},
                                                            'regra_destaque': 'Se o cavalo '
                                                                              'consegue se colocar '
                                                                              'à frente do peão, é '
                                                                              'empate contra '
                                                                              'qualquer peão das '
                                                                              'quatro colunas '
                                                                              'centrais, mesmo na '
                                                                              'sétima fila.'},
                                                        {   'rotulo': 'Controlando a casa de '
                                                                      'coroação pelo lado',
                                                            'fen': '8/8/8/8/5N2/8/2p4K/2k5 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': [   'Ne2+',
                                                                         'Kd1',
                                                                         'Nc3+',
                                                                         'Kd2',
                                                                         'Na2'],
                                                            'notas': {   0: 'O cavalo não chega a '
                                                                            'tempo de bloquear o '
                                                                            'peão em c1, mas pode '
                                                                            'controlá-lo de outra '
                                                                            'forma: colocando-se '
                                                                            'na segunda fila, em '
                                                                            'e2, ele ameaça o '
                                                                            'circuito e2-c3-a2, '
                                                                            'que termina '
                                                                            'controlando c1 à '
                                                                            'distância, pela '
                                                                            'diagonal do cavalo.',
                                                                         1: '**1...Rd2 empata na '
                                                                            'hora**: o cavalo '
                                                                            'simplesmente fica em '
                                                                            'e2, controlando c1 '
                                                                            'para sempre. A linha '
                                                                            'principal é a réplica '
                                                                            'mais exigente, '
                                                                            '**1...Rd1**, que '
                                                                            'tenta expulsar o '
                                                                            'cavalo do circuito '
                                                                            'bom — e aqui o peão '
                                                                            '**não pode coroar '
                                                                            'ainda**: **2.Nc3+** é '
                                                                            'xeque, então as '
                                                                            'pretas são obrigadas '
                                                                            'a responder a ele '
                                                                            'antes de pensar em '
                                                                            'promover.',
                                                                         2: 'O xeque é essencial: '
                                                                            'sem ele, as pretas '
                                                                            'simplesmente '
                                                                            'coroariam a dama em '
                                                                            'vez de responder ao '
                                                                            'cavalo (veja o aviso '
                                                                            'ao lado — **2.Nd4?** '
                                                                            'erra exatamente por '
                                                                            'não dar xeque).',
                                                                         4: 'O cavalo chega à casa '
                                                                            'ideal (a2) e mantém o '
                                                                            'controle de c1 '
                                                                            'indefinidamente.'},
                                                            'alternativas': [   {   'titulo': 'O '
                                                                                              'lance '
                                                                                              'natural '
                                                                                              'que '
                                                                                              'perde',
                                                                                    'linha': [   'Nd3+',
                                                                                                 'Kd2',
                                                                                                 'Nc5',
                                                                                                 'Kc3',
                                                                                                 'Ne4+',
                                                                                                 'Kd3',
                                                                                                 'Nc5+',
                                                                                                 'Kc4'],
                                                                                    'nota': '**1.Nd3+??** '
                                                                                            'parece '
                                                                                            'controlar '
                                                                                            'o '
                                                                                            'mesmo '
                                                                                            'tipo '
                                                                                            'de '
                                                                                            'casa, '
                                                                                            'mas '
                                                                                            'expulsa '
                                                                                            'o '
                                                                                            'próprio '
                                                                                            'cavalo '
                                                                                            'do '
                                                                                            'circuito '
                                                                                            'bom: '
                                                                                            'depois '
                                                                                            'de '
                                                                                            '**1...Rd2!** '
                                                                                            'não '
                                                                                            'há '
                                                                                            'mais '
                                                                                            'como '
                                                                                            'impedir '
                                                                                            'a '
                                                                                            'coroação. '
                                                                                            '**2.Nc5!?** '
                                                                                            'é a '
                                                                                            'última '
                                                                                            'armadilha '
                                                                                            '— um '
                                                                                            'erro '
                                                                                            'de '
                                                                                            'cálculo '
                                                                                            'típico '
                                                                                            'deste '
                                                                                            'final, '
                                                                                            'porque '
                                                                                            'parece '
                                                                                            'reconquistar '
                                                                                            'o '
                                                                                            'controle '
                                                                                            '— mas '
                                                                                            '**2...Rc3!** '
                                                                                            'evita '
                                                                                            'o '
                                                                                            'truque, '
                                                                                            'ameaça '
                                                                                            'a '
                                                                                            'coroação '
                                                                                            'e '
                                                                                            'controla '
                                                                                            'as '
                                                                                            'duas '
                                                                                            'casas '
                                                                                            "'boas' "
                                                                                            'do '
                                                                                            'cavalo '
                                                                                            '(b3 e '
                                                                                            'd3). '
                                                                                            'Todas '
                                                                                            'as '
                                                                                            'réplicas '
                                                                                            'já '
                                                                                            'perdem; '
                                                                                            'o '
                                                                                            'resto '
                                                                                            'é só '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'se '
                                                                                            'debatendo '
                                                                                            'antes '
                                                                                            'do '
                                                                                            'peão '
                                                                                            'coroar.'},
                                                                                {   'titulo': '2.Cd4?? '
                                                                                              '— '
                                                                                              'por '
                                                                                              'que '
                                                                                              'precisa '
                                                                                              'ser '
                                                                                              'xeque',
                                                                                    'linha': [   'Ne2+',
                                                                                                 'Kd1',
                                                                                                 'Nd4',
                                                                                                 'c1=Q'],
                                                                                    'nota': 'Depois '
                                                                                            'de '
                                                                                            '**1...Rd1**, '
                                                                                            'trocar '
                                                                                            'de '
                                                                                            'circuito '
                                                                                            'sem '
                                                                                            'dar '
                                                                                            'xeque '
                                                                                            'é um '
                                                                                            'erro '
                                                                                            'decisivo: '
                                                                                            'como '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'deixa '
                                                                                            'de '
                                                                                            'controlar '
                                                                                            'c1 '
                                                                                            'por '
                                                                                            'um '
                                                                                            'instante '
                                                                                            'e as '
                                                                                            'brancas '
                                                                                            'não '
                                                                                            'ameaçam '
                                                                                            'nada, '
                                                                                            'as '
                                                                                            'pretas '
                                                                                            'têm '
                                                                                            'tempo '
                                                                                            'de '
                                                                                            'simplesmente '
                                                                                            'coroar '
                                                                                            'a '
                                                                                            'dama '
                                                                                            '— e '
                                                                                            'ganham. '
                                                                                            'É por '
                                                                                            'isso '
                                                                                            'que a '
                                                                                            'linha '
                                                                                            'principal '
                                                                                            'insiste '
                                                                                            'em '
                                                                                            '**2.Nc3+**: '
                                                                                            'só o '
                                                                                            'xeque '
                                                                                            'garante '
                                                                                            'que '
                                                                                            'as '
                                                                                            'pretas '
                                                                                            'não '
                                                                                            'têm '
                                                                                            'essa '
                                                                                            'folga.'}]}],
                                        'regras': [   'Contra qualquer peão das quatro colunas '
                                                      'centrais (c, d, e, f) na sétima fila: se o '
                                                      'cavalo consegue se colocar à frente do '
                                                      'peão, é empate.',
                                                      'Se não consegue se colocar à frente, mas '
                                                      "controla a casa de coroação 'pelo lado' (a "
                                                      'partir da segunda fila, na mesma fila da '
                                                      'casa de coroação), também é empate.',
                                                      'Se não consegue nenhuma das duas coisas, o '
                                                      'peão coroa.']},
                                    {   'n': 11,
                                        'titulo': 'O peão de cavalo',
                                        'conceito': 'Por que o peão de cavalo (coluna b ou g) '
                                                    'quebra a regra do final anterior?',
                                        'texto': [   'Até agora falamos sempre de peões das quatro '
                                                     'colunas centrais. Com os dois peões mais '
                                                     'próximos da borda — o peão de cavalo e o '
                                                     'peão de torre — aparecem exceções, porque a '
                                                     'proximidade do canto tira do cavalo a '
                                                     'liberdade de manobrar para os dois lados.',
                                                     'O peão de cavalo na sétima é o primeiro '
                                                     'caso, e o mais drástico: se o cavalo não '
                                                     'consegue se colocar à frente do peão a '
                                                     'tempo, **não existe mais a alternativa de '
                                                     'controlar a casa de coroação pelo lado.** Do '
                                                     'lado do canto, o cavalo simplesmente não tem '
                                                     'essa casa boa.'],
                                        'posicoes': [   {   'rotulo': 'O cavalo não chega a tempo',
                                                            'fen': '8/8/8/8/4N3/1p6/7K/1k6 b - - 0 '
                                                                   '1',
                                                            'resultado': 'Pretas ganham',
                                                            'linha': [   'b2',
                                                                         'Nd2+',
                                                                         'Kc1',
                                                                         'Nb3+',
                                                                         'Kd1'],
                                                            'notas': {   0: '**1...b2!** — um '
                                                                            'lance excelente e '
                                                                            'fácil de encontrar, '
                                                                            'sabendo a regra: com '
                                                                            'o peão de cavalo na '
                                                                            'sétima, se o cavalo '
                                                                            'não consegue se '
                                                                            'colocar à frente '
                                                                            'dele, não há como '
                                                                            'detê-lo.',
                                                                         1: 'O único xeque '
                                                                            'disponível, mas o '
                                                                            'cavalo não tem mais '
                                                                            'recursos depois dele.',
                                                                         2: 'Aqui está a diferença '
                                                                            'em relação ao peão '
                                                                            'central: do outro '
                                                                            'lado do peão não '
                                                                            "existe 'casa boa' "
                                                                            'para o cavalo '
                                                                            'continuar controlando '
                                                                            'a coroação.',
                                                                         4: 'E o peão promove no '
                                                                            'lance seguinte — o '
                                                                            'cavalo esgotou os '
                                                                            'xeques.'},
                                                            'alternativas': [   {   'titulo': 'O '
                                                                                              'erro '
                                                                                              'que '
                                                                                              'salva '
                                                                                              'as '
                                                                                              'brancas: '
                                                                                              '1...Rc2?',
                                                                                    'linha': [   'Kc2',
                                                                                                 'Nd6',
                                                                                                 'Kc3',
                                                                                                 'Ne4+',
                                                                                                 'Kd4',
                                                                                                 'Nd2',
                                                                                                 'b2',
                                                                                                 'Nb1',
                                                                                                 'Kd3',
                                                                                                 'Kg2',
                                                                                                 'Kc2',
                                                                                                 'Na3+',
                                                                                                 'Kb3',
                                                                                                 'Nb1'],
                                                                                    'nota': 'Tentar '
                                                                                            'impedir '
                                                                                            'a '
                                                                                            'aproximação '
                                                                                            'do '
                                                                                            'cavalo '
                                                                                            'com o '
                                                                                            'rei, '
                                                                                            'em '
                                                                                            'vez '
                                                                                            'de '
                                                                                            'empurrar '
                                                                                            'o '
                                                                                            'peão '
                                                                                            'imediatamente, '
                                                                                            'é um '
                                                                                            'erro '
                                                                                            'instrutivo. '
                                                                                            '**2.Nd6!** '
                                                                                            'é o '
                                                                                            'detalhe '
                                                                                            'tático '
                                                                                            'que '
                                                                                            'salva '
                                                                                            'as '
                                                                                            'brancas: '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'se '
                                                                                            'afasta '
                                                                                            'temporariamente '
                                                                                            'do '
                                                                                            'peão '
                                                                                            '— um '
                                                                                            'recurso '
                                                                                            'muito '
                                                                                            'comum '
                                                                                            'nesta '
                                                                                            'luta '
                                                                                            '— '
                                                                                            'porque '
                                                                                            'mesmo '
                                                                                            'longe '
                                                                                            'ele '
                                                                                            'volta '
                                                                                            'a '
                                                                                            'tempo '
                                                                                            'de '
                                                                                            'bloquear. '
                                                                                            'Depois '
                                                                                            'de '
                                                                                            '**4...b2 '
                                                                                            '5.Nb1** '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'já '
                                                                                            'está '
                                                                                            'à '
                                                                                            'frente '
                                                                                            'do '
                                                                                            'peão, '
                                                                                            'e '
                                                                                            'embora '
                                                                                            'tenha '
                                                                                            'menos '
                                                                                            'mobilidade '
                                                                                            'que '
                                                                                            'no '
                                                                                            'caso '
                                                                                            'central '
                                                                                            '(o '
                                                                                            'canto '
                                                                                            'limita '
                                                                                            'seus '
                                                                                            'saltos), '
                                                                                            'ainda '
                                                                                            'é '
                                                                                            'suficiente: '
                                                                                            'quando '
                                                                                            'o rei '
                                                                                            'preto '
                                                                                            'finalmente '
                                                                                            'ataca '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'em '
                                                                                            'b1, '
                                                                                            '**7.Na3+!** '
                                                                                            'dá um '
                                                                                            'xeque '
                                                                                            'de '
                                                                                            'desvio '
                                                                                            'que '
                                                                                            'ganha '
                                                                                            'o '
                                                                                            'tempo '
                                                                                            'necessário '
                                                                                            'para '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'voltar '
                                                                                            'à '
                                                                                            'casa '
                                                                                            'de '
                                                                                            'bloqueio. '
                                                                                            'O '
                                                                                            'cerco '
                                                                                            'nunca '
                                                                                            'se '
                                                                                            'fecha.'}]}],
                                        'regras': [   'Com o peão de cavalo na sétima: se o cavalo '
                                                      'se coloca à frente do peão, é empate.',
                                                      'Se o cavalo não consegue se colocar à '
                                                      'frente, o peão coroa — ao contrário do peão '
                                                      'central, aqui não existe a opção de '
                                                      'controlar a casa de coroação pelo lado.']},
                                    {   'n': 12,
                                        'titulo': 'O peão de torre na sexta',
                                        'conceito': 'Com o peão mais perigoso de todos — o de '
                                                    'torre — o que muda em relação ao peão '
                                                    'central?',
                                        'texto': [   'Como quase sempre no xadrez, o peão de torre '
                                                     'tem regras próprias. Na luta do cavalo '
                                                     'contra peão, ele é o mais perigoso dos oito: '
                                                     'a proximidade da borda tira do cavalo boa '
                                                     'parte da liberdade de manobra.',
                                                     'Começamos pelo peão de torre na sexta fila — '
                                                     'aqui, por sorte, as chances de empate ainda '
                                                     'são parecidas com as do peão central na '
                                                     'sétima.',
                                                     'Se o cavalo consegue a casa à frente do '
                                                     'peão, não há problema. Se só consegue '
                                                     'controlar a casa de avanço, então o empate '
                                                     'exige encontrar o **circuito certo**: no '
                                                     'caso do peão h, as quatro casas '
                                                     'g4-e3-f1-h2.'],
                                        'posicoes': [   {   'rotulo': 'O circuito correto',
                                                            'fen': '8/8/K7/4N3/8/7p/7k/8 w - - 0 1',
                                                            'resultado': 'Empate',
                                                            'linha': [   'Ng4+',
                                                                         'Kg3',
                                                                         'Ne3',
                                                                         'Kf3',
                                                                         'Nf1',
                                                                         'Kf2',
                                                                         'Nh2'],
                                                            'notas': {   0: 'O cavalo entra direto '
                                                                            'no circuito certo.',
                                                                         6: 'O cavalo roda pelas '
                                                                            'quatro casas do '
                                                                            'circuito '
                                                                            '(h2-f1-e3-g4) e o rei '
                                                                            'preto nunca consegue '
                                                                            'expulsá-lo de lá. '
                                                                            'Empate.'},
                                                            'alternativas': [   {   'titulo': 'Outro '
                                                                                              'caminho '
                                                                                              'até '
                                                                                              'o '
                                                                                              'circuito: '
                                                                                              '1.Nc4',
                                                                                    'linha': [   'Nc4',
                                                                                                 'Kg2',
                                                                                                 'Ne3+'],
                                                                                    'nota': 'Também '
                                                                                            'empata, '
                                                                                            'graças '
                                                                                            'a um '
                                                                                            'detalhe '
                                                                                            'tático '
                                                                                            'curioso '
                                                                                            'e um '
                                                                                            'tanto '
                                                                                            'paradoxal: '
                                                                                            'partindo '
                                                                                            'de '
                                                                                            'longe '
                                                                                            '(como '
                                                                                            'aqui), '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'consegue '
                                                                                            'atravessar '
                                                                                            'o '
                                                                                            'tabuleiro '
                                                                                            'a '
                                                                                            'tempo '
                                                                                            'de '
                                                                                            'encontrar '
                                                                                            'o '
                                                                                            'circuito '
                                                                                            'certo, '
                                                                                            'usando '
                                                                                            'os '
                                                                                            'xeques '
                                                                                            'como '
                                                                                            'atalho '
                                                                                            '— '
                                                                                            'algo '
                                                                                            'que, '
                                                                                            'veremos '
                                                                                            'a '
                                                                                            'seguir, '
                                                                                            'nem '
                                                                                            'sempre '
                                                                                            'funciona '
                                                                                            'partindo '
                                                                                            'de '
                                                                                            'perto.'},
                                                                                {   'titulo': '1.Nc4 '
                                                                                              'Rg1 '
                                                                                              '— o '
                                                                                              'detalhe '
                                                                                              'que '
                                                                                              'falta '
                                                                                              'explorar',
                                                                                    'linha': [   'Nc4',
                                                                                                 'Kg1',
                                                                                                 'Ne5',
                                                                                                 'Kf1',
                                                                                                 'Ng4'],
                                                                                    'nota': 'O '
                                                                                            'ponto '
                                                                                            'fino '
                                                                                            'da '
                                                                                            'linha: '
                                                                                            'com o '
                                                                                            'rei '
                                                                                            'em g1 '
                                                                                            'o '
                                                                                            'peão '
                                                                                            'não '
                                                                                            'consegue '
                                                                                            'avançar, '
                                                                                            'e o '
                                                                                            'cavalo '
                                                                                            'chega '
                                                                                            'a g4 '
                                                                                            'de '
                                                                                            'qualquer '
                                                                                            'forma '
                                                                                            '— o '
                                                                                            'circuito '
                                                                                            'certo, '
                                                                                            'outra '
                                                                                            'vez.'},
                                                                                {   'titulo': '1.Nc4 '
                                                                                              'Rg3 '
                                                                                              '— '
                                                                                              'ainda '
                                                                                              'mais '
                                                                                              'direto',
                                                                                    'linha': [   'Nc4',
                                                                                                 'Kg3',
                                                                                                 'Ne3'],
                                                                                    'nota': 'O '
                                                                                            'caminho '
                                                                                            'mais '
                                                                                            'curto '
                                                                                            'de '
                                                                                            'todos '
                                                                                            'até a '
                                                                                            'casa '
                                                                                            'e3, '
                                                                                            'dentro '
                                                                                            'do '
                                                                                            'circuito.'},
                                                                                {   'titulo': 'O '
                                                                                              'erro '
                                                                                              'aparentemente '
                                                                                              'natural: '
                                                                                              '1.Nf3+?',
                                                                                    'linha': [   'Nf3+',
                                                                                                 'Kg2',
                                                                                                 'Nh4+',
                                                                                                 'Kf2'],
                                                                                    'nota': 'Parece '
                                                                                            'levar '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'para '
                                                                                            'perto '
                                                                                            'da '
                                                                                            'ação, '
                                                                                            'mas '
                                                                                            'na '
                                                                                            'verdade '
                                                                                            'o '
                                                                                            'joga '
                                                                                            'num '
                                                                                            '**circuito '
                                                                                            'errado**, '
                                                                                            'do '
                                                                                            'qual '
                                                                                            'acaba '
                                                                                            'sendo '
                                                                                            'expulso '
                                                                                            'pelo '
                                                                                            'próprio '
                                                                                            'rei '
                                                                                            'adversário '
                                                                                            '— e o '
                                                                                            'peão '
                                                                                            'corona.'},
                                                                                {   'titulo': '1.Nf3+? '
                                                                                              'Rg2 '
                                                                                              '2.Ne1+ '
                                                                                              '— '
                                                                                              'mesmo '
                                                                                              'problema',
                                                                                    'linha': [   'Nf3+',
                                                                                                 'Kg2',
                                                                                                 'Ne1+',
                                                                                                 'Kg3'],
                                                                                    'nota': 'Qualquer '
                                                                                            'xeque '
                                                                                            'a '
                                                                                            'partir '
                                                                                            'do '
                                                                                            'circuito '
                                                                                            'errado '
                                                                                            'só '
                                                                                            'adia '
                                                                                            'o '
                                                                                            'problema: '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'acaba '
                                                                                            'preso '
                                                                                            'e '
                                                                                            'perdido.',
                                                                                    'espera_resultado': 'erro'}]}],
                                        'regras': [   'O cavalo empata contra o peão de torre na '
                                                      'sexta se consegue se colocar à frente dele.',
                                                      'Se só controla a casa de avanço, precisa '
                                                      'fazer isso a partir do circuito correto '
                                                      '(g4-e3-f1, visando o canto h1) — e não a '
                                                      'partir de f3, que é um circuito errado.']},
                                    {   'n': 13,
                                        'titulo': 'O peão de torre na sétima — a barreira',
                                        'conceito': 'Com o peão já na sétima, o cavalo sozinho não '
                                                    'segura mais nada — mas ainda pode ganhar '
                                                    'tempo?',
                                        'texto': [   'Falta analisar o caso mais extremo: o peão '
                                                     'de torre na sétima fila. Aqui o cavalo '
                                                     'sempre pode ser expulsado ou capturado pelo '
                                                     'rei adversário — sozinho, ele não seca mais '
                                                     'o peão. As esperanças de empate dependem da '
                                                     'ajuda do próprio rei, mas são bem maiores do '
                                                     'que parece à primeira vista.',
                                                     'O recurso chave é a **barreira**: mesmo sem '
                                                     'conseguir deter o peão, o cavalo consegue '
                                                     'ocupar uma casa a partir da qual controla '
                                                     'uma diagonal inteira de casas, impedindo o '
                                                     'rei adversário de atravessá-la em linha '
                                                     'reta. O rei preto precisa contornar essa '
                                                     'barreira por um caminho bem mais longo — e é '
                                                     'exatamente esse tempo extra que permite ao '
                                                     'rei branco chegar a tempo de ajudar.'],
                                        'posicoes': [   {   'rotulo': 'A primeira barreira',
                                                            'fen': 'K7/8/8/5N2/8/3k3p/8/8 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': ['Ng3', 'h2', 'Kb7'],
                                                            'notas': {   0: 'O rei branco está '
                                                                            'muito longe, e à '
                                                                            'primeira vista parece '
                                                                            'desesperador para o '
                                                                            'lado do cavalo — mas '
                                                                            'é empate.',
                                                                         2: 'O cavalo já ergueu '
                                                                            'uma barreira: as '
                                                                            'casas d2-e2-e3-e4, em '
                                                                            'forma de L, impedem o '
                                                                            'rei preto de '
                                                                            'atravessar direto. '
                                                                            'Para contorná-la ele '
                                                                            'precisa de uma rota '
                                                                            'bem mais longa — '
                                                                            'd4-e5-f4 ou '
                                                                            'c2-d1-e1-f2 — e '
                                                                            'qualquer uma das duas '
                                                                            'dá tempo ao rei '
                                                                            'branco de se '
                                                                            'aproximar.'},
                                                            'alternativas': [   {   'titulo': '1...Rc2 '
                                                                                              '— '
                                                                                              'contornando '
                                                                                              'a '
                                                                                              'barreira '
                                                                                              'por '
                                                                                              'baixo',
                                                                                    'linha': [   'Ng3',
                                                                                                 'h2',
                                                                                                 'Kb7',
                                                                                                 'Kc2',
                                                                                                 'Kc6',
                                                                                                 'Kd1',
                                                                                                 'Kd5',
                                                                                                 'Ke1',
                                                                                                 'Ke4',
                                                                                                 'Kf2',
                                                                                                 'Kf4'],
                                                                                    'nota': 'O '
                                                                                            'caminho '
                                                                                            'por '
                                                                                            'baixo '
                                                                                            'também '
                                                                                            'é '
                                                                                            'muito '
                                                                                            'longo, '
                                                                                            'e dá '
                                                                                            'exatamente '
                                                                                            'o '
                                                                                            'mesmo '
                                                                                            'tempo '
                                                                                            'ao '
                                                                                            'rei '
                                                                                            'branco.'},
                                                                                {   'titulo': '1...Re3 '
                                                                                              '— '
                                                                                              'tentando '
                                                                                              'evitar '
                                                                                              'a '
                                                                                              'barreira '
                                                                                              'logo '
                                                                                              'de '
                                                                                              'início',
                                                                                    'linha': [   'Ng3',
                                                                                                 'Ke3',
                                                                                                 'Nf1+'],
                                                                                    'nota': 'Em '
                                                                                            'vez '
                                                                                            'de '
                                                                                            'deixar '
                                                                                            'o '
                                                                                            'peão '
                                                                                            'avançar, '
                                                                                            'as '
                                                                                            'pretas '
                                                                                            'tentam '
                                                                                            'atacar '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'direto '
                                                                                            '— mas '
                                                                                            'ele '
                                                                                            'chega '
                                                                                            'a h2 '
                                                                                            'de '
                                                                                            'qualquer '
                                                                                            'forma, '
                                                                                            'com '
                                                                                            'xeque.'},
                                                                                {   'titulo': '1...Rd4 '
                                                                                              '— '
                                                                                              'contornando '
                                                                                              'a '
                                                                                              'barreira '
                                                                                              'por '
                                                                                              'cima',
                                                                                    'linha': [   'Ng3',
                                                                                                 'h2',
                                                                                                 'Kb7',
                                                                                                 'Kd4',
                                                                                                 'Kc6',
                                                                                                 'Ke5',
                                                                                                 'Kc5',
                                                                                                 'Kf4',
                                                                                                 'Nh1',
                                                                                                 'Kf3',
                                                                                                 'Kd4',
                                                                                                 'Kg2',
                                                                                                 'Ke3',
                                                                                                 'Kxh1',
                                                                                                 'Kf2'],
                                                                                    'nota': 'O rei '
                                                                                            'branco '
                                                                                            'chega '
                                                                                            'bem a '
                                                                                            'tempo '
                                                                                            'de '
                                                                                            'ocupar '
                                                                                            'f2 '
                                                                                            'assim '
                                                                                            'que o '
                                                                                            'cavalo '
                                                                                            'precisa '
                                                                                            'se '
                                                                                            'refugiar '
                                                                                            'em h1 '
                                                                                            '— '
                                                                                            'mesmo '
                                                                                            'deixando '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'cair, '
                                                                                            'o '
                                                                                            'resultado '
                                                                                            'é '
                                                                                            'empate: '
                                                                                            'o rei '
                                                                                            'preto '
                                                                                            'fica '
                                                                                            'preso '
                                                                                            'no '
                                                                                            'canto, '
                                                                                            'bloqueando '
                                                                                            'o '
                                                                                            'próprio '
                                                                                            'peão.'},
                                                                                {   'titulo': '1...Rd4 '
                                                                                              '— '
                                                                                              'variante '
                                                                                              'com '
                                                                                              'o '
                                                                                              'cavalo '
                                                                                              'recuando '
                                                                                              'antes',
                                                                                    'linha': [   'Ng3',
                                                                                                 'h2',
                                                                                                 'Kb7',
                                                                                                 'Kd4',
                                                                                                 'Kc6',
                                                                                                 'Ke5',
                                                                                                 'Nh1',
                                                                                                 'Ke4',
                                                                                                 'Kc5'],
                                                                                    'nota': 'O '
                                                                                            'cavalo '
                                                                                            'também '
                                                                                            'pode '
                                                                                            'recuar '
                                                                                            'a h1 '
                                                                                            'um '
                                                                                            'pouco '
                                                                                            'antes, '
                                                                                            'sem '
                                                                                            'alterar '
                                                                                            'o '
                                                                                            'resultado.'}]},
                                                        {   'rotulo': 'A outra barreira (final de '
                                                                      'um estudo de Grigoriev)',
                                                            'fen': '8/2K5/8/8/4N3/2k5/7p/8 b - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': [   'Kc2',
                                                                         'Ng3',
                                                                         'Kd1',
                                                                         'Kd6',
                                                                         'Ke1',
                                                                         'Ke5',
                                                                         'Kf2',
                                                                         'Kf4'],
                                                            'notas': {   0: 'Começando em e4, o '
                                                                            'cavalo consegue deter '
                                                                            'o peão e construir '
                                                                            'barreiras tanto a '
                                                                            'partir de f2 quanto '
                                                                            'de g3 — a escolha '
                                                                            'depende de para onde '
                                                                            'o rei preto for.',
                                                                         1: 'O cavalo escolhe o '
                                                                            'circuito certo para '
                                                                            'esta posição do rei '
                                                                            'preto.'},
                                                            'alternativas': [   {   'titulo': '2.Nf2? '
                                                                                              '— o '
                                                                                              'circuito '
                                                                                              'errado '
                                                                                              'perde',
                                                                                    'linha': [   'Kc2',
                                                                                                 'Nf2',
                                                                                                 'Kd2'],
                                                                                    'nota': 'Com o '
                                                                                            'rei '
                                                                                            'já '
                                                                                            'perto '
                                                                                            'do '
                                                                                            'lado '
                                                                                            'd, '
                                                                                            'este '
                                                                                            'circuito '
                                                                                            'não '
                                                                                            'segura '
                                                                                            'mais '
                                                                                            'nada.'},
                                                                                {   'titulo': '1...Rd3 '
                                                                                              '— '
                                                                                              'transpõe '
                                                                                              'para '
                                                                                              'a '
                                                                                              'barreira '
                                                                                              'já '
                                                                                              'conhecida',
                                                                                    'linha': [   'Kd3',
                                                                                                 'Ng3',
                                                                                                 'Kc2',
                                                                                                 'Kd6',
                                                                                                 'Kd1',
                                                                                                 'Ke5',
                                                                                                 'Ke1',
                                                                                                 'Kf4'],
                                                                                    'nota': 'Um '
                                                                                            'pouco '
                                                                                            'imprecisa, '
                                                                                            'mas '
                                                                                            'transpõe '
                                                                                            'para '
                                                                                            'a '
                                                                                            'mesma '
                                                                                            'barreira '
                                                                                            'em L '
                                                                                            'da '
                                                                                            'posição '
                                                                                            'anterior.'},
                                                                                {   'titulo': '1...Rd4 '
                                                                                              '— '
                                                                                              'uma '
                                                                                              'barreira '
                                                                                              'diferente',
                                                                                    'linha': [   'Kd4',
                                                                                                 'Nf2'],
                                                                                    'nota': 'Agora '
                                                                                            'aparece '
                                                                                            'uma '
                                                                                            'segunda '
                                                                                            'barreira, '
                                                                                            'com '
                                                                                            'outra '
                                                                                            'forma '
                                                                                            'de L '
                                                                                            '(casas '
                                                                                            'e5-e4-e3-d3) '
                                                                                            '— a '
                                                                                            'mais '
                                                                                            'incômoda '
                                                                                            'possível '
                                                                                            'para '
                                                                                            'esta '
                                                                                            'posição '
                                                                                            'do '
                                                                                            'rei '
                                                                                            'preto.'},
                                                                                {   'titulo': '1...Rd4 '
                                                                                              '2.Ng3?? '
                                                                                              '— o '
                                                                                              'circuito '
                                                                                              'errado '
                                                                                              'desta '
                                                                                              'vez',
                                                                                    'linha': [   'Kd4',
                                                                                                 'Ng3',
                                                                                                 'Ke5',
                                                                                                 'Kc6',
                                                                                                 'Kf4',
                                                                                                 'Nh1',
                                                                                                 'Kf3'],
                                                                                    'nota': 'Escolher '
                                                                                            'o '
                                                                                            'circuito '
                                                                                            'errado '
                                                                                            'aqui '
                                                                                            'perde: '
                                                                                            'o '
                                                                                            'cavalo '
                                                                                            'acaba '
                                                                                            'expulso '
                                                                                            'e o '
                                                                                            'rei '
                                                                                            'branco '
                                                                                            'não '
                                                                                            'chega '
                                                                                            'a '
                                                                                            'tempo '
                                                                                            'de '
                                                                                            'ocupar '
                                                                                            'f2.'},
                                                                                {   'titulo': '1...Rd4 '
                                                                                              '2.Nf2 '
                                                                                              'Rc3 '
                                                                                              '— '
                                                                                              'contornando '
                                                                                              'a '
                                                                                              'nova '
                                                                                              'barreira',
                                                                                    'linha': [   'Kd4',
                                                                                                 'Nf2',
                                                                                                 'Kc3',
                                                                                                 'Kd6',
                                                                                                 'Kd2',
                                                                                                 'Ke5',
                                                                                                 'Ke2',
                                                                                                 'Nh1',
                                                                                                 'Kf3',
                                                                                                 'Kd4',
                                                                                                 'Kg2',
                                                                                                 'Ke3',
                                                                                                 'Kxh1',
                                                                                                 'Kf2'],
                                                                                    'nota': 'De '
                                                                                            'novo '
                                                                                            'o rei '
                                                                                            'branco '
                                                                                            'chega '
                                                                                            'bem a '
                                                                                            'tempo, '
                                                                                            'e a '
                                                                                            'posição '
                                                                                            'final '
                                                                                            'é a '
                                                                                            'mesma '
                                                                                            'fortaleza: '
                                                                                            'rei '
                                                                                            'preto '
                                                                                            'preso '
                                                                                            'no '
                                                                                            'canto, '
                                                                                            'bloqueando '
                                                                                            'o '
                                                                                            'próprio '
                                                                                            'peão.'}]}],
                                        'regras': [   'O cavalo sozinho não detém o peão de torre '
                                                      'na sétima — mas sua capacidade de erguer '
                                                      'barreiras (sempre em forma de L) obriga o '
                                                      'rei adversário a um desvio longo, dando '
                                                      'tempo ao próprio rei de chegar e salvar o '
                                                      'empate.']},
                                    {   'n': 14,
                                        'titulo': 'O rei e o cavalo dão mate',
                                        'conceito': 'Existe mesmo um jeito de o lado mais fraco '
                                                    '(rei e cavalo contra rei e peão) dar '
                                                    'xeque-mate?',
                                        'texto': [   'Esta é uma posição rara, mas vale conhecer — '
                                                     'até para nunca cair nela por excesso de '
                                                     'ambição. Se o rei do lado do peão fica preso '
                                                     'na própria casa de canto, à frente do seu '
                                                     'peão de torre já na sexta ou sétima fila, o '
                                                     'rei e o cavalo adversários podem dar mate.',
                                                     'A manobra é sempre curta, mas exige '
                                                     'precisão: o perigo constante é afogar o rei '
                                                     'antes de conseguir o xeque-mate.'],
                                        'posicoes': [   {   'rotulo': 'O mate do canto',
                                                            'fen': '8/8/8/8/8/p7/2K1N3/k7 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Brancas ganham',
                                                            'linha': ['Nc1', 'a2', 'Nb3#'],
                                                            'notas': {   0: 'O cavalo se prepara '
                                                                            'para o salto '
                                                                            'decisivo.',
                                                                         1: 'Único lance legal — '
                                                                            'qualquer outro '
                                                                            'deixaria as pretas '
                                                                            'afogadas, e o '
                                                                            'resultado seria '
                                                                            'empate.',
                                                                         2: 'Xeque-mate.'}}],
                                        'regras': [   'Se o rei do lado mais fraco fica preso no '
                                                      'canto, à frente do próprio peão de torre já '
                                                      'avançado, o rei e o cavalo adversários '
                                                      'podem dar mate — mas a manobra precisa ser '
                                                      'exata, para não afogar o rei.']},
                                    {   'n': 15,
                                        'titulo': 'A casa boba do cavalo',
                                        'conceito': 'Existe uma casa em que o próprio cavalo '
                                                    'atrapalha a defesa do seu rei?',
                                        'texto': [   'A segunda casa da grande diagonal — b7 (ou, '
                                                     'por simetria, g7, b2 e g2) — pode ser '
                                                     'chamada de **casa boba do cavalo**. Já vimos '
                                                     'no Final 9 que esta mesma casa é fatal na '
                                                     'luta contra a torre; aqui, contra um simples '
                                                     'peão passado, o problema é outro: mesmo sem '
                                                     'estar na borda, a mobilidade do cavalo ali é '
                                                     'tão pobre que ele não consegue se voltar '
                                                     'contra o peão que o ataca.',
                                                     'No caso limite a seguir, o cavalo está na '
                                                     'pior casa imaginável: não só não detém o '
                                                     'peão, como **impede o próprio rei de '
                                                     'fazê-lo**.'],
                                        'posicoes': [   {   'rotulo': 'O cavalo atrapalha o '
                                                                      'próprio rei',
                                                            'fen': '3k4/1n6/8/P7/8/8/7K/8 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Brancas ganham',
                                                            'linha': ['a6', 'Kc8', 'a7'],
                                                            'notas': {   0: 'O peão avança '
                                                                            'livremente — o cavalo '
                                                                            'em b7 tapa exatamente '
                                                                            'a casa por onde o '
                                                                            'próprio rei '
                                                                            'precisaria passar '
                                                                            'para ajudar.',
                                                                         2: 'O peão chega a sétima '
                                                                            'sem que nada o '
                                                                            'detenha, e promove no '
                                                                            'lance seguinte.'}}],
                                        'regras': [   'A segunda casa da diagonal do canto '
                                                      "(b7/g7/b2/g2) é a 'casa boba' do cavalo: "
                                                      'mesmo sem estar na borda, a mobilidade ali '
                                                      'é tão baixa que o cavalo pode acabar '
                                                      'atrapalhando a própria defesa.']}]},
                  {   'id': 'dama-peao',
                      'titulo': 'Dama contra peão',
                      'resumo': 'O final mais comum de todos, fruto de corridas de peões: o método '
                                'geral para a dama ganhar, as exceções por afogamento dos peões de '
                                'torre e bispo, e as armadilhas mais frequentes na prática.',
                      'finais': [   {   'n': 16,
                                        'titulo': 'Dama contra peão na sétima — o método vencedor',
                                        'conceito': 'Como a dama sozinha consegue parar e depois '
                                                    'capturar um peão já na sétima fila?',
                                        'texto': [   'A tarefa das brancas aqui é relativamente '
                                                     'simples, mas vale a pena ver o método '
                                                     'completo com atenção, porque ele reaparece, '
                                                     'com pequenas variações, em quase todos os '
                                                     'finais deste capítulo.',
                                                     'A ideia é dar xeques que, aos poucos, '
                                                     'empurram o rei adversário para a frente do '
                                                     'próprio peão e, ao mesmo tempo, aproximam o '
                                                     'rei branco. Uma vez que o rei chega perto o '
                                                     'suficiente, surge uma posição de mate — '
                                                     'normalmente facilitada pela borda do '
                                                     'tabuleiro.'],
                                        'posicoes': [   {   'rotulo': 'O método completo',
                                                            'fen': '6K1/8/3Q4/8/8/8/5kp1/8 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Brancas ganham',
                                                            'linha': [   'Qf4+',
                                                                         'Ke2',
                                                                         'Qg3',
                                                                         'Kf1',
                                                                         'Qf3+',
                                                                         'Kg1',
                                                                         'Kg7',
                                                                         'Kh2',
                                                                         'Qf2',
                                                                         'Kh1',
                                                                         'Qh4+',
                                                                         'Kg1',
                                                                         'Kg6',
                                                                         'Kf1',
                                                                         'Qf4+',
                                                                         'Ke2',
                                                                         'Qg3',
                                                                         'Kf1',
                                                                         'Qf3+',
                                                                         'Kg1',
                                                                         'Kg5',
                                                                         'Kh2',
                                                                         'Kh4',
                                                                         'g1=Q',
                                                                         'Qh3#'],
                                                            'notas': {   0: 'A dama se aproxima '
                                                                            'dando xeque.',
                                                                         2: 'Uma manobra '
                                                                            'necessária: repetir '
                                                                            'os xeques não adianta '
                                                                            'nada se o rei preto '
                                                                            'apenas oscilar entre '
                                                                            'e2 e f2.',
                                                                         4: 'O xeque-chave: agora '
                                                                            'o rei é obrigado a se '
                                                                            'colocar na frente do '
                                                                            'próprio peão.',
                                                                         6: 'Com o rei preto '
                                                                            'fixado, o rei branco '
                                                                            'pode se aproximar.',
                                                                         8: 'O processo se repete, '
                                                                            'para continuar '
                                                                            'aproximando o rei.',
                                                                         14: 'E tudo se repete '
                                                                             'mais uma vez — o '
                                                                             'padrão de xeques é '
                                                                             'sempre o mesmo.',
                                                                         21: 'Com o rei branco já '
                                                                             'perto, é fácil '
                                                                             'enxergar uma posição '
                                                                             'de mate — aqui '
                                                                             'facilitada pela '
                                                                             'borda do tabuleiro.',
                                                                         23: 'O peão finalmente '
                                                                             'promove — mas é '
                                                                             'tarde demais.',
                                                                         24: 'Xeque-mate.'},
                                                            'regra_destaque': 'Em uma posição '
                                                                              'normal, a dama '
                                                                              'ganha contra um '
                                                                              'peão na sétima fila '
                                                                              '(e com mais razão '
                                                                              'ainda na sexta ou '
                                                                              'mais atrás) — mas '
                                                                              'há exceções, por '
                                                                              'duas causas: '
                                                                              'recursos de '
                                                                              'afogamento, ou o '
                                                                              'próprio rei forte '
                                                                              'atrapalhando os '
                                                                              'xeques da dama. Os '
                                                                              'próximos finais '
                                                                              'mostram essas '
                                                                              'exceções.'},
                                                        {   'rotulo': 'Quando o próprio rei '
                                                                      'atrapalha',
                                                            'fen': '2Q5/3K4/8/8/8/8/3kp3/8 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': [],
                                                            'notas': {   0: 'A primeira exceção ao '
                                                                            'método do final '
                                                                            'anterior: mesmo com o '
                                                                            'lance, as brancas não '
                                                                            'conseguem ganhar '
                                                                            'aqui, porque **não '
                                                                            'têm nenhum xeque '
                                                                            'disponível** — o '
                                                                            'próprio rei branco, '
                                                                            'tentando ajudar, '
                                                                            'acabou tapando as '
                                                                            'linhas de ataque da '
                                                                            'dama. É uma situação '
                                                                            'típica de como '
                                                                            'terminam corridas de '
                                                                            'peões.'}}],
                                        'regras': [   'Em uma posição normal, a dama ganha contra '
                                                      'um peão nas colunas b, d, e ou g na sétima '
                                                      'fila (e com mais razão ainda na sexta ou '
                                                      'mais atrás), se consegue dar xeques.',
                                                      'Há duas exceções: o próprio rei '
                                                      'atrapalhando os xeques da dama, ou — com os '
                                                      'peões de torre e de bispo — o recurso do '
                                                      'afogamento, vistos nos próximos finais.']},
                                    {   'n': 17,
                                        'titulo': 'Dama contra peão de torre na sétima',
                                        'conceito': 'Por que o peão de torre é mais difícil de '
                                                    'vencer para a dama do que um peão central?',
                                        'texto': [   'A segunda exceção ao método geral envolve os '
                                                     'peões de torre e de bispo: o chamado '
                                                     '**recurso do afogamento**. Vamos ver '
                                                     'primeiro o caso do peão de torre.',
                                                     'Com o peão de torre já apoiado pelo próprio '
                                                     'rei na sétima fila, o método de xeques do '
                                                     'final anterior pode simplesmente não '
                                                     'funcionar — às vezes a defesa correta é bem '
                                                     'mais direta.'],
                                        'posicoes': [   {   'rotulo': 'O recurso do afogamento',
                                                            'fen': '8/6KP/8/4k3/3q4/8/8/8 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': ['h8=Q'],
                                                            'notas': {   0: 'A tentação é repetir '
                                                                            'o método do final '
                                                                            'anterior, afastando o '
                                                                            'rei com xeques — mas '
                                                                            'aqui isso **perde** '
                                                                            '(veja a variante ao '
                                                                            'lado): com o rei '
                                                                            'preto já tão perto, '
                                                                            'as brancas não teriam '
                                                                            'tempo de se '
                                                                            'reorganizar depois. O '
                                                                            'recurso salvador é '
                                                                            'outro, e muito mais '
                                                                            'direto: **coroar '
                                                                            'imediatamente**. A '
                                                                            'nova dama nasce numa '
                                                                            'casa protegida ao '
                                                                            'mesmo tempo pelos '
                                                                            'dois reis — o branco '
                                                                            'tapa a diagonal para '
                                                                            'ela dar xeque, e o '
                                                                            'preto tapa a mesma '
                                                                            'diagonal para a dama '
                                                                            'inimiga conseguir '
                                                                            'capturá-la. '
                                                                            'Resultado: empate na '
                                                                            'hora, duas damas no '
                                                                            'tabuleiro sem que '
                                                                            'nenhum lado consiga '
                                                                            'progredir.'},
                                                            'alternativas': [   {   'titulo': '1.Rg8?? '
                                                                                              '— o '
                                                                                              'método '
                                                                                              'do '
                                                                                              'final '
                                                                                              'anterior '
                                                                                              'não '
                                                                                              'funciona '
                                                                                              'aqui',
                                                                                    'linha': [   'Kg8',
                                                                                                 'Qd8+',
                                                                                                 'Kg7',
                                                                                                 'Qg5+'],
                                                                                    'nota': 'Parece '
                                                                                            'natural '
                                                                                            'tentar '
                                                                                            'o '
                                                                                            'mesmo '
                                                                                            'processo '
                                                                                            'de '
                                                                                            'xeques '
                                                                                            'do '
                                                                                            'Final '
                                                                                            '16, '
                                                                                            'mas '
                                                                                            'com o '
                                                                                            'rei '
                                                                                            'preto '
                                                                                            'já '
                                                                                            'tão '
                                                                                            'bem '
                                                                                            'posicionado '
                                                                                            'isso '
                                                                                            'é um '
                                                                                            'erro '
                                                                                            'decisivo '
                                                                                            '— as '
                                                                                            'brancas '
                                                                                            'simplesmente '
                                                                                            'perdem, '
                                                                                            'sem '
                                                                                            'chance '
                                                                                            'de '
                                                                                            'empate. '
                                                                                            'A '
                                                                                            'diferença '
                                                                                            'para '
                                                                                            'a '
                                                                                            'posição '
                                                                                            'anterior '
                                                                                            '(diagrama '
                                                                                            '4.2) '
                                                                                            'é que '
                                                                                            'ali '
                                                                                            'as '
                                                                                            'brancas '
                                                                                            'não '
                                                                                            'tinham '
                                                                                            'pressa; '
                                                                                            'aqui, '
                                                                                            'perder '
                                                                                            'um '
                                                                                            'único '
                                                                                            'tempo '
                                                                                            'já é '
                                                                                            'fatal.'}],
                                                            'regra_destaque': 'Contra um peão de '
                                                                              'torre já apoiado '
                                                                              'pelo próprio rei na '
                                                                              'sétima, às vezes a '
                                                                              'defesa correta não '
                                                                              'é o método de '
                                                                              'xeques de sempre, e '
                                                                              'sim coroar na hora: '
                                                                              'a nova dama pode '
                                                                              'nascer protegida '
                                                                              'pelos dois reis ao '
                                                                              'mesmo tempo, '
                                                                              'travando a posição '
                                                                              'num empate '
                                                                              'imediato.'},
                                                        {   'rotulo': 'A que distância o rei forte '
                                                                      'precisa estar',
                                                            'fen': '8/5K1P/8/8/3q4/8/8/2k5 b - - 0 '
                                                                   '1',
                                                            'resultado': 'Pretas ganham',
                                                            'linha': [   'Qh8',
                                                                         'Kg6',
                                                                         'Kd2',
                                                                         'Kf7',
                                                                         'Qxh7+',
                                                                         'Ke6'],
                                                            'notas': {   0: 'Esta posição foi '
                                                                            'escolhida porque, '
                                                                            'apesar de o rei preto '
                                                                            'estar bem longe, '
                                                                            'ainda dá tempo de '
                                                                            'ganhar — mas é '
                                                                            'preciso jogar com '
                                                                            'cuidado. O primeiro '
                                                                            'lance já é o mais '
                                                                            'importante: a dama '
                                                                            'corta a saída do rei '
                                                                            'branco antes de '
                                                                            'qualquer outra coisa.',
                                                                         4: 'Com o rei branco '
                                                                            'afastado do canto, a '
                                                                            'dama já pode '
                                                                            'simplesmente capturar '
                                                                            'o peão com xeque.',
                                                                         5: 'Sem o peão, a posição '
                                                                            'é uma vitória trivial '
                                                                            'de dama e rei contra '
                                                                            'rei solitário — só '
                                                                            'falta trazer o rei '
                                                                            'preto para ajudar a '
                                                                            'dar mate.'},
                                                            'regra_destaque': 'Contra um peão de '
                                                                              'torre na sétima, o '
                                                                              'rei do lado forte '
                                                                              'não precisa estar '
                                                                              'tão perto quanto se '
                                                                              'poderia pensar — '
                                                                              'mesmo bem longe, '
                                                                              'muitas vezes ainda '
                                                                              'dá tempo de vencer, '
                                                                              'se a dama jogar com '
                                                                              'precisão para '
                                                                              'impedir o rei '
                                                                              'adversário de se '
                                                                              'estabilizar perto '
                                                                              'do próprio peão.'}],
                                        'regras': [   'Contra um peão de torre já apoiado pelo '
                                                      'próprio rei na sétima, o método de xeques '
                                                      'do final anterior pode falhar — às vezes a '
                                                      'defesa correta é coroar na hora, '
                                                      'aproveitando que a nova dama pode nascer '
                                                      'protegida pelos dois reis ao mesmo tempo.',
                                                      'Mesmo com o rei do lado forte bem longe, '
                                                      'muitas vezes ainda dá tempo de vencer '
                                                      'contra um peão de torre na sétima, se a '
                                                      'dama jogar com precisão.']},
                                    {   'n': 18,
                                        'titulo': 'Dama contra peão de bispo na sétima — rei forte '
                                                  'distante',
                                        'conceito': 'Com o peão de bispo, o recurso do afogamento '
                                                    'também existe — mas depende de qual lado o '
                                                    'rei fraco fica?',
                                        'texto': [   'O peão de bispo também tem seu recurso de '
                                                     'afogamento, mas a situação é um pouco mais '
                                                     'complexa: o rei do lado fraco pode ficar de '
                                                     'um lado ou do outro do peão, e as chances de '
                                                     'empate mudam bastante entre os dois casos.',
                                                     'Neste primeiro exemplo vemos os principais '
                                                     'recursos do lado defensor com o rei do lado '
                                                     'forte ainda distante.'],
                                        'posicoes': [   {   'rotulo': 'O rei forte ainda longe',
                                                            'fen': '8/5P2/3K4/8/8/1k6/8/q7 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': [   'Ke7',
                                                                         'Qe5+',
                                                                         'Kd7',
                                                                         'Qf6',
                                                                         'Ke8',
                                                                         'Qe6+',
                                                                         'Kf8',
                                                                         'Kc4',
                                                                         'Kg7',
                                                                         'Qe7',
                                                                         'Kg8',
                                                                         'Qg5+',
                                                                         'Kh8',
                                                                         'Qf6+',
                                                                         'Kg8',
                                                                         'Qg6+',
                                                                         'Kh8'],
                                                            'notas': {   0: 'O rei apoia a futura '
                                                                            'promoção. Vale notar '
                                                                            'que promover na hora '
                                                                            'não é automático: '
                                                                            '**1.f8=Q??** perde na '
                                                                            'hora.',
                                                                         1: 'A dama inicia a '
                                                                            'manobra de '
                                                                            'aproximação que já '
                                                                            'conhecemos dos finais '
                                                                            'anteriores.',
                                                                         8: 'Isso permite ao rei '
                                                                            'preto se aproximar '
                                                                            'mais uma casa.',
                                                                         9: 'Mas agora o rei '
                                                                            'branco passou para o '
                                                                            '**outro lado** do '
                                                                            'peão — que, como '
                                                                            'veremos, é o lado bom '
                                                                            '— e as pretas não '
                                                                            'conseguem mais ganhar '
                                                                            'tempos para aproximar '
                                                                            'o próprio rei.',
                                                                         16: 'Aqui está o detalhe '
                                                                             'que salva as '
                                                                             'brancas: ameaça-se '
                                                                             'promover, e se '
                                                                             '**9...Dxf7** é '
                                                                             'afogado.'},
                                                            'alternativas': [   {   'titulo': '1.f8=Q?? '
                                                                                              '— '
                                                                                              'promover '
                                                                                              'na '
                                                                                              'hora '
                                                                                              'perde',
                                                                                    'linha': [   'f8=Q',
                                                                                                 'Qa3+'],
                                                                                    'nota': 'Um '
                                                                                            'espeto: '
                                                                                            'o '
                                                                                            'xeque '
                                                                                            'obriga '
                                                                                            'o rei '
                                                                                            'a se '
                                                                                            'mexer '
                                                                                            'e '
                                                                                            'descobre '
                                                                                            'o '
                                                                                            'ataque '
                                                                                            'da '
                                                                                            'dama '
                                                                                            'preta, '
                                                                                            'na '
                                                                                            'diagonal '
                                                                                            'a3-f8, '
                                                                                            'contra '
                                                                                            'a '
                                                                                            'dama '
                                                                                            'branca '
                                                                                            'recém-nascida.'}],
                                                            'regra_destaque': 'Com o peão de '
                                                                              'bispo, o lado do '
                                                                              'peão quer trazer o '
                                                                              'próprio rei para o '
                                                                              'lado **oposto** ao '
                                                                              'do rei adversário — '
                                                                              'esse é o lado bom, '
                                                                              'onde o recurso do '
                                                                              'afogamento '
                                                                              'funciona.'},
                                                        {   'rotulo': 'A zona vencedora — rei '
                                                                      'fraco do lado bom',
                                                            'fen': '8/5PK1/8/6k1/8/8/q7/8 b - - 0 '
                                                                   '1',
                                                            'resultado': 'Pretas ganham',
                                                            'linha': [   'Qa7',
                                                                         'Kh8',
                                                                         'Kg6',
                                                                         'f8=Q',
                                                                         'Qh7#'],
                                                            'notas': {   0: 'Com o peão de bispo, '
                                                                            'a pergunta é a mesma '
                                                                            'de antes: a que '
                                                                            'distância o rei forte '
                                                                            'precisa estar? Mas '
                                                                            'aqui a resposta '
                                                                            'depende de qual lado '
                                                                            'do peão o rei fraco '
                                                                            'ocupa. Com o rei '
                                                                            'fraco do **lado bom** '
                                                                            '(o do canto), a zona '
                                                                            'vencedora é menor do '
                                                                            'que no caso do peão '
                                                                            'de torre — porque não '
                                                                            'é possível ganhar com '
                                                                            'um lance calmo de rei '
                                                                            'depois da promoção: a '
                                                                            'dama promovida não '
                                                                            'fica presa pela borda '
                                                                            'do tabuleiro, então o '
                                                                            'mate precisa ser '
                                                                            'imediato.',
                                                                         2: 'O rei preto chega à '
                                                                            'casa crítica g6 — mas '
                                                                            'só tem este único '
                                                                            'tempo, porque assim '
                                                                            'que o peão promover a '
                                                                            'dama branca ataca '
                                                                            'livremente, sem o '
                                                                            'amparo do canto.',
                                                                         3: 'A outra casa crítica '
                                                                            'seria e7: se o rei '
                                                                            'forte pudesse, em um '
                                                                            'lance, controlar a '
                                                                            'casa de promoção a '
                                                                            'partir dali, o '
                                                                            'resultado seria o '
                                                                            'mesmo.',
                                                                         4: 'Mate.'},
                                                            'alternativas': [   {   'titulo': '2.Rg8 '
                                                                                              '— a '
                                                                                              'mesma '
                                                                                              'ideia',
                                                                                    'linha': [   'Qa7',
                                                                                                 'Kg8'],
                                                                                    'nota': 'Dá '
                                                                                            'exatamente '
                                                                                            'no '
                                                                                            'mesmo.'}],
                                                            'regra_destaque': 'Contra peão de '
                                                                              'bispo na sétima, '
                                                                              'com o rei fraco do '
                                                                              'lado bom (o do '
                                                                              'canto), o rei forte '
                                                                              'precisa estar a 1 '
                                                                              'passo de uma das '
                                                                              'duas casas '
                                                                              'críticas, g6 ou '
                                                                              'e7.'},
                                                        {   'rotulo': 'A zona vencedora — rei '
                                                                      'fraco do lado mau',
                                                            'fen': '8/4KP2/8/1k6/8/8/q7/8 b - - 0 '
                                                                   '1',
                                                            'resultado': 'Pretas ganham',
                                                            'linha': [   'Qa7+',
                                                                         'Ke8',
                                                                         'Qb8+',
                                                                         'Ke7',
                                                                         'Qe5+',
                                                                         'Kd7',
                                                                         'Qf6',
                                                                         'Ke8',
                                                                         'Qe6+',
                                                                         'Kf8'],
                                                            'notas': {   0: 'Com o peão de bispo e '
                                                                            'o rei fraco do **lado '
                                                                            'mau**, a zona '
                                                                            'vencedora é bem maior '
                                                                            '— maior até do que no '
                                                                            'caso do peão de '
                                                                            'torre. Existem duas '
                                                                            'imagens de mate: uma '
                                                                            'com o rei forte '
                                                                            'defendendo a dama em '
                                                                            'd2, outra obrigando o '
                                                                            'rei adversário a '
                                                                            'passar para o lado '
                                                                            'bom, a mesma que já '
                                                                            'vimos (com o rei '
                                                                            'forte chegando a g6). '
                                                                            'Aqui mostramos o '
                                                                            'caminho até g6.',
                                                                         8: 'A primeira fase é '
                                                                            'simples de entender: '
                                                                            'trata-se de obrigar o '
                                                                            'rei branco a passar '
                                                                            'para o outro lado.'},
                                                            'regra_destaque': 'Com a dama cortando '
                                                                              'o caminho a cada '
                                                                              'xeque, o rei preto '
                                                                              'tem tempo de sobra '
                                                                              'para caminhar até '
                                                                              'g5 e depois g6, '
                                                                              'aproveitando cada '
                                                                              'tempo ganho pelos '
                                                                              'xeques da dama — a '
                                                                              'torcida de xeques '
                                                                              'força o rei branco '
                                                                              'a gastar lances só '
                                                                              'defendendo, '
                                                                              'enquanto o rei '
                                                                              'preto se aproxima '
                                                                              'livremente. Uma vez '
                                                                              'em g6, a posição '
                                                                              'transpõe para a '
                                                                              'mesma rede de mate '
                                                                              'vista na posição '
                                                                              'anterior. (Se, em '
                                                                              'vez de se '
                                                                              'aproximar, o rei '
                                                                              'preto hesitasse — '
                                                                              'por exemplo com '
                                                                              '...Rd7?! — as '
                                                                              'brancas ainda '
                                                                              'poderiam, com '
                                                                              '...Rh8!?, obrigar '
                                                                              'as pretas a recuar, '
                                                                              'porque o rei forte '
                                                                              'não estaria a tempo '
                                                                              'de se aproximar '
                                                                              'naquele momento.) '
                                                                              'Contra peão de '
                                                                              'bispo na sétima, '
                                                                              'com o rei fraco do '
                                                                              'lado mau, o rei '
                                                                              'forte precisa estar '
                                                                              'a 2 passos de uma '
                                                                              'das duas casas '
                                                                              'críticas (neste '
                                                                              'caso, d7 e g6).'},
                                                        {   'rotulo': 'O mate em d7',
                                                            'fen': '8/4KP2/8/8/6k1/8/q7/8 b - - 0 '
                                                                   '1',
                                                            'resultado': 'Pretas ganham',
                                                            'linha': ['Qa3+', 'Ke8'],
                                                            'notas': {   0: 'Com o rei forte '
                                                                            'dentro da zona '
                                                                            'vencedora, mas a dois '
                                                                            'passos de d7, é '
                                                                            'preciso jogar com '
                                                                            'cuidado para impedir '
                                                                            'que o rei adversário '
                                                                            'escape para o lado '
                                                                            'bom sem perder '
                                                                            'tempos.',
                                                                         1: 'Na prática, os outros '
                                                                            'xeques também ganham, '
                                                                            'mas exigem mais '
                                                                            'precisão logo a '
                                                                            'seguir.'},
                                                            'alternativas': [   {   'titulo': '1...Qa7+ '
                                                                                              '— '
                                                                                              'também '
                                                                                              'ganha, '
                                                                                              'com '
                                                                                              'mais '
                                                                                              'cuidado',
                                                                                    'linha': [   'Qa7+',
                                                                                                 'Kf8',
                                                                                                 'Qg1'],
                                                                                    'nota': 'Depois '
                                                                                            'deste '
                                                                                            'xeque, '
                                                                                            'só há '
                                                                                            'um '
                                                                                            'lance '
                                                                                            'que '
                                                                                            'mantém '
                                                                                            'a '
                                                                                            'vantagem.'},
                                                                                {   'titulo': '1...Qa7+ '
                                                                                              '2.Rf6?? '
                                                                                              '— '
                                                                                              'perde '
                                                                                              'na '
                                                                                              'hora',
                                                                                    'linha': [   'Qa7+',
                                                                                                 'Kf6',
                                                                                                 'Qd4+'],
                                                                                    'nota': 'Simples '
                                                                                            'demais: '
                                                                                            'o rei '
                                                                                            'branco '
                                                                                            'nunca '
                                                                                            'deveria '
                                                                                            'se '
                                                                                            'afastar '
                                                                                            'assim '
                                                                                            'da '
                                                                                            'zona '
                                                                                            'de '
                                                                                            'defesa.'}],
                                                            'regra_destaque': 'A partir daqui, a '
                                                                              'dama persegue o rei '
                                                                              'branco com xeques '
                                                                              '(…Qa8+, …Qe4+ etc.) '
                                                                              'enquanto o rei '
                                                                              'preto caminha até '
                                                                              'controlar as duas '
                                                                              'casas-chave do '
                                                                              'final: d7 (onde o '
                                                                              'rei forte, apoiando '
                                                                              'a dama, dá mate '
                                                                              'direto) e g6 (de '
                                                                              'onde, como já '
                                                                              'vimos, o mate '
                                                                              'também está '
                                                                              'garantido assim que '
                                                                              'o peão promove). O '
                                                                              'cuidado principal é '
                                                                              'não deixar o rei '
                                                                              'branco atravessar '
                                                                              'para o lado bom do '
                                                                              'peão sem perder '
                                                                              'tempo algum — por '
                                                                              'isso a dama escolhe '
                                                                              'seus xeques com uma '
                                                                              'ordem precisa, e '
                                                                              'não qualquer uma.'}],
                                        'regras': [   'Com o peão de bispo, assim como com o peão '
                                                      'de torre, para ganhar a dama precisa da '
                                                      'colaboração do próprio rei.',
                                                      'O lado do peão quer trazer o rei para o '
                                                      'lado oposto ao do rei adversário — esse é o '
                                                      'lado bom, onde o recurso do afogamento '
                                                      'ainda funciona.',
                                                      'Com o rei fraco do lado bom, o rei forte '
                                                      'precisa estar a 1 passo de uma das casas '
                                                      'críticas g6 ou e7; do lado mau, a 2 passos '
                                                      'de d7 ou g6.',
                                                      'Se o lado do peão tem outro peão além do de '
                                                      'bispo, o recurso do afogamento desaparece '
                                                      'automaticamente.']},
                                    {   'n': 19,
                                        'titulo': 'Uma armadilha comum demais',
                                        'conceito': 'O rei forte está fora da zona vencedora — '
                                                    'então por que tanta gente ainda perde esta '
                                                    'posição?',
                                        'texto': [   'Este capítulo de dama contra peão já poderia '
                                                     'terminar aqui — todas as circunstâncias '
                                                     'essenciais já foram vistas, e não há mais '
                                                     'exceções de resultado. Mas é comum demais '
                                                     'ver jogadores caírem na armadilha a seguir, '
                                                     'então vale a pena dedicar mais dois '
                                                     'diagramas a ela.',
                                                     'Nos dois exemplos, o rei forte está fora da '
                                                     'zona vencedora, e portanto a posição é de '
                                                     'empate. Mas se quem joga com as brancas for '
                                                     'experiente, vai tentar nos levar à posição '
                                                     'crítica depois de alguns lances de pura '
                                                     'confusão — e aí, sim, é fácil errar.'],
                                        'posicoes': [   {   'rotulo': 'A armadilha de um lado',
                                                            'fen': '8/8/8/3K4/8/4Q3/2p5/1k6 w - - '
                                                                   '0 1',
                                                            'resultado': 'Empate',
                                                            'linha': [   'Qb3+',
                                                                         'Ka1',
                                                                         'Qe3',
                                                                         'Kb1',
                                                                         'Qe4',
                                                                         'Kb2',
                                                                         'Qe2',
                                                                         'Ka1',
                                                                         'Kc4',
                                                                         'c1=Q+',
                                                                         'Kb3',
                                                                         'Qb1+'],
                                                            'notas': {   0: 'Primeira fase: só '
                                                                            'confusão, como já '
                                                                            'conhecemos de outros '
                                                                            'finais — por si só, '
                                                                            'esses xeques não '
                                                                            'mudam nada.',
                                                                         6: 'E agora vem a isca.',
                                                                         7: 'Esquisito, mas é o '
                                                                            'único lance certo — '
                                                                            'difícil de encontrar '
                                                                            'para quem não conhece '
                                                                            'esta posição a fundo.',
                                                                         9: 'Depois da promoção '
                                                                            'com xeque, o único '
                                                                            'lance que ainda '
                                                                            'empata é devolver o '
                                                                            'xeque — mas é '
                                                                            'suficiente.'},
                                                            'alternativas': [   {   'titulo': '7...Rb1?? '
                                                                                              '— o '
                                                                                              'erro '
                                                                                              'típico',
                                                                                    'linha': [   'Qb3+',
                                                                                                 'Ka1',
                                                                                                 'Qe3',
                                                                                                 'Kb1',
                                                                                                 'Qe4',
                                                                                                 'Kb2',
                                                                                                 'Qe2',
                                                                                                 'Kb1',
                                                                                                 'Kc4'],
                                                                                    'nota': 'O '
                                                                                            'lance '
                                                                                            'natural, '
                                                                                            'e o '
                                                                                            'erro '
                                                                                            'que '
                                                                                            'leva '
                                                                                            'à '
                                                                                            'conclusão '
                                                                                            'conhecida: '
                                                                                            'depois '
                                                                                            'de '
                                                                                            '**8.Rc4!!**, '
                                                                                            'com o '
                                                                                            'rei '
                                                                                            'branco '
                                                                                            'marchando '
                                                                                            'até o '
                                                                                            'próprio '
                                                                                            'peão, '
                                                                                            'a '
                                                                                            'promoção '
                                                                                            'já '
                                                                                            'não '
                                                                                            'salva '
                                                                                            'mais '
                                                                                            'as '
                                                                                            'pretas '
                                                                                            '— '
                                                                                            'apesar '
                                                                                            'da '
                                                                                            'dama '
                                                                                            'preta '
                                                                                            'parecer '
                                                                                            'muito '
                                                                                            'mais '
                                                                                            'solta '
                                                                                            'do '
                                                                                            'que '
                                                                                            'ficaria '
                                                                                            'em '
                                                                                            'a1, '
                                                                                            'ela '
                                                                                            'não '
                                                                                            'encontra '
                                                                                            'mais '
                                                                                            'lance '
                                                                                            'nenhum '
                                                                                            'para '
                                                                                            'evitar '
                                                                                            'o '
                                                                                            'mate.'},
                                                                                {   'titulo': '7...Rc3?? '
                                                                                              '— '
                                                                                              'também '
                                                                                              'não '
                                                                                              'empata',
                                                                                    'linha': [   'Qb3+',
                                                                                                 'Ka1',
                                                                                                 'Qe3',
                                                                                                 'Kb1',
                                                                                                 'Qe4',
                                                                                                 'Kb2',
                                                                                                 'Qe2',
                                                                                                 'Kc3',
                                                                                                 'Qe5+'],
                                                                                    'nota': 'Também '
                                                                                            'não é '
                                                                                            'suficiente: '
                                                                                            'depois '
                                                                                            'deste '
                                                                                            'xeque, '
                                                                                            'o rei '
                                                                                            'preto '
                                                                                            'é '
                                                                                            'forçado '
                                                                                            'a '
                                                                                            'passar '
                                                                                            'para '
                                                                                            'o '
                                                                                            'lado '
                                                                                            'mau '
                                                                                            'do '
                                                                                            'peão, '
                                                                                            'e o '
                                                                                            'rei '
                                                                                            'branco '
                                                                                            'entra '
                                                                                            'automaticamente '
                                                                                            'na '
                                                                                            "'nova' "
                                                                                            'zona '
                                                                                            'vencedora '
                                                                                            'que '
                                                                                            'isso '
                                                                                            'cria.'}],
                                                            'regra_destaque': 'Mesmo com o rei '
                                                                              'forte fora da zona '
                                                                              'vencedora, um peão '
                                                                              'de bispo perto da '
                                                                              'borda ainda guarda '
                                                                              'uma armadilha: o '
                                                                              'rei fraco precisa '
                                                                              'encontrar a única '
                                                                              'casa certa no '
                                                                              'momento do truque, '
                                                                              'ou o rei forte '
                                                                              'consegue entrar a '
                                                                              'tempo na zona '
                                                                              'vencedora.'},
                                                        {   'rotulo': 'A mesma armadilha do outro '
                                                                      'lado',
                                                            'fen': '8/8/8/4K3/8/1Q6/2pk4/8 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Empate',
                                                            'linha': ['Qa2', 'Kc3', 'Qa1+', 'Kd2'],
                                                            'notas': {   0: 'O mesmo truque pode '
                                                                            'ser tentado do outro '
                                                                            'lado — e na prática '
                                                                            'funciona ainda '
                                                                            'melhor, porque a '
                                                                            'defesa correta é mais '
                                                                            'difícil de encontrar. '
                                                                            '(Antes desta posição, '
                                                                            'as brancas já '
                                                                            'passaram pela mesma '
                                                                            'fase de confusão: '
                                                                            '**1.Db2 Rd1 2.Db3 '
                                                                            'Rd2**.) Agora vem a '
                                                                            'isca de novo.',
                                                                         1: 'De novo, um lance '
                                                                            'único e bem estranho '
                                                                            '— quem não conhece '
                                                                            'esta posição a fundo '
                                                                            'tem dificuldade em '
                                                                            'encontrá-lo.',
                                                                         3: 'E, de novo, devolver '
                                                                            'o xeque é o único '
                                                                            'lance que ainda '
                                                                            'empata.'},
                                                            'alternativas': [   {   'titulo': '3...Rd1?? '
                                                                                              '— o '
                                                                                              'erro '
                                                                                              'natural',
                                                                                    'linha': [   'Qa2',
                                                                                                 'Kd1',
                                                                                                 'Kd4',
                                                                                                 'c1=Q',
                                                                                                 'Kd3'],
                                                                                    'nota': 'O '
                                                                                            'lance '
                                                                                            'natural '
                                                                                            '— e o '
                                                                                            'erro '
                                                                                            'que '
                                                                                            'leva '
                                                                                            'à '
                                                                                            'mesma '
                                                                                            'conclusão '
                                                                                            'de '
                                                                                            'sempre: '
                                                                                            'o rei '
                                                                                            'branco '
                                                                                            'chega '
                                                                                            'a '
                                                                                            'tempo, '
                                                                                            'e a '
                                                                                            'promoção '
                                                                                            'não '
                                                                                            'salva '
                                                                                            'mais '
                                                                                            'as '
                                                                                            'pretas.'},
                                                                                {   'titulo': '3...Rd3?? '
                                                                                              '— '
                                                                                              'também '
                                                                                              'não '
                                                                                              'é '
                                                                                              'suficiente',
                                                                                    'linha': [   'Qa2',
                                                                                                 'Kd3',
                                                                                                 'Qb2',
                                                                                                 'Kd2',
                                                                                                 'Ke4'],
                                                                                    'nota': 'Para '
                                                                                            'evitar '
                                                                                            '**Qc1**, '
                                                                                            'o rei '
                                                                                            'preto '
                                                                                            'é '
                                                                                            'obrigado '
                                                                                            'a '
                                                                                            'cravar '
                                                                                            'o '
                                                                                            'próprio '
                                                                                            'peão '
                                                                                            '— e é '
                                                                                            'exatamente '
                                                                                            'esse '
                                                                                            'momento '
                                                                                            'que o '
                                                                                            'rei '
                                                                                            'branco '
                                                                                            'aproveita '
                                                                                            'para '
                                                                                            'entrar '
                                                                                            'na '
                                                                                            'zona '
                                                                                            'vencedora.'}],
                                                            'regra_destaque': 'A mesma armadilha, '
                                                                              'espelhada: contra o '
                                                                              'peão de bispo perto '
                                                                              'da borda, o lado '
                                                                              'fraco sempre '
                                                                              'precisa conhecer a '
                                                                              'casa exata de '
                                                                              'defesa — o lance '
                                                                              "'natural' quase "
                                                                              'sempre perde.'}],
                                        'regras': [   'Mesmo com o rei forte fora da zona '
                                                      'vencedora, um peão de bispo (ou de torre) '
                                                      'perto da borda ainda guarda uma armadilha '
                                                      'de afogamento: o rei fraco precisa '
                                                      'encontrar a única casa certa no momento do '
                                                      "truque, porque o lance 'natural' costuma "
                                                      'perder.']},
                                    {   'n': 20,
                                        'titulo': 'Dama contra dama',
                                        'conceito': 'Quando os dois peões promovem, a partida é '
                                                    'sempre empate?',
                                        'texto': [   'Embora não seja estritamente uma batalha de '
                                                     'dama contra peão, vale a pena estudar esta '
                                                     'posição — muito útil, e intimamente '
                                                     'relacionada, porque costuma aparecer como '
                                                     'desfecho de uma corrida de peões.',
                                                     'A primeira coisa a observar é que **nem '
                                                     'sempre que os dois jogadores promovem a dama '
                                                     'a partida é empate.** Há bastante chance de '
                                                     'perder, sobretudo se a dama promove bem na '
                                                     'casa do canto: nos primeiros instantes em '
                                                     'que ela está na borda, pode ser atrapalhada '
                                                     'pelo próprio rei e capturada, ou cair numa '
                                                     'rede de mate. Quando isso acontece, '
                                                     'geralmente as variantes são simples — já '
                                                     'vimos vários exemplos assim neste capítulo.',
                                                     'O caso interessante — e que vale a pena '
                                                     'estudar a fundo, porque serve de padrão para '
                                                     'posições parecidas — é quando o rei do lado '
                                                     'forte está relativamente perto: '
                                                     'especificamente, na casa do diagrama a '
                                                     'seguir (d3 ou c4, neste canto; f4 ou e3, se '
                                                     'a dama tivesse promovido em h1).'],
                                        'posicoes': [   {   'rotulo': 'O rei forte perto o '
                                                                      'bastante',
                                                            'fen': '8/8/8/8/8/k2K4/2Q5/q7 w - - 0 '
                                                                   '1',
                                                            'resultado': 'Brancas ganham',
                                                            'linha': [   'Qc5+',
                                                                         'Ka2',
                                                                         'Qc4+',
                                                                         'Ka3',
                                                                         'Qa6+',
                                                                         'Kb2',
                                                                         'Qb5+',
                                                                         'Ka3',
                                                                         'Qa5+',
                                                                         'Kb2',
                                                                         'Qb4+',
                                                                         'Ka2',
                                                                         'Kc2'],
                                                            'notas': {   0: 'A réplica mais tenaz.',
                                                                         12: 'Chegando a uma '
                                                                             'posição vencedora já '
                                                                             'conhecida — o mesmo '
                                                                             'método de aproximar '
                                                                             'o rei dando xeques '
                                                                             'que vimos no início '
                                                                             'deste capítulo.'},
                                                            'alternativas': [   {   'titulo': '1...Ra4?! '
                                                                                              '— '
                                                                                              'pior '
                                                                                              'ainda',
                                                                                    'linha': [   'Qc5+',
                                                                                                 'Ka4',
                                                                                                 'Qa7+'],
                                                                                    'nota': 'Perde '
                                                                                            'a '
                                                                                            'dama '
                                                                                            'na '
                                                                                            'hora.'},
                                                                                {   'titulo': '1...Rb3 '
                                                                                              '— '
                                                                                              'transpõe '
                                                                                              'para '
                                                                                              'a '
                                                                                              'linha '
                                                                                              'principal',
                                                                                    'linha': [   'Qc5+',
                                                                                                 'Kb3',
                                                                                                 'Qb5+',
                                                                                                 'Ka3',
                                                                                                 'Qa5+',
                                                                                                 'Kb2',
                                                                                                 'Qb4+'],
                                                                                    'nota': 'Chega '
                                                                                            'à '
                                                                                            'mesma '
                                                                                            'posição '
                                                                                            'da '
                                                                                            'linha '
                                                                                            'principal, '
                                                                                            'só '
                                                                                            'que '
                                                                                            'mais '
                                                                                            'cedo.'},
                                                                                {   'titulo': '1...Rb2 '
                                                                                              '— '
                                                                                              'encurta '
                                                                                              'ainda '
                                                                                              'mais',
                                                                                    'linha': [   'Qc5+',
                                                                                                 'Kb2',
                                                                                                 'Qb4+'],
                                                                                    'nota': 'O '
                                                                                            'caminho '
                                                                                            'mais '
                                                                                            'curto '
                                                                                            'de '
                                                                                            'todos '
                                                                                            'até a '
                                                                                            'mesma '
                                                                                            'posição.'},
                                                                                {   'titulo': '2.Da7+? '
                                                                                              '— o '
                                                                                              'erro '
                                                                                              'que '
                                                                                              'devolve '
                                                                                              'o '
                                                                                              'empate',
                                                                                    'linha': [   'Qc5+',
                                                                                                 'Ka2',
                                                                                                 'Qa7+',
                                                                                                 'Kb1'],
                                                                                    'nota': 'Esta '
                                                                                            'variante '
                                                                                            'ensina '
                                                                                            'duas '
                                                                                            'coisas '
                                                                                            'importantes: '
                                                                                            'não '
                                                                                            'se '
                                                                                            'ganha '
                                                                                            'com a '
                                                                                            'dama '
                                                                                            'branca '
                                                                                            'em '
                                                                                            'qualquer '
                                                                                            'posição '
                                                                                            'inicial, '
                                                                                            'e o '
                                                                                            'lado '
                                                                                            'fraco '
                                                                                            'deve '
                                                                                            'sempre '
                                                                                            'buscar '
                                                                                            'esta '
                                                                                            'posição '
                                                                                            'relativa '
                                                                                            'entre '
                                                                                            'o '
                                                                                            'próprio '
                                                                                            'rei e '
                                                                                            'a '
                                                                                            'dama, '
                                                                                            'sempre '
                                                                                            'que '
                                                                                            'possível. '
                                                                                            'Depois '
                                                                                            'deste '
                                                                                            'erro, '
                                                                                            'não é '
                                                                                            'mais '
                                                                                            'possível '
                                                                                            'voltar '
                                                                                            'à '
                                                                                            'manobra '
                                                                                            'correta.'},
                                                                                {   'titulo': 'Outra '
                                                                                              'ordem '
                                                                                              'de '
                                                                                              'xeques '
                                                                                              'até '
                                                                                              'a '
                                                                                              'mesma '
                                                                                              'posição',
                                                                                    'linha': [   'Qc5+',
                                                                                                 'Ka2',
                                                                                                 'Qc4+',
                                                                                                 'Kb2',
                                                                                                 'Qb4+'],
                                                                                    'nota': 'Mais '
                                                                                            'uma '
                                                                                            'ordem '
                                                                                            'possível, '
                                                                                            'levando '
                                                                                            'ao '
                                                                                            'mesmo '
                                                                                            'ponto.'},
                                                                                {   'titulo': 'Posição '
                                                                                              'se '
                                                                                              'repete '
                                                                                              'se '
                                                                                              'o '
                                                                                              'rei '
                                                                                              'insistir '
                                                                                              'em '
                                                                                              'c1',
                                                                                    'linha': [   'Qc5+',
                                                                                                 'Ka2',
                                                                                                 'Qc4+',
                                                                                                 'Ka3',
                                                                                                 'Qa6+',
                                                                                                 'Kb2',
                                                                                                 'Qb5+',
                                                                                                 'Kc1',
                                                                                                 'Qc4+',
                                                                                                 'Kb2',
                                                                                                 'Qb4+'],
                                                                                    'nota': 'O rei '
                                                                                            'preto '
                                                                                            'pode '
                                                                                            'tentar '
                                                                                            'fugir '
                                                                                            'para '
                                                                                            'c1, '
                                                                                            'mas a '
                                                                                            'mesma '
                                                                                            'posição '
                                                                                            'simplesmente '
                                                                                            'se '
                                                                                            'repete.'},
                                                                                {   'titulo': 'A '
                                                                                              'outra '
                                                                                              'imagem '
                                                                                              'de '
                                                                                              'mate',
                                                                                    'linha': [   'Qc5+',
                                                                                                 'Ka2',
                                                                                                 'Qc4+',
                                                                                                 'Ka3',
                                                                                                 'Qa6+',
                                                                                                 'Kb2',
                                                                                                 'Qb5+',
                                                                                                 'Ka3',
                                                                                                 'Qa5+',
                                                                                                 'Kb2',
                                                                                                 'Qb4+',
                                                                                                 'Kc1',
                                                                                                 'Qd2+',
                                                                                                 'Kb1',
                                                                                                 'Qc2#'],
                                                                                    'nota': 'Se, '
                                                                                            'em '
                                                                                            'vez '
                                                                                            'de '
                                                                                            'voltar '
                                                                                            'para '
                                                                                            'a2, o '
                                                                                            'rei '
                                                                                            'preto '
                                                                                            'insistir '
                                                                                            'em '
                                                                                            'c1, '
                                                                                            'surge '
                                                                                            'uma '
                                                                                            'segunda '
                                                                                            'rede '
                                                                                            'de '
                                                                                            'mate.'}],
                                                            'regra_destaque': 'Com o rei forte '
                                                                              'perto o bastante do '
                                                                              'canto onde a dama '
                                                                              'inimiga promoveu, '
                                                                              'uma sequência '
                                                                              'precisa de xeques '
                                                                              'aproxima o próprio '
                                                                              'rei até criar uma '
                                                                              'rede de mate — mas '
                                                                              'a ordem dos xeques '
                                                                              'importa: um lance '
                                                                              'impreciso (como '
                                                                              'Da7+ cedo demais) '
                                                                              'pode devolver o '
                                                                              'empate de graça.'}],
                                        'regras': [   'Nem sempre que os dois jogadores promovem a '
                                                      'dama a partida é empate — há bastante '
                                                      'chance de perder, sobretudo se a dama '
                                                      'promove na casa do canto.',
                                                      'Com o rei forte perto o bastante do canto, '
                                                      'uma sequência precisa de xeques aproxima o '
                                                      'próprio rei até criar uma rede de mate — '
                                                      'mas a ordem dos xeques importa.']}]}]}
CAPITULO_3 = {'numero': 3,
 'titulo': 'Torre contra peão',
 'intro': 'O duelo mais frequente e mais complexo de peça contra peão passado: ao '
          'contrário do cavalo e da dama, a torre atua o tabuleiro inteiro, então o '
          'resultado quase sempre depende dos dois reis — contagem de tempos, corte '
          'horizontal, rodeio, ombrada (empurrar o rei adversário com o próprio rei) e '
          'zugzwang se cruzam o tempo todo. Muitos finais de torre do meio-jogo acabam '
          'se transformando em um destes, quando um lado entrega a torre por um peão '
          'passado.',
 'secoes': [{'id': 'torre-peao',
             'titulo': 'Torre contra peão',
             'resumo': 'Os nove finais fundamentais de torre contra peão passado: '
                       'contagem simples de tempos, corte horizontal, rei forte atrás '
                       'e lateral do peão (com a ombrada e o rodeio), zugzwang, os '
                       'casos especiais do peão de cavalo e de torre, e o limite em '
                       'que o peão, sozinho, já vence a torre.',
             'finais': [{'n': 21,
                         'titulo': 'Os reis não se incomodam',
                         'conceito': 'Quando nenhum dos reis consegue atrapalhar o '
                                     'plano do outro, o resultado se decide por uma '
                                     'simples contagem de tempos.',
                         'texto': ['A forma mais simples de abordar esses finais é '
                                   'contar tempos: quantos lances o lado da torre '
                                   'precisa para controlar a casa de coroação com o '
                                   'rei e a torre juntos, contra quantos lances o lado '
                                   'do peão precisa para levar o rei até perto e '
                                   'coroar.',
                                   'Essa contagem simples só funciona quando nenhum '
                                   'rei consegue atrapalhar o plano do outro no '
                                   'caminho — e é exatamente essa a situação da '
                                   'posição a seguir: os reis não se incomodam, os '
                                   'xeques de torre não ganham tempo, e não há nenhuma '
                                   'outra circunstância especial.'],
                         'posicoes': [{'rotulo': 'Simplesmente contando',
                                       'fen': '4R3/8/7K/8/1kp5/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Kg5',
                                                 'Kc3',
                                                 'Kf4',
                                                 'Kd2',
                                                 'Rd8+',
                                                 'Ke2',
                                                 'Rc8'],
                                       'notas': {0: 'O rei branco está longe, mas tem '
                                                    'tempo: ele precisa de 5 lances '
                                                    'para ajudar a controlar a casa de '
                                                    'coroação (c1), e as pretas '
                                                    'precisam de 4 para coroar. '
                                                    'Jogando as brancas, isso é '
                                                    'suficiente — **1.Rg5!** começa a '
                                                    'aproximação.',
                                                 6: 'A torre já está atrás do peão e o '
                                                    'rei branco cortou o caminho do '
                                                    'rei preto: daqui em diante é só '
                                                    'técnica, o peão cai e a torre '
                                                    'garante a vitória.'},
                                       'regra_destaque': 'Quando os reis não '
                                                         'interferem um no outro, o '
                                                         'resultado se decide pela '
                                                         'contagem simples: tempos do '
                                                         'rei+torre para controlar a '
                                                         'coroação contra tempos do '
                                                         'rei+peão para coroar.'},
                                      {'rotulo': 'A mesma posição, com as pretas a '
                                                 'jogar',
                                       'fen': '4R3/8/7K/8/1kp5/8/8/8 b - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': ['c3',
                                                 'Kg6',
                                                 'Kb3',
                                                 'Re6',
                                                 'Kb2',
                                                 'Re2+',
                                                 'c2',
                                                 'Kf5',
                                                 'Kb1',
                                                 'Rxc2'],
                                       'notas': {0: 'A mesma posição exata, mas agora '
                                                    'é a vez das pretas jogarem '
                                                    'primeiro — e isso já basta para '
                                                    'inverter o resultado: a contagem '
                                                    'de tempos agora favorece o peão, '
                                                    'e o melhor que as brancas '
                                                    'conseguem é um empate.',
                                                 9: 'O rei branco nunca chega a tempo '
                                                    'de impedir a coroação por conta '
                                                    'própria; a torre acaba capturando '
                                                    'o peão, mas só depois dele já ter '
                                                    'cumprido seu papel de forçar as '
                                                    'trocas — posição de tablas.'},
                                       'regra_destaque': 'A mesma posição, com o lado '
                                                         'a jogar trocado, muda o '
                                                         'resultado: a contagem de '
                                                         'tempos é decisiva até no '
                                                         'detalhe de quem tem a vez.'}],
                         'regras': ['Em finais de torre contra peão onde nenhum rei '
                                    'consegue atrapalhar o plano do outro, o resultado '
                                    'se decide por uma contagem simples de tempos: '
                                    'quantos lances o rei e a torre precisam para '
                                    'controlar a casa de coroação, contra quantos '
                                    'lances o rei do peão precisa para apoiar a '
                                    'coroação.']},
                        {'n': 22,
                         'titulo': 'Rei defensor na terceira. O corte horizontal',
                         'conceito': 'Quando o rei e o peão do lado fraco ainda estão '
                                     'atrasados, cortar o rei adversário '
                                     'horizontalmente com a torre pode ser, por si só, '
                                     'suficiente para ganhar — mas só funciona dentro '
                                     'de certas condições.',
                         'texto': ['Quando o rei defensor e seu peão ainda estão '
                                   'bastante atrasados (em geral, se ainda não '
                                   'cruzaram a metade do tabuleiro), vale a pena '
                                   'considerar o corte horizontal antes de mais nada: '
                                   'se esse recurso funcionar, o resto se torna '
                                   'irrelevante.',
                                   'O corte horizontal é eficaz quando o rei do lado '
                                   'fraco fica na terceira fila (contada a partir do '
                                   'próprio campo) e é completamente decisivo quando o '
                                   'peão é de torre, ou quando o rei e o peão já se '
                                   'separaram. Fora dessas condições, o rei defensor '
                                   'pode simplesmente contornar o corte pelo lado '
                                   'oposto do peão — perdendo tempo, mas quase sempre '
                                   'salvando a partida.',
                                   'Antes de ver a posição principal, vale registrar o '
                                   'Diagrama 5.2, um estudo de Max Euwe (1934) sobre o '
                                   'mesmo princípio simples de contagem do Final 21: '
                                   'com rei e peão pretos fixos e a torre branca em '
                                   'a1, Euwe mapeou, casa a casa, de qual lugar do '
                                   'tabuleiro o rei branco ainda consegue chegar a '
                                   'tempo de ajudar a conter o peão — e de qual lugar '
                                   'não consegue mais. A lição prática é que essa '
                                   "'zona de empate' não é um corte limpo e óbvio: ela "
                                   'depende de detalhes finos de geometria do '
                                   'tabuleiro, por isso vale sempre conferir com '
                                   'cálculo (ou com o motor) em vez de confiar só na '
                                   'intuição de contagem simples.'],
                         'posicoes': [{'rotulo': 'O corte horizontal decide sozinho',
                                       'fen': '7K/6R1/1k6/p7/8/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Rg5',
                                                 'a4',
                                                 'Kg7',
                                                 'a3',
                                                 'Rg3',
                                                 'a2',
                                                 'Ra3',
                                                 'Kb5',
                                                 'Rxa2'],
                                       'notas': {0: 'O rei branco está muito longe do '
                                                    'peão (h8), mas isso não importa: '
                                                    '**1.Rg5!** corta o rei preto na '
                                                    'quinta fila, impedindo-o de '
                                                    'cruzar para apoiar o peão. É a '
                                                    'única jogada que ganha — 1.Rg8? '
                                                    'deixa o rei preto escapar por c5 '
                                                    'ou b5 (ver lance alternativo).',
                                                 4: 'Com o rei preto definitivamente '
                                                    'cortado, a torre ainda precisa '
                                                    'fechar o cerco: **3.Rg3!** ameaça '
                                                    'ir a a3 e capturar o peão, já que '
                                                    'o rei preto não pode atravessar a '
                                                    'terceira fila para defendê-lo.',
                                                 6: 'A torre ocupa a coluna a: a '
                                                    'partir daqui, qualquer avanço do '
                                                    'peão termina em captura, e o rei '
                                                    'preto nunca conseguiu se '
                                                    'aproximar o suficiente para '
                                                    'ajudar.'},
                                       'regra_destaque': 'Com o rei do lado fraco '
                                                         'ainda na terceira fila (a '
                                                         'partir do seu próprio campo) '
                                                         'e separado do peão pelo '
                                                         'corte, a torre resolve '
                                                         'sozinha — não é preciso '
                                                         'esperar pelo rei forte.',
                                       'alternativas': [{'titulo': '1.Rg8?? — erro: '
                                                                   'deixa o rei preto '
                                                                   'escapar',
                                                         'linha': ['Rg8',
                                                                   'Kc5',
                                                                   'Kg7',
                                                                   'a4',
                                                                   'Kf6',
                                                                   'a3',
                                                                   'Ke5',
                                                                   'Kc4',
                                                                   'Ke4',
                                                                   'a2',
                                                                   'Ra8',
                                                                   'Kb3',
                                                                   'Kd3',
                                                                   'Kb2'],
                                                         'nota': 'Sem cortar a quinta '
                                                                 'fila, o rei preto '
                                                                 'passa por c5/b5 e '
                                                                 'acompanha o peão até '
                                                                 'a coroação com '
                                                                 'tranquilidade — o '
                                                                 'resultado cai de '
                                                                 'vitória para empate '
                                                                 '(confirmado pelo '
                                                                 'Stockfish em 0.00 do '
                                                                 'lance 1 em diante). '
                                                                 'Essa mesma posição '
                                                                 'de empate vai '
                                                                 'reaparecer mais '
                                                                 'adiante (Final 28).',
                                                         'espera_resultado': 'erro'}]},
                                      {'rotulo': 'Série do corte horizontal — corte '
                                                 'contundente',
                                       'fen': '7K/6R1/2k5/1p6/8/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': [],
                                       'notas': {0: 'Mesma ideia do diagrama '
                                                    'principal, com o peão uma coluna '
                                                    'mais perto do centro (b, não a): '
                                                    'o corte na quinta fila continua '
                                                    'sendo, sozinho, suficiente para '
                                                    'ganhar — **1.Rg5!** é a única '
                                                    'jogada vencedora.'}},
                                      {'rotulo': 'Série do corte horizontal — corte '
                                                 'pouco à frente',
                                       'fen': '7K/8/8/2k5/1p4R1/8/8/8 w - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': [],
                                       'notas': {0: 'O livro classifica esta posição '
                                                    "como 'o corte não é contundente, "
                                                    'mas ainda assim 1.Rg5 é a única '
                                                    "que ganha'. A verificação "
                                                    'exaustiva com Stockfish (todos os '
                                                    'lances legais das brancas, '
                                                    'incluindo 1.Rg5, com profundidade '
                                                    'até 40) mostra 0.00 em qualquer '
                                                    'um deles: a posição exata da '
                                                    'torre, do rei e do peão foi '
                                                    'conferida pixel a pixel contra a '
                                                    'imagem do livro e está correta, '
                                                    'então aqui preferimos o veredito '
                                                    'do motor ao do livro — um rei e '
                                                    'peão já nessa fila, com o rei '
                                                    'forte ainda na casa do canto, '
                                                    'bastam para segurar o empate.'}},
                                      {'rotulo': 'Série do corte horizontal — corte '
                                                 'inútil',
                                       'fen': '7R/8/2K5/8/1pk5/8/8/8 w - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': [],
                                       'notas': {0: 'Mesmo com o rei branco já bem '
                                                    'adiantado (c6, perto da ação) e a '
                                                    'torre pronta para qualquer corte, '
                                                    'uma fila mais adiantada do rei e '
                                                    'do peão pretos já basta para '
                                                    'anular completamente o recurso — '
                                                    'as brancas não ganham nem '
                                                    'jogando, confirmando por que o '
                                                    'corte horizontal só funciona '
                                                    'enquanto o lado fraco ainda está '
                                                    'atrasado.'}}],
                         'regras': ['Com o rei do lado fraco ainda na terceira fila '
                                    '(contada a partir do seu próprio campo) e '
                                    'separado do seu peão, o corte horizontal da torre '
                                    'já é suficiente, sozinho, para ganhar — sobretudo '
                                    'com peão de torre.',
                                    'Uma fila mais adiantado o corte perde força '
                                    'rapidamente: pode ainda decidir a partida '
                                    '(dependendo de detalhes finos que vale conferir '
                                    'com cálculo), mas deixa de ser um recurso '
                                    'automático, e mais uma fila à frente deixa de '
                                    'funcionar por completo.']},
                        {'n': 23,
                         'titulo': 'O rei forte na zona de trás do peão',
                         'conceito': 'Empurrar o rei adversário só de frente, pela '
                                     'retaguarda, não funciona contra a maioria dos '
                                     'peões: a coroação de cavalo salva o lado fraco. '
                                     'O recurso realmente eficaz é o rodeio — '
                                     'contornar o peão e aparecer do lado oposto.',
                         'texto': ['Quando o rei forte pressiona o adversário pela '
                                   'retaguarda (na mesma coluna do peão, vindo de '
                                   'trás) e o rei inimigo lhe barra o caminho, pode '
                                   'parecer que basta continuar empurrando com xeques '
                                   'de torre. Mas, com a maioria dos peões, essa '
                                   'pressão simples não funciona: o lado fraco sempre '
                                   'tem o recurso da coroação de cavalo, mantendo o '
                                   'cavalo grudado ao próprio rei para nunca ser '
                                   'capturado.',
                                   'O procedimento realmente eficaz, quando o rei '
                                   'forte está atrás do peão, é o rodeio: dar a volta '
                                   'e aparecer do lado oposto do peão, abandonando a '
                                   'pressão direta que não leva a nada.',
                                   'Há uma exceção de tempo: o rei forte não tem tempo '
                                   'de completar o rodeio se o peão já estiver na '
                                   'quinta fila — a menos que a torre já esteja '
                                   'posicionada atrás do peão. Por isso, uma fila mais '
                                   'adiantado (Diagrama 5.5), o rodeio já funciona; '
                                   'ver a comparação completa na série de diagramas a '
                                   'seguir.'],
                         'posicoes': [{'rotulo': 'A coroação de cavalo salva as pretas',
                                       'fen': '8/8/3K3R/8/2pk4/8/8/8 w - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': ['Rh4+',
                                                 'Kd3',
                                                 'Kd5',
                                                 'c3',
                                                 'Rh3+',
                                                 'Kd2',
                                                 'Kc4',
                                                 'c2',
                                                 'Rh2+',
                                                 'Kd1',
                                                 'Kd3',
                                                 'c1=N+',
                                                 'Ke3',
                                                 'Nb3',
                                                 'Rb2',
                                                 'Nc1'],
                                       'notas': {0: 'O rei branco empurra pela '
                                                    'retaguarda e a torre vai dando '
                                                    'xeques, mas isso não basta: o '
                                                    'peão sempre consegue chegar à '
                                                    'primeira fila a tempo de coroar '
                                                    'em cavalo.',
                                                 11: '**12...c1=N+!** É só '
                                                     'aparentemente um choque: coroar '
                                                     'em dama perderia a peça '
                                                     'imediatamente ao xeque de mate '
                                                     'ameaçado, mas o cavalo, com '
                                                     'xeque, é perfeitamente '
                                                     'suficiente para empatar.',
                                                 13: 'A partir daqui, a tarefa das '
                                                     'pretas é só manter o cavalo '
                                                     'sempre o mais perto possível do '
                                                     'próprio rei, quase sempre com '
                                                     'lances únicos — exatamente o '
                                                     'mesmo recurso do Final 8. '
                                                     '(Atenção: esse recurso só '
                                                     'funciona com o peão coroando em '
                                                     'colunas centrais ou de '
                                                     'cavalo/bispo; com peão de torre '
                                                     'o cavalo se perderia — ver Final '
                                                     '27.)'},
                                       'regra_destaque': 'A pressão do rei forte vindo '
                                                         'só pela retaguarda é '
                                                         'ineficaz contra peões das '
                                                         'colunas b a g, graças à '
                                                         'coroação de cavalo — o '
                                                         'recurso que realmente ganha '
                                                         'é o rodeio.'},
                                      {'rotulo': 'Uma fila mais adiantado, o rodeio já '
                                                 'funciona',
                                       'fen': '8/3K3R/8/2pk4/8/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Rh5+',
                                                 'Kd4',
                                                 'Kc6',
                                                 'c4',
                                                 'Kb5',
                                                 'c3',
                                                 'Rc5',
                                                 'Kd3',
                                                 'Kb4',
                                                 'c2',
                                                 'Kb3',
                                                 'c1=Q',
                                                 'Rxc1',
                                                 'Kd4',
                                                 'Kb4',
                                                 'Kd5'],
                                       'notas': {0: 'Com os reis e o peão uma fila '
                                                    'mais adiantados em relação ao '
                                                    'diagrama anterior, o rei branco '
                                                    'já tem tempo de completar o '
                                                    'rodeio: **1.Rh5+!** primeiro '
                                                    'afasta o rei preto do caminho, e '
                                                    '**2.Kc6!** já inicia a volta por '
                                                    'trás do peão.',
                                                 11: 'Dessa vez a coroação não salva: '
                                                     'sem o apoio do próprio rei (que '
                                                     'ficou para trás, cortado pelo '
                                                     'rodeio), a torre simplesmente '
                                                     'captura a dama assim que ela '
                                                     'nasce.'},
                                       'regra_destaque': 'Com o peão uma fila mais '
                                                         'adiantado (mas ainda não na '
                                                         'quinta), o rei forte já tem '
                                                         'tempo de completar o rodeio '
                                                         'e ganhar, mesmo que o rei '
                                                         'fraco tente bloquear pela '
                                                         'frente.'},
                                      {'rotulo': 'A mesma posição, com as pretas a '
                                                 'jogar',
                                       'fen': '8/3K3R/8/2pk4/8/8/8/8 b - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': ['c4',
                                                 'Rh1',
                                                 'c3',
                                                 'Rh3',
                                                 'Kc4',
                                                 'Rxc3+',
                                                 'Kxc3'],
                                       'notas': {0: 'A mesma posição exata do diagrama '
                                                    'anterior, mas agora com a vez de '
                                                    'jogar trocada: as pretas ganham '
                                                    'justamente o tempo que faltava '
                                                    'para o rei preto se manter em '
                                                    'oposição e segurar o empate — o '
                                                    'rodeio deixa de dar tempo.'},
                                       'regra_destaque': 'A mesma posição, só com o '
                                                         'lado a mover trocado, já não '
                                                         'é suficiente para as '
                                                         'brancas: o rodeio depende do '
                                                         'tempo exato disponível.'},
                                      {'rotulo': 'Série da oposição do rei por trás — '
                                                 'coroação de cavalo',
                                       'fen': '8/8/3K3R/8/2pk4/8/8/8 w - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': [],
                                       'notas': {0: 'A mesma posição do primeiro '
                                                    'diagrama deste final: tablas '
                                                    'jogue quem jogar, graças à '
                                                    'coroação de cavalo (ver análise '
                                                    'completa acima). Única observação '
                                                    'extra: com a torre já em h1 em '
                                                    'vez de h6, as brancas ganham de '
                                                    'corrida — a contagem simples de '
                                                    'tempos (Final 21) volta a valer '
                                                    'quando a torre já está '
                                                    'posicionada.'}},
                                      {'rotulo': 'Série da oposição do rei por trás — '
                                                 'rodeio',
                                       'fen': '8/3K3R/8/2pk4/8/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': [],
                                       'notas': {0: 'A mesma posição do segundo '
                                                    'diagrama deste final: as brancas '
                                                    'ganham jogando elas, mas as '
                                                    'pretas empatam se tiverem a vez — '
                                                    'o rodeio funciona, mas só com o '
                                                    'tempo certo (ver análise completa '
                                                    'acima).'}},
                                      {'rotulo': 'Série da oposição do rei por trás — '
                                                 'rodeio garantido',
                                       'fen': '3K3R/8/2pk4/8/8/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': [],
                                       'notas': {0: 'Mais uma fila adiantados, o '
                                                    'resultado já não depende de quem '
                                                    'tem a vez: o rodeio é tão rápido '
                                                    'que as brancas ganham jogando '
                                                    'qualquer um dos dois lados '
                                                    '(confirmado pelo Stockfish: '
                                                    'nitidamente a favor das brancas '
                                                    'tanto com elas quanto com as '
                                                    'pretas a mover). A torre funciona '
                                                    'bem em quase qualquer casa, mas '
                                                    'as casas do extremo da coluna '
                                                    'favorecem ainda mais o rodeio.'}}],
                         'regras': ['A pressão do rei forte só pela retaguarda é '
                                    'ineficaz contra a maioria dos peões, graças à '
                                    'coroação de cavalo — o recurso que realmente '
                                    'ganha é o rodeio: dar a volta e atacar o peão '
                                    'pelo lado oposto.',
                                    'O rei forte só não tem tempo de rodear se o peão '
                                    'já estiver na quinta fila — exceto se a torre já '
                                    'estiver posicionada atrás dele.']},
                        {'n': 24,
                         'titulo': 'O rei forte numa zona lateral',
                         'conceito': 'O lado da torre depende da colaboração do '
                                     'próprio rei para cercar o peão adversário — por '
                                     'isso é vantajoso para o rei inimigo se meter no '
                                     'caminho, obstruindo essa aproximação. Quando os '
                                     'reis se encontram de frente, o recurso chave é '
                                     'empurrar com o ombro (a ombrada).',
                         'texto': ['Como já vimos, o lado da torre precisa que seu '
                                   'próprio rei ajude a controlar e capturar o peão '
                                   'adversário. Por isso é vantajoso para o rei '
                                   'inimigo se colocar no caminho, obstruindo essa '
                                   'aproximação — um recurso sempre interessante, mas '
                                   'especialmente crítico quando o rei forte se '
                                   'aproxima por um lado lateral.',
                                   'Em muitas posições, a única forma de a torre '
                                   'receber apoio é colocar o próprio rei em oposição '
                                   "ao rival, com o objetivo de dar xeque e 'empurrar' "
                                   'o rei inimigo uma coluna (ou fila) para alcançar '
                                   'dois objetivos: aproximar o próprio rei e limitar '
                                   'a mobilidade do rei e/ou do peão adversários. A '
                                   'esse procedimento de disputa por uma casa-chave '
                                   "chamaremos 'empurrar com o ombro', ou simplesmente "
                                   '**ombrada**. O lado da torre tem todas as '
                                   'vantagens a seu favor nessa disputa, mas só a '
                                   'longo prazo — às vezes não há tempo de '
                                   'aproveitá-la.',
                                   'Outro recurso típico, especialmente quando o rei '
                                   'forte vem de um lado lateral, é o xeque oportuno '
                                   'de torre para ganhar um tempo importante, '
                                   'permitindo que a própria torre se posicione '
                                   'controlando o peão.'],
                         'posicoes': [{'rotulo': 'Os reis se empurram',
                                       'fen': '8/8/8/7K/3pk3/8/8/3R4 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Kg4',
                                                 'd3',
                                                 'Re1+',
                                                 'Kd4',
                                                 'Kf3',
                                                 'd2',
                                                 'Rd1',
                                                 'Kd3',
                                                 'Kf2',
                                                 'Kd4',
                                                 'Rxd2+',
                                                 'Ke4',
                                                 'Rd1',
                                                 'Kf4',
                                                 'Re1',
                                                 'Kg5'],
                                       'notas': {0: '**1.Kg4!** é a jogada mais '
                                                    'gráfica para empurrar o rei '
                                                    'adversário (embora não seja a '
                                                    'única que ganha — 1.Kh4! também '
                                                    'funciona): a ideia é chegar a g3 '
                                                    'no lance seguinte e, a partir '
                                                    'daí, empurrar o rei preto '
                                                    '(ombrada) para fora da zona-chave '
                                                    'e4-g3. Já se ameaça Re1, já que a '
                                                    'torre está em d1.',
                                                 2: 'O rei branco continua a oposição '
                                                    'para empurrar com eficácia '
                                                    '(ombrada): as pretas não '
                                                    'conseguem mais evitá-la, porque '
                                                    'precisam permanecer ao lado do '
                                                    'próprio peão.'},
                                       'regra_destaque': 'Quando os dois reis estão do '
                                                         'mesmo lado do peão, os '
                                                         'recursos principais são a '
                                                         'ombrada mútua entre os reis '
                                                         'e os xeques de torre para '
                                                         'ganhar tempo.'},
                                      {'rotulo': 'Ganhando um tempo com xeque',
                                       'fen': '7R/8/8/8/2K3p1/8/5k2/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Rf8+',
                                                 'Ke3',
                                                 'Rg8',
                                                 'Kf3',
                                                 'Kd3',
                                                 'Kf4',
                                                 'Rg7',
                                                 'g3',
                                                 'Rg8',
                                                 'Kf3',
                                                 'Rf8+',
                                                 'Kg4'],
                                       'notas': {0: 'O rei preto já está pronto para '
                                                    'apoiar o peão até a oitava fila e '
                                                    'não tem mais como melhorar de '
                                                    'posição — por isso a torre se '
                                                    'coloca atrás do peão sem perder '
                                                    'tempo: **1.Rf8+!** Cuidado para '
                                                    'não dar este xeque numa posição '
                                                    'em que o rei preto ainda possa '
                                                    'melhorar, e atenção para nunca '
                                                    'avançar o próprio rei antes do '
                                                    'peão.',
                                                 4: '**3.Kd3!** Empurrando com o ombro '
                                                    '(ombrada): o rei branco se '
                                                    'aproxima pelo lado, limitando '
                                                    'cada vez mais o espaço do rei '
                                                    'preto.'}},
                                      {'rotulo': 'Combinando xeque de torre e ombrada',
                                       'fen': '8/8/8/8/4p3/7K/5k2/R7 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Ra2+',
                                                 'Kf3',
                                                 'Ra7',
                                                 'e3',
                                                 'Rf7+',
                                                 'Ke2',
                                                 'Kg2',
                                                 'Kd1',
                                                 'Kf3',
                                                 'e2',
                                                 'Rd7+',
                                                 'Kc2'],
                                       'notas': {0: 'Este exemplo combina os dois '
                                                    'recursos dominantes quando os '
                                                    'reis estão do mesmo lado do peão: '
                                                    'de novo o rei preto já está na '
                                                    'posição ideal em relação ao '
                                                    'próprio peão, e por isso '
                                                    '**1.Ra2!** (o xeque) é muito '
                                                    'incômodo para ele. Outras jogadas '
                                                    'não ganham.',
                                                 4: 'Agora os reis ficam de frente um '
                                                    'para o outro — a situação mais '
                                                    'favorável para um xeque vindo de '
                                                    'trás e a consequente ombrada do '
                                                    'rei forte.'}}],
                         'regras': ['Quando os dois reis estão do mesmo lado do peão, '
                                    'os recursos principais do lado forte são empurrar '
                                    'o rei inimigo com o próprio rei (a ombrada) e '
                                    'usar xeques de torre para ganhar tempo.',
                                    'Em posições normais da torre, o lado forte ganha '
                                    'se conseguir a oposição lateral dos reis antes de '
                                    'o peão chegar à sexta fila.']},
                        {'n': 25,
                         'titulo': 'A torre na frente do peão',
                         'conceito': 'Ao contrário dos finais de peões (ou de peças '
                                     'menos poderosas), com uma torre no tabuleiro é '
                                     'raro encontrar zugzwang — mas, quando a torre '
                                     'controla o peão pela frente, o zugzwang pode ser '
                                     'exatamente o que decide a partida.',
                         'texto': ['Diferentemente dos finais de peões ou de outras '
                                   'peças menos poderosas, com uma torre no tabuleiro '
                                   'é pouco frequente encontrar posições de zugzwang, '
                                   'já que a torre costuma ter muitos lances '
                                   'disponíveis e dificilmente todos eles são '
                                   'prejudiciais ao próprio lado.',
                                   'Apesar disso, no final de torre contra peão o '
                                   'zugzwang desempenha um papel essencial quando a '
                                   'torre controla o peão pela frente — como neste '
                                   'famoso estudo composto por Reti em 1928, que '
                                   'ilustra bem essa importância teórica.'],
                         'posicoes': [{'rotulo': 'Reti, 1928 — o duplo zugzwang',
                                       'fen': '8/5K2/8/4pk2/4R3/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Re2',
                                                 'e4',
                                                 'Re1',
                                                 'Kf4',
                                                 'Ke6',
                                                 'e3',
                                                 'Kd5',
                                                 'Kf3',
                                                 'Kd4',
                                                 'e2',
                                                 'Kd3',
                                                 'Kf4',
                                                 'Rxe2',
                                                 'Kf5'],
                                       'notas': {0: '**1.Re2!** (ou 1.Re3) é a jogada '
                                                    'correta. A tentação natural seria '
                                                    '1.Re1?, mas depois de 1...e4! a '
                                                    'posição vira zugzwang: a oposição '
                                                    'dos reis impede o rei branco de '
                                                    'se aproximar, qualquer lance de '
                                                    'torre pela primeira fila libera o '
                                                    'avanço do peão, e os lances de '
                                                    'torre a e2/e3 ou o xeque em f1 só '
                                                    'dão tempo às pretas — é '
                                                    'exatamente a posição do Diagrama '
                                                    'de análise 5.10, mostrado a '
                                                    'seguir, onde o resultado já é '
                                                    'apenas empate.',
                                                 3: 'Com a torre bem colocada desde o '
                                                    'início, agora sim tudo fica fácil '
                                                    'de entender: as pretas não '
                                                    'conseguem manter a posição, e '
                                                    'confirma-se que esta é uma '
                                                    'posição de duplo zugzwang — ruim '
                                                    'para qualquer um dos dois lados '
                                                    'que tenha de jogar.',
                                                 5: 'O rei preto agora precisa ceder '
                                                    'passagem ao rival e permitir o '
                                                    'rodeio.'},
                                       'regra_destaque': 'Com a torre já bem postada '
                                                         'na frente do peão '
                                                         '(controlando-o sem ficar '
                                                         'presa a xeques), a posição '
                                                         'pode virar um duplo '
                                                         'zugzwang: tanto faz quem tem '
                                                         'de jogar, é sempre ruim para '
                                                         'quem joga.'},
                                      {'rotulo': 'Diagrama de análise 5.10 — depois do '
                                                 'erro 1.Re1? e4!',
                                       'fen': '8/5K2/8/5k2/4p3/8/8/4R3 w - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': ['Ke7',
                                                 'Ke5',
                                                 'Ra1',
                                                 'e3',
                                                 'Rb1',
                                                 'Kd4',
                                                 'Ra1',
                                                 'e2',
                                                 'Ke6',
                                                 'Ke4',
                                                 'Rb1',
                                                 'Ke3',
                                                 'Ke5',
                                                 'Kd2'],
                                       'notas': {0: 'É exatamente a posição de '
                                                    'zugzwang que o livro quer '
                                                    'discutir: a oposição dos reis '
                                                    'impede o rei branco de se '
                                                    'aproximar, qualquer lance de '
                                                    'torre pela primeira fila deixa o '
                                                    'peão avançar, e mover a torre '
                                                    'para e2/e3 (ou dar xeque em f1) '
                                                    'só serve para as pretas ganharem '
                                                    'tempo no futuro.',
                                                 1: '**2.Ke7** é a tentativa mais '
                                                    'lógica: o rei branco tenta '
                                                    'completar o rodeio. As pretas '
                                                    'respondem mantendo a oposição dos '
                                                    'reis — de novo uma posição de '
                                                    'zugzwang, sem progresso possível '
                                                    'para as brancas.'},
                                       'regra_destaque': 'Um único lance de diferença '
                                                         'na posição da torre (e1 em '
                                                         'vez de e2/e3) transforma uma '
                                                         'vitória clara num empate — '
                                                         'prova de como o zugzwang '
                                                         'pode ser decisivo mesmo em '
                                                         'finais de torre.'}],
                         'regras': ['Com a torre controlando o peão pela frente, o '
                                    'zugzwang pode decidir a partida: vale a pena '
                                    'sempre verificar se a posição não é, na verdade, '
                                    'de duplo zugzwang antes de escolher o lance da '
                                    'torre.',
                                    'A casa exata em que a torre se coloca na frente '
                                    'do peão importa — uma diferença de uma única casa '
                                    'pode transformar vitória em empate.']},
                        {'n': 26,
                         'titulo': 'Temas especiais do peão de cavalo',
                         'conceito': 'O peão de cavalo tem personalidade própria: além '
                                     'de abrir possibilidades de afogamento que '
                                     'favorecem o lado do peão, ele cria um corredor '
                                     'estreito — a coluna de torre — que pode obrigar '
                                     'o rei fraco a se colocar na frente do próprio '
                                     'peão repetidas vezes, quase sempre fatal.',
                         'texto': ['Como já sabemos, os peões das colunas extremas '
                                   'costumam ter personalidade própria. O mais '
                                   "'caprichoso' é quase sempre o peão de torre, ao "
                                   'qual dedicamos uma seção especial mais adiante. '
                                   'Mas o peão de cavalo também tem suas '
                                   'particularidades.',
                                   'Além de algumas posições de afogamento que '
                                   'favorecem o lado do peão, existe uma circunstância '
                                   'importante que favorece o lado da torre: se o rei '
                                   'fraco é obrigado a se colocar na frente do próprio '
                                   'peão e depois aparece pelo lado da coluna de '
                                   'torre, ele pode facilmente ser obrigado a se '
                                   'colocar na frente do peão outra vez — e a coluna '
                                   'de torre é um corredor muito estreito para escapar '
                                   'dessa armadilha.',
                                   'A posição a seguir é um estudo de Kopaev que, além '
                                   'de ilustrar os temas especiais do peão de cavalo, '
                                   'serve para revisar quase todos os temas dos finais '
                                   'de torre contra peão vistos até aqui.'],
                         'posicoes': [{'rotulo': 'Kopaev, 1954',
                                       'fen': '3K4/4R3/8/1p6/8/2k5/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Rc7+',
                                                 'Kb3',
                                                 'Kd7',
                                                 'b4',
                                                 'Kd6',
                                                 'Ka2',
                                                 'Kc5',
                                                 'b3',
                                                 'Kb4',
                                                 'b2',
                                                 'Ra7+',
                                                 'Kb1',
                                                 'Kb3',
                                                 'Kc1',
                                                 'Rc7+',
                                                 'Kb1',
                                                 'Rb7',
                                                 'Kc1',
                                                 'Ka2'],
                                       'notas': {0: '**1.Rc7+!** ganha um tempo com o '
                                                    'xeque. A posição relativa do rei '
                                                    'e do peão pretos é a mesma do '
                                                    'Diagrama 5.6 — a mais favorável '
                                                    'para preparar o avanço —, por '
                                                    'isso este xeque é especialmente '
                                                    'incômodo.',
                                                 2: '**2.Kd7** — o sentido de 1...Kb3 '
                                                    '(em vez de 1...Kd3) está '
                                                    'exatamente em ganhar um tempo em '
                                                    'relação à variante 2.Rb7? b4 '
                                                    '3.Kc7 Kc3!, onde as pretas já '
                                                    'teriam ganhado um tempo a mais.',
                                                 4: '**3.Kd6!** Um detalhe importante: '
                                                    'o rei branco continua se '
                                                    'aproximando, mas evitando que o '
                                                    "rei preto escape pelo 'lado bom' "
                                                    'do peão de cavalo. Um erro típico '
                                                    'seria 3.Kc6?, que cai direto para '
                                                    'empate (ver lance alternativo).',
                                                 5: '**3...Ka2** — aqui reside o '
                                                    'desastre. É claro que o rei preto '
                                                    'precisa se afastar do caminho do '
                                                    'próprio peão, mas a coluna de '
                                                    'torre é um corredor muito '
                                                    'estreito para fazer isso com '
                                                    'segurança.',
                                                 6: '**4.Kc5!** Já não importa mais '
                                                    'ocupar a coluna c — 4.Kd5 também '
                                                    'ganha. Até mesmo 4.Ra7+?! (mais '
                                                    'desajeitado) ganha, o que só '
                                                    'confirma o quanto é incômodo para '
                                                    'as pretas ter o rei na frente do '
                                                    'peão de cavalo.',
                                                 8: '**5.Kb4!** O rei branco se '
                                                    'aproveita — e até abusa — da '
                                                    'posição desajeitada do '
                                                    'adversário. Aqui 5.Ra7 ou 5.Kc4 '
                                                    'também ganham.',
                                                 10: '**6.Ra7+** — com qualquer outro '
                                                     'peão o rei preto poderia fugir '
                                                     'para a esquerda, mas aqui ele é '
                                                     'obrigado a voltar a obstruir o '
                                                     'próprio peão.',
                                                 16: 'Agora aparece outro tema '
                                                     'específico do peão de cavalo, '
                                                     'desta vez a favor do '
                                                     '**defensor**: a possibilidade de '
                                                     'um afogamento. Mas aqui as '
                                                     'brancas conseguem evitá-lo — é '
                                                     'preciso cuidado: 9.Rc2?? '
                                                     'permitiria 9...Ka1! e as pretas '
                                                     'escapariam para o empate.',
                                                 18: '**10.Ka2+-** Conclusão prática '
                                                     'confirmada: quando o rei fraco é '
                                                     'forçado a se colocar '
                                                     'repetidamente na frente do '
                                                     'próprio peão de cavalo (ou de '
                                                     'torre), suas opções de defesa '
                                                     'diminuem drasticamente.'},
                                       'regra_destaque': 'Se for possível obrigar o '
                                                         'rei fraco a ficar na frente '
                                                         'do próprio peão de cavalo '
                                                         '(ou de torre) mais de uma '
                                                         'vez, as opções de defesa '
                                                         'desaparecem rapidamente — '
                                                         'vale a pena jogar para esse '
                                                         'tema.',
                                       'alternativas': [{'titulo': '3.Kc6? — erro: '
                                                                   'ombrada das pretas '
                                                                   'salva o empate',
                                                         'linha': ['Rc7+',
                                                                   'Kb3',
                                                                   'Kd7',
                                                                   'b4',
                                                                   'Kc6',
                                                                   'Kc4',
                                                                   'Kb6+',
                                                                   'Kd3',
                                                                   'Ka5',
                                                                   'b3',
                                                                   'Rb7',
                                                                   'Kc2',
                                                                   'Ka4',
                                                                   'b2'],
                                                         'nota': 'Depois de 3.Kc6?, as '
                                                                 'pretas respondem '
                                                                 '3...Kc4! empurrando '
                                                                 'com o ombro '
                                                                 '(ombrada) — e, uma '
                                                                 'vez desfeitas todas '
                                                                 'as interferências '
                                                                 'entre os reis, basta '
                                                                 'contar: as pretas '
                                                                 'precisam de 4 tempos '
                                                                 'para coroar e as '
                                                                 'brancas de 5 para '
                                                                 'controlar b1 com rei '
                                                                 'e torre juntos. '
                                                                 'Resultado: empate '
                                                                 '(confirmado pelo '
                                                                 'Stockfish em 0.00 do '
                                                                 'lance 5 em diante).',
                                                         'espera_resultado': 'erro'}]}],
                         'regras': ['O peão de cavalo cria um corredor estreito (a '
                                    'coluna de torre) perto do canto: se o rei fraco '
                                    'for obrigado a se colocar repetidamente na frente '
                                    'do próprio peão, suas chances de defesa '
                                    'desaparecem rapidamente.',
                                    'O peão de cavalo também guarda, a favor do '
                                    'defensor, possibilidades de afogamento — um '
                                    'detalhe que o lado forte precisa sempre verificar '
                                    'antes de cada lance de torre.']},
                        {'n': 27,
                         'titulo': 'Peão de torre — o empurrão desde trás',
                         'conceito': 'O cavalo no canto sempre se perde — por isso, '
                                     'com peão de torre, a pressão do rei forte vindo '
                                     'pela retaguarda (que falhava com qualquer outro '
                                     'peão) volta a ser muito eficaz.',
                         'texto': ['No estudo do Final 9 já vimos que o cavalo no '
                                   'canto do tabuleiro se perde. Por isso, a mesma '
                                   'posição do Diagrama 5.4 — mas com peão de torre em '
                                   'vez de peão de cavalo — tem um desfecho bem '
                                   'diferente: essa circunstância torna muito eficaz a '
                                   'pressão do rei por trás contra o peão de torre, já '
                                   'que a coroação de cavalo deixa de ser um recurso '
                                   'salvador.',
                                   'Mas o peão de torre tem outro truque na manga: '
                                   'embora não consiga coroar em cavalo com segurança, '
                                   'ele compensa um pouco essa limitação com a '
                                   'possibilidade de afogar o próprio rei — o tema do '
                                   'segundo diagrama deste final.'],
                         'posicoes': [{'rotulo': 'O cavalo no canto se perde: o '
                                                 'empurrão funciona',
                                       'fen': '7R/8/1K6/8/pk6/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Rh4+',
                                                 'Kb3',
                                                 'Kb5',
                                                 'a3',
                                                 'Rh3+',
                                                 'Kb2',
                                                 'Kb4',
                                                 'a2',
                                                 'Rh2+',
                                                 'Kb1',
                                                 'Kb3',
                                                 'a1=N+',
                                                 'Kc3'],
                                       'notas': {0: 'As brancas ganham de corrida, sem '
                                                    'sutilezas: **1.Th4+!** inicia uma '
                                                    'sequência de xeques combinados '
                                                    'com a aproximação do rei.',
                                                 11: 'Mesmo coroando em cavalo com '
                                                     'xeque, o cavalo nasce preso no '
                                                     'canto — e, como sempre acontece '
                                                     'com o cavalo no canto, se perde '
                                                     'imediatamente. (Coroar em dama '
                                                     'seria ainda pior: 12...a1=Q '
                                                     'permite 13.Th1#, mate.)'},
                                       'regra_destaque': 'O empurrão do rei desde a '
                                                         'retaguarda (combinado com '
                                                         'xeques de torre) é eficaz '
                                                         'contra o peão de torre — '
                                                         'justamente porque, ao '
                                                         'contrário dos demais peões, '
                                                         'o cavalo no canto não '
                                                         'oferece defesa real.',
                                       'alternativas': [{'titulo': '12...a1=Q?? '
                                                                   'permite mate '
                                                                   'imediato',
                                                         'linha': ['Rh4+',
                                                                   'Kb3',
                                                                   'Kb5',
                                                                   'a3',
                                                                   'Rh3+',
                                                                   'Kb2',
                                                                   'Kb4',
                                                                   'a2',
                                                                   'Rh2+',
                                                                   'Kb1',
                                                                   'Kb3',
                                                                   'a1=Q',
                                                                   'Rh1'],
                                                         'nota': 'Coroar em dama '
                                                                 'parece mais forte '
                                                                 'que coroar em '
                                                                 'cavalo, mas aqui é '
                                                                 'pior: o rei preto '
                                                                 'fica preso no canto '
                                                                 'e **13.Th1** é '
                                                                 'xeque-mate imediato.',
                                                         'espera_resultado': 'valido'}]},
                                      {'rotulo': 'Afogado no canto: a posição limite',
                                       'fen': '7R/8/8/8/8/8/pk1K4/8 w - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': ['Rb8+',
                                                 'Ka1',
                                                 'Ra8',
                                                 'Kb2',
                                                 'Rb8+',
                                                 'Ka1',
                                                 'Rc8',
                                                 'Kb2'],
                                       'notas': {0: '**1.Tb8+ Ka1!** O rei se esconde '
                                                    'na frente do próprio peão e fica '
                                                    'afogado — por isso o rei branco '
                                                    'não tem tempo de se aproximar, e '
                                                    'a posição é tablas. Com qualquer '
                                                    'outro peão, a1 seria a casa '
                                                    'escolhida para buscar o empate do '
                                                    'mesmo jeito, mas aqui a beirada '
                                                    'do tabuleiro impede qualquer '
                                                    'tentativa de coroar com '
                                                    'conforto.'},
                                       'regra_destaque': 'O peão de torre não é pior '
                                                         'que os demais peões contra o '
                                                         'empurrão lateral, graças à '
                                                         'possibilidade de afogamento '
                                                         '— mesmo quando a pressão por '
                                                         'trás (como no diagrama '
                                                         'anterior) é devastadora.',
                                       'alternativas': [{'titulo': '1...Ka3? — erro: '
                                                                   'abre mão do '
                                                                   'afogamento',
                                                         'linha': ['Rb8+',
                                                                   'Ka3',
                                                                   'Kc2'],
                                                         'nota': 'Com outro peão, a3 '
                                                                 'seria a casa certa '
                                                                 'para buscar o empate '
                                                                 '— mas aqui a beirada '
                                                                 'do tabuleiro impede '
                                                                 'o rei de coroar com '
                                                                 'conforto, e '
                                                                 '**2.Kc2!** já ganha: '
                                                                 'a peça que coroar '
                                                                 'será capturada, '
                                                                 'porque o cavalo no '
                                                                 'canto sempre se '
                                                                 'perde (como no '
                                                                 'diagrama anterior).',
                                                         'espera_resultado': 'erro'}]}],
                         'regras': ['O cavalo no canto do tabuleiro sempre se perde — '
                                    'por isso, com peão de torre, o empurrão do rei '
                                    'forte desde a retaguarda volta a ser eficaz '
                                    '(diferente do que acontece com qualquer outro '
                                    'peão).',
                                    'Mesmo assim, o peão de torre guarda um último '
                                    'recurso que os demais peões não têm: a '
                                    'possibilidade de afogar o próprio rei na beirada '
                                    'do tabuleiro, escondendo-se na frente do peão.']},
                        {'n': 28,
                         'titulo': 'Peão de torre — o empurrão lateral',
                         'conceito': 'O peão de torre não é pior que os demais contra '
                                     'o empurrão lateral do rei forte, graças à '
                                     'possibilidade de afogamento — mas essa defesa é '
                                     'uma posição-limite: tudo depende de quem tem a '
                                     'vez de jogar, e até de uma única casa do rei '
                                     'branco.',
                         'texto': ['Embora o peão de torre não possa aspirar a coroar '
                                   'em cavalo, ele parece compensar um pouco essa '
                                   'deficiência com a possibilidade de afogar o '
                                   'próprio rei. Por isso alguns jogadores confiam '
                                   'mais no peão de torre para buscar o empate contra '
                                   'a torre — mas isso é um erro, como mostra esta '
                                   'posição-chave que vale a pena memorizar.',
                                   'A maioria das posições que não estão claramente '
                                   'decididas a favor de um lado acaba passando por '
                                   'esta, mais cedo ou mais tarde. É uma '
                                   'posição-limite: jogando as pretas, fazem tablas; '
                                   'jogando as brancas, ganham (simplesmente com Tb8). '
                                   'A posição da torre branca (com exceção da casa b8) '
                                   'é indiferente.',
                                   'Como mostram os diagramas gêmeos da série a '
                                   'seguir, a situação muda completamente se '
                                   'deslocarmos as peças uma fila para cima ou para '
                                   'baixo: os mesmos enunciados valeriam também '
                                   'deslocando reis e peão uma coluna para a direita, '
                                   'embora alguns lances defensivos exatos mudassem.'],
                         'posicoes': [{'rotulo': 'Posição-limite do empurrão lateral',
                                       'fen': '7R/8/8/8/8/pk1K4/8/8 b - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': ['Kb2',
                                                 'Rb8+',
                                                 'Kc1',
                                                 'Kc3',
                                                 'a2',
                                                 'Ra8',
                                                 'Kb1',
                                                 'Rb8+',
                                                 'Kc1'],
                                       'notas': {0: '**1...Kb2!** evita o empurrão do '
                                                    'rei rival. Avançar o peão direto '
                                                    '(1...a2?) perde: 2.Tb8+ Ka3 '
                                                    '3.Kc2! — o cavalo no canto sempre '
                                                    'se perde, como já vimos no Final '
                                                    '27.',
                                                 2: '**2...Kc1!** Seria tolice '
                                                    'obstruir o próprio peão agora — '
                                                    'não há tempo de buscar o '
                                                    'afogamento ainda.',
                                                 8: 'As pretas repetem a mesma ideia e '
                                                    'seguram o empate — mas atenção: '
                                                    'tentar o afogamento com 5...Ka1?? '
                                                    'aqui seria um erro fatal (ver '
                                                    'lance alternativo), porque o rei '
                                                    'branco está em d3, não em d2.'},
                                       'regra_destaque': 'O peão de torre contra o '
                                                         'empurrão lateral só empata '
                                                         'se o defensor souber '
                                                         'exatamente quando NÃO se '
                                                         'esconder na frente do peão — '
                                                         'confiar cegamente no '
                                                         'afogamento pode custar a '
                                                         'partida.',
                                       'alternativas': [{'titulo': '1...a2? — erro: o '
                                                                   'cavalo no canto '
                                                                   'volta a se perder',
                                                         'linha': ['a2',
                                                                   'Rb8+',
                                                                   'Ka3',
                                                                   'Kc2',
                                                                   'a1=N+',
                                                                   'Kc3'],
                                                         'nota': 'Avançar o peão de '
                                                                 'imediato entrega a '
                                                                 'partida: depois de '
                                                                 '2.Tb8+ Ka3, '
                                                                 '**3.Kc2!** já ganha, '
                                                                 'porque — como no '
                                                                 'Final 27 — qualquer '
                                                                 'peça que coroe no '
                                                                 'canto será capturada '
                                                                 'em seguida.',
                                                         'espera_resultado': 'erro'},
                                                        {'titulo': '5...Ka1?? — erro: '
                                                                   'aqui o afogamento '
                                                                   'NÃO salva',
                                                         'linha': ['Kb2',
                                                                   'Rb8+',
                                                                   'Kc1',
                                                                   'Kc3',
                                                                   'a2',
                                                                   'Ra8',
                                                                   'Kb1',
                                                                   'Rb8+',
                                                                   'Ka1',
                                                                   'Rf8'],
                                                         'nota': 'Cuidado para não '
                                                                 'confiar demais no '
                                                                 'afogamento: essa '
                                                                 'ideia funcionava com '
                                                                 'o rei branco em d2 '
                                                                 '(ver Diagrama 5.13, '
                                                                 'Final 27), mas aqui, '
                                                                 'com o rei branco em '
                                                                 'd3, **6.Tf8** já é '
                                                                 'xeque-mate.',
                                                         'espera_resultado': 'erro'}]},
                                      {'rotulo': 'Série do empurrão lateral — tablas '
                                                 'com afogamento',
                                       'fen': '7R/8/8/8/8/8/pk1K4/8 w - - 0 1',
                                       'resultado': 'Empate',
                                       'linha': [],
                                       'notas': {0: 'Uma fila mais atrás do diagrama '
                                                    'principal deste final (rei branco '
                                                    'em d2 em vez de d3): tablas jogue '
                                                    'quem jogar, graças ao afogamento '
                                                    '— é exatamente a mesma posição do '
                                                    'Diagrama 5.13 (Final 27).'}},
                                      {'rotulo': 'Série do empurrão lateral — '
                                                 'posição-limite',
                                       'fen': '7R/8/8/8/8/pk1K4/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': [],
                                       'notas': {0: 'A posição principal deste final: '
                                                    'jogando as brancas, ganham '
                                                    'simplesmente com Tb8; jogando as '
                                                    'pretas, empatam (ver análise '
                                                    'completa acima).'}},
                                      {'rotulo': 'Série do empurrão lateral — ganham '
                                                 'sempre',
                                       'fen': '7R/8/8/8/pk1K4/8/8/8 w - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': [],
                                       'notas': {0: 'Mais uma fila à frente, o '
                                                    'resultado já não depende de quem '
                                                    'tem a vez: as brancas ganham '
                                                    'jogando qualquer um dos dois '
                                                    'lados (confirmado pelo Stockfish: '
                                                    'nitidamente a favor das brancas '
                                                    'tanto com elas quanto com as '
                                                    'pretas a mover) — o rei fraco já '
                                                    'não tem mais tempo de buscar o '
                                                    'afogamento.'}}],
                         'regras': ['O peão de torre contra o empurrão lateral guarda '
                                    'a possibilidade de afogamento, mas essa defesa é '
                                    'delicada: funciona só em certas posições exatas '
                                    'do rei branco, e confiar nela sem calcular pode '
                                    'custar a partida.',
                                    'Avançar o peão de torre cedo demais, sem apoio do '
                                    'próprio rei, costuma perder: o cavalo (ou a dama) '
                                    'que nasce no canto se perde do mesmo jeito que no '
                                    'empurrão por trás.']},
                        {'n': 29,
                         'titulo': 'O peão ganha da torre',
                         'conceito': 'Até aqui vimos sempre a torre tentando ganhar do '
                                     'peão — mas há posições em que a torre tem '
                                     'problemas reais para detê-lo, e pode até perder. '
                                     'Dada a posição dos reis e do peão, só há duas '
                                     'casas no tabuleiro onde a torre perde: aqui '
                                     'estão elas.',
                         'texto': ['Até agora estudamos sempre exemplos em que a torre '
                                   'tentava ganhar do peão. Mas existe uma situação em '
                                   'que a torre tem dificuldades reais para deter o '
                                   'peão — e pode até perder a partida. O exemplo mais '
                                   'conhecido é a posição chamada de Barbier e '
                                   'Saavedra, que envolve temas de afogamento e uma '
                                   'sub-promoção; mas o fenômeno também pode acontecer '
                                   'de forma mais simples e direta, como mostra este '
                                   'diagrama.',
                                   'Dada a posição dos reis e do peão, e jogando o '
                                   'lado da torre, só existem duas casas no tabuleiro '
                                   'em que a torre perde: são as duas marcadas no '
                                   'diagrama, f5 e b5. A manobra é longa, mas bastante '
                                   'clara. Para começar, a torre precisa dar xeque '
                                   'para evitar a coroação imediata.'],
                         'posicoes': [{'rotulo': 'As duas casas onde a torre perde: f5 '
                                                 'e b5',
                                       'fen': '8/2P2k2/3K4/5r2/8/8/8/8 b - - 0 1',
                                       'resultado': 'Brancas ganham',
                                       'linha': ['Rf6+',
                                                 'Kd5',
                                                 'Rf5+',
                                                 'Kd4',
                                                 'Rf4+',
                                                 'Kd3',
                                                 'Rf3+',
                                                 'Kc2',
                                                 'Rf2+',
                                                 'Kb3',
                                                 'Rf3+',
                                                 'Kb4',
                                                 'Rf4+',
                                                 'Kb5',
                                                 'Rf5+',
                                                 'Kb6',
                                                 'Rf6+',
                                                 'Kb7'],
                                       'notas': {0: '**1...Tf6+** é obrigatório: sem o '
                                                    'xeque, o peão simplesmente coroa. '
                                                    '**2.Rd5!** é a primeira sutileza '
                                                    '— é preciso evitar 2.Rd7? Tf1!=, '
                                                    'quando o rei já não consegue mais '
                                                    'escapar dos xeques.',
                                                 2: '**2...Tf5+ 3.Rd4!** De novo é '
                                                    'preciso cuidado: 3.Rc4? Tf1! '
                                                    'também empataria. Pode parecer '
                                                    'que o rei branco não vai '
                                                    'conseguir escapar dos xeques '
                                                    'eternos, mas existe uma casa '
                                                    'segura para se esconder — e o '
                                                    'segredo está em atravessar a '
                                                    'coluna c.',
                                                 9: '**6.Rb3!** É a maneira certa: '
                                                    'agora o rei branco consegue se '
                                                    'esconder em b7 sem mais '
                                                    'problemas, fora do alcance dos '
                                                    'xeques pela coluna f.',
                                                 17: 'O rei branco chegou com '
                                                     'segurança a b7. A partir daqui o '
                                                     'peão coroa sem mais obstáculos, '
                                                     'e a dama nova decide a partida '
                                                     'com folga.'},
                                       'regra_destaque': 'Contra um rei e peão bem '
                                                         'coordenados, a torre sozinha '
                                                         'pode não bastar: o rei forte '
                                                         'precisa apenas encontrar uma '
                                                         'rota segura — atravessando '
                                                         'para o lado oposto dos '
                                                         'xeques — para escoltar o '
                                                         'próprio peão até a '
                                                         'coroação.'}],
                         'regras': ['Nem sempre a torre ganha do peão passado: em '
                                    'certas posições (aqui, com a torre exatamente em '
                                    'f5 ou b5), o rei do peão consegue se esconder dos '
                                    'xeques e escoltar a coroação.',
                                    'A manobra de fuga do rei costuma exigir '
                                    'atravessar para o lado oposto de onde a torre '
                                    'está dando os xeques — procurando sempre a '
                                    'primeira casa segura disponível.'],
                         'exemplo_pratico': {'titulo': 'Svidler x Topalov, '
                                                       'Morelia-Linares 2006',
                                             'texto': ['O livro cita, sem reproduzir, '
                                                       "'uma reciente partida "
                                                       "Svidler-Topalov de Morelia' "
                                                       'como exemplo de aplicação '
                                                       'prática destas ideias em uma '
                                                       'posição mais complexa. A '
                                                       'partida é real — Svidler x '
                                                       'Topalov, Morelia-Linares 2006, '
                                                       '1ª rodada — e a notação '
                                                       'completa está disponível, '
                                                       'então vale a pena acompanhá-la '
                                                       'a partir do lance 51, quando a '
                                                       'disputa de torre contra peão '
                                                       'passado (o tema deste '
                                                       'capítulo) realmente começa.'],
                                             'posicoes': [{'rotulo': 'Depois de '
                                                                     '50...Txh5+, o '
                                                                     'final de torre '
                                                                     'contra peão '
                                                                     'começa de '
                                                                     'verdade',
                                                           'fen': '8/8/2k2Pp1/p1p1R1Kr/p1p5/2P5/1P6/8 '
                                                                  'w - - 2 51',
                                                           'resultado': 'Brancas '
                                                                        'ganham',
                                                           'linha': ['Kxg6',
                                                                     'Rxe5',
                                                                     'f7',
                                                                     'Re6+',
                                                                     'Kg5',
                                                                     'Re5+',
                                                                     'Kg4',
                                                                     'Re4+',
                                                                     'Kg3',
                                                                     'Re3+',
                                                                     'Kf2',
                                                                     'a3',
                                                                     'f8=Q',
                                                                     'axb2',
                                                                     'Qc8+',
                                                                     'Kb5',
                                                                     'Qb7+',
                                                                     'Ka4',
                                                                     'Kxe3',
                                                                     'Ka3',
                                                                     'Qb5',
                                                                     'a4',
                                                                     'Qxc5+',
                                                                     'Kb3',
                                                                     'Qb4+',
                                                                     'Kc2',
                                                                     'Qxa4+',
                                                                     'Kxc3',
                                                                     'Qa5+',
                                                                     'Kc2',
                                                                     'Qf5+',
                                                                     'Kc1',
                                                                     'Qf1+'],
                                                           'notas': {0: 'Partida real '
                                                                        'entre dois '
                                                                        'dos melhores '
                                                                        'jogadores do '
                                                                        'mundo da '
                                                                        'época. Depois '
                                                                        'da captura '
                                                                        '**51...Txe5**, '
                                                                        'sobra '
                                                                        'exatamente o '
                                                                        'tipo de final '
                                                                        'deste '
                                                                        'capítulo: rei '
                                                                        'e peão '
                                                                        'passado '
                                                                        'contra rei e '
                                                                        'torre (com '
                                                                        'alguns peões '
                                                                        'laterais '
                                                                        'ainda no '
                                                                        'tabuleiro, '
                                                                        'que não mudam '
                                                                        'a ideia '
                                                                        'central).',
                                                                     2: 'O peão branco '
                                                                        'já chega a '
                                                                        '**f7**, e as '
                                                                        'pretas tentam '
                                                                        'o único '
                                                                        'recurso '
                                                                        'disponível: '
                                                                        'uma série de '
                                                                        'xeques de '
                                                                        'torre para '
                                                                        'atrasar a '
                                                                        'coroação.',
                                                                     11: 'Como no '
                                                                         'Final 29, a '
                                                                         'torre não '
                                                                         'consegue '
                                                                         'impedir a '
                                                                         'coroação '
                                                                         'sozinha: o '
                                                                         'rei branco '
                                                                         'encontra uma '
                                                                         'casa segura '
                                                                         '(**f2**) e '
                                                                         'escapa dos '
                                                                         'xeques.',
                                                                     12: 'O peão '
                                                                         'coroa. A '
                                                                         'partir '
                                                                         'daqui, dama '
                                                                         'e rei ganham '
                                                                         'com folga '
                                                                         'contra a '
                                                                         'torre e os '
                                                                         'peões '
                                                                         'remanescentes '
                                                                         'das pretas — '
                                                                         'é só questão '
                                                                         'de '
                                                                         'técnica.'}}],
                                             'fecho': 'A partir da coroação, dama e '
                                                      'rei ganham com folga contra a '
                                                      'torre e os peões remanescentes '
                                                      'das pretas — é só questão de '
                                                      'técnica, exatamente como nos '
                                                      'finais teóricos deste '
                                                      'capítulo.'}}]}]}
CAPITULOS = [CAPITULO_1, CAPITULO_2, CAPITULO_3]
