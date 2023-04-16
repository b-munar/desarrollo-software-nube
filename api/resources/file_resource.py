from flask_restful import Resource

from db import db
from utils import authenticate
from models import File as FileModel
from flask import send_from_directory
from schemas import TaskSchema

class File(Resource):
    method_decorators = [authenticate]
    def get(self, id_file, **kwargs):
        schema = TaskSchema()
        file = FileModel.query.get_or_404(id_file)
        task = schema.dump(file.tasks[0])
        if task['status']:
            return send_from_directory(file.dir, file.name.rsplit('.', 1)[0] + '.' + str(task['type_task']).lower(), as_attachment=True)
        else:
            return send_from_directory(file.dir, file.name, as_attachment=True)