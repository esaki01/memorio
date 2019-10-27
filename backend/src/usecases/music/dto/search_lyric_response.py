import dataclasses
from typing import List

from src.domain.music_detail import MusicDetail


@dataclasses.dataclass
class SearchLyricResponse:
    music_details: List[MusicDetail]
