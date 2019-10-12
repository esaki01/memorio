from flask import Blueprint, request

from src.handlers import weblio_handler
from src.services.weblio_service import WeblioService

weblio = Blueprint('weblio', __name__, url_prefix='/weblio')


@weblio.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        keyword = request.args.get('keyword')

        if not keyword:
            return weblio_handler.handle_invalid_request('No keyword param.')

        weblio_service = WeblioService()
        word_definition = weblio_service.get_word_definition(keyword)

        if word_definition:
            return weblio_handler.handle_success(keyword, word_definition)
        else:
            return weblio_handler.handle_not_found(keyword)
