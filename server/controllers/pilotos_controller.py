from server.services import piloto_service


def get_pilotos():
    return piloto_service.get_pilotos(), 200


def post_piloto(piloto_input):
    return piloto_service.post_piloto(piloto_input), 201
