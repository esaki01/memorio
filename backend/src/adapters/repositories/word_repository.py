from abc import ABCMeta, abstractmethod

from src.domain.word import Word
from typing import Optional


class WordRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Word]:
        raise NotImplementedError()
