from dataclasses import dataclass


@dataclass
class LizardVoteCandidate:
    id: str
    vote_id: str
    species_id: str
    votes_count: int = 0

    def __repr__(self) -> str:
        return (
            f"LizardVoteCandidate("
            f"id={self.id}, "
            f"vote_id={self.vote_id}, "
            f"species_id={self.species_id}, "
            f"votes_count={self.votes_count})"
        )