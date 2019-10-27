import dataclasses

from src.exception.error import ValidationError


@dataclasses.dataclass
class GetPronunciationRequest:
    lyric: str

    def __post_init__(self):
        if not self.lyric:
            raise ValidationError("lyric is required.")
