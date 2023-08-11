from src.domain.use_case_interfaces.create_user_interface import CreateUserInterface
from src.infra.db.repositories.user_repository_interface import UserRepositoryInterface

from src.domain.validators.validate_brazilian_document import ValidateBrazilianDocument
from src.domain.validators.validation_name import ValidateName
from src.domain.validators.validate_phone_number import ValidatePhoneNumber
from src.domain.validators.validate_email import ValidateEmail
from typing import Dict
from src.errors.types.http_bad_request import HttpBadResquestError


class CreateUser(CreateUserInterface):

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, *, nome: str, data_de_nascimento: str, email: str, telefone: str, documento: str) -> Dict:
        validated_name = self.validated_name(nome=nome)
        validated_email = self.validated_email(email=email)
        validated_telefone = self.validated_telefone(telefone=telefone)
        validated_documento = self.validated_documento(documento=documento)

        self.user_repository.create_user(
            nome=validated_name,
            data_de_nascimento=data_de_nascimento,
            email=validated_email,
            telefone=validated_telefone,
            documento=validated_documento
        )

        return {'data': {
            "nome": nome,
            "data_de_nascimento": data_de_nascimento,
            "email": email,
            "telefone": telefone,
            "documento": documento
        }}

    @classmethod
    def validated_name(cls, *, nome: str) -> str:
        try:
            return ValidateName(nome=nome).get_value()
        except Exception as e:
            raise HttpBadResquestError(message=e.args[0])

    @classmethod
    def validated_email(cls, *, email: str) -> str:
        try:
            return ValidateEmail(email=email).get_value()
        except Exception as e:
            raise HttpBadResquestError(message=e.args[0])

    @classmethod
    def validated_telefone(cls, *, telefone: str) -> str:
        try:
            return ValidatePhoneNumber(telefone=telefone).get_value()
        except Exception as e:
            raise HttpBadResquestError(message=e.args[0])

    @classmethod
    def validated_documento(cls, *, documento: str) -> str:
        try:
            return ValidateBrazilianDocument(documento=documento).get_value()
        except Exception as e:
            raise HttpBadResquestError(message=e.args[0])
