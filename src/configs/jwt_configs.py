import os

jwt_info = {
    "KEY": os.getenv("JWT_KEY"),
    "ALGORITHM": os.getenv("JWT_ALGORITHM"),
    "JWT_HOURS": int(os.getenv("JWT_HOURS"))
}
