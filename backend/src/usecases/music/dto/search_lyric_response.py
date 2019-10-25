import dataclasses


@dataclasses.dataclass
class SearchLyricResponse:
    artist: str
    song: str
    image_url: str
    lyric: str
