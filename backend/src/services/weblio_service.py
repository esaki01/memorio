from typing import Optional

import requests
from bs4 import BeautifulSoup

from src.models.word_definition import WordDefinition


class WeblioService:
    WEBLIO_SITE_URL = 'https://ejje.weblio.jp/'

    def get_word_definition(self, keyword: str) -> Optional[WordDefinition]:

        response = requests.get(f'{self.WEBLIO_SITE_URL}/content/{keyword}')

        if not response:
            return

        soup = BeautifulSoup(response.text, 'lxml')

        fields = {
            'word': soup.find(id='h1Query'),
            'meaning': soup.select_one('td.content-explanation'),
            'phonetic_symbol': soup.select_one('span.phoneticEjjeDesc'),
            'audio_url': soup.select_one("audio.contentAudio")
        }

        for v in fields.values():
            if not v:
                break
        else:
            return WordDefinition(
                word=fields['word'].string,
                meaning=fields['meaning'].string,
                phonetic_symbol=fields['phonetic_symbol'].string,
                audio_url=fields['audio_url'].contents[0].attrs['src'])
