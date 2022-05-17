from marshmallow import Schema, fields, validate


class UserRegisterSchema(Schema):
    """ Marshmallow schema for Entity """
    name = fields.Str(required=True, allow_none=False,
                      validate=validate.Length(min=1, max=200, error="it must be between 1 and 200")
                      )
    username = fields.Str(required=True, allow_none=False,
                          validate=validate.Length(min=1, max=30, error="it must be between 1 and 30"))
    password = fields.Str(required=True, allow_none=False,
                          validate=validate.Length(min=1, error="it must be between 1 and 200")
                          )
    is_admin = fields.Bool(required=False, allow_none=True)


class UserLoginSchema(Schema):
    """ Marshmallow schema for Entity """
    username = fields.Str(required=True, allow_none=False,
                          validate=validate.Length(min=1, max=30, error="it must be between 1 and 30"))
    password = fields.Str(required=True, allow_none=False,
                          validate=validate.Length(min=1, max=200, error="it must be between 1 and 200"))


class GetSingleJsonFileSchema(Schema):
    filepath = fields.Str(required=True)


class EditFileSchema(Schema):
    edited_tag = fields.Str(required=True)
    old_tag = fields.Str(required=True)
    filepath = fields.Str(required=True)


class AddNewTagSchema(Schema):
    tag = fields.Str(required=True)
    patterns = fields.List(fields.String(), required=True)
    responses = fields.List(fields.String(), required=True)
    context = fields.List(fields.String(), required=True)
    filepath = fields.Str(required=True)


class CreateNewJSONFileSchema(Schema):
    filename = fields.Str(required=True)
    foldername = fields.Str(required=True)
