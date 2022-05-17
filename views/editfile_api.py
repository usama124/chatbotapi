import json
from utils.utils import JsonLib

from flask import Blueprint, request
from flask_restful import Api, Resource

import settings as app_settings
from schemas import EditFileSchema

blueprint = Blueprint('edit_files_api', __name__)
api = Api(blueprint)


class EditFile(Resource):

    @app_settings.login_required()
    def post(self, **kwargs):
        try:
            args = EditFileSchema().load(request.json)
        except Exception as e:
            return app_settings.error_response(e.args[0], 400), 400

        try:
            old_tag = args.get("old_tag")
            edited_tag = args.get("edited_tag")
            filepath = args.get("filepath")

            print(old_tag, edited_tag, filepath)

            old_tag = json.loads(old_tag)
            edited_tag = json.loads(edited_tag)
            script = JsonLib()
            current_data = script.read_json_file(filepath)

            for index, item in enumerate(current_data):
                if item['tag'] == old_tag['tag']:
                    search_index = index

            current_data[search_index].update(
                {
                    "tag": edited_tag['tag'],
                    "patterns": edited_tag['patterns'],
                    "responses": edited_tag['responses'],
                    "context": edited_tag['context']

                }
            )
            script.write_json_file(filepath, current_data)
            return script.read_json_file(filepath)
        except Exception as e:
            return app_settings.error_response(str(e), 500), 500


api.add_resource(EditFile, "/api/v1/edit-file")
