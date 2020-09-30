from typing import List

from server.models.piloto_model import Piloto


def find_all_pilotos() -> List[Piloto]:
    pilotos = []

    piloto = Piloto(id=1,
                    nome="Rubens Barrichello",
                    nacionalidade="Brasileiro",
                    cidade_natal="São Paulo",
                    nascimento="23-05-1972",
                    vitorias=38,
                    corridas_participadas=578,
                    pole_positions=45,
                    voltas_mais_rapidas=50,
                    podios=136,
                    biografia="o cara é bom mesmo ele é paulistano a ferrari paga ele pra pilotar formula carro")

    pilotos.append(piloto)

    return pilotos
