# utils/auth.py

from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# ------------------------------------
# CONFIG (CHANGE SECRET IN PRODUCTION)
# ------------------------------------
SECRET_KEY = "CHANGE_THIS_SECRET_KEY_TO_SOMETHING_LONG_AND_RANDOM"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 1 day

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Tell FastAPI which route is used for token login (not actually used, but required)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# ------------------------------------
# PASSWORD HELPERS
# ------------------------------------
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# ------------------------------------
# JWT CREATION
# ------------------------------------
def create_access_token(data: dict) -> str:
    """
    Creates a JWT token containing:
    - 'sub': email
    - 'exp': expiration datetime
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


# ------------------------------------
# JWT VERIFICATION + USER EXTRACTION
# ------------------------------------
def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """
    Extracts the user's email from the JWT token.
    Used as a dependency in protected routes.
    """

    if not token:
        raise HTTPException(status_code=401, detail="Missing authentication token.")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token: missing subject.")

        return email  # We return the email as the 'current user'

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token.")
