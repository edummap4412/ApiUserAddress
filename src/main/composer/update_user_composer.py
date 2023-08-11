from src.infra.db.repositories.user_repository import UserRepository
from src.data.use_cases.update_user import UpdateUser
from src.presentation.controllers.controller_update_user import ControllerUpdateUser


def update_user_composer():
    repository = UserRepository()
    use_case = UpdateUser(repository)
    controller = ControllerUpdateUser(use_case)
    return controller.handle
