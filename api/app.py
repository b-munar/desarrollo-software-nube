from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from db import db
from resources import Signin, Signup, Task, Tasks, File

def create_app(config_filename=Config):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    db.init_app(app)
    Migrate(app, db)
    
    api = Api(app)
    api.add_resource(Signup, '/api/signup')
    api.add_resource(Signin, '/api/signin')
    api.add_resource(Tasks, '/api/tasks')
    api.add_resource(Task, '/api/tasks/<int:id_task>')
    api.add_resource(File, '/api/files/<int:id_file>')

    return app
