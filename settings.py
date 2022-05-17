import os
import uuid
from datetime import datetime, timedelta
from functools import wraps

from flask import request
from jose import jwt
from jose.exceptions import JWTError

DATABASE_URI = "mysql+pymysql://root:temppass123@127.0.0.1:4001/jsonmodifier"
SECRET_KEY = "hiuy7GUI7yIBUi89yilu6k9U8O7ukFO9hhi76kki8N"

ALGORITHM = "HS256"

TOKEN_EXPIRES_AFTER = 60 * 24  # minutes
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

folder_path_for_root = "/home/usama/PycharmProjects/Personal/chatbotapi/trained_models"


def error_response(message: str, code: int):
    return {
        "message": message,
        "code": code,
        "traceId": str(uuid.uuid4())
    }


def create_access_token(username: str, user_id: int, expires_delta):
    encode = {
        "user_id": user_id,
        "sub": username
    }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15 * 10000)
    encode.update({
        "exp": expire
    })
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def login_required():
    def requires_auth_decorator(f):
        @wraps(f)
        def decorated(args, **kwargs):
            try:
                auth = request.headers.get('Authorization', None)
                if not auth or not ' ' in auth:
                    return {'message': 'Token is Required in Header.'}, 401

                token = auth.split(' ')[1]
                if not token:
                    return {'message': 'Token is Required in Header.'}, 401

                # token_content = jwt.decode(token, PUBLIC_KEY, algorithms='RS256')
                token_content = jwt.decode(token, SECRET_KEY, ALGORITHM)

                kwargs.update(token_content)
                kwargs.update({'token': token})
                return f(args, **kwargs)
            except JWTError:
                return {'message': 'Token is invalid.'}, 401
            except Exception as e:
                return {'message': str(e)}, 500

        return decorated

    return requires_auth_decorator
