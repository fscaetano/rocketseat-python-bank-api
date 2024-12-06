from .user_register import UserRegister


class MockUserRepository:
    def __init__(self):
        self.registry_user_attributes = {}

    def register_user(self, username, password) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password


def test_register():
    repository = MockUserRepository()
    controller = UserRegister(repository)

    username = "new-user"
    password = "sldfdlkfjsl"
    response = controller.register(username, password)

    print()
    print(repository.registry_user_attributes)

    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password
