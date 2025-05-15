# app/adapters/auth_service.py

import bcrypt
from app.ports.auth_service import AuthService

class BcryptAuthService(AuthService):

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password=password.encode(), salt=salt).decode()

    def verify_password(self, password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(password=password.encode(), hashed_password=password_hash.encode())