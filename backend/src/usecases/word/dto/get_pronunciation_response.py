import dataclasses
from typing import Optional, List


@dataclasses.dataclass
class GetPronunciationResponse:
    phonetic_symbols: List[Optional[str]]
