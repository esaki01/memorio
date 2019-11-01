from abc import ABCMeta, abstractmethod

from src.usecases.trending.dtos.get_trending_request import GetTrendingRequest
from src.usecases.trending.dtos.get_trending_response import GetTrendingResponse


class GetTrendingUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: GetTrendingRequest) -> GetTrendingResponse:
        raise NotImplementedError()
