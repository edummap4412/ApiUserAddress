from src.presentation.controllers.controller_update_user import ControllerUpdateUser
from tests.mocks.users_cases_mock.user_update_mock import UpdateUserMock


def test_update_user_controller():

    class HttpRequestMock:
        def __init__(self):
            self.body = {
                "user_id": "12345",
                "nome": "Michael",
                "data_de_nascimento": "30/06/1994",
                "email": "eduardo@email.com",
                "telefone": '+123(45) 0987-1234',
                "documento": "789.123.456-08"
            }
    update_user_mock = UpdateUserMock()
    controller_user = ControllerUpdateUser(update_user_mock)
    http_request = HttpRequestMock()
    assert http_request.body['email'] == 'eduardo@email.com'
    http_request.body['email'] = 'michael@gmail.com'

    response = controller_user.handle(http_request)
    assert http_request.body['email'] == 'michael@gmail.com'
    assert response.body['data'] == 'Usuario atualizado com sucesso'
    assert response.status_code == 200

