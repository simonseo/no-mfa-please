class AuthenticationException(Exception):
    """Raised when user authentication fails"""
    pass

class WrongPasswordException(AuthenticationException):
    """Raised when user account exists but wrong password"""
    pass

class UserDataNotFoundException(AuthenticationException):
    """Raised when user account does not exist at all"""
    pass

class UniqueViolationException(Exception):
    """Raised when psycopg2 throws psycopg2.errors.UniqueViolation"""
    pass
