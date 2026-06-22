from backend.domain.entities.account import Account


class AccountMapper:

    @staticmethod
    def to_domain(model):
        return Account(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            password_hash=model.password_hash,
            role=model.role,
        )