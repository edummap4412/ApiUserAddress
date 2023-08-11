from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def save_address_validator(request: any):
    query_validator = Validator({
        "cep": {"type": "string", "required": True, "empty": False},
    })

    response = query_validator.validate(request.args)
    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
