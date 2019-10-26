import dataclasses
from typing import List


@dataclasses.dataclass
class GetPronunciationResponse:
    phonetic_symbols: List[str]
