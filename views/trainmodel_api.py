import time

from flask import Blueprint, request
from flask_restful import Api, Resource

import settings as app_settings
from schemas import GetSingleJsonFileSchema

blueprint = Blueprint('train_model_api', __name__)
api = Api(blueprint)


def train_model_function(filepath):
    time.sleep(10)
    return "Model Trained"


class TrainModel(Resource):

    @app_settings.login_required()
    def post(self, **kwargs):
        try:
            args = GetSingleJsonFileSchema().load(request.json)
        except Exception as e:
            return app_settings.error_response(str(e.args), 400), 400

        try:
            filepath = args.get("filepath")

            background.add_task(train_model_function, filepath)

            return "Your model is being trained in the bacground"
        except Exception as e:
            return app_settings.error_response(str(e.args), 500), 500


api.add_resource(TrainModel, "/api/v1/train-model")
