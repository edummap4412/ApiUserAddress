from src.domain.use_case_interfaces.delete_user_interface import DeleteUserInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface


class ControllerDeleteUser(ControllerInterface):

    def __init__(self, use_case: DeleteUserInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest = None) -> HttpResponse:
        self.use_case.delete_user(user_id=http_request.body['user_id'])

        return HttpResponse(
            body={'data': 'Usario foi deletado'},
            status_code=200
        )