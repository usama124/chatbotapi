from flask import Blueprint, request
from flask_restful import Api, Resource

import settings as app_settings
from schemas import AddNewTagSchema
from utils.utils import JsonLib

blueprint = Blueprint('add_tags_api', __name__)
api = Api(blueprint)


class AddTag(Resource):

    @app_settings.login_required()
    def post(self, **kwargs):
        try:
            args = AddNewTagSchema().load(request.json)
        except Exception as e:
            return app_settings.error_response(str(e.args), 400), 400

        try:
            filepath = args.get("filepath")

            del args["filepath"]

            script = JsonLib()
            fresh_data = script.add_tag_to_json_file(
                filepath=filepath, new_tag=args)

            return fresh_data
        except Exception as e:
            return app_settings.error_response(str(e.args), 500), 500


api.add_resource(AddTag, "/api/v1/add_new_tag")
