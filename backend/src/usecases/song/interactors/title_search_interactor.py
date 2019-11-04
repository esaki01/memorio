import lyricsgenius
from flask import current_app

from src.entities.song import Song
from src.exception.error import UnexpectedError
from src.usecases.song.requests.title_search_request import TitleSearchRequest
from src.usecases.song.responses.title_search_response import TitleSearchResponse
from src.usecases.song.title_search_usecase import TitleSearchUseCase


class TitleSearchInteractor(TitleSearchUseCase):
    def __init__(self):
        self._genius = lyricsgenius.Genius(current_app.config["GENIUS_TOKEN"])
        self._genius.verbose = False
        self._genius.remove_section_headers = True
        self._genius.skip_non_songs = False
        self._genius.excluded_terms = ["(Remix)", "(Live)"]

    def handle(self, request: TitleSearchRequest) -> TitleSearchResponse:
        song = self._genius.search_song(request.title, get_full_info=False)

        if not song:
            raise UnexpectedError(f"Not found {request.title}.")

        songs = [
            Song(artist=song.artist, title=song.title, lyrics=song.lyrics, jacket_image_url=song.song_art_image_url)
        ]

        return TitleSearchResponse(songs)
