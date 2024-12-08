from flask import request
from src.drivers.jwt_handler import JwtHandler


def auth_jwt_verify():
    jwt_handler = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = int(request.headers.get("uid"))
    
    print("****\nraw_token", raw_token)
    print("user_id", user_id, type(user_id))

    if not raw_token or not user_id:
        raise Exception("Invalid Auth informations.")

    token = raw_token.split()[1]
    token_information = jwt_handler.decode_jwt_token(token)
    token_uid = int(token_information["user_id"])
    print("token_uid", token_uid, type(token_uid))

    if user_id and token_uid and (token_uid == user_id):
        return token_information

    raise Exception("Unauthorized user.")
