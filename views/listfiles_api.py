import os

from flask import Blueprint
from flask_restful import Api, Resource

import settings as app_settings

blueprint = Blueprint('list_files_api', __name__)
api = Api(blueprint)


class ListFiles(Resource):

    @app_settings.login_required()
    def get(self, **kwargs):
        filelist = []

        for root, dirs, files in os.walk(app_settings.folder_path_for_root):
            for file in files:
                if ".json" in file:
                    filelist.append(os.path.join(root, file))
        return filelist


api.add_resource(ListFiles, "/api/v1/list-json-files")
