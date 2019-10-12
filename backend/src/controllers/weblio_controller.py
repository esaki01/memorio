from flask import Blueprint, request

weblio = Blueprint('weblio', __name__, url_prefix='/weblio')


@weblio.route('/search', methods=['GET'])
def index():
    if request.method == 'GET':
        word = request.args.get('word')

        if word:
            return word + '!'
