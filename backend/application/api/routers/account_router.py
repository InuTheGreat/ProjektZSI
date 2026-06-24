from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer

from backend.domain.exceptions.custom_exceptions import NotFoundError
from backend.application.api.dependencies import get_uow
from backend.application.schemas.account import AccountCreateRequest
from backend.application.schemas.login import LoginRequest
from backend.application.schemas.account_response import AccountResponse
from backend.application.schemas.token_response import TokenResponse
from backend.application.schemas.role_update import RoleUpdateRequest

from backend.domain.services.account_service import AccountService
from backend.domain.services.auth_service import AuthService

from backend.auth.auth_dependency import authorize, require_admin

security = HTTPBearer()

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post(
    "/register",
    response_model=AccountResponse,
    status_code=201,
)
def register(
    request: AccountCreateRequest,
    uow=Depends(get_uow),
):
    service = AccountService(uow)

    try:
        return service.create_account(request)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    uow=Depends(get_uow),
):
    service = AuthService(uow)

    try:
        return service.login(request)
    except NotFoundError:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )


@router.get(
    "/me",
    response_model=AccountResponse,
)
def me(
    payload=Depends(authorize),
    uow=Depends(get_uow),
):
    account = uow.accounts.get_account_by_id(
        payload["sub"]
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not found",
        )

    return account


@router.get("/verify-token")
def verify_token(payload=Depends(authorize)):
    return {
        "valid": True,
        "user_id": payload["sub"],
        "role": payload["role"],
    }

@router.patch(
    "/{account_id}/role",
    response_model=AccountResponse,
)
def update_account_role(
    account_id: str,
    request: RoleUpdateRequest,
    uow=Depends(get_uow),
    _admin=Depends(require_admin),
):
    service = AccountService(uow)
    try:
        return service.update_role(account_id, request.role)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))