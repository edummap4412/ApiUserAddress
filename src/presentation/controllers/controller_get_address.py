from src.domain.use_case_interfaces.get_address_interface import GetAddressInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface


class ControllerGetAddress(ControllerInterface):

    def __init__(self, use_case: GetAddressInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest = None) -> HttpResponse:
        response = self.use_case.get_address()
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
