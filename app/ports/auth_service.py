# File: app/ports/auth_service.py

from abc import ABC, abstractmethod

class AuthService(ABC):

    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass

    @abstractmethod
    def verify_password(self, password: str, password_hash: str) -> bool:
        pass
    