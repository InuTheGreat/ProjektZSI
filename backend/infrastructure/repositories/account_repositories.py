from sqlalchemy.orm import Session

from backend.infrastructure.orm.account_model import (
    AccountModel,
)
from backend.infrastructure.mappers.account_mapper import (
    AccountMapper,
)


class AccountRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_account_by_id(
        self,
        account_id: str,
    ):
        account_model = (
            self.db_session.query(AccountModel)
            .filter(AccountModel.id == account_id)
            .first()
        )

        if account_model is None:
            return None

        return AccountMapper.to_domain(
            account_model
        )

    def get_account_by_email(
        self,
        email: str,
    ):
        account_model = (
            self.db_session.query(AccountModel)
            .filter(AccountModel.email == email)
            .first()
        )

        if account_model is None:
            return None

        return AccountMapper.to_domain(
            account_model
        )

    def create_account(
        self,
        account_model,
    ):
        self.db_session.add(account_model)

        self.db_session.flush()

        return AccountMapper.to_domain(
            account_model
        )
    
    def update_role(self, account_id: str, new_role: str):
        account_model = (
                self.db_session.query(AccountModel)
                .filter(AccountModel.id == account_id)
            .first()
        )
        if account_model is None:
            return None

        account_model.role = new_role
        self.db_session.flush()
        return AccountMapper.to_domain(account_model)