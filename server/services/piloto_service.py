from server import Piloto, pilotos
from server.data_access_object import piloto_DAO


def get_pilotos():
    return piloto_DAO.find_all_pilotos()


def post_piloto(piloto_input):
    piloto = Piloto(
        id=gera_novo_id(),
        nome=piloto_input['nome'],
        nacionalidade=piloto_input['nacionalidade'],
        cidade_natal=piloto_input['cidade_natal'],
        nascimento=piloto_input['nascimento'],
        vitorias=piloto_input['vitorias'],
        corridas_participadas=piloto_input['corridas_participadas'],
        pole_positions=piloto_input['pole_positions'],
        voltas_mais_rapidas=piloto_input['voltas_mais_rapidas'],
        podios=piloto_input['podios'],
        biografia=piloto_input['biografia']
    )
    pilotos.append(piloto)
    return piloto


def gera_novo_id() -> int:
    return max([p.id for p in pilotos]) + 1
