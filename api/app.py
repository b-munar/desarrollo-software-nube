from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from db import db
from resources import Signin, Signup, Task, Tasks

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Signup, '/api/signup')
api.add_resource(Signin, '/api/signin')
api.add_resource(Tasks, '/api/tasks')
api.add_resource(Task, '/api/tasks/<int:id_task>')

if __name__ == '__main__':
    app.run(debug=True)
