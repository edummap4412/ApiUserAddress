from src.domain.validators.validators_interface import ValidatorInterface
import re


class ValidateName(ValidatorInterface):

    def __init__(self, *, nome: str) -> None:
        self.nome = nome
        self.validate()

    def get_value(self) -> str:
        return self.nome

    def validate(self) -> None:
        if not re.match(r'^[a-z A-Z]+$', self.nome):
            raise ValueError("Nome invalido.")

