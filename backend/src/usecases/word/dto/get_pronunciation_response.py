import dataclasses
from typing import Optional


@dataclasses.dataclass
class GetPronunciationResponse:
    phonetic_symbol: Optional[str]
