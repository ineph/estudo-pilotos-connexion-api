from server.models.piloto_model import Piloto

pilotos = []

pilotos = [
    Piloto(id=1,
           nome="Rubens Barrichello",
           nacionalidade="Brasileiro",
           cidade_natal="São Paulo",
           nascimento="23-05-1972",
           vitorias=38,
           corridas_participadas=578,
           pole_positions=45,
           voltas_mais_rapidas=50,
           podios=136,
           biografia="o cara é bom mesmo ele é paulistano a ferrari paga ele pra pilotar formula carro"),
    Piloto(id=2,
           nome="Michael Schumacher",
           nacionalidade="Alemao",
           cidade_natal="Hürth-Hermühlheim",
           nascimento="03-01-1969",
           vitorias=115,
           corridas_participadas=370,
           pole_positions=80,
           voltas_mais_rapidas=50,
           podios=194,
           biografia="esse alemão é foda")
]
