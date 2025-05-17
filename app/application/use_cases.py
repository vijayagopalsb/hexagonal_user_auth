# app/application/use_cases.py

from app.ports.user_repository import UserRepository
from app.ports.auth_service import AuthService
from app.core.models import User
from app.core.exceptions import InvalidCredentialsException

class UserService:
    def __init__(self, user_repo: UserRepository, auth_service: AuthService):
        self.user_repo = user_repo
        self.auth_service = auth_service

    def register_user(self, username: str, password: str, email: str) -> User:
        password_hash = self.auth_service.hash_password(password)
        user = User(username=username, password_hash=password_hash, email=email)
        return self.user_repo.create_user(user)

    def login_user(self, username: str, password: str) -> bool:
        user = self.user_repo.get_user_by_username(username)
        if not user or not self.auth_service.verify_password(password, user.password_hash):
            raise InvalidCredentialsException("Invalid username or password")
        return True
