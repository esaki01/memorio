import logging
import re
from typing import Optional, List

import requests
from bs4 import BeautifulSoup

from src.adapters.repositories.word_repository import WordRepository
from src.domain.word import Word
from src.usecases.word.dto.get_pronunciation_request import GetPronunciationRequest
from src.usecases.word.dto.get_pronunciation_response import GetPronunciationResponse
from src.usecases.word.get_pronunciation_usecase import GetPronunciationUseCase


class GetPronunciationInteractor(GetPronunciationUseCase):
    _WEBLIO_SITE_URL = "https://ejje.weblio.jp/"

    def __init__(self, word_repo: WordRepository):
        self._word_repo = word_repo

    def handle(self, request: GetPronunciationRequest) -> GetPronunciationResponse:
        keywords = [re.sub("['\",.?+:;*!#$%&]", "", k.lower()) for k in request.keyword.split()]
        words = self._get_pronunciation_from_repository(keywords)
        words_map = {w.id: w.phonetic_symbol for w in words if w}

        phonetic_symbols = [words_map.get(k) for k in keywords]

        # TODO Access weblio
        # if not phonetic_symbol:
        #     phonetic_symbol = self._get_pronunciation_from_weblio(k)

        return GetPronunciationResponse(phonetic_symbols)

    def _get_pronunciation_from_repository(
            self, keywords: List[str]
    ) -> List[Optional[Word]]:
        return self._word_repo.find_by_ids(keywords)

    def _get_pronunciation_from_weblio(self, keyword: str) -> Optional[str]:
        response = requests.get(f"{self._WEBLIO_SITE_URL}/content/{keyword}")

        if response:
            soup = BeautifulSoup(response.text, "lxml")
            phonetic_tag = soup.select("span.phoneticEjjeDesc")
        else:
            phonetic_tag = None

        if phonetic_tag:
            return phonetic_tag[-1].string
        else:
            logging.info(f"Pronunciation of {keyword} is not found.")
            return None
