import dataclasses

from src.exception.error import ValidationError


@dataclasses.dataclass
class GetPronunciationRequest:
    keyword: str

    def __post_init__(self):
        if not self.keyword:
            raise ValidationError("keyword is required.")
