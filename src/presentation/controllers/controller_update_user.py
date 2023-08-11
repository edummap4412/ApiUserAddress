from src.domain.use_case_interfaces.update_user_interface import UpdateUserInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface


class ControllerUpdateUser(ControllerInterface):
    def __init__(self, use_case: UpdateUserInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest = None) -> HttpResponse:
        self.use_case.update_user(
            user_id=http_request.body['user_id'],
            nome=http_request.body['nome'],
            data_de_nascimento=http_request.body['data_de_nascimento'],
            documento=http_request.body['documento'],
            email=http_request.body['email'],
            telefone=http_request.body['telefone']
        )

        return HttpResponse(
            body={'data': 'Usuario atualizado com sucesso'},
            status_code=200
        )

