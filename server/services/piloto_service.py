from server.data_access_object import piloto_DAO


def get_pilotos():
    return piloto_DAO.find_all_pilotos()
