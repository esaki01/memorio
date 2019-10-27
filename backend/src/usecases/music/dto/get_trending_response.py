import dataclasses
from typing import List

from src.domain.trending import Trending


@dataclasses.dataclass
class GetTrendingResponse:
    trending: List[Trending]
