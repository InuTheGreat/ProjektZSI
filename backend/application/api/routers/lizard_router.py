from fastapi import APIRouter, Depends, HTTPException

from backend.application.api.dependencies import get_uow
from backend.application.schemas.lizard_response import LizardResponse
from backend.application.schemas.lizard import LizardCreateRequest
from backend.domain.services.lizard_service import LizardService
from backend.domain.exceptions.custom_exceptions import NotFoundError

router = APIRouter(prefix="/lizards", tags=["Lizards"])

@router.get("", response_model=list[LizardResponse])
def get_lizards(uow=Depends(get_uow)):
    service = LizardService(uow)

    try:
        return service.get_lizards()
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{lizard_id}", response_model=LizardResponse)
def get_lizard(lizard_id: str, uow=Depends(get_uow)):
    service = LizardService(uow)

    try:
        return service.get_lizard_by_id(lizard_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("", response_model=LizardResponse, status_code=201)
def create_lizard(
    request: LizardCreateRequest,
    uow=Depends(get_uow)
):
    service = LizardService(uow)

    lizard = service.create_lizard(request)

    return lizard

@router.get("/search")
def search_lizards(
    phrase: str,
    uow=Depends(get_uow)
):
    service = LizardService(uow)

    return service.find_lizards_by_phrase(phrase)
