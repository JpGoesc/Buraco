class Jogador:
    def __init__(self, id: int, nome: str, senha: str):
        self.id = id
        self.nome = nome
        self.senha = senha

class Partida:
    def __init__(self, id: int, jogador_1_id: int, jogador_2_id: int):
        self.id = id
        self.jogador_1_id = jogador_1_id
        self.jogador_2_id = jogador_2_id
