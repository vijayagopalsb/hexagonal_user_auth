# app/main.py

from fastapi import FastAPI, HTTPException
from app.adapters.sqlite_user_respository import SQLiteUserRepository
from app.adapters.bcrypt_auth_service import  BcryptAuthService
from app.application.use_cases import UserService
from app.domain.exceptions import UserAlreadyExistsException, InvalidCredentialsException
from app.schemas.user_schemas import UserCreate, UserLogin

app = FastAPI()

# Dependency Injection
user_repo = SQLiteUserRepository()
auth_service = BcryptAuthService()
user_service = UserService(user_repo, auth_service)

@app.post("/register")
def register(user: UserCreate):
    try:
        new_user = user_service.register_user(
            username=user.username,
            password=user.password,
            email=user.email
        )
        return {"message": "User registered successfully", "user_id": new_user.id}
    except UserAlreadyExistsException as e:
        print(f"[DEBUG] Caught exception: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
def login(user: UserLogin):
    try:
        if user_service.login_user(user.username, user.password):
            return {"message": "Login successful"}
    except InvalidCredentialsException as e:
        raise HTTPException(status_code=401, detail=str(e))
