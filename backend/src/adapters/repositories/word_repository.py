from abc import ABCMeta, abstractmethod

from src.domain.word import Word
from typing import Optional, List


class WordRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_ids(self, ids: List[str]) -> List[Optional[Word]]:
        raise NotImplementedError()
