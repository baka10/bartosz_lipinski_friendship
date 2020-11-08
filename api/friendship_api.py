from typing import Dict, Tuple


from flask import Blueprint
from flask import current_app as app
from flask_restful import Api, Resource


from utils import log_errors

blueprint = Blueprint("friendship_api", __name__, url_prefix="/api")
api = Api(blueprint)


class FriendshipListResource(Resource):
    @log_errors
    def get(self, from_user, to_user) -> Tuple[Dict, int]:
        app.logger.info(f"Endpoint: /api/friendship/{from_user}/{to_user} GET")
        return {"results": f"Endpoint: /api/friendship GET"}, 200


class FriendshipResource(Resource):
    @log_errors
    def post(self) -> Tuple[Dict, int]:
        app.logger.info(f"Endpoint: /api/friendship POST")
        return {"results": f"Endpoint: /api/friendship POST"}, 200

    @log_errors
    def delete(self) -> Tuple[Dict, int]:
        app.logger.info(f"Endpoint: /api/friendship DELETE")
        return {"results": "Endpoint: /api/friendship DELETE"}, 200


api.add_resource(FriendshipListResource, "/friendships/<from_user>/<to_user>")
api.add_resource(FriendshipResource, "/friendships")
