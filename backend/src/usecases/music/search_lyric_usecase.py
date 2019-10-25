from abc import ABCMeta, abstractmethod
from typing import List

from src.usecases.music.dto.search_lyric_request import SearchLyricRequest
from src.usecases.music.dto.search_lyric_response import SearchLyricResponse


class SearchLyricUseCase(metaclass=ABCMeta):

    @abstractmethod
    def search_by_artist_song(self, request: SearchLyricRequest) -> List[SearchLyricResponse]:
        raise NotImplementedError()

    @abstractmethod
    def search_by_artist(self, request: SearchLyricRequest) -> List[SearchLyricResponse]:
        raise NotImplementedError()

    @abstractmethod
    def search_by_song(self, request: SearchLyricRequest) -> List[SearchLyricResponse]:
        raise NotImplementedError()
