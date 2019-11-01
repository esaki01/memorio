import dataclasses
from typing import List

from src.domain.song import Song


@dataclasses.dataclass
class ArtistSearchResponse:
    songs: List[Song]
