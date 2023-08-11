from src.domain.use_case_interfaces.save_address_interface import SaveAddressInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.main.sdks.via_cep.get_cep import ViaCepSdk


class ControllerSaveAddress(ControllerInterface):

    def __init__(self, use_case: SaveAddressInterface):
        self.use_case = use_case
        self.via_cep = ViaCepSdk()

    def handle(self, http_request: HttpRequest = None) -> HttpResponse:
        get_cep_param = http_request.query_params.get('cep')
        address = self.via_cep.get_address_by_cep(cep=get_cep_param)
        response = self.use_case.save_address(
            cep=address['cep'],
            logradouro=address['logradouro'],
            complemento=address['complemento'],
            bairro=address['bairro'],
            cidade=address['localidade'],
            uf=address['uf']
        )
        return HttpResponse(
            status_code=200,
            body=response
        )
