import dataclasses
from typing import Optional

from src.exception.error import ValidationError


@dataclasses.dataclass
class SearchLyricRequest:
    artist: Optional[str]
    song: Optional[str]

    def __post_init__(self):
        if not self.artist and not self.song:
            raise ValidationError('at least artist or song is required.')
