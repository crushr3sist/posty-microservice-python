from passlib.context import CryptContext


class Config:
    jwt_secret = "blahblahblah"
    password_context = CryptContext(schemes=["pbkdf2_sha256"])
