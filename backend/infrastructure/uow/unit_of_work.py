from backend.infrastructure.core.db import SessionLocal
from backend.infrastructure.repositories.account_repositories import AccountRepository
from backend.infrastructure.repositories.species_repositories import SpeciesRepository


class UnitOfWork:

    def __init__(self):
        self.db = SessionLocal()

        self.species = SpeciesRepository(self.db)
        self.accounts = AccountRepository(self.db)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.db.close()