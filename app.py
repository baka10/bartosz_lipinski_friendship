from typing import Any

from flask import Flask, jsonify

from werkzeug.exceptions import HTTPException, default_exceptions

from api import users_api, friendship_api


def make_json_error(ex: Exception) -> jsonify:  # pragma: no cover
    """
    All error responses that you don't specifically
    manage yourself will have application/json content
    type, and will contain JSON like this (just an example):

    { 'message': '405: Method Not Allowed' }
    """

    response = jsonify(message=str(ex))
    response.status_code = ex.code if isinstance(ex, HTTPException) else 500
    return response


def create_app(config: Any) -> Flask:
    app = Flask(f"bartosz-lipinski-friendship-{config.ENV}")

    with app.app_context():
        app.secret_key = config.SECRET_KEY
        app.config.from_object(config)

        for code in default_exceptions.keys():
            # make response always in JSON
            app.register_error_handler(code, make_json_error)

    for api in [users_api, friendship_api]:
        app.register_blueprint(api.blueprint)

    return app
