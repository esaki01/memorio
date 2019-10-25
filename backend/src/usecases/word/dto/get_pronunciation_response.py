import dataclasses


@dataclasses.dataclass
class GetPronunciationResponse:
    phonetic_symbol: str
