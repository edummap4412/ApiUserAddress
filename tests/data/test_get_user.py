from src.data.use_cases.get_user import GetUser
from tests.mocks.user_repository_mock.user_repository_mock import UserRepositoryMock


def test_use_case_get_user():
    user_repository = UserRepositoryMock()
    use_case = GetUser(user_repository)

    use_case_get = use_case.get_user()
    get_user = user_repository.get_user_attributes

    assert len(use_case_get) == len(get_user)
