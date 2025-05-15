# app/main.py

from fastapi import FastAPI, HTTPException
from app.adapters.user_repository import SQLiteUserRepository
from app.adapters.auth_service import BcryptAuthService
from app.application.use_cases import UserService
from app.domain.exceptions import UserAlreadyExistsException, InvalidCredentialsException

app = FastAPI()

# Dependency Injection
user_repo = SQLiteUserRepository()
auth_service = BcryptAuthService()
user_service = UserService(user_repo, auth_service)

@app.post("/register")
def register(username: str, password: str, email: str):
    try:
        user = user_service.register_user(username, password, email)
        return {"message": "User registered successfully", "user_id": user.id}
    except UserAlreadyExistsException as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
def login(username: str, password: str):
    try:
        if user_service.login_user(username, password):
            return {"message": "Login successful"}
    except InvalidCredentialsException as e:
        raise HTTPException(status_code=401, detail=str(e))
