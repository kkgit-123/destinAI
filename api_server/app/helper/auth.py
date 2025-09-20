from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import get_config
from logger import setup_logging
import jwt
from jwt import PyJWTError

logger = setup_logging()
config = get_config()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Dummy token URL, not implemented here

JWT_SECRET_KEY = config.get("AUTH", "JWT_SECRET_KEY")
ALGORITHM = config.get("AUTH", "ALGORITHM")

async def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    """
    Decodes a JWT token from the Authorization header and extracts the user_id.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub") # 'sub' is commonly used for user ID
        if user_id is None:
            logger.warning("JWT token missing 'sub' (user_id) claim.")
            raise credentials_exception
        logger.info(f"User ID {user_id} extracted from JWT.")
        return user_id
    except PyJWTError as e:
        logger.warning(f"Invalid JWT token: {e}")
        raise credentials_exception
    except Exception as e:
        logger.error(f"Unexpected error during JWT decoding: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during authentication",
        )

# Example usage (for testing purposes, not directly runnable)
if __name__ == "__main__":
    print("This module defines authentication logic and is meant to be imported.")
    # To generate a dummy token for testing:
    # import jwt
    # token_payload = {"sub": 123, "name": "testuser"}
    # encoded_jwt = jwt.encode(token_payload, "your-super-secret-jwt-key", algorithm="HS256")
    # print(f"Generated Token: {encoded_jwt}")
