import logging
from typing import Optional

import requests
from bs4 import BeautifulSoup

from src.adapters.repositories.word_repository import WordRepository
from src.exception.error import UnexpectedError
from src.usecases.word.dto.get_pronunciation_request import GetPronunciationRequest
from src.usecases.word.dto.get_pronunciation_response import GetPronunciationResponse
from src.usecases.word.get_pronunciation_usecase import GetPronunciationUseCase


class GetPronunciationInteractor(GetPronunciationUseCase):
    _WEBLIO_SITE_URL = "https://ejje.weblio.jp/"

    def __init__(self, word_repo: WordRepository):
        self._word_repo = word_repo

    def handle(self, request: GetPronunciationRequest) -> GetPronunciationResponse:
        phonetic_symbol = self._get_pronunciation_from_repository(request.keyword)

        if not phonetic_symbol:
            phonetic_symbol = self._get_pronunciation_from_weblio(request.keyword)

        if not phonetic_symbol:
            raise UnexpectedError(f"Pronunciation of {request.keyword} is not found.")

        return GetPronunciationResponse(phonetic_symbol)

    def _get_pronunciation_from_repository(self, keyword: str) -> Optional[str]:
        word = self._word_repo.find_by_id(keyword)

        if word:
            return word.phonetic_symbol
        else:
            logging.info(f"Pronunciation of {keyword} is not found.")
            return None

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
