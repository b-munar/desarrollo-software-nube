from flask_restful import Resource
from utils import authenticate
from cloud_db.models import File as FileModel
from flask import send_from_directory
from cloud_db.schemas import TaskSchema
from database import Session

class File(Resource):
    method_decorators = [authenticate]
    def get(self, id_file, **kwargs):
        schema = TaskSchema()
        session = Session()
        file = session.query(FileModel).get(id_file)
        task = schema.dump(file.tasks[0])
        session.close()
        if task['status']:
            return send_from_directory(file.dir, file.name.rsplit('.', 1)[0] + '.' + str(task['type_task']).lower(), as_attachment=True)
        else:
            return send_from_directory(file.dir, file.name, as_attachment=True)