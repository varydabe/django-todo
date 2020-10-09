from functools import wraps
from todoproject.jwt import JWTAuth
from todoproject.response import Response


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            decode(args[0].headers.get('Authorization'))
        except Exception:
            return Response.unauthorized(message='Unauthorized!')
        return fn(*args, **kwargs)
    return wrapper


def decode(token):
    token = str(token).split(' ')
    return JWTAuth().decode(token[1])
