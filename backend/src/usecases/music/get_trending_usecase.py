from abc import ABCMeta, abstractmethod

from src.usecases.music.dto.get_trending_request import GetTrendingRequest
from src.usecases.music.dto.get_trending_response import GetTrendingResponse


class GetTrendingUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetTrendingRequest) -> GetTrendingResponse:
        raise NotImplementedError()
