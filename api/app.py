from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config

from db import db
from resources import Signin, Signup, Task

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Signup, '/signup')
api.add_resource(Signin, '/signin')
api.add_resource(Task, '/api/task')

if __name__ == '__main__':
    app.run(debug=True)
