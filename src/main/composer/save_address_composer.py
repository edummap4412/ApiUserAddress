from src.infra.db.repositories.address_repository import AddressRepository
from src.data.use_cases.save_address import SaveAddress
from src.presentation.controllers.controller_save_address import ControllerSaveAddress


def save_address_composer():
    repository = AddressRepository()
    use_case = SaveAddress(repository)
    controller = ControllerSaveAddress(use_case)
    return controller.handle
