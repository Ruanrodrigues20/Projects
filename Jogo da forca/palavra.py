# função responsavel por escolher uma palavra a respeito
# nivel de dificuldade escolhido

from random import choice

def palavra(escolha):
    frutas = [
    'maca', 'banana', 'abacaxi', 'morango', 'uva', 'laranja', 'limao', 'mamao', 
    'manga', 'melancia', 'melao', 'pera', 'pessego', 'ameixa', 'kiwi', 'figo', 
    'coco', 'carambola', 'pitaya', 'tangerina', 'maracuja', 'acerola', 'goiaba', 
    'cereja', 'roma', 'acai', 'graviola', 'jabuticaba', 'caju', 'jambo', 'damasco',
    'framboesa', 'mirtilo', 'nectarina', 'physalis', 'uvaia', 'abiu', 'atemoia', 
    'bacaba', 'biriba', 'caja', 'caqui', 'cupuacu', 'jaca', 'jatoba', 'longan', 
    'mangaba', 'marolo', 'murici', 'pequi', 'pitaia', 'sapoti', 'seriguela', 
    'taruma', 'tomate', 'umbu', 'acerola', 'abacate', 'abiu', 'açai', 'acerola', 
    'amora', 'anona', 'banana', 'biriba', 'caju', 'caqui', 'carambola', 'caja', 
    'cereja', 'coco', 'cupuacu', 'damasco', 'framboesa', 'figo', 'goiaba', 'graviola', 
    'jaca', 'jambo', 'kiwi', 'laranja', 'limao', 'mamao', 'manga', 'melancia', 'melao', 
    'morango', 'mirtilo', 'nectarina', 'pitaya', 'pessego', 'pera', 'roma', 'seriguela', 
    'tamarindo', 'tangerina', 'umbu', 'uva'
    ]

    profissoes = [
    'medico', 'engenheiro', 'advogado', 'arquiteto', 'professor', 'cientista', 'programador', 'designer',
    'enfermeiro', 'dentista', 'veterinario', 'psicologo', 'contador', 'fisioterapeuta', 'eletricista', 'mecanico',
    'jornalista', 'farmaceutico', 'policial', 'bombeiro', 'piloto', 'chef', 'atleta', 'ator',
    'cantor', 'dancarino', 'pintor', 'escultor', 'cineasta', 'produtor', 'vendedor', 'gerente',
    'diretor', 'executivo', 'pedreiro', 'carpinteiro', 'encanador', 'marceneiro', 'serralheiro', 'padeiro',
    'confeiteiro', 'copeiro', 'bartender', 'garcom', 'consultor', 'analista', 'tecnologo', 'recepcionista',
    'secretario', 'officeboy', 'entregador', 'acupunturista', 'agricultor', 'artesao', 'astronomo', 'engenheiro-de-software',
    'barista', 'biologo', 'bibliotecario', 'bilheteiro', 'bioquimico', 'carteiro', 'chauffeur', 'corretor',
    'datilografista', 'decorador', 'diarista', 'diplomata', 'empresario', 'escritor', 'espião', 'esteticista',
    'ferreiro', 'florista', 'funileiro', 'geologo', 'guarda', 'historiador', 'jardineiro', 'jogador',
    'juiz', 'marinheiro', 'matematico', 'metalurgico', 'meteorologista', 'motorista', 'notario', 'nutricionista',
    'oftalmologista', 'operador', 'orientador', 'paisagista', 'pastor', 'patologista', 'pedagogo', 'perito',
    'personal', 'plastico', 'podologo', 'quimico', 'radiologista', 'recepcionista', 'relojoeiro', 'repórter',
    'sociologo', 'soldador', 'tatuador', 'terapeuta', 'tesoureiro', 'topografo', 'treinador', 'urbanista',
    'urologista', 'webdesigner', 'zelador'
    ]

    animais = [
    'gato', 'cachorro', 'leao', 'elefante', 'tigre', 'urso', 'leopardo', 'girafa', 'camelo', 'hipopotamo',
    'rinoceronte', 'zebra', 'macaco', 'gorila', 'orangotango', 'chimpanze', 'koala', 'canguru', 'coalas',
    'golfinho', 'baleia', 'orca', 'tubarao', 'tartaruga', 'cobra', 'jacare', 'crocodilo', 'lagarto', 'lagartixa',
    'iguana', 'sapo', 'ra', 'salamandra', 'lagosta', 'camarao', 'caranguejo', 'lagosta', 'polvo', 'lula',
    'ourico', 'esquilo', 'raposa', 'guaxinim', 'panda', 'peixe', 'papagaio', 'ave', 'passaro', 'pombo',
    'corvo', 'gaivota', 'avestruz', 'pavao', 'flamingo', 'pato', 'cisne', 'cisne', 'cavalo', 'vaca',
    'ovelha', 'cabra', 'porco', 'javalis', 'coelho', 'camundongo', 'esquilo', 'morcego', 'raposa', 'furao',
    'canguru', 'ornitorrinco', 'ganso', 'patos', 'pato', 'pombo', 'coruja', 'ganso', 'siri', 'camelo',
    'avestruz', 'foca', 'morsa', 'pinguim', 'lontra', 'foca', 'leao-marinho', 'orca', 'tubarao', 'baleia',
    'peixe-boi', 'tubarao', 'caracol', 'tarantula', 'lagarta', 'libelula', 'borboleta', 'aranha', 'abelha',
    'formiga', 'besouro', 'mosquito', 'grilo', 'mosca', 'besouro', 'aranha', 'escorpiao', 'mosquito'
    ]

    paises = [
    'afeganistao', 'albania', 'argelia', 'andorra', 'angola', 'antigua-e-barbuda', 'argentina', 'armenia', 'australia', 'austria',
    'azerbaijao', 'bahamas', 'bahrein', 'bangladesh', 'barbados', 'belarus', 'belgica', 'belize', 'benin', 'butao',
    'bolivia', 'bosnia-e-herzegovina', 'botsuana', 'brasil', 'brunei', 'bulgaria', 'burkina-faso', 'burundi', 'cabo-verde', 'camboja',
    'camaroes', 'canada', 'republica-centro-africana', 'chade', 'chile', 'china', 'colombia', 'comores', 'republica-democratica-do-congo', 'republica-do-congo',
    'costa-rica', 'costa-do-marfim', 'croacia', 'cuba', 'chipre', 'republica-checa', 'dinamarca', 'djibouti', 'dominica', 'republica-dominicana',
    'timor-leste', 'equador', 'egito', 'el-salvador', 'guine-equatorial', 'eritreia', 'estonia', 'etiopia', 'fiji', 'finlandia',
    'franca', 'gabao', 'gambia', 'georgia', 'alemanha', 'ghana', 'grecia', 'granada', 'guatemala', 'guine',
    'guine-bissau', 'guiana', 'haiti', 'honduras', 'hungria', 'islandia', 'india', 'indonesia', 'ira', 'irao',
    'iraque', 'irlanda', 'israel', 'italia', 'jamaica', 'japao', 'jordania', 'casaquistao', 'quenia', 'kiribati',
    'kosovo', 'kuwait', 'quirguistao', 'laos', 'letonia', 'libano', 'lesoto', 'liberia', 'libia', 'liechtenstein',
    'lituania', 'luxemburgo', 'macedonia', 'madagascar', 'malawi', 'malasia', 'maldivas', 'mali', 'malta', 'ilhas-marshall',
    'mauritania', 'mauricia', 'mexico', 'micronesia', 'moldavia', 'monaco', 'mongolia', 'montenegro', 'marrocos', 'mocambique',
    'mianmar', 'namibia', 'nauru', 'nepal', 'holanda', 'nova-zelandia', 'nicaragua', 'niger', 'nigeria', 'coreia-do-norte',
    'noruega', 'oman', 'paquistao', 'palau', 'palestina', 'panama', 'papua-nova-guin', 'paraguai', 'peru', 'filipinas',
    'polonia', 'portugal', 'qatar', 'romenia', 'russia', 'ruanda', 'sao-cristovao-e-nevis', 'santa-lucia', 'sao-vicente-e-granadinas', 'samoa',
    'san-marino', 'sao-tome-e-principe', 'arabia-saudita', 'senegal', 'servia', 'seicheles', 'serra-leoa', 'singapura', 'eslovaquia', 'eslovenia',
    'ilhas-salomao', 'somalia', 'africa-do-sul', 'coreia-do-sul', 'sudao-do-sul', 'espanha', 'sri-lanka', 'sudao', 'suriname', 'suazilandia',
    'suecia', 'suica', 'siria', 'tajiquistao', 'tanzania', 'tailandia', 'togo', 'tonga', 'trindade-e-tobago', 'tunisia',
    'turquia', 'turquemenistao', 'tuvalu', 'uganda', 'ucrania', 'emirados-arabes-unidos', 'reino-unido', 'estados-unidos', 'uruguai', 'uzbequistao',
    'vanuatu', 'cidade-do-vaticano', 'venezuela', 'vietna', 'iemen', 'zambia', 'zimbabue'
    ]

    cores = [
    'vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta', 'branco', 'preto', 'cinza',
    'marrom', 'rosa', 'roxo', 'ciano', 'magenta', 'lima', 'teal', 'prata', 'ouro', 'bronze',
    'marfim', 'navy', 'turquesa', 'vinho', 'oliva', 'salmão', 'lavanda', 'pêssego', 'ameixa', 'bege',
    'azul-celeste', 'verde-floresta', 'vermelho-rubi', 'azul-safira', 'verde-esmeralda', 'amarelo-topázio', 'roxo-ametista', 'verde-jade', 'branco-pérola', 'preto-carvão'
    ]

    objetos = [
    'cadeira', 'mesa', 'sofa', 'estante', 'televisao', 'geladeira', 'fogao', 'microondas', 'liquidificador', 'aspirador-de-po',
    'computador', 'celular', 'tablet', 'teclado', 'mouse', 'fones-de-ouvido', 'carro', 'moto', 'bicicleta', 'aviao',
    'navio', 'barco', 'helicoptero', 'carrinho-de-bebe', 'berco', 'luminaria', 'abajur', 'espelho', 'quadro', 'camera',
    'relogio', 'culos-de-sol', 'mochila', 'bolsa', 'carteira', 'chave', 'livro', 'revista', 'jornal', 'caneta',
    'lapis', 'caderno', 'agenda', 'folha-de-papel', 'pincel', 'tinta', 'escova-de-dente', 'pasta-de-dente', 'sabonete',
    'toalha', 'pente', 'shampoo', 'condicionador', 'gel-de-cabelo', 'secador-de-cabelo', 'forno', 'panela', 'prato',
    'copo', 'talher', 'garrafa', 'abridor-de-latas', 'sacola', 'caixa', 'chave-de-fenda', 'martelo', 'prego',
    'parafuso', 'serrote', 'lixadeira', 'escada', 'cadeado', 'chaveiro', 'borracha', 'tesoura', 'agulha', 'linha',
    'botao', 'fita', 'tesoura', 'vela', 'fita-adesiva', 'canivete', 'isqueiro', 'fita-metrica', 'balde', 'esponja',
    'vassoura', 'rodo', 'papel-higienico', 'escova-de-lavar', 'detergente', 'desinfetante', 'vaso-sanitario', 'pia', 'torneira',
    'abajur', 'mangueira', 'escorredor', 'cinzeiro', 'escada', 'ventilador', 'grampeador', 'binoculo', 'bussola', 'escorredor-de-pratos',
    'lava-loucas', 'apontador', 'estojo', 'lupa', 'tear', 'maquina-de-escrever', 'maquina-de-lavar', 'maquina-de-coser', 'projetor', 'trena',
    'radiador', 'cabide', 'varal', 'piscina', 'churrasqueira', 'guarda-chuva', 'cortina', 'porta', 'janela', 'quadro-branco',
    'telefone', 'celular', 'camera', 'caixa-de-correio', 'lixeira', 'cama', 'almofada', 'cobertor', 'travesseiro', 'comoda',
    'mesinha-de-cabeceira', 'criado-mudo', 'armario', 'guarda-roupa', 'cabideiro', 'sapateira', 'escrivaninha', 'cadeira', 'poltrona', 'sofa',
    'tapete', 'espelho', 'porta-retratos', 'lustre', 'abajur', 'luminaria', 'abajur', 'porta-lapis', 'porta-trecos', 'estante',
    'prateleira', 'cortina', 'tapete', 'porta-retratos', 'vaso-de-flores', 'jardineira', 'quadro-de-avisos', 'relogio-de-parede', 'comoda', 'espelho'
    ]

    if escolha == 'frutas':
        return choice(frutas)
    elif escolha == 'profissoes':
        return choice(profissoes)
    elif escolha == 'animais':
        return choice(animais)
    elif escolha == 'cores':
        return choice(cores)
    elif escolha == 'objetos':
        return choice(objetos)
    elif escolha == 'paises':
        return choice(paises)



