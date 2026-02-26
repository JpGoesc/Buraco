from .ports import IPlayerRepository, IMatchRepository
from typing import Optional

class CreateMatchService:
    def __init__(self, player_repo: IPlayerRepository, match_repo: IMatchRepository):
        self.player_repo = player_repo
        self.match_repo = match_repo

    def execute(self, player1_id: int, player2_id: int) -> Optional[int]:
        if not self.player_repo.player_exists(player1_id):
            raise ValueError(f"Jogador com ID {player1_id} não existe.")
        if not self.player_repo.player_exists(player2_id):
            raise ValueError(f"Jogador com ID {player2_id} não existe.")

        return self.match_repo.create_match(player1_id, player2_id)
