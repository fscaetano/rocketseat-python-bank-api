from flask import Blueprint, jsonify

bank_account_routes = Blueprint("bank_account", __name__)


@bank_account_routes.route("/", methods=["GET"])
def hello():
    return jsonify({"hello": "world"}), 200
