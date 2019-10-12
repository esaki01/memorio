import dataclasses


@dataclasses.dataclass
class WordDefinition:
    word: str  # 単語
    meaning: str  # 単語の主な意味
    phonetic_symbol: str  # 発音記号
    audio_url: str  # 音声ファイルのURL
