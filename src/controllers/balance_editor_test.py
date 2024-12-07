from .balance_editor import BalanceEditor


class MockRepository:
    def __init__(self):
        self.user_id = 0
        self.balance = 0

    def edit_balance(self, user_id, new_balance) -> None:
        self.user_id = user_id
        self.balance = new_balance


def test_edit_balance():
    user_id = 10
    new_balance = 1000.0

    user_repository = MockRepository()
    balance_editor = BalanceEditor(user_repository)
    balance_editor.edit(user_id, new_balance)

    assert user_repository.user_id == user_id
    assert user_repository.balance == new_balance
