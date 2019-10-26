from typing import Optional

from google.cloud import bigquery

from src.adapters.repositories.word_repository import WordRepository
from src.domain.word import Word


class BigQueryRepository(WordRepository):
    def __init__(self):
        self._client = bigquery.Client()

    def find_by_id(self, id: str) -> Optional[Word]:
        query = f"SELECT id, phonetic_symbol FROM `parrot.word` WHERE id = '{id}'"
        results = list(self._client.query(query, location="US"))

        if results and len(results) >= 1:
            return Word(**results[0])
        else:
            return None
