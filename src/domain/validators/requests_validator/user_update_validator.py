from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def user_update_validator(request: any):
    body_validator = Validator({
        "user_id":{"type": "string", "required": False, "empty": False},
        "nome": {"type": "string", "required": False, "empty": False},
        "data_de_nascimento": {"type": "string", "required": True, "empty": False},
        "email": {"type": "string", "required": False, "empty": False},
        "telefone": {"type": "string", "required": False, "empty": False},
        "documento": {"type": "string", "required": False, "empty": False}
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
