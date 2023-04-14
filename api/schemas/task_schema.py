from marshmallow import Schema, fields
from models import TypeTask

class TaskSchema(Schema):
    id = fields.Int()
    status = fields.Bool()
    time_stamp = fields.DateTime(format='timestamp')
    file_id = fields.Int()
    user_id = fields.Int()
    type_task = fields.Function(lambda obj: TypeTask(obj.type_task).name)