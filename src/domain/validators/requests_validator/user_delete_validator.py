from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def user_delete_validator(request: any):
    body_validator = Validator({
        "user_id":{"type": "string", "required": True, "empty": False},
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
