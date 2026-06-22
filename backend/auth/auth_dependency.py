# backend/auth/auth_dependency.py

from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import (
    HTTPAuthorizationCredentials,
)

from fastapi.security import (
    HTTPBearer,
)

from jose import jwt
from jose import JWTError

from backend.domain.services.jwt_service import (
    JwtService, 
)

security = HTTPBearer()


def authorize(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
):
    try:

        payload = jwt.decode(
            credentials.credentials,
            JwtService.SECRET_KEY,
            algorithms=[
                JwtService.ALGORITHM
            ],
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )