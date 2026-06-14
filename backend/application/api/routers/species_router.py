from fastapi import APIRouter, Depends, HTTPException

from backend.application.api.dependencies import get_uow
from backend.domain.services.species_service import SpeciesService
from backend.application.schemas.species import SpeciesCreateRequest
from backend.application.schemas.species_response import SpeciesResponse
from backend.domain.exceptions.custom_exceptions import NotFoundError

router = APIRouter(prefix="/species", tags=["Species"])

@router.get("", response_model=list[SpeciesResponse])
def get_species(
    page: int = 1,
    limit: int = 5,
    uow=Depends(get_uow)
):
    service = SpeciesService(uow)

    skip = (page - 1) * limit

    return service.get_species_paginated(skip, limit)

    service = SpeciesService(uow)

    try:
        return service.get_species()

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/{species_id}", response_model=SpeciesResponse)
def get_species_by_id(species_id: str, uow=Depends(get_uow)):
    service = SpeciesService(uow)

    try:
        return service.get_species_by_id(species_id)

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.post("", response_model=SpeciesResponse, status_code=201)
def create_species(
    request: SpeciesCreateRequest,
    uow=Depends(get_uow)
):
    service = SpeciesService(uow)

    species = service.create_species(request)

    return species

def update_species(
    species_id: str,
    request: SpeciesCreateRequest,
    uow=Depends(get_uow)
):
    service = SpeciesService(uow)

    try:
        return service.update_species(
            species_id,
            request
        )

    except NotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    
@router.delete("/{species_id}", status_code=204)
    
def delete_species(
    species_id: str,
    uow=Depends(get_uow)
):
    service = SpeciesService(uow)

    try:
        service.delete_species(species_id)

    except NotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
