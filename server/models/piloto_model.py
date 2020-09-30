from dataclasses import dataclass


@dataclass
class Piloto:
    id: int = None
    nome: str = None
    podios: int = None
    vitorias: int = None
    biografia: str = None
    nascimento: str = None
    cidade_natal: str = None
    nacionalidade: str = None
    pole_positions: int = None
    voltas_mais_rapidas: int = None
    corridas_participadas: int = None
