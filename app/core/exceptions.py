# File: app/domain/exception.py

# Domain exception classes

class UserAlreadyExistsException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class InvalidCredentialsException(Exception):
    pass