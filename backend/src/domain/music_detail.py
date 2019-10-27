import dataclasses

from src.domain.music import Music


@dataclasses.dataclass
class MusicDetail:
    music: Music
    lyric: str
