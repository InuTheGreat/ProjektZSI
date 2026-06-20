from backend.domain.services.auth_service import (
    AuthService,
)
from backend.domain.services.password_service import (
    PasswordService,
)

from backend.infrastructure.orm.account_model import (
    AccountModel,
)


class AccountService:

    def __init__(self, uow):
        self.uow = uow

    def create_account(self, request):

        existing_account = (
            self.uow.accounts.get_account_by_email(
                request.email
            )
        )

        if existing_account:
            raise ValueError("Account already exists")

        account_model = AccountModel(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password_hash=PasswordService.hash_password(
                request.password
            ),
            role="STANDARD",
        )

        account = self.uow.accounts.create_account(
            account_model
        )

        self.uow.commit()

        return account