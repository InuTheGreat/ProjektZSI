from fastapi import APIRouter, Depends, HTTPException

from backend.application.api.dependencies import get_uow
from backend.application.schemas.lizard_vote import LizardVoteCreateRequest
from backend.application.schemas.lizard_vote_response import (
    LizardVoteResponse,
    LizardVoteCandidateResponse,
)
from backend.domain.exceptions.custom_exceptions import NotFoundError
from backend.domain.services.lizard_vote_service import LizardVoteService

router = APIRouter(prefix="/votes", tags=["Votes"])

@router.post("", status_code=201)
def create_vote(
    request: LizardVoteCreateRequest,
    uow=Depends(get_uow),
):
    service = LizardVoteService(uow)

    try:
        vote_id = service.create_vote(
            title=request.title,
            species_ids=request.lizard_ids,
        )

        uow.commit()

        return {"vote_id": vote_id}

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("/{candidate_id}/vote")
def vote(
    candidate_id: str,
    uow=Depends(get_uow),
):
    service = LizardVoteService(uow)

    try:
        service.vote(candidate_id)

        uow.commit()

        return {"status": "ok"}

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{vote_id}", response_model=LizardVoteResponse)
def get_vote(
    vote_id: str,
    uow=Depends(get_uow),
):
    service = LizardVoteService(uow)

    try:
        result = service.get_results(vote_id)

        return LizardVoteResponse(
            id=result["vote"].id,
            title=result["vote"].title,
            candidates=[
                LizardVoteCandidateResponse(
                    id=c.id,
                    lizard_id=c.lizard_id,
                    votes_count=c.votes_count,
                )
                for c in result["candidates"]
            ],
        )

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))