from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.balance_editor_composer import balance_editor_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.middlewares.auth_jwt import auth_jwt_verify

bank_account_routes = Blueprint("bank_account", __name__)


@bank_account_routes.route("/bank/register", methods=["POST"])
def register_user():
    http_request = HttpRequest(body=request.json)
    http_response = user_register_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@bank_account_routes.route("/bank/login", methods=["POST"])
def create_login():
    http_request = HttpRequest(body=request.json)
    http_response = login_creator_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@bank_account_routes.route("/bank/balance/<user_id>", methods=["PATCH"])
def edit_balance(user_id):
    token_information = auth_jwt_verify()
    http_request = HttpRequest(
        body=request.json,
        params={"user_id": int(user_id)},
        token_infos=token_information
    )
    http_response = balance_editor_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code
