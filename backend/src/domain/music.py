import dataclasses


@dataclasses.dataclass
class Music:
    artist: str
    song: str
    image_url: str
