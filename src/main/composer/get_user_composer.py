from src.infra.db.repositories.user_repository import UserRepository
from src.data.use_cases.get_user import GetUser
from src.presentation.controllers.controller_get_user import ControllerGetUser


def get_user_composer():
    repository = UserRepository()
    use_case = GetUser(repository)
    controller = ControllerGetUser(use_case)
    return controller.handle
