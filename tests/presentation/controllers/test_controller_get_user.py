from src.presentation.controllers.controller_get_user import ControllerGetUser
from tests.mocks.users_cases_mock.user_get_mock import GetUserMock


def test_get_user_controller():
    get_user_mock = GetUserMock()
    controller_user = ControllerGetUser(get_user_mock)

    controller_user.handle()
