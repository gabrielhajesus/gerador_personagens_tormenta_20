from random import randint
from math import floor
from tkinter import *

""" Para depois(nessa ordem) equipamentos, deuses, poderes, magias."""

""" Dicionario com todas as raças do livro base
    Contém o nome da raça, os bonus da raça e os nomes mais comuns da raça. adicionar depois: poderes de raça, descrição base. 
    Bônus : FORCA, DESTREZA, CONSTITUICAO, INTELIGENCIA, SABEDORIA, CARISMA, QUANTIDADE DO BONUS EM VARIOS, QUANTOS ATRIBUTOS ENTRA, EXCESSÃO
    """
racas = {
    1  : {'nome': 'Humano'           , 'bonus': [ 0, 0, 0, 0, 0, 0, 1, 3, 0], 'nome_racas': [ 'Alysia', 'Aldor', 'Avelin', 'Aran', 'Braya', 'Beren', 'Catryn', 'Cyriac', 'Darna', 'Darik', 'Elenya', 'Dravor', 'Emeria', 'Drystan','Glenda', 'Eldred', 'Gylda', 'Ghart', 'Isolda', 'Gryffen', 'Jeanne', 'Jarad', 'Kiara', 'Holdred', 'Kathelyn', 'Khellus', 'Linette', 'Pelim', 'Lora', 'Nalan', 'Malin', 'Radan', 'Merewyn', 'Thedon', 'Rianna', 'Thulin', 'Tedwyn', 'Varn', 'Tila', 'Warin']},
    2  : {'nome': 'Anão'             , 'bonus': [ 0,-1, 2, 0, 1, 0, 0, 0, 0], 'nome_racas': [ 'Artrudda', 'Arduramm', 'Burgala', 'Bartarinn', 'Dorotha', 'Doragramm', 'Durdala', 'Dastoroc', 'Gardrina', 'Gardrumm', 'Ragardda', 'Guldaramm', 'Thratilga', 'Hortroc', 'Thorkala', 'Kradug', 'Thundrila', 'Khovarinn', 'Urdresia', 'Thardaramm']},
    3  : {'nome': 'Dahllan'          , 'bonus': [ 0, 1, 0,-1, 2, 0, 0, 0, 0], 'nome_racas': ["Aster", "Azalia", "Celandine", "Dhala", "Galya", "Lhyria", "Lura", "Tulipa", "Tyka", "Violeta"]},
    4  : {'nome': 'Elfo'             , 'bonus': [ 0, 1,-1, 2, 0, 0, 0, 0, 0], 'nome_racas': ["Allora", "Avoldar","Auruel", "Ellandor", "Calaena", "Felarin", "Eloen", "Glorandal", "Faunalyn", "Farandhil", "Kethrylliia", "Kirrion", "Laurena", "Lurienthel", "Merethy", "Myrthallar"]},
    5  : {'nome': 'Goblin'           , 'bonus': [ 0, 2, 0, 1, 0,-1, 0, 0, 0], 'nome_racas': [ "Ashi", "Ark", "Floba", "Barg", "Grin", "Buduc", "Iga", "Crag", "Mikhi", "Krig", "Prixa", "Rasg", "Pylda", "Tabo", "Shug", "Ulerc","Sizz", "Vrix", "Vruga", "Vrug"]},
    6  : {'nome': 'Lefou'            , 'bonus': [ 0, 0, 0, 0, 0,-1, 1, 3, 6], 'nome_racas': [ "Alma", "Eco", "Estrela", "Fulgor", "Furacão", "Sol", "Tempestade", "Tremor", "Uivo", "Zênite", "Afiada(o)", "Cadavérica(o)", "da Perdição", "do Ocaso", "Eterna(o)", "Herege", "Imortal", "Maldita(o)", "Rubra(o)", "Serrilhada(o)"]},
    7  : {'nome': 'Minotauro'        , 'bonus': [ 2, 0, 1, 0,-1, 0, 0, 0, 0], 'nome_racas': [ "Asterius", "Aulus", "Caelus", "Glabus", "Jartus", "Kargan", "Orgun", "Tiberius", "Tyraxus", "Vobius"]},
    8  : {'nome': 'Qareen'           , 'bonus': [ 0, 0, 0, 1,-1, 2, 0, 0, 0], 'nome_racas': [ "Urdresia", "Aliyah", "Batuhla", "Hanifa", "Jahira", "Lalyla", "Mhyla", "Nirad", "Safirah", "Sahla", "Zakiya", "Thardaramm", "Ahad", "Barakat", "Dawud", "Hossam", "Jaffah", "Kirud", "Nizur", "Sulid", "Tariq", "Wassim"]},
    9  : {'nome': 'Golem'            , 'bonus': [ 2, 0, 1, 0, 0,-1, 0, 0, 0], 'nome_racas': [ "Mágico Explorador Astuto", "Mágico Guardião Silencioso", "Mágico Criador Invencível", "Mecânico Guardião Implacável", "Mecânico Destruidor Veloz", "Mecânico Criador Astuto", "Ferro Gigante Implacável", "Ferro Guardião Forte", "Ferro Destruidor Veloz", "Fogo Gigante Destruidor", "Fogo Guardião Implacável", "Fogo Criador Veloz", "Pedra Gigante Forte", "Pedra Guardião Silencioso", "Pedra Destruidor Implacável", "Vapor Guardião Veloz", "Vapor Criador Astuto", "Vapor Explorador Invencível", "Gelo Gigante Forte", "Gelo Guardião Silencioso", "Gelo Destruidor Implacável"]},
    10 : {'nome': 'Hynne'            , 'bonus': [-1, 2, 0, 0, 0, 1, 0, 0, 0], 'nome_racas': [ "Arabella", "Ghyla", "Joly", "Lili", "Lobelia", "Malva", "Prinna", "Nyra", "Arno", "Flippo", "Glepin", "Guido", "Haldo", "Meric",  "Pippo", "Saruc"]},
    11 : {'nome': 'Kliren'           , 'bonus': [-1, 0, 0, 0, 2, 1, 0, 0, 0], 'nome_racas': ['Bilgrim', 'Toscomola', 'Nimble', 'Coggen', 'Pippo', 'Ferrabico', 'Zindle', 'Flintquill', 'Wizzle', 'Turbovolt', 'Glimmer', 'Whistlewhisk', 'Fibble', 'Tinkerspark', 'Brixie', 'Geargrind', 'Tolli', 'Shatterpuff', 'Grindle', 'Copperleaf']},
    12 : {'nome': 'Medusa'           , 'bonus': [ 0, 2, 0, 0, 0, 1, 0, 0, 0], 'nome_racas': [ 'Selkira', 'Viperfang', 'Ithra', 'Serpentgaze', 'Nyxira', 'Venombreath', 'Zyphora', 'Coilstrike', 'Myrka', 'Shadewhisper', 'Thessala', 'Stoneglare', 'Veshka', 'Deathcoil', 'Lyrissis', 'Fangveil', 'Othana', 'Gorgonshade', 'Zalithra', 'Darkscale']},
    13 : {'nome': 'Osteon'           , 'bonus': [ 0, 0,-1, 0, 0, 0, 1, 3, 3], 'nome_racas': [ 'Kharos Ossomante', 'Varnok Sepulcral', 'Morthar Sombrosso', 'Drakthos Ossotrevas', 'Zarthan Desossado', 'Rhazak Quebraossos', 'Velkan Ossovento', 'Thalkor Rachadura', 'Sivak Ossolume', 'Grimnok Mortemarcha']},
    14 : {'nome': 'Sereia/tritão'    , 'bonus': [ 0, 0, 0, 0, 0, 0, 1, 3, 0], 'nome_racas': [ 'Nerithia Marésombra', 'Thalron Profundamar', 'Sirynna Ondastral', 'Kaelen Coraltrovão', 'Lyriena Espumabranca', 'Zarion Marévolta', 'Elarya Algaestrela', 'Nymar Neptunius', 'Aqualis Cristalina', 'Virellan Encantomar']},
    15 : {'nome': 'Sílfide'          , 'bonus': [-2, 1, 0, 0, 0, 2, 0, 0, 0], 'nome_racas': ["Céu", "Bedra", "Flama", "Gerânia", "Liri", "Luriel", "Marly", "Pétala", "Cecil", "Burble", "Flax", "Ginko", "Novus", "Olmo", "Pingo", "Rolyn"]},
    16 : {'nome': 'Suraggel(aggleus)', 'bonus': [ 0, 0, 0, 0, 2, 1, 0, 0, 0], 'nome_racas': [ 'Celestia Dawnwhisper', 'Seraphiel Aetherwing', 'Lysandra Starfall', 'Gavriel Lightbringer', 'Auriel Emberheart', 'Elowen Radiantshade', 'Thaliel Sunstrider', 'Israfel Halocharm', 'Caelum Brightflare', 'Seraphius Luminar']},
    17 : {'nome': 'Suraggel(sulfure)', 'bonus': [ 0, 2, 0, 1, 0, 0, 0, 0, 0], 'nome_racas': [ 'Zarek Thalor', 'Lirael Voss', 'Kaelith Duskwhisper', 'Xandros Firoth', 'Seraphine Nocturne', 'Varok Ashenfire', 'Nyxara Blackthorn', 'Talindra Shadowblade', 'Draven Infernal', 'Isolde Emberveil']},
    18 : {'nome': 'Trog'             , 'bonus': [ 1, 0, 2,-1, 0, 0, 0, 0, 0], 'nome_racas': [ "Arxsa", "Bakzha", "Chask", "Darsza", "Jacha", "Shuruh", "Thuji", "Urla", "Atszo", "Bhaz", "Crosk", "Drurg", "Glulg", "Orzok", "Qrux", "Truusz"]}
}

""" Dicionario com todas as classes do livro base
    Contém o nome da classe, o foco de atributos, o status base, as pericias base e aleatorias. adicionar depois: proeficiencias, poderes de classe, requisito de nivel, contador de xp, tesouro.
    Foco: Foco padrão de atributos para cada classe.
    Status : VIDA, PONTOS DE MANA"""
classes = {
    1: {'nome' : 'arcanista(bruxo)', 'foco': ['forca', 'constituicao', 'destreza', 'carisma', 'sabedoria', 'inteligencia'], 'status' : [8, 6] , 'pericias': {'base':  ['misticismo', 'vontade'], 'aleatorio': [2, 'conhecimento', 'diplomacia' , 'enganacao', 'guerra', 'iniciativa', 'intimidacao','intuicao', 'investigacao', 'nobreza', 'oficio', 'percepcao']}},
    2: {'nome' : 'arcanista(feiticeiro)', 'foco': ['forca', 'constituicao', 'destreza', 'inteligencia', 'sabedoria', 'carisma'], 'status' : [8, 6], 'pericias':{'base':  ['misticismo', 'vontade'], 'aleatorio': [2, 'conhecimento', 'diplomacia' , 'enganacao', 'guerra', 'iniciativa', 'intimidacao','intuicao', 'investigacao', 'nobreza', 'oficio', 'percepcao']}},
    3: {'nome' : 'arcanista(mago)', 'foco': ['forca', 'constituicao', 'destreza', 'inteligencia', 'sabedoria', 'carisma'], 'status' : [8, 6], 'pericias':{'base':  ['misticismo', 'vontade'], 'aleatorio': [2, 'conhecimento', 'diplomacia' , 'enganacao', 'guerra', 'iniciativa', 'intimidacao','intuicao', 'investigacao', 'nobreza', 'oficio', 'percepcao']}},
    4: {'nome' : 'barbaro', 'foco': ['inteligencia', 'sabedoria', 'carisma', 'destreza', 'constituicao', 'forca'], 'status' : [24, 3], 'pericias': {'base':  ['fortitude','luta'], 'aleatorio': [4, 'adestramento', 'atletismo', 'cavalgar', 'iniciativa', 'intimidacao', 'oficio', 'percepcao', 'pontaria','sobrevivencia', 'vontade']}},
    5: {'nome' : 'bardo', 'foco': ['forca', 'constituicao', 'destreza', 'inteligencia', 'sabedoria', 'carisma'], 'status' : [12, 4], 'pericias':{'base':  ['atuacao', 'reflexos'], 'aleatorio': [6,  'acrobacia','cavalgar', 'conhecimento', 'diplomacia', 'enganacao', 'furtividade', 'iniciativa','intuicao', 'investigacao', 'jogatina', 'ladinagem' , 'luta', 'misticismo', 'nobreza','percepcao', 'pontaria', 'vontade']}},
    6: {'nome' : 'bucaneiro', 'foco': ['sabedoria', 'constituicao', 'forca', 'inteligencia', 'carisma', 'destreza'], 'status' : [16, 3], 'pericias':{'base':  ['pontaria', 'reflexos'], 'aleatorio': [4, 'acrobacia','atletismo', 'atuacao', 'enganacao', 'fortitude', 'furtividade', 'iniciativa', 'intimidacao', 'jogatina', 'luta', 'oficio', 'percepcao', 'pilotagem']}},
    7: {'nome' : 'cacador', 'foco': ['sabedoria', 'carisma', 'constituicao', 'inteligencia', 'forca', 'destreza'], 'status' : [16, 4], 'pericias':{'base':  ['pontaria', 'sobrevivencia' ], 'aleatorio': [6, 'adestramento', 'atletismo', 'cavalgar', 'cura', 'fortitude', 'furtividade', 'iniciativa', 'investigacao', 'luta', 'oficio', 'percepcao', 'reflexos']}},
    8: {'nome' : 'cavaleiro', 'foco': ['inteligencia', 'sabedoria', 'carisma', 'destreza', 'constituicao', 'forca'], 'status' : [20, 3], 'pericias':{'base':  ['fortitude', 'luta'], 'aleatorio': [2, 'adestramento', 'atletismo', 'cavalgar', 'diplomacia', 'guerra', 'iniciativa', 'intimidacao', 'nobreza', 'percepcao', 'vontade']}},
    9: {'nome' : 'clerigo', 'foco': ['forca', 'constituicao', 'destreza', 'carisma', 'inteligencia', 'sabedoria'], 'status' : [16, 5], 'pericias':{'base':  ['religiao', 'vontade'], 'aleatorio': [2, 'conhecimento','cura', 'diplomacia', 'fortitude', 'iniciativa', 'intuicao', 'luta', 'misticismo', 'nobreza', 'oficio', 'percepcao']}},
    10: {'nome' : 'druida', 'foco': ['forca', 'constituicao', 'destreza', 'carisma', 'inteligencia', 'sabedoria'], 'status' : [16, 4], 'pericias':{'base':  ['sobrevivencia' , 'vontade'], 'aleatorio': [4,  'adestramento', 'atletismo', 'cavalgar', 'conhecimento', 'cura', 'fortitude', 'iniciativa','intuicao', 'luta', 'misticismo', 'oficio', 'percepcao', 'religiao']}},
    11: {'nome' : 'guerreiro', 'foco': ['inteligencia', 'sabedoria', 'carisma', 'constituicao', 'destreza', 'forca'], 'status' : [20, 3], 'pericias':{'base':  ['luta', 'fortitude'], 'aleatorio': [2, 'adestramento', 'atletismo', 'cavalgar', 'guerra', 'iniciativa', 'intimidacao', 'luta', 'oficio', 'percepcao', 'pontaria', 'reflexos']}},
    12: {'nome' : 'inventor', 'foco': ['forca', 'constituicao', 'destreza', 'carisma', 'sabedoria', 'inteligencia'], 'status' : [12, 4], 'pericias':{'base':  ['oficio', 'vontade'], 'aleatorio': [4, 'conhecimento', 'cura', 'diplomacia', 'fortitude', 'iniciativa', 'investigacao', 'luta', 'misticismo', 'oficio', 'pilotagem', 'pontaria', 'percepcao']}},
    13: {'nome' : 'ladino', 'foco': ['inteligencia', 'sabedoria', 'constituicao', 'forca', 'carisma', 'destreza'], 'status' : [12, 4], 'pericias':{'base':  ['ladinagem', 'reflexos'], 'aleatorio': [8,  'acrobacia', 'atletismo', 'atuacao', 'cavalgar', 'conhecimento', 'diplomacia', 'enganacao', 'furtividade', 'iniciativa', 'intimidacao', 'intuicao', 'investigacao','jogatina', 'luta', 'oficio', 'percepcao', 'pilotagem', 'pontaria']}},
    14: {'nome' : 'lutador', 'foco': ['inteligencia', 'sabedoria', 'carisma', 'destreza', 'constituicao', 'forca'], 'status' : [20, 3], 'pericias':{'base':  ['fortitude', 'luta'], 'aleatorio': [4, 'acrobacia','adestramento', 'atletismo', 'enganacao', 'furtividade', 'iniciativa', 'intimidacao','oficio', 'percepcao', 'pontaria', 'reflexos']}},
    15: {'nome' : 'nobre', 'foco': ['inteligencia', 'sabedoria', 'destreza', 'constituicao', 'forca', 'carisma'], 'status' : [16, 4], 'pericias':{'base':  ['diplomacia', 'vontade'], 'aleatorio': [4, 'adestramento', 'atuacao', 'cavalgar', 'conhecimento', 'diplomacia', 'enganacao', 'fortitude', 'guerra', 'iniciativa', 'intimidacao', 'intuicao', 'investigacao', 'jogatina', 'luta', 'nobreza', 'oficio', 'percepcao', 'pontaria']}},
    16: {'nome' : 'paladino', 'foco': ['inteligencia', 'sabedoria', 'carisma', 'destreza', 'constituicao', 'forca'], 'status' : [20, 3], 'pericias':{'base': ['luta', 'vontade'], 'aleatorio': [2,  'adestramento', 'atletismo', 'cavalgar', 'cura', 'diplomacia','fortitude', 'guerra', 'iniciativa','intuicao', 'nobreza', 'percepcao', 'religiao']}}
}

""" Dicionario com todas as origens do livro base
    

"""

origens = {
    1: 'Acolito',
    2: 'Amigo dos Animais',
    3: 'Amnésico',
    4: 'Aristocrata',
    5: 'Artesão',
    6: 'Artista',
    7: 'Assistente de Laboratório',
    8: 'Batedor',
    9: 'Capanga',
    10: 'Charlatão',
    11: 'Circense',
    12: 'Criminoso',
    13: 'Curandeiro',
    14: 'Eremita',
    15: 'Escravo',
    16: 'Estudioso',
    17: 'Fazendeiro',
    18: 'Forasteiro',
    19: 'Gladiador',
    20: 'Guarda',
    21: 'Herdeiro',
    22: 'Herói Camponês',
    23: 'Marujo',
    24: 'Mateiro',
    25: 'Membro de Guilda',
    26: 'Mercador',
    27: 'Minerador',
    28: 'Nômade',
    29: 'Pivete',
    30: 'Refugiado',
    31: 'Seguidor',
    32: 'Selvagem',
    33: 'Soldado',
    34: 'Taverneiro',
    35: 'Trabalhador'
}

origem_pericias_poderes = {
    "Acolito": {
        "pericias": ["cura", "religiao", "vontade"],
        "poderes_de_origem": ["Medicina", "Membro da Igreja", "Vontade de Ferro"]
    },
    "Amigo dos Animais": {
        "pericias": ["adestramento", "cavalgar"],
        "poderes_de_origem": ["Amigo Especial"]
    },
    "Amnésico": {
        "pericias": ["vontade"],
        "poderes_de_origem": ["um poder escolhidos pelo mestre", "Lembranças Guardadas"]
    },
    "Aristocrata": {
        "pericias": ["diplomacia", "enganacao", "nobreza"],
        "poderes_de_origem": ["Comandar", "Sangue Azul"]
    },
    "Artesão": {
        "pericias": ["oficio", "vontade"],
        "poderes_de_origem": ["Frutos do Trabalho", "Sortudo"]
    },
    "Artista": {
        "pericias": ["atuacao", "enganacao"],
        "poderes_de_origem": ["Atraente", "Dom Artístico", "Sortudo", "Torcida"]
    },
    "Assistente de Laboratório": {
        "pericias": ["oficio", "misticismo"],
        "poderes_de_origem": ["Esse Cheiro...", "Venefício"]
    },
    "Batedor": {
        "pericias": ["furtividade", "percepcao", "sobrevivencia"],
        "poderes_de_origem": ["A Prova de Tudo", "Estilo de Disparo", "Sentidos Aguçados"]
    },
    "Capanga": {
        "pericias": ["luta", "intimidacao"],
        "poderes_de_origem": ["Confissão", "Um poder de combate à sua escolha"]
    },
    "Charlatão": {
        "pericias": ["enganacao", "jogatina"],
        "poderes_de_origem": ["Alpinista Social", "Aparência Inofensiva", "Sortudo"]
    },
    "Circense": {
        "pericias": ["acrobacia", "atuacao", "reflexos"],
        "poderes_de_origem": ["Acrobático", "Torcida", "Truque de Mágica"]
    },
    "Criminoso": {
        "pericias": ["enganacao", "furtividade", "ladinagem"],
        "poderes_de_origem": ["Punguista", "Venefício"]
    },
    "Curandeiro": {
        "pericias": ["cura", "vontade"],
        "poderes_de_origem": ["Medicina", "Médico de Campo", "Venefício"]
    },
    "Eremita": {
        "pericias": ["misticismo", "religiao", "sobrevivencia"],
        "poderes_de_origem": ["Busca Interior", "Lobo Solitário"]
    },
    "Escravo": {
        "pericias": ["atletismo", "fortitude", "furtividade"],
        "poderes_de_origem": ["Desejo de Liberdade", "Vitalidade"]
    },
    "Estudioso": {
        "pericias": ["conhecimento", "guerra", "misticismo"],
        "poderes_de_origem": ["Aparência Inofensiva", "Palpite Fundamentado"]
    },
    "Fazendeiro": {
        "pericias": ["adestramento", "cavalgar", "oficio", "sobrevivencia"],
        "poderes_de_origem": ["Água no Feijão", "Gente Boa"]
    },
    "Forasteiro": {
        "pericias": ["cavalgar", "pilotagem", "sobrevivencia"],
        "poderes_de_origem": ["Cultura Exótica", "Lobo Solitário"]
    },
    "Gladiador": {
        "pericias": ["atuacao", "luta"],
        "poderes_de_origem": ["Atraente", "Pão e Circo", "Torcida", "Um poder de combate à sua escolha"]
    },
    "Guarda": {
        "pericias": ["investigacao", "luta", "percepcao"],
        "poderes_de_origem": ["Detetive", "Investigador", "Um poder de combate à sua escolha"]
    },
    "Herdeiro": {
        "pericias": ["misticismo", "nobreza", "oficio"],
        "poderes_de_origem": ["Comandar", "Herança"]
    },
    "Herói Camponês": {
        "pericias": ["adestramento", "oficio"],
        "poderes_de_origem": ["Amigos dos Plebeus", "Sortudo", "Surto Heroico", "Torcida"]
    },
    "Marujo": {
        "pericias": ["atletismo", "jogatina", "pilotagem"],
        "poderes_de_origem": ["Acrobático", "Passagem de Navio"]
    },
    "Mateiro": {
        "pericias": ["atletismo", "furtividade", "sobrevivencia"],
        "poderes_de_origem": ["Lobo Solitário", "Sentidos Aguçados", "Vendedor de Carcaças"]
    },
    "Membro de Guilda": {
        "pericias": ["diplomacia", "enganacao", "misticismo", "oficio"],
        "poderes_de_origem": ["Ficou sem Perícia", "Rede de Contatos"]
    },
    "Mercador": {
        "pericias": ["diplomacia", "intuicao", "oficio"],
        "poderes_de_origem": ["Negociação", "Proficência", "Sortudo"]
    },
    "Minerador": {
        "pericias": ["atletismo", "oficio"],
        "poderes_de_origem": ["Ataque Poderoso", "Escavador", "Sentidos Aguçados"]
    },
    "Nômade": {
        "pericias": ["cavalgar", "pilotagem", "sobrevivencia"],
        "poderes_de_origem": ["Lobo Solitário", "Mochileiro", "Sentidos Aguçados"]
    },
    "Pivete": {
        "pericias": ["furtividade", "iniciativa", "ladinagem"],
        "poderes_de_origem": ["Aparência Inofensiva", "Quebra-Galho"]
    },
    "Refugiado": {
        "pericias": ["fortitude", "reflexos", "vontade"],
        "poderes_de_origem": ["Estoico", "Vontade de Ferro"]
    },
    "Seguidor": {
        "pericias": ["adestramento", "oficio"],
        "poderes_de_origem": ["Antigo Mestre", "Proficiente", "Sortudo"]
    },
    "Selvagem": {
        "pericias": ["percepcao", "reflexos", "sobrevivencia"],
        "poderes_de_origem": ["Lobo Solitário", "Vida Rústica", "Vitalidade"]
    },
    "Soldado": {
        "pericias": ["diplomacia", "guerra", "luta", "pontaria"],
        "poderes_de_origem": ["Intuição Militar", "Um poder de combate à sua escolha"]
    },
    "Taberneiro": {
        "pericias": ["atuacao", "oficio"],
        "poderes_de_origem": ["Gororoba", "Proficência", "Vitalidade"]
    },
    "Trabalhador": {
        "pericias": ["atletismo", "fortitude"],
        "poderes_de_origem": ["Atlético", "Esforçado"]
    }
}

modificadores = {
    3: -2,
    4: -2,
    5: -2,
    6: -2,
    7: -2, 
    8: -1,
    9: -1,
    10: 0,
    11: 0,
    12: 1,
    13: 1,
    14: 2,
    15: 2,
    16: 3,
    17: 3,
    18: 4
}

alinhamento = {
    1: 'Leal Bom',
    2: 'Neutro Bom',
    3: 'Caotico Bom',
    4: 'Leal Neutro',
    5: 'Neutro Neutro',
    6: 'Caotico Neutro',
    7: 'Leal Mal',
    8: 'Neutro Mal',
    9: 'Caotico Mal'
}

pericias_iniciais = {
    "acrobacia"    : {"atributo": "destreza"    , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": True , 'valor': 0},
    "adestramento" : {"atributo": "carisma"     , "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "atletismo"    : {"atributo": "forca"       , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "atuacao"      : {"atributo": "carisma"     , "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "cavalgar"     : {"atributo": "destreza"    , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "conhecimento" : {"atributo": "inteligencia", "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "cura"         : {"atributo": "sabedoria"   , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "diplomacia"   : {"atributo": "carisma"     , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "enganacao"    : {"atributo": "carisma"     , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "fortitude"    : {"atributo": "constituicao", "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": True, 'valor': 0},
    "furtividade"  : {"atributo": "destreza"    , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": True, 'valor': 0},
    "guerra"       : {"atributo": "inteligencia", "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "iniciativa"   : {"atributo": "destreza"    , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "intimidacao"  : {"atributo": "carisma"     , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "intuicao"     : {"atributo": "sabedoria"   , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "investigacao" : {"atributo": "inteligencia", "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "jogatina"     : {"atributo": "carisma"     , "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "ladinagem"    : {"atributo": "destreza"    , "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": True, 'valor': 0},
    "luta"         : {"atributo": "forca"       , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": True, 'valor': 0},
    "misticismo"   : {"atributo": "inteligencia", "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "nobreza"      : {"atributo": "inteligencia", "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "oficio"       : {"atributo": "inteligencia", "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "percepcao"    : {"atributo": "sabedoria"   , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "pilotagem"    : {"atributo": "destreza"    , "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "pontaria"     : {"atributo": "destreza"    , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "reflexos"     : {"atributo": "destreza"    , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "religiao"     : {"atributo": "sabedoria"   , "necessario_ser_treinado": True, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "sobrevivencia": {"atributo": "sabedoria"   , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0},
    "vontade"      : {"atributo": "sabedoria"   , "necessario_ser_treinado": False, "treinada": False, "penalidade_armadura": False, 'valor': 0}
}

class Personagem():
    def rolando_atributos(self):
        aux1 = randint(1,6)
        aux2 = randint(1,6)
        aux3 = randint(1,6)
        aux4 = randint(1,6)

        if (aux1 <= aux2 and aux1 <= aux3 and aux1 <= aux4):
            valor = aux2 + aux3 + aux4
            return valor
        elif (aux2 <= aux1 and aux2 <= aux3 and aux2 <= aux4):
            valor = aux1 + aux3 + aux4
            return valor
        elif (aux3 <= aux1 and aux3 <= aux2 and aux3 <= aux4):
            valor = aux1 + aux2 + aux4
            return valor
        elif (aux4 <= aux1 and aux4 <= aux2 and aux4 <= aux3):
            valor = aux1 + aux2 + aux3
            return valor
        
    def __init__(self):
        self.nome = ""
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.raca = racas[randint(1,18)]['nome']
        self.classe = classes[randint(1,16)]['nome']
        self.origem = origens[randint(1,35)]
        self.alinhamento = alinhamento[randint(1,9)]
        self.vida = 0
        self.nivel = 1
        self.pm = 0
        self.cd = 10
        self.proeficiencias =[]
        self.pericias_treinadas = {}
        self.pericias_valor = {
                                "acrobacia": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "adestramento": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "atletismo": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "atuacao": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "cavalgar": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "conhecimento": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "cura": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "diplomacia": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "enganacao": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "fortitude": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "furtividade": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "guerra": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "iniciativa": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "intimidacao": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "intuicao": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "investigacao": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "jogatina": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "ladinagem": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "luta": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "misticismo": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "nobreza": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "oficio": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "percepcao": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "pilotagem": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "pontaria": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "reflexos": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "religiao": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "sobrevivencia": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0},
                                "vontade": {'total':0, 'treinadas': 0, 'modificador': 0, 'bonus_nivel': 0, 'penalidade_armadura' : 0}
        }
                
    def pericias_treinadas_valores(self, bonus_nivel):
        pericias_lista = [
            'misticismo', 'vontade', 'conhecimento', 'diplomacia', 'enganacao', 'guerra', 'iniciativa', 'intimidacao',
            'intuicao', 'investigacao', 'nobreza', 'oficio', 'percepcao', 'fortitude', 'luta', 'adestramento', 'atletismo',
            'cavalgar', 'acrobacia', 'atuacao', 'furtividade', 'jogatina', 'ladinagem', 'pontaria', 'sobrevivencia', 'reflexos',
            'cura', 'religiao', 'pilotagem'
        ]

        for classe in classes:
            if self.classe == classes[classe]['nome']:
                pericias_base = classes[classe]['pericias']['base']
                pericias_aleatorio = classes[classe]['pericias']['aleatorio']
        for origem in origem_pericias_poderes:
            if origem == self.origem:
                for pericia in origem_pericias_poderes[origem]['pericias']:
                    if pericia not in self.pericias_treinadas:
                        self.pericias_treinadas[pericia] = 'treinada'

        
        for pericia in pericias_base:
            if pericia not in self.pericias_treinadas:
                self.pericias_treinadas[pericia] = 'treinada'

        
        lista = pericias_aleatorio
        for i in range(lista[0]+1):
            cont = 0
            while cont <= len(pericias_aleatorio):
                aux = len(pericias_aleatorio) - 1
                numero_pericia = randint(1, aux)
                if lista[numero_pericia] not in self.pericias_treinadas and i != 0:
                    self.pericias_treinadas[lista[numero_pericia]] = 'treinada'
                    break
                cont += 1

        for i in range(self.inteligencia):
            for pericia in pericias_lista:
                if pericia not in self.pericias_treinadas:
                    self.pericias_treinadas[pericia] = 'treinada'
                    break

        for treinadas in self.pericias_treinadas:
            self.pericias_valor[treinadas]['treinadas'] = 2

        for pericia in self.pericias_valor:
            if pericias_iniciais[pericia]['atributo'] == 'forca':
                self.pericias_valor[pericia]['modificador'] += self.forca
                self.pericias_valor[pericia]['bonus_nivel'] += bonus_nivel
                self.pericias_valor[pericia]['total'] = self.pericias_valor[pericia]['treinadas'] + self.pericias_valor[pericia]['modificador'] + self.pericias_valor[pericia]['bonus_nivel']
            if pericias_iniciais[pericia]['atributo'] == 'destreza':
                self.pericias_valor[pericia]['modificador'] += self.destreza
                self.pericias_valor[pericia]['bonus_nivel'] += bonus_nivel
                self.pericias_valor[pericia]['total'] = self.pericias_valor[pericia]['treinadas'] + self.pericias_valor[pericia]['modificador'] + self.pericias_valor[pericia]['bonus_nivel']
            if pericias_iniciais[pericia]['atributo'] == 'constituicao':
                self.pericias_valor[pericia]['modificador'] += self.constituicao
                self.pericias_valor[pericia]['bonus_nivel'] += bonus_nivel
                self.pericias_valor[pericia]['total'] = self.pericias_valor[pericia]['treinadas'] + self.pericias_valor[pericia]['modificador'] + self.pericias_valor[pericia]['bonus_nivel']
            if pericias_iniciais[pericia]['atributo'] == 'inteligencia':
                self.pericias_valor[pericia]['modificador'] += self.inteligencia
                self.pericias_valor[pericia]['bonus_nivel'] += bonus_nivel
                self.pericias_valor[pericia]['total'] = self.pericias_valor[pericia]['treinadas'] + self.pericias_valor[pericia]['modificador'] + self.pericias_valor[pericia]['bonus_nivel']
            if pericias_iniciais[pericia]['atributo'] == 'sabedoria':
                self.pericias_valor[pericia]['modificador']+= self.sabedoria
                self.pericias_valor[pericia]['bonus_nivel'] += bonus_nivel
                self.pericias_valor[pericia]['total'] = self.pericias_valor[pericia]['treinadas'] + self.pericias_valor[pericia]['modificador'] + self.pericias_valor[pericia]['bonus_nivel']
            if pericias_iniciais[pericia]['atributo'] == 'carisma':
                self.pericias_valor[pericia]['modificador']+= self.carisma
                self.pericias_valor[pericia]['bonus_nivel'] += bonus_nivel
                self.pericias_valor[pericia]['total'] = self.pericias_valor[pericia]['treinadas'] + self.pericias_valor[pericia]['modificador'] + self.pericias_valor[pericia]['bonus_nivel']

    def gerador_nomes(self):
        for raca in racas:
            if racas[raca]['nome'] == self.raca:
                nome = racas[raca]['nome_racas'][randint(0, len(racas[raca]['nome_racas']) - 1) ]
                self.nome = nome

    def definindo_atributos(self):
        atributos = self.atributos_rolados()
        atributos_finais = []

        """self.mostrando_personagem('inicial')"""
        for classe in classes:
            if self.classe == classes[classe]['nome']:
                atributos_finais = classes[classe]['foco']

        for i in range(6):
            if atributos_finais[i] == 'forca':
                self.forca = modificadores[atributos[i]]
            if atributos_finais[i] == 'destreza':
                self.destreza = modificadores[atributos[i]]
            if atributos_finais[i] == 'constituicao':
                self.constituicao = modificadores[atributos[i]]
            if atributos_finais[i] == 'inteligencia':
                self.inteligencia = modificadores[atributos[i]]
            if atributos_finais[i] == 'sabedoria':
                self.sabedoria = modificadores[atributos[i]]
            if atributos_finais[i] == 'carisma':
                self.carisma = modificadores[atributos[i]]
        
        for raca in racas:
            if self.raca == racas[raca]['nome']:
                atributos_raca = racas[raca]['bonus']
                break
        
        
        if self.raca == 'Humano' or self.raca == 'Sereia/tritão':
            for i in range(6):
                if atributos_finais[i] == 'forca':
                    if atributos_raca[0] > 0:
                        self.forca += atributos_raca[0]
                    if i>=3:
                        self.forca += 1
                if atributos_finais[i] == 'destreza':
                    if atributos_raca[1] > 0:
                        self.destreza += atributos_raca[1]
                    if i>=3:
                        self.destreza += 1
                if atributos_finais[i] == 'constituicao':
                    if atributos_raca[2] > 0:
                        self.constituicao += atributos_raca[2]
                    if i>=3:
                        self.constituicao += 1
                if atributos_finais[i] == 'inteligencia':
                    if atributos_raca[3] > 0:
                        self.inteligencia += atributos_raca[3]
                    if i>=3:
                        self.inteligencia += 1
                if atributos_finais[i] == 'sabedoria':
                    if atributos_raca[4] > 0:
                        self.sabedoria += atributos_raca[4]
                    if i>=3:
                        self.sabedoria += 1
                if atributos_finais[i] == 'carisma':
                    if atributos_raca[5] > 0:
                        self.carisma += atributos_raca[5]
                    if i>=3:
                        self.carisma += 1
        elif self.raca == 'Lefou':
            for i in range(6):
                if atributos_finais[i] == 'forca':
                    self.forca += atributos_raca[0]
                    if i>=2:
                        self.forca += 1
                if atributos_finais[i] == 'destreza':
                    self.destreza += atributos_raca[1]
                    if i>=2:
                        self.destreza += 1
                if atributos_finais[i] == 'constituicao':
                    self.constituicao += atributos_raca[2]
                    if i>=2:
                        self.constituicao += 1
                if atributos_finais[i] == 'inteligencia':
                    self.inteligencia += atributos_raca[3]
                    if i>=2:
                        self.inteligencia += 1
                if atributos_finais[i] == 'sabedoria':
                    self.sabedoria += atributos_raca[4]
                    if i>=2:
                        self.sabedoria += 1
                if atributos_finais[i] == 'carisma':
                    self.carisma += atributos_raca[5]
        elif self.raca == 'Osteon':
            for i in range(6):
                if atributos_finais[i] == 'forca':
                    self.forca += atributos_raca[0]
                    if i>=2:
                        self.forca += 1
                if atributos_finais[i] == 'destreza':
                    self.destreza += atributos_raca[1]
                    if i>=2:
                        self.destreza += 1
                if atributos_finais[i] == 'constituicao':
                    self.constituicao += atributos_raca[2]
                if atributos_finais[i] == 'inteligencia':
                    self.inteligencia += atributos_raca[3]
                    if i>=2:
                        self.inteligencia += 1
                if atributos_finais[i] == 'sabedoria':
                    self.sabedoria += atributos_raca[4]
                    if i>=2:
                        self.sabedoria += 1
                if atributos_finais[i] == 'carisma':
                    self.carisma += atributos_raca[5]
                    if i>=2:
                        self.carisma += 1
        else:
            for i in range(6):
                if atributos_finais[i] == 'forca':
                    self.forca += atributos_raca[0]
                if atributos_finais[i] == 'destreza':
                    self.destreza += atributos_raca[1]
                if atributos_finais[i] == 'constituicao':
                    self.constituicao += atributos_raca[2]
                if atributos_finais[i] == 'inteligencia':
                    self.inteligencia += atributos_raca[3]
                if atributos_finais[i] == 'sabedoria':
                    self.sabedoria += atributos_raca[4]
                if atributos_finais[i] == 'carisma':
                    self.carisma += atributos_raca[5]

    def mostrando_personagem(self):
        texto = f'''\n Personagem Criado \n\n     Nome:  {self.nome}    Alinhamento: {self.alinhamento}     Nivel: {str(self.nivel)}
        \n     Raça: {str(self.raca)}     Classe: {str(self.classe)}     Origem: {str(self.origem)}\n     For: {str(self.forca)}   Des: {str(self.destreza)}   Con: {str(self.constituicao)}   Int: {str(self.inteligencia)}   Sab: {str(self.sabedoria)}   Car: {str(self.carisma)}\n\n     Vida: {str(self.vida)} PM: {str(self.pm)} CD: {str(self.cd)}
        \n     Pericias: \n'''
        cont = 0
        for pericia in self.pericias_valor:
            texto += '             ' + str(pericia) + ' : ' + str(self.pericias_valor[pericia]['total'])
            cont +=1
            if cont%5==0:
                texto += '\n'
        
        texto +='\n     Pericias treinadas: \n'
        cont = 0
        for pericia_treinada in self.pericias_treinadas:
            texto +='             ' + str(pericia_treinada) + ' : ' + str(self.pericias_treinadas[pericia_treinada])
            cont +=1
            if cont%5==0:
                texto += '\n'
        texto += '\n'
        return texto

    def atributos_rolados(self):
        atributos = []
        
        for i in range(6):
            atributos.append(self.rolando_atributos())

        atributos.sort()
        
        if modificadores[atributos[0]] + modificadores[atributos[1]] + modificadores[atributos[2]] + modificadores[atributos[3]] + modificadores[atributos[4]] + modificadores[atributos[5]] < 6:
            while modificadores[atributos[0]] + modificadores[atributos[1]] + modificadores[atributos[2]] + modificadores[atributos[3]] + modificadores[atributos[4]] + modificadores[atributos[5]] < 6:
                atributos[0] = self.rolando_atributos()
                atributos.sort()
            return atributos
        else:
            return atributos
        
    def definincdo_status(self):
        for classe in classes:
            if self.classe == classes[classe]['nome']:
                status = classes[classe]['status']
        
        self.vida = status[0] + self.constituicao
        self.pm = status[1] 
        self.cd += self.destreza
        bonus_nivel = self.nivel

        if self.nivel > 1:
            self.vida += int((status[0])/4 + self.constituicao)*self.nivel
            self.pm += (status[1])*self.nivel
            bonus_nivel = floor(self.nivel/2)
        self.pericias_treinadas_valores(bonus_nivel)
        self.gerador_nomes()     
    
    def montando_personagem(self):
        self.definindo_atributos()
        self.definincdo_status()
        print('Personagem montado com sucesso')

def criacao_personagem():
    personagem1 = Personagem()
    personagem1.montando_personagem()
    personagem1.nivel = 1
    texto_personagens["text"] = personagem1.mostrando_personagem()

janela = Tk()
janela.title("Gerador de Personagens Tormenta")

texto_orientacao = Label(janela, text = 'Criando personagem aleatorio')
texto_orientacao.grid(column= 0 , row=0, padx=10, pady=10)

botao = Button(janela, text='Criar', command = criacao_personagem)
botao.grid(column= 0, row = 1, padx=0, pady=0)

texto_personagens = Label(janela, text="")
texto_personagens.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()