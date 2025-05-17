import pytest

from app.application.use_cases import UserService
from app.adapters.bcrypt_auth_service import AuthService
from app.core.exceptions import UserAlreadyExistsException, InvalidCredentialsException
from app.core.models import User

# ---- Mock implementations ----

class InMemoryUserRepo:
    def __init__(self):
        self.users = {}

    def get_user_by_username(self, username):
        return self.users.get(username)

    def create_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistsException("User already exists")
        user.id = len(self.users) + 1
        self.users[user.username] = user
        return user

class FakeAuthService(AuthService):
    def hash_password(self, password: str) -> str:
        return f"hashed:{password}"

    def verify_password(self, password: str, password_hash: str) -> bool:
        return password_hash == f"hashed:{password}"

# ---- Fixtures ----

@pytest.fixture
def user_service():
    repo = InMemoryUserRepo()
    auth = FakeAuthService()
    return UserService(repo, auth)

# ---- Tests ----

def test_register_user_success(user_service):
    user = user_service.register_user("vijay", "abcd", "vijay@gmail.com")
    assert user.username == "vijay"
    assert user.id == 1
    assert user.password_hash.startswith("hashed:")

def test_register_user_duplicate(user_service):
    user_service.register_user("vijay", "abcd", "vijay@gmail.com")
    with pytest.raises(UserAlreadyExistsException):
        user_service.register_user("vijay", "xyz", "vijay2@gmail.com")

def test_login_user_success(user_service):
    user_service.register_user("vijay", "abcd", "vijay@gmail.com")
    result = user_service.login_user("vijay", "abcd")
    assert result is True

def test_login_user_wrong_password(user_service):
    user_service.register_user("vijay", "abcd", "vijay@gmail.com")
    with pytest.raises(InvalidCredentialsException):
        user_service.login_user("vijay", "wrongpassword")

def test_login_user_not_found(user_service):
    with pytest.raises(InvalidCredentialsException):
        user_service.login_user("unknown", "any")
