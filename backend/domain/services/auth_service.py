from backend.domain.services.jwt_service import (
    JwtService,
)
from backend.domain.services.password_service import (
    PasswordService,
)

from backend.domain.exceptions.custom_exceptions import (
    NotFoundError,
)


class AuthService:

    def __init__(self, uow):
        self.uow = uow

    def login(self, request):

        account = self.uow.accounts.get_account_by_email(
            request.email
        )

        if account is None:
            raise NotFoundError("Invalid credentials")

        valid = PasswordService.verify_password(
            request.password,
            account.password_hash,
        )

        if not valid:
            raise NotFoundError("Invalid credentials")

        token = JwtService.generate_token(
            account.id,
            account.role,
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }