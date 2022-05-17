import os

from flask import Blueprint
from flask_restful import Api, Resource

import settings as app_settings

blueprint = Blueprint('about_api', __name__)
api = Api(blueprint)


class About(Resource):

    def get(self, **kwargs):
        return {"info": "API is working fine."}


api.add_resource(About, "/api/v1/about")
