import dataclasses


@dataclasses.dataclass
class Word:
    id: str
    phonetic_symbol: str
