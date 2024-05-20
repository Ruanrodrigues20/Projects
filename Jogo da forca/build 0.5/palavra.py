# função responsavel por escolher uma palavra a respeito
# nivel de dificuldade escolhido

from random import choice

def palavra(assunto, nivel):
    frutas = {'facil': ['maca', 'banana', 'abacaxi', 'morango', 'uva', 'laranja', 'limao', 'mamao', 'manga', 'melao', 
               'pera', 'pessego', 'ameixa', 'kiwi', 'figo', 'coco', 'pitaya', 'acerola', 'goiaba', 'cereja', 
               'roma', 'acai', 'caju', 'jambo', 'damasco', 'mirtilo', 'uvaia', 'abiu', 'atemoia', 'bacaba', 
               'biriba', 'caja', 'caqui', 'cupuacu', 'jaca', 'jatoba', 'longan', 'mangaba', 'marolo', 'murici', 
               'pequi', 'pitaia', 'sapoti', 'taruma', 'tomate', 'umbu', 'acerola', 'abacate', 'abiu', 'açai', 
               'acerola', 'amora', 'anona', 'banana', 'biriba', 'caju', 'caqui', 'caja', 'cereja', 'coco', 'cupuacu', 
               'damasco', 'figo', 'goiaba', 'jaca', 'jambo', 'kiwi', 'laranja', 'limao', 'mamao', 'manga', 'melao', 
               'morango', 'mirtilo', 'pitaya', 'pessego', 'pera', 'roma', 'umbu', 'uva'], 
     'medio': ['melancia', 'carambola', 'tangerina', 'maracuja', 'graviola', 'jabuticaba', 'framboesa', 'nectarina', 
               'physalis', 'seriguela', 'carambola', 'framboesa', 'graviola', 'melancia', 'nectarina', 'seriguela', 
               'tamarindo', 'tangerina'], 
     'dificil': ['tamarindo-do-amazonas', 'seriguela-de-pomba', 'sapoti-de-vinheiro', 'rambutan-vermelho', 'pitaya-branca', 
                 'cereja-do-rio-grande', 'carambola-gigante', 'abacaxi-roxo']
     }

    profissoes = {'facil': ['medico', 'piloto', 'chef', 'atleta', 'ator', 'cantor', 'pintor', 'gerente', 'diretor', 'padeiro', 
                            'copeiro', 'garcom', 'artesao', 'barista', 'biologo', 'espião', 'geologo', 'guarda', 'jogador', 'juiz', 
                            'notario', 'pastor', 'perito', 'quimico', 'zelador'], 
                  'medio': ['engenheiro', 'advogado', 'arquiteto', 'professor', 'cientista', 'programador', 'designer', 'enfermeiro', 
                            'dentista', 'veterinario', 'psicologo', 'contador', 'eletricista', 'mecanico', 'jornalista', 'policial', 
                            'bombeiro', 'dancarino', 'escultor', 'cineasta', 'produtor', 'vendedor', 'executivo', 'pedreiro', 
                            'carpinteiro', 'encanador', 'marceneiro', 'serralheiro', 'confeiteiro', 'bartender', 'consultor', 
                            'analista', 'tecnologo', 'secretario', 'officeboy', 'entregador', 'agricultor', 'astronomo', 'bilheteiro', 
                            'bioquimico', 'carteiro', 'chauffeur', 'corretor', 'decorador', 'diarista', 'diplomata', 'empresario', 
                            'escritor', 'esteticista', 'ferreiro', 'florista', 'funileiro', 'historiador', 'jardineiro', 'marinheiro', 
                            'matematico', 'metalurgico', 'motorista', 'operador', 'orientador', 'paisagista', 'patologista', 'pedagogo', 'personal', 'plastico', 'podologo', 'relojoeiro', 'repórter', 'sociologo', 'soldador', 'tatuador', 
                            'terapeuta', 'tesoureiro', 'topografo', 'treinador', 'urbanista', 'urologista', 'webdesigner'], 
                  'dificil': ['fisioterapeuta', 'farmaceutico', 'recepcionista', 'acupunturista', 'engenheiro-de-software', 'bibliotecario', 
                              'datilografista', 'meteorologista', 'nutricionista', 'oftalmologista', 'radiologista', 'recepcionista']}

    animais = {'facil': ['gato', 'leao', 'tigre', 'urso', 'girafa', 'camelo', 'zebra', 'macaco', 'gorila', 'koala', 'canguru', 
                         'coalas', 'baleia', 'orca', 'tubarao', 'cobra', 'jacare', 'lagarto', 'iguana', 'sapo', 'ra', 'lagosta', 
                         'camarao', 'lagosta', 'polvo', 'lula', 'ourico', 'esquilo', 'raposa', 'panda', 'peixe', 'ave', 'passaro', 
                         'pombo', 'corvo', 'gaivota', 'pavao', 'pato', 'cisne', 'cisne', 'cavalo', 'vaca', 'ovelha', 'cabra', 'porco', 
                         'javalis', 'coelho', 'esquilo', 'morcego', 'raposa', 'furao', 'canguru', 'ganso', 'patos', 'pato', 'pombo', 
                         'coruja', 'ganso', 'siri', 'camelo', 'foca', 'morsa', 'pinguim', 'lontra', 'foca', 'orca', 'tubarao', 'baleia', 
                         'tubarao', 'caracol', 'lagarta', 'aranha', 'abelha', 'formiga', 'besouro', 'grilo', 'mosca', 'besouro', 'aranha'], 
               'medio': ['cachorro', 'elefante', 'leopardo', 'hipopotamo', 'rinoceronte', 'orangotango', 'chimpanze', 'golfinho', 'tartaruga', 
                         'crocodilo', 'lagartixa', 'salamandra', 'caranguejo', 'guaxinim', 'papagaio', 'avestruz', 'flamingo', 'camundongo', 
                         'avestruz', 'peixe-boi', 'tarantula', 'libelula', 'borboleta', 'mosquito', 'escorpiao', 'mosquito'], 
               'dificil': ['ornitorrinco', 'leao-marinho']}

    paises = {'facil': ['albania', 'argelia', 'andorra', 'angola', 'armenia', 'austria', 'bahamas', 'bahrein', 'belarus', 
                        'belgica', 'belize', 'benin', 'butao', 'bolivia', 'brasil', 'brunei', 'burundi', 'camboja', 'canada', 
                        'chade', 'chile', 'china', 'comores', 'croacia', 'cuba', 'chipre', 'equador', 'egito', 'estonia', 'etiopia',
                          'fiji', 'franca', 'gabao', 'gambia', 'georgia', 'ghana', 'grecia', 'granada', 'guine', 'guiana', 'haiti', 
                          'hungria', 'india', 'ira', 'irao', 'iraque', 'irlanda', 'israel', 'italia', 'jamaica', 'japao', 'quenia',
                            'kosovo', 'kuwait', 'laos', 'letonia', 'libano', 'lesoto', 'liberia', 'libia', 'malawi', 'malasia', 'mali',
                              'malta', 'mexico', 'monaco', 'mianmar', 'namibia', 'nauru', 'nepal', 'holanda', 'niger', 
                              'nigeria', 'noruega', 'oman', 'palau', 'panama', 'peru', 'polonia', 'qatar', 'romenia', 
                              'russia', 'ruanda', 'samoa', 'senegal', 'servia', 'somalia', 'espanha', 'sudao', 'suecia', 
                              'suica', 'siria', 'togo', 'tonga', 'tunisia', 'turquia', 'tuvalu', 'uganda', 'ucrania', 
                              'uruguai', 'vanuatu', 'vietna', 'iemen', 'zambia'], 
              'medio': ['afeganistao', 'argentina', 'australia', 'azerbaijao', 'bangladesh', 'barbados', 'botsuana', 'bulgaria',
                         'cabo-verde', 'camaroes', 'colombia', 'costa-rica', 'dinamarca', 'djibouti', 'dominica', 'timor-leste',
                           'el-salvador', 'eritreia', 'finlandia', 'alemanha', 'guatemala', 'honduras', 'islandia', 'indonesia',
                             'jordania', 'casaquistao', 'kiribati', 'quirguistao', 'lituania', 'luxemburgo', 'macedonia', 
                             'madagascar', 'maldivas', 'mauritania', 'mauricia', 'micronesia', 'moldavia', 'mongolia', 
                             'montenegro', 'marrocos', 'mocambique', 'nicaragua', 'paquistao', 'palestina', 'paraguai', 
                             'filipinas', 'portugal', 'santa-lucia', 'san-marino', 'seicheles', 'serra-leoa', 'singapura',
                               'eslovaquia', 'eslovenia', 'sri-lanka', 'suriname', 'suazilandia', 'tajiquistao', 'tanzania',
                                 'tailandia', 'reino-unido', 'uzbequistao', 'venezuela', 'zimbabue'], 
              'dificil': ['antigua-e-barbuda', 'bosnia-e-herzegovina', 'burkina-faso', 'republica-centro-africana', 
                          'republica-democratica-do-congo', 'republica-do-congo', 'costa-do-marfim', 'republica-checa',
                            'republica-dominicana', 'guine-equatorial', 'guine-bissau', 'liechtenstein', 'ilhas-marshall',
                              'nova-zelandia', 'coreia-do-norte', 'papua-nova-guin', 'sao-cristovao-e-nevis',
                                'sao-vicente-e-granadinas', 'sao-tome-e-principe', 'arabia-saudita', 'ilhas-salomao',
                                  'africa-do-sul', 'coreia-do-sul', 'sudao-do-sul', 'trindade-e-tobago', 'turquemenistao',
                                    'emirados-arabes-unidos', 'estados-unidos', 'cidade-do-vaticano']}

    cores = {'facil': ['laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta', 'branco', 
                       'preto', 'cinza', 'marrom', 'rosa', 'roxo', 'ciano', 'magenta', 
                       'lima', 'teal', 'prata', 'ouro', 'bronze', 'marfim', 'navy', 
                       'vinho', 'oliva', 'salmão', 'lavanda', 'pêssego', 'ameixa', 'bege'], 
             'medio': ['vermelho', 'turquesa', 'azul-safira', 'verde-jade'], 
             'dificil': ['azul-celeste', 'verde-floresta', 'vermelho-rubi', 'verde-esmeralda', 
                         'amarelo-topázio', 'roxo-ametista', 'branco-pérola', 'preto-carvão']}
    
    objetos = {'facil': ['cadeira', 'mesa', 'sofa', 'estante', 'fogao', 'celular', 'tablet', 
                         'teclado', 'mouse', 'carro', 'moto', 'aviao', 'navio', 'barco',
                           'berco', 'abajur', 'espelho', 'quadro', 'camera', 'relogio', 
                           'mochila', 'bolsa', 'chave', 'livro', 'revista', 'jornal', 
                           'caneta', 'lapis', 'caderno', 'agenda', 'pincel', 'tinta', 
                           'toalha', 'pente', 'shampoo', 'forno', 'panela', 'prato', 
                           'copo', 'talher', 'garrafa', 'sacola', 'caixa', 'martelo', 
                           'prego', 'serrote', 'escada', 'cadeado', 'tesoura', 'agulha',
                           'linha', 'botao', 'fita', 'tesoura', 'vela', 'balde', 'esponja', 
                           'rodo', 'pia', 'abajur', 'escada', 'bussola', 'estojo', 'lupa',
                             'tear', 'trena', 'cabide', 'varal', 'piscina', 'cortina', 'porta',
                               'janela', 'celular', 'camera', 'lixeira', 'cama', 'comoda', 'armario',
                                 'cadeira', 'sofa', 'tapete', 'espelho', 'lustre', 'abajur', 'abajur',
                                   'estante', 'cortina', 'tapete', 'comoda', 'espelho'], 
               'medio': ['televisao', 'geladeira', 'microondas', 'computador', 'bicicleta', 'helicoptero', 
                         'luminaria', 'carteira', 'sabonete', 'parafuso', 'lixadeira', 'chaveiro',
                           'borracha', 'canivete', 'isqueiro', 'vassoura', 'detergente', 'torneira', 
                           'mangueira', 'escorredor', 'cinzeiro', 'ventilador', 'grampeador', 'binoculo', 
                           'lava-loucas', 'apontador', 'projetor', 'radiador', 'telefone', 'almofada', 
                           'cobertor', 'travesseiro', 'criado-mudo', 'cabideiro', 'sapateira', 'poltrona',
                             'luminaria', 'porta-lapis', 'prateleira', 'jardineira'], 
               'dificil': ['liquidificador', 'aspirador-de-po', 'fones-de-ouvido', 'carrinho-de-bebe', 
                           'culos-de-sol', 'folha-de-papel', 'escova-de-dente', 'pasta-de-dente',
                             'condicionador', 'gel-de-cabelo', 'secador-de-cabelo', 'abridor-de-latas',
                               'chave-de-fenda', 'fita-adesiva', 'fita-metrica', 'papel-higienico', 
                               'escova-de-lavar', 'desinfetante', 'vaso-sanitario', 'escorredor-de-pratos', 
                               'maquina-de-escrever', 'maquina-de-lavar', 'maquina-de-coser', 'churrasqueira',
                                 'guarda-chuva', 'quadro-branco', 'caixa-de-correio', 'mesinha-de-cabeceira', 
                                 'guarda-roupa', 'escrivaninha', 'porta-retratos', 'porta-trecos', 
                                 'porta-retratos', 'vaso-de-flores', 'quadro-de-avisos', 'relogio-de-parede']}

    if assunto == 'frutas':
        return choice(frutas[nivel])
    elif assunto == 'profissoes':
        return choice(profissoes[nivel])
    elif assunto == 'animais':
        return choice(animais[nivel])
    elif assunto == 'cores':
        return choice(cores[nivel])
    elif assunto == 'objetos':
        return choice(objetos[nivel])
    elif assunto == 'paises':
        return choice(paises[nivel])


