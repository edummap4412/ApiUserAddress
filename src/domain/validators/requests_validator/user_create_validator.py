from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def user_create_validator(request: any):
    body_validator = Validator({
        "nome": {"type": "string", "required": True, "empty": False},
        "data_de_nascimento": {"type": "string", "required": True, "empty": False},
        "email": {"type": "string", "required": True, "empty": False},
        "telefone": {"type": "string", "required": True, "empty": False},
        "documento": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
