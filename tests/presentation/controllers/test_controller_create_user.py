from src.presentation.controllers.controller_create_user import ControllerCreateUser
from tests.mocks.users_cases_mock.user_create_mock import CreateUserMock


def test_create_user_controller():
    class HttpRequestMock:
        def __init__(self):
            self.body = {
                "nome": "Michael",
                "data_de_nascimento": "30/06/1994",
                "email": "eduardo@email.com",
                "telefone": '+123(45) 0987-1234',
                "documento": "789.123.456-08"
            }

    create_user_mock = CreateUserMock()
    controller_user = ControllerCreateUser(create_user_mock)

    response = controller_user.handle(HttpRequestMock())

    assert response.body['data'] == 'Usuario registrado com sucesso'
    assert response.status_code == 201
