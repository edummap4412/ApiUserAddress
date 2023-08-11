from src.domain.use_case_interfaces.get_user_interface import GetUserInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface


class ControllerGetUser(ControllerInterface):

    def __init__(self, use_case: GetUserInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest = None) -> HttpResponse:
        response = self.use_case.get_user()
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
