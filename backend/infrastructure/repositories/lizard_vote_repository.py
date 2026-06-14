from sqlalchemy.orm import Session

from backend.infrastructure.orm.lizard_vote_model import LizardVoteModel
from backend.infrastructure.orm.lizard_vote_candidate_model import LizardVoteCandidateModel

from backend.infrastructure.mappers.lizard_vote_mapper import LizardVoteMapper
from backend.infrastructure.mappers.lizard_vote_candidate_mapper import (
    LizardVoteCandidateMapper,
)

from sqlalchemy.orm import joinedload

class LizardVoteRepository:

    def __init__(self, db_session):
        self.db_session = db_session

    def create_vote(self, vote_model: LizardVoteModel) -> None:
        self.db_session.add(vote_model)
        self.db_session.flush()

    def get_vote(self, vote_id: str):
        model = self.db_session.get(LizardVoteModel, vote_id)
        if not model:
            return None
        return LizardVoteMapper.to_entity(model)


    def add_candidate(self, candidate_model: LizardVoteCandidateModel) -> None:
        self.db_session.add(candidate_model)
        self.db_session.flush()

    def get_candidates(self, vote_id: str):
        models = (
            self.db_session.query(LizardVoteCandidateModel)
            .options(joinedload(LizardVoteCandidateModel.species))
            .filter(LizardVoteCandidateModel.vote_id == vote_id)
            .all()
        )

        return [
            LizardVoteCandidateMapper.to_entity(m)
            for m in models
        ]

    def increment_vote(self, candidate_id: str) -> None:
        candidate = self.db_session.get(
            LizardVoteCandidateModel,
            candidate_id,
        )

        if not candidate:
            return

        candidate.votes_count += 1
        self.db_session.flush()
    

