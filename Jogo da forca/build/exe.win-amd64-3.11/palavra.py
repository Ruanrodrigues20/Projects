# função responsavel por escolher uma palavra a respeito
# nivel de dificuldade escolhido

from random import choice

def palavra(nivel):
    dificil = [
        "quinquagésimo", "hipercolesterolêmico", "pneumoultramicroscopicossilicovulcanoconiótico",
        "anticonstitucionalissimamente", "desoxirribonucleico", "supercalifragilisticexpialidocious",
        "eletroencefalografista", "desencabrestamento", "inconstitucionalissimamente",
        "inconstitucionalíssimo", "eletroencefalograma", "oftalmotorrinolaringologista",
        "paralelepípedo", "eletrocardiograma", "eletrodoméstico", "otorrinolaringologista",
        "psiconeuroendocrinologia", "polissilábico", "eletroencefalograma", "biomatemática",
        "anticonstitucionalismo", "eletroencefalografia", "psicofarmacoterapia", "neuroanatomia",
        "anticonstitucionalidade", "eletrocardiografia", "pneumoultramicroscopicossilicovulcanoconiose",
        "anticonstitucional", "neurocirurgião", "parassimpaticomimético", "biotecnologia",
        "paleontologia", "neurologista", "pneumoultramicroscopicossilicovulcanoconiótico",
        "endocrinologista", "imunofarmacologia", "pneumoultramicroscopicossilicovulcanoc",
        "biblioteconomista", "pneumoultramicroscopicossilicovulcanoconiose", "paleontológico",
        "imunodeficiência", "neurofisiologia", "eletromagnético", "endocrinologia",
        "neuroendocrinologia", "desoxirribonucleotídeo", "pneumoultramicroscópico",
        "eletroencefalografista", "supraespinhoso", "oftalmologistas", "oftalmológicos",
        "imunofarmacologia", "cardiopulmonares", "interdisciplinaridade", "interministerial",
        "cardiovascular", "eletrocardiograma", "antimicrobiano", "antisséptico",
        "parassimpático", "parassimpaticomimético", "bacteriologia", "endocrinologia",
        "psicofarmacologia", "parassimpaticolítico", "neurofisiologia", "suprarrenal",
        "biomolecular", "eletromagnético", "psicoterapia", "otorrinolaringologista",
        "antidepressivo", "neurotransmissores", "antipsicótico", "anticonvulsivante",
        "antipsicóticos", "neurotransmissão", "biomolecular", "hipercolesterolêmico",
        "antidepressivos", "anticoagulante", "hormonioterapia", "neurocirurgião",
        "interdisciplinar", "desencabrestamento", "neurofisiológico", "eletroencefalograma",
        "parassimpaticolítico", "desencabrestar", "psicoterapêutico", "neuroanatomia",
        "desoxirribonucleotídeo", "biotecnológico", "neurotransmissor", "eletrocardiograma",
        "desoxirribonucleotídeos", "parassimpaticomiméticos", "neurotransmissores",
        "desoxirribonucleotídeos", "hipercolesterolemia", "hipercolesterolemia",
        "pneumoultramicroscopicossilicovulcanoconiótico", "neurocirurgiãos",
        "parassimpaticomiméticos", "interdisciplinaridades", "neuroanatomias",
        "parassimpaticolíticos", "hiperparatiroidismo", "pneumoultramicroscópicos",
        "neurotransmissões", "neurotransmissoras", "desencabrestamentos", "hipercolesterolêmicos",
        "supraespinhosos", "neurofisiológicas", "supraescapulares", "interministeriais",
        "interdepartamentais", "eletroencefalografistas"
    ]

    medio = [
        'abacaxi', 'banheiro', 'cachorro', 'dinheiro', 'elefante', 'foguete', 
        'geleira', 'helicóptero', 'iguana', 'jacaré', 'lagoa', 'montanha', 
        'navio', 'oceano', 'palmeira', 'queijo', 'relógio', 'sapato', 
        'tigre', 'umbigo', 'ventilador', 'xadrez', 'zebra', 'amarelo', 
        'biblioteca', 'caravana', 'desenho', 'espanhol', 'flauta', 
        'gorila', 'harmonia', 'inseto', 'jardim', 'limonada', 'música', 
        'neve', 'orelha', 'pirulito', 'quebra-cabeça', 'rinoceronte', 
        'sorvete', 'tartaruga', 'universo', 'violino', 'xícara', 'zoológico',
        'aniversário', 'baleia', 'computador', 'dente', 'espelho', 
        'fogão', 'guitarra', 'hipopótamo', 'internet', 'janela', 
        'kiwi', 'lápis', 'macaco', 'navalha', 'ovo', 'piano', 
        'quadrado', 'rato', 'semente', 'telefone', 'urso', 
        'vaso', 'waffle', 'xerox', 'yoga', 'zangão',
        'abelha', 'bicicleta', 'cadeira', 'dado', 'escola', 
        'faca', 'gato', 'hamburguer', 'igreja', 'jogo', 
        'ketchup', 'lanche', 'morango', 'nuvem', 'óculos', 
        'pão', 'queijo', 'rato', 'sapato', 'tênis', 
        'uva', 'vela', 'windsurf', 'xícara', 'yak',
        'zíper'
    ]

    facil = [
        'cão', 'gato', 'sol', 'lua', 'flor', 'pato', 'rosa', 'mãe', 'pão', 'mar',
        'água', 'peixe', 'vento', 'luz', 'fruta', 'branco', 'bola', 'lápis', 'mala', 'rato',
        'café', 'mesa', 'copo', 'cama', 'fogo', 'piso', 'porta', 'livro', 'amigo', 'bola',
        'azul', 'verde', 'casa', 'pé', 'faca', 'céu', 'mão', 'nariz', 'olho', 'boca',
        'lábio', 'pé', 'pente', 'copo', 'cama', 'relógio', 'avião', 'terra', 'tijolo', 'ferro',
        'saco', 'bolo', 'lápis', 'caixa', 'macaco', 'rato', 'pato', 'cachorro', 'gato', 'rosa',
        'árvore', 'céu', 'nuvem', 'montanha', 'rato', 'água', 'comida', 'trabalho', 'escola', 'férias',
        'rio', 'cidade', 'mar', 'lago', 'praia', 'fazenda', 'amigo', 'jogo', 'música', 'filme',
        'cinema', 'teatro', 'cama', 'quarto', 'sala', 'banheiro', 'cozinha', 'rua', 'carro', 'ônibus',
        'avião', 'barco', 'trem', 'bicicleta', 'pé', 'corrida', 'andar', 'nadar', 'cantar', 'dormir',
        'comer', 'beber', 'correr', 'pular', 'sentar', 'estar', 'ficar', 'ir', 'vir', 'chegar'
    ]

    if nivel == 'f':
      return choice(facil)

    elif nivel == 'm':
        return choice(medio)
    
    elif nivel == 'd':
        return choice(dificil)
