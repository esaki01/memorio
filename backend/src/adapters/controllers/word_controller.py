from flask import Blueprint, request

from src.adapters.repositories.impl.bigquery_repository import BigQueryRepository
from src.adapters.repositories.word_repository import WordRepository
from src.exception.error import ValidationError
from src.exception.handler import handle_validation_error, handle_success
from src.usecases.word.dto.get_pronunciation_request import GetPronunciationRequest
from src.usecases.word.interactors.get_pronunciation_interactor import GetPronunciationInteractor

word = Blueprint("word", __name__, url_prefix="/word")


@word.route("/pronunciation/search", methods=["GET"])
def pronunciation_search():
    if request.method == "GET":
        lyric = request.args.get("lyric")

        try:
            gp_request = GetPronunciationRequest(lyric)
        except ValidationError as e:
            return handle_validation_error(e)

        word_repo: WordRepository = BigQueryRepository()

        gp_interactor = GetPronunciationInteractor(word_repo)

        gp_response = gp_interactor.handle(gp_request)

        return handle_success(gp_response)
