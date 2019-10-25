import dataclasses


@dataclasses.dataclass
class GetRecommendedResponse:
    artist: str
    song: str
    image_url: str
    external_url: str
