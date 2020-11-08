from typing import Dict, Tuple


from flask import Blueprint
from flask import current_app as app
from flask_restful import Api, Resource


from utils import log_errors

blueprint = Blueprint("user_api", __name__, url_prefix="/api")
api = Api(blueprint)


class UserResourceList(Resource):
    @log_errors
    def get(self) -> Tuple[Dict, int]:
        app.logger.info(f"Endpoint: /api/user GET")
        return {"results": "Endpoint: /api/user GET"}, 200


class UserResource(Resource):
    @log_errors
    def get(self, user_id) -> Tuple[Dict, int]:
        app.logger.info(f"Endpoint: /api/user/{user_id} GET")
        return {"results": "Endpoint: /api/user/{user} GET"}, 200

    @log_errors
    def post(self, user_id) -> Tuple[Dict, int]:
        app.logger.info(f"Endpoint: /api/user/{user_id} POST")
        return {"results": "Endpoint: /api/user/{user} GET"}, 200


api.add_resource(UserResourceList, "/users")
api.add_resource(UserResource, "/users/<user_id>")
