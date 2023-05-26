import jwt
from datetime import datetime, timedelta
from config import Config
from flask import request
from flask_restful import Resource
from cloud_db.schemas import UserSchema
from cloud_db.models import User

from database import Session

class Signin(Resource):
    def post(self):
        user_schema = UserSchema()
        user_schema_dump = user_schema.dump(request.get_json())
        # try:
        if 'username' in user_schema_dump:
            #user = User.query.filter_by(username=user_schema_dump['username']).first()
            session = Session()
            user  = session.query(User).filter(User.username==user_schema_dump['username']).first()
            session.close()
        elif 'email' in user_schema_dump:
            #user = User.query.filter_by(email=user_schema_dump['email']).first()
            session = Session()
            user  = session.query(User).filter(User.email==user_schema_dump['email']).first()
            session.close()
        else:
            return {
                'status': 'fail',
                'message': 'Send a valid username or email'
            }, 400
        if user.check_password(user_schema_dump['password']):
            auth_token = jwt.encode({
                        'user_id': user.id,
                        'exp' : datetime.utcnow() + timedelta(minutes = 30)
                    }, Config.SECRET_KEY, algorithm="HS256")
            return {'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token
                }, 200
        else:
            raise Exception()

        # except:
        #     return {
        #         'status': 'fail',
        #         'message': 'Try again'
        #     }, 500
