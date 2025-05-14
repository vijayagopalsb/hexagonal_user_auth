# File: app/domain/user.py

# Domain model: User

from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int] = None
    username: str = ""
    password_hash: str = ""
    email: str = ""
