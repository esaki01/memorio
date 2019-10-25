import dataclasses


@dataclasses.dataclass
class GetTrendingResponse:
    title: str
    external_url: str
