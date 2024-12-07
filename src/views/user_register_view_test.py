from pytest import raises
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView


class MockController:
    def register(self, username: str, password: str) -> dict:
        return {"some": "thing"}


def test_handle_user_register():
    body = {
        "username": "my-username",
        "password": "qwoeiru238947"
    }

    request = HttpRequest(body=body)
    controller = MockController()
    user_register_view = UserRegisterView(controller)

    response = user_register_view.handle(request)

    print()
    print(response)
    print(response.body)

    assert isinstance(response, HttpResponse)
    assert response.body == {"data": {"some": "thing"}}
    assert response.status_code == 201


def test_handle_user_register_with_error():
    body = {
        "username": "my-username",
    }

    request = HttpRequest(body=body)
    controller = MockController()
    user_register_view = UserRegisterView(controller)

    with raises(Exception):
        response = user_register_view.handle(request)
