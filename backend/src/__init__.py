from flask import Flask
from flask_cors import CORS

from src.controllers.weblio_controller import weblio


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(weblio)

    # TODO add production origin
    CORS(app, origins=['http://localhost:8080/*', 'https://frontend-n2zzz72gsq-uc.a.run.app'])

    return app
