import json
from utils.utils import JsonLib

from flask import Blueprint, request
from flask_restful import Api, Resource

import settings as app_settings
from schemas import GetSingleJsonFileSchema

blueprint = Blueprint('read_files_api', __name__)
api = Api(blueprint)


class ReadFile(Resource):

    @app_settings.login_required()
    def post(self, **kwargs):
        try:
            args = GetSingleJsonFileSchema().load(request.json)
        except Exception as e:
            return app_settings.error_response(e.args[0], 400), 400
        script = JsonLib()
        try:
            data = script.read_json_file(args.get("filepath"))
            return data
        except json.decoder.JSONDecodeError as e:
            return str(e)


api.add_resource(ReadFile, "/api/v1/read-single-json-file")
