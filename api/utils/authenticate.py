from functools import wraps
from flask import request
from config import Config
import jwt
from cloud_db.models import User
from database import Session
def authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            header_authorization = request.headers.get("Authorization")
            if not header_authorization:
                return {
                    'status': 'fail',
                    'message': 'Provide auth token'
                }, 403    

            try:
                auth_token = request.headers.get("Authorization").split(" ")[1]
                data = jwt.decode(auth_token, Config.SECRET_KEY, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return {
                'status': 'fail',
                'message': 'the token expired.'
                }, 403
            except jwt.DecodeError:
                return {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
                }, 403   
            except jwt.InvalidTokenError:
                return {
                'status': 'fail',
                'message': 'Provide auth token or a valid auth token 1.'
                }, 403   
            
            session = Session()
            kwargs["user"] = session.query(User).get(data['user_id'])
            session.close()
            return func(*args, **kwargs)

    return decorated

