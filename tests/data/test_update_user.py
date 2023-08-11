from src.data.use_cases.update_user import UpdateUser
from tests.mocks.user_repository_mock.user_repository_mock import UserRepositoryMock


def test_use_cases_update_user():

    user_repository = UserRepositoryMock()
    use_case = UpdateUser(user_repository)

    user = use_case.update_user(
        user_id='12345',
        nome="Michael",
        data_de_nascimento="30/06/1994",
        email="eduardo@email.com",
        telefone='+123(45) 0987-1234',
        documento='964.157.430-23'
    )

    updated_user = user_repository.get_user_attributes

    assert user['data']['nome'] == updated_user[0]['user1']['nome']
    assert user['data']['email'] == updated_user[0]['user1']['email']
    assert user['data']['telefone'] == updated_user[0]['user1']['telefone']

