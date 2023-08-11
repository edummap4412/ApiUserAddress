from src.infra.db.repositories.address_repository import AddressRepository
from src.data.use_cases.get_address import GetAddress
from src.presentation.controllers.controller_get_address import ControllerGetAddress


def get_address_composer():
    repository = AddressRepository()
    use_case = GetAddress(repository)
    controller = ControllerGetAddress(use_case)
    return controller.handle
