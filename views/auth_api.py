from datetime import timedelta

from flask import request, Blueprint
from flask_restful import Api, Resource
from marshmallow import EXCLUDE
from passlib.context import CryptContext

import settings as app_settings
from models import User, db
from schemas import UserRegisterSchema, UserLoginSchema

user_reg_schema = UserRegisterSchema(unknown=EXCLUDE)
user_login_schema = UserLoginSchema(unknown=EXCLUDE)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

blueprint = Blueprint('auth_api', __name__)
api = Api(blueprint)


class UserRegister(Resource):

    def post(self, **kwargs):
        try:
            args = user_reg_schema.load(request.json)
        except Exception as e:
            return app_settings.error_response(e.args[0], 400), 400
        password = bcrypt_context.hash(args.get("password"))
        user = User(name=args.get("name"), username=args.get("username"), password=password)
        db.session.add(user)
        db.session.commit()
        return user.as_dict(), 201


class UserLogin(Resource):

    def post(self, **kwargs):
        args = user_login_schema.load(request.json)
        user = User.query.filter_by(username=args.get("username")).first()
        if bcrypt_context.verify(args.get("password"), user.password):
            if not user.is_admin:
                return app_settings.error_response("User not authorized.", 403), 403
            token_expires = timedelta(minutes=app_settings.TOKEN_EXPIRES_AFTER)
            token = app_settings.create_access_token(
                user.username, user.id, expires_delta=token_expires)
            return {
                "token": token
            }
        else:
            return app_settings.error_response("User not authenticated.", 401), 401


api.add_resource(UserRegister, "/api/v1/register")
api.add_resource(UserLogin, "/api/v1/login")
