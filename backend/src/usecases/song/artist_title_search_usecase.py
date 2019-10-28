from abc import ABCMeta, abstractmethod

from src.usecases.song.dtos.artist_title_search_request import ArtistTitleSearchRequest
from src.usecases.song.dtos.artist_title_search_response import ArtistTitleSearchResponse


class ArtistTitleSearchUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, request: ArtistTitleSearchRequest) -> ArtistTitleSearchResponse:
        raise NotImplementedError()
