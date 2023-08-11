from src.presentation.controllers.controller_delete_user import ControllerDeleteUser
from tests.mocks.users_cases_mock.user_delete_mock import DeleteUserMock


def test_delete_user_controller():
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

    delete_user_mock = DeleteUserMock()
    controller_user = ControllerDeleteUser(delete_user_mock)

    response = controller_user.handle(HttpRequestMock())

    assert response.body['data'] == 'Usario foi deletado'
    assert response.status_code == 200
