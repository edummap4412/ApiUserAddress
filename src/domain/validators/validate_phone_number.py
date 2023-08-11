import re

from src.domain.validators.validators_interface import ValidatorInterface


class ValidatePhoneNumber(ValidatorInterface):
    def __init__(self, telefone: str) -> None:
        self.telefone = telefone
        self.validate()

    def get_value(self) -> str:
        return self.telefone

    def validate(self) -> None:
        if not re.match(r'^(\+[0-9]{1,3}|\+1[0-9]{3})(\([0-9]{2}\))([ ]?)([0-9]{4,5})([-]?)([0-9]{4})$', self.telefone):
            raise ValueError('Numero de telefone invalido')
