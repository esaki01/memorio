import dataclasses

from src.domain.music import Music


@dataclasses.dataclass
class Recommended:
    music: Music
    external_url: str
