# File: app/ports/user_repository.py

# Secondary adapter (Driven by application)

from abc import abstractmethod, ABC
from typing import Optional
from app.core.models import User

class UserRepository(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    