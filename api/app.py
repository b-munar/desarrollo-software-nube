from flask import Flask
from flask_restful import Api
from config import Config
from resources import Signup, Signin ,Tasks, Task, File

def create_app(config_filename=Config):
    app = Flask(__name__)
    # app.config.from_object(config_filename)
    
    
    api = Api(app)
    api.add_resource(Signup, '/api/auth/signup')
    api.add_resource(Signin, '/api/auth/login')
    api.add_resource(Tasks, '/api/tasks')
    api.add_resource(Task, '/api/tasks/<int:id_task>')
    api.add_resource(File, '/api/files/<int:id_file>')

    return app
