# File: app/adapters/sqlite_user_repository.py

from typing import Optional
from app.domain.models import User
from app.ports.user_repository import UserRepository
from app.domain.exceptions import UserAlreadyExistsException, UserNotFoundException
import sqlite3

class SQLiteUserRepository(UserRepository):

    def __init__(self, db_path ="user.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cusor = conn.cursor()
        cusor.execute(
            """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password_hash TEXT,
                    email TEXT UNIQUE
                )
            """
        )
        conn.commit()
        conn.close()

    def get_user_by_username(self, username: str) -> Optional[User]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, password_hash, email from users WHERE username=?", (username,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return User(id=row[0], username=row[1], password_hash=row[2], email=row[3])
        return None

    def create_user(self, user: User) -> User:
        if self.get_user_by_username(user.username):
            raise UserAlreadyExistsException("User already exists")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()  # ✅ get a cursor from the connection

        cursor.execute(
            "INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)",
            (user.username, user.password_hash, user.email)
        )

        user.id = cursor.lastrowid  # ✅ This now works as expected

        conn.commit()
        conn.close()

        return user

