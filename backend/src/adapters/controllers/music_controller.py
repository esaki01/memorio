from flask import Blueprint, request

from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import (
    handle_validation_error,
    handle_unexpected_error,
    handle_success,
)
from src.usecases.music.dto.get_recommended_request import GetRecommendedRequest
from src.usecases.music.dto.get_trending_request import GetTrendingRequest
from src.usecases.music.dto.search_lyric_request import SearchLyricRequest
from src.usecases.music.interactors.get_recommended_interactor import (
    GetRecommendedInteractor,
)
from src.usecases.music.interactors.get_trending_interactor import GetTrendingInteractor
from src.usecases.music.interactors.search_lyric_interactor import SearchLyricInteractor

music = Blueprint("music", __name__, url_prefix="/music")


@music.route("/lyric/artist-song/search", methods=["GET"])
def artist_song_search():
    if request.method == "GET":
        artist = request.args.get("artist")
        song = request.args.get("song")

        try:
            sl_request = SearchLyricRequest(artist, song)
        except ValidationError as e:
            return handle_validation_error(e)

        sl_interactor = SearchLyricInteractor()

        try:
            sl_response = sl_interactor.search_by_artist_song(sl_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(sl_response)


@music.route("/lyric/artist/search", methods=["GET"])
def artist_search():
    if request.method == "GET":
        artist = request.args.get("artist")
        song = request.args.get("song")

        try:
            sl_request = SearchLyricRequest(artist, song)
        except ValidationError as e:
            return handle_validation_error(e)

        sl_interactor = SearchLyricInteractor()

        try:
            sl_response = sl_interactor.search_by_artist(sl_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(sl_response)


@music.route("/lyric/song/search", methods=["GET"])
def song_search():
    if request.method == "GET":
        artist = request.args.get("artist")
        song = request.args.get("song")

        try:
            sl_request = SearchLyricRequest(artist, song)
        except ValidationError as e:
            return handle_validation_error(e)

        sl_interactor = SearchLyricInteractor()

        try:
            sl_response = sl_interactor.search_by_song(sl_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(sl_response)


@music.route("/trending/list", methods=["GET"])
def trending_list():
    if request.method == "GET":
        limit = request.args.get("limit")
        offset = request.args.get("offset")

        try:
            gt_request = GetTrendingRequest(limit, offset)
        except ValidationError as e:
            return handle_validation_error(e)

        gt_interactor = GetTrendingInteractor()

        try:
            gt_response = gt_interactor.handle(gt_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(gt_response)


@music.route("/recommended/list", methods=["GET"])
def recommended_list():
    if request.method == "GET":
        limit = request.args.get("limit")
        offset = request.args.get("offset")

        try:
            gr_request = GetRecommendedRequest(limit, offset)
        except ValidationError as e:
            return handle_validation_error(e)

        gr_interactor = GetRecommendedInteractor()

        try:
            gr_response = gr_interactor.handle(gr_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(gr_response)
