import dataclasses
from typing import List

from src.domain.recommended import Recommended


@dataclasses.dataclass
class GetRecommendedResponse:
    recommended: List[Recommended]
