from src.domain.use_case_interfaces.create_user_interface import CreateUserInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface


class ControllerCreateUser(ControllerInterface):

    def __init__(self, use_case: CreateUserInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest = None) -> HttpResponse:
        self.use_case.create_user(
            nome=http_request.body['nome'],
            data_de_nascimento=http_request.body['data_de_nascimento'],
            documento=http_request.body['documento'],
            email=http_request.body['email'],
            telefone=http_request.body['telefone']
        )

        return HttpResponse(
            body={'data': 'Usuario registrado com sucesso'},
            status_code=201
        )
