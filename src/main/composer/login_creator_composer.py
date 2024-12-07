from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator import LoginCreator
from src.views.login_creator_view import LoginCreatorView


def balance_editor_composer():
    connection = db_connection_handler.get_connection()
    model = UserRepository(connection)
    controller = LoginCreator(model)
    view = LoginCreatorView(controller)

    return view
