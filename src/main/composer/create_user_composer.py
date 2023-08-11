from src.infra.db.repositories.user_repository import UserRepository
from src.data.use_cases.create_user import CreateUser
from src.presentation.controllers.controller_create_user import ControllerCreateUser


def create_user_composer():
    repository = UserRepository()
    use_case = CreateUser(repository)
    controller = ControllerCreateUser(use_case)
    return controller.handle
