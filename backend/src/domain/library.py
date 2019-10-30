import dataclasses
from typing import List

from src.domain.song import Song


@dataclasses.dataclass
class Library:
    user_id: str
    songs: List[Song]
