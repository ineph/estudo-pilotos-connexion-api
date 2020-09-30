from server.services import piloto_service


def get_pilotos():
    return piloto_service.get_pilotos(), 200

