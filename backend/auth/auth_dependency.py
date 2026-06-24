# backend/auth/auth_dependency.py

from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request 
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
    
def get_optional_account_id(request: Request) -> str | None:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    token = auth_header.removeprefix("Bearer ")
    try:
        payload = jwt.decode(
            token,
            JwtService.SECRET_KEY,
            algorithms=[JwtService.ALGORITHM],
        )
        return payload.get("sub")
    except JWTError:
        return None

