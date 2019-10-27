from typing import List

import spotipy
from flask import current_app
from spotipy.oauth2 import SpotifyClientCredentials

from src.exception.error import UnexpectedError
from src.usecases.music.dto.get_recommended_request import GetRecommendedRequest
from src.usecases.music.dto.get_recommended_response import GetRecommendedResponse
from src.usecases.music.get_recommended_usecase import GetRecommendedUseCase


class GetRecommendedInteractor(GetRecommendedUseCase):
    def __init__(self):
        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
            current_app.config["SPOTIFY_CLIENT_ID"], current_app.config["SPOTIFY_CLIENT_SECRET"]
        )

        self._spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def handle(self, request: GetRecommendedRequest) -> List[GetRecommendedResponse]:
        results = self._spotify.new_releases(limit=request.limit, offset=request.offset)["albums"]["items"]

        if not results:
            raise UnexpectedError("Not found recommended.")

        return [
            GetRecommendedResponse(
                r["artists"][0]["name"], r["name"], r["images"][0]["url"], r["external_urls"]["spotify"]
            )
            for r in results
        ]
