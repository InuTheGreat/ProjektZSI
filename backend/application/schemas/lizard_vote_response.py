from pydantic import BaseModel


class LizardVoteCandidateResponse(BaseModel):
    id: str
    species_id: str
    votes_count: int


class LizardVoteResponse(BaseModel):
    id: str
    title: str
    candidates: list[LizardVoteCandidateResponse]