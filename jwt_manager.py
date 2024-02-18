import os
from dotenv import load_dotenv
from jwt import encode

load_dotenv

secretKey = os.getenv("SECRET_KEY")


def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="secretKey", algorithm="HS256")
    return token
