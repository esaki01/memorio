from flask import Blueprint, request

from src.adapters.repositories.impl.bigquery_repository import BigQueryRepository
from src.adapters.repositories.word_repository import WordRepository
from src.exception.error import ValidationError, UnexpectedError
from src.exception.handler import (
    handle_validation_error,
    handle_unexpected_error,
    handle_success,
)
from src.usecases.word.dto.get_pronunciation_request import GetPronunciationRequest
from src.usecases.word.interactors.get_pronunciation_interactor import (
    GetPronunciationInteractor,
)

word = Blueprint("word", __name__, url_prefix="/word")


@word.route("/pronunciation/search", methods=["GET"])
def pronunciation_search():
    if request.method == "GET":
        keyword = request.args.get("keyword")

        try:
            gp_request = GetPronunciationRequest(keyword)
        except ValidationError as e:
            return handle_validation_error(e)

        word_repo: WordRepository = BigQueryRepository()

        gp_interactor = GetPronunciationInteractor(word_repo)

        try:
            gp_response = gp_interactor.handle(gp_request)
        except UnexpectedError as e:
            return handle_unexpected_error(e)

        return handle_success(gp_response.__dict__)
