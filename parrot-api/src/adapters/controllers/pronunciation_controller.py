from flask import Blueprint, request

from src.adapters.repositories.impl.word_repository_impl import WordRepositoryImpl
from src.adapters.repositories.word_repository import WordRepository
from src.exception.error import ValidationError
from src.exception.handler import handle_validation_error, handle_success
from src.usecases.pronunciation.dtos.get_pronunciation_request import GetPronunciationRequest
from src.usecases.pronunciation.interactors.get_pronunciation_interactor import GetPronunciationInteractor

pronunciation = Blueprint("pronunciation", __name__, url_prefix="/pronunciation")


@pronunciation.route("/search", methods=["GET"])
def pronunciation_search():
    if request.method == "GET":
        words = request.args.get("words")

        try:
            gp_request = GetPronunciationRequest(words)
        except ValidationError as e:
            return handle_validation_error(e)

        word_repo: WordRepository = WordRepositoryImpl()

        gp_interactor = GetPronunciationInteractor(word_repo)

        gp_response = gp_interactor.handle(gp_request)

        return handle_success(gp_response)
