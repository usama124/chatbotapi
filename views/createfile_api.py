from flask import Blueprint, request
from flask_restful import Api, Resource

import settings as app_settings
from schemas import CreateNewJSONFileSchema
from utils.utils import JsonLib

blueprint = Blueprint('create_file_api', __name__)
api = Api(blueprint)


class CreateFile(Resource):

    @app_settings.login_required()
    def post(self, **kwargs):
        try:
            args = CreateNewJSONFileSchema().load(request.json)
        except Exception as e:
            return app_settings.error_response(str(e.args), 400), 400

        try:
            script = JsonLib()
            is_folder_created = script.create_new_folder(args.get("foldername"))

            msg = ""
            if is_folder_created:
                msg = "Folder Created, "
            is_file_created = script.create_json_file(args.get("foldername"), args.get("filename"))
            if is_file_created:
                msg = msg + "File Created, "

            return msg
        except Exception as e:
            return app_settings.error_response(str(e.args), 500), 500


api.add_resource(CreateFile, "/api/v1/create-new-json-file")
