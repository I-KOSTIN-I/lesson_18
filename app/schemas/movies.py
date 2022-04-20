from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int(required=True)
    rating = fields.Int()
