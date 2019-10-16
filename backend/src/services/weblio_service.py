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
            'word': soup.find(id='h1Query').string,
            'meaning': soup.select_one('td.content-explanation').string,
            'phonetic_symbol': soup.select('span.phoneticEjjeDesc'),
            'audio_url': soup.select_one("audio.contentAudio")
        }

        if fields['word'] and fields['meaning']:
            return WordDefinition(
                word=fields['word'],
                meaning=fields['meaning'],
                phonetic_symbol=fields['phonetic_symbol'][-1].string if fields['phonetic_symbol'] else None,
                audio_url=fields['audio_url'].contents[0].attrs['src'])
