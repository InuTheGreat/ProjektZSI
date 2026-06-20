from backend.infrastructure.core.db import SessionLocal
from backend.infrastructure.repositories.account_repositories import AccountRepository
from backend.infrastructure.repositories.lizard_repositories import LizardRepository
from backend.infrastructure.repositories.species_repositories import SpeciesRepository
from backend.infrastructure.repositories.lizard_vote_repository import LizardVoteRepository


class UnitOfWork:

    def __init__(self):
        self.db = SessionLocal()

        self.lizards = LizardRepository(self.db)
        self.species = SpeciesRepository(self.db)
        self.lizard_votes = LizardVoteRepository(self.db)
        self.accounts = AccountRepository(self.db)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.db.close()