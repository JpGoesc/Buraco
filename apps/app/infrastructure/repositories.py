from django.db import connection
from app.domain.ports import IPlayerRepository, IMatchRepository
from typing import Optional

class PlayerRepository(IPlayerRepository):
    def player_exists(self, player_id: int) -> bool:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM Jogador WHERE ID = %s", [player_id])
            return cursor.fetchone()[0] > 0

class MatchRepository(IMatchRepository):
    def create_match(self, player1_id: int, player2_id: int) -> Optional[int]:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Partida (Jogador_1, Jogador_2) VALUES (%s, %s)",
                [player1_id, player2_id]
            )
            return cursor.lastrowid
