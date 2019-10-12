from flask import jsonify

from src.models.word_definition import WordDefinition


def handle_invalid_request(msg: str):
    return jsonify({
        'message': f'The request is invalid. {msg}',
        'data': None
    })


def handle_not_found(keyword: str):
    return jsonify({
        'message': f'Sorry, {keyword} is not found.',
        'data': None
    })


def handle_success(keyword: str, word_definition: WordDefinition):
    return jsonify({
        'message': f'{keyword} is found.',
        'data': word_definition.__dict__
    })
