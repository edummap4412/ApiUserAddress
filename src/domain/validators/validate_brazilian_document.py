from pycpfcnpj import cpfcnpj  # type: ignore

from src.domain.validators.validators_interface import ValidatorInterface


class ValidateBrazilianDocument(ValidatorInterface):
    def __init__(self, documento: str) -> None:
        self.documento = documento
        self.validate()

    def get_value(self) -> str:
        return self.documento

    def validate(self) -> None:
        if not cpfcnpj.validate(self.documento):
            raise ValueError('Documento Invalido')
