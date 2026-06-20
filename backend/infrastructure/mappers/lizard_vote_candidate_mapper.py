from backend.domain.entities.lizard_vote_candidate import LizardVoteCandidate
from backend.infrastructure.orm.lizard_vote_candidate_model import LizardVoteCandidateModel


class LizardVoteCandidateMapper:

    @staticmethod
    def to_entity(model):
        return LizardVoteCandidate(
            id=model.id,
            vote_id=model.vote_id,
            species_id=model.species_id,
            votes_count=model.votes_count,
        )

    @staticmethod
    def to_model(entity):
        return LizardVoteCandidateModel(
            id=entity.id,
            vote_id=entity.vote_id,
            species_id=entity.species_id,
            votes_count=entity.votes_count,
        )