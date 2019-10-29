from abc import ABCMeta, abstractmethod

from src.usecases.pronunciation.dtos.get_pronunciation_request import GetPronunciationRequest
from src.usecases.pronunciation.dtos.get_pronunciation_response import GetPronunciationResponse


class GetPronunciationUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetPronunciationRequest) -> GetPronunciationResponse:
        raise NotImplementedError()
