from flask import Flask
from flask_cors import CORS

from src.controllers.genius_controller import genius
from src.controllers.weblio_controller import weblio


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('../config.py', silent=True)

    app.register_blueprint(weblio)
    app.register_blueprint(genius)

    CORS(app, origins=['http://localhost:8080/*', 'https://frontend-n2zzz72gsq-uc.a.run.app'])

    return app
