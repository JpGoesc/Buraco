from abc import ABC, abstractmethod
from typing import Optional

class IPlayerRepository(ABC):
    @abstractmethod
    def player_exists(self, player_id: int) -> bool:
        pass

class IMatchRepository(ABC):
    @abstractmethod
    def create_match(self, player1_id: int, player2_id: int) -> Optional[int]:
        pass
