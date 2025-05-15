# app/main.py

from fastapi import FastAPI, HTTPException
from app.adapters.sqlite_user_respository import SQLiteUserRepository
from app.adapters.bcrypt_auth_service import  BcryptAuthService
from app.application.use_cases import UserService
from app.domain.exceptions import UserAlreadyExistsException, InvalidCredentialsException
from app.schemas.user_schemas import UserCreate, UserLogin
from app.utils.logger import setup_logger

# Initialize logger
logger = setup_logger(__name__)

logger.info("Initializing logger...")
app = FastAPI()

# Dependency Injection
user_repo = SQLiteUserRepository()
auth_service = BcryptAuthService()
user_service = UserService(user_repo, auth_service)

@app.post("/register")
def register(user: UserCreate):
    logger.info("User registration API called.")
    try:
        new_user = user_service.register_user(
            username=user.username,
            password=user.password,
            email=user.email
        )
        logger.info("User created successfully.")
        return {"message": "User registered successfully", "user_id": new_user.id}
    except UserAlreadyExistsException as e:
        logger.info(f"[DEBUG] Caught exception: {e}")
        logger.info("Duplicate user, Please try with another name")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
def login(user: UserLogin):
    logger.info("User login API called.")
    try:
        if user_service.login_user(user.username, user.password):
            logger.info("User login successfull.")
            return {"message": "Login successful"}
    except InvalidCredentialsException as e:
        logger.info("User Not Found.")
        raise HTTPException(status_code=401, detail=str(e))
