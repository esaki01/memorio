import requests
from bs4 import BeautifulSoup

from src.exception.error import UnexpectedError
from src.usecases.word.dto.get_pronunciation_request import GetPronunciationRequest
from src.usecases.word.dto.get_pronunciation_response import GetPronunciationResponse
from src.usecases.word.get_pronunciation_usecase import GetPronunciationUseCase


class GetPronunciationInteractor(GetPronunciationUseCase):
    WEBLIO_SITE_URL = 'https://ejje.weblio.jp/'

    def handle(self, request: GetPronunciationRequest) -> GetPronunciationResponse:
        response = requests.get(f'{self.WEBLIO_SITE_URL}/content/{request.keyword}')

        if response:
            soup = BeautifulSoup(response.text, 'lxml')
            phonetic_tag = soup.select('span.phoneticEjjeDesc')
        else:
            phonetic_tag = None

        if phonetic_tag:
            return GetPronunciationResponse(phonetic_tag[-1].string)
        else:
            raise UnexpectedError(f'Pronunciation of {request.keyword} is not found.')
