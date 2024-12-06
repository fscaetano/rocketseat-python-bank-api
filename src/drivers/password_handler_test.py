from .password_handler import PasswordHandler


def test_password_handler():
    password = "my-secret-password-123"
    handler = PasswordHandler()
    hashed_password = handler.encrypt_password(password)
    print()
    print(password, hashed_password)

    password_ok = handler.check_password(password, hashed_password)
    assert password_ok
