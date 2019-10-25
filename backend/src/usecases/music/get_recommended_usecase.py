from abc import ABCMeta, abstractmethod
from typing import List

from src.usecases.music.dto.get_recommended_request import GetRecommendedRequest
from src.usecases.music.dto.get_recommended_response import GetRecommendedResponse


class GetRecommendedUseCase(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, request: GetRecommendedRequest) -> List[GetRecommendedResponse]:
        raise NotImplementedError()
