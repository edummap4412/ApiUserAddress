import re

from src.domain.validators.validators_interface import ValidatorInterface


class ValidateEmail(ValidatorInterface):
    def __init__(self, email: str) -> None:
        self.email = email
        self.validate()

    def get_value(self) -> str:
        return self.email

    def validate(self) -> None:
        if not re.match(r'^[\w-]+(\.[\w-]+)*@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$', self.email):
            raise ValueError('Email invalido')
