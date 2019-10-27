from flask import Flask
from flask_cors import CORS

from src.adapters.controllers.music_controller import music
from src.adapters.controllers.word_controller import word

config = {"development": "config.DevelopmentConfig", "production": "config.ProductionConfig"}

secrets = "secrets.Secrets"

origins = ["http://localhost:8080/*", "https://frontend-n2zzz72gsq-uc.a.run.app"]


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[app.config.get("ENV", "development")])
    app.config.from_object(secrets)

    app.register_blueprint(music)
    app.register_blueprint(word)

    CORS(app, origins=origins)

    return app
