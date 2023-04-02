from marshmallow import Schema, fields

class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    email = fields.Str()