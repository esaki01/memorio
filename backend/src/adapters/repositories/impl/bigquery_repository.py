from typing import Optional, List

from google.cloud import bigquery

from src.adapters.repositories.word_repository import WordRepository
from src.domain.word import Word


class BigQueryRepository(WordRepository):
    def __init__(self):
        self._client = bigquery.Client()

    def find_by_ids(self, ids: List[str]) -> List[Optional[Word]]:
        query_ids = ", ".join([f"'{i}'" for i in ids])
        query = f"SELECT id, phonetic_symbol FROM `parrot.word` WHERE id in ({query_ids})"
        results = list(self._client.query(query, location="US"))

        return [Word(**r) for r in results]
