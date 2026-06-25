import pytest

from backend.domain.services.species_service import SpeciesService
from backend.domain.exceptions.custom_exceptions import NotFoundError
from backend.application.schemas.species import SpeciesCreateRequest


class FakeSpeciesRepository:

    def __init__(self):
        self.species = []

    def get_all_species(self):
        return self.species

    def get_species_by_id(self, species_id):
        for s in self.species:
            if s["id"] == species_id:
                return s
        return None

    def create_species(self, species_data):
        species = {
            "id": str(len(self.species) + 1),
            "common_name": species_data.common_name,
            "scientific_name": species_data.scientific_name,
        }
        self.species.append(species)
        return species


class FakeUow:

    def __init__(self):
        self.species = FakeSpeciesRepository()

    def commit(self):
        pass


def test_create_species():
    service = SpeciesService(FakeUow())

    request = SpeciesCreateRequest(
        common_name="Gecko",
        scientific_name="Gekko gecko"
    )

    result = service.create_species(request)

    assert result["common_name"] == "Gecko"
    assert result["scientific_name"] == "Gekko gecko"


def test_get_species():
    uow = FakeUow()
    service = SpeciesService(uow)

    request = SpeciesCreateRequest(
        common_name="Gecko",
        scientific_name="Gekko gecko"
    )

    service.create_species(request)

    result = service.get_species()

    assert len(result) == 1


def test_get_species_by_id():
    uow = FakeUow()
    service = SpeciesService(uow)

    request = SpeciesCreateRequest(
        common_name="Gecko",
        scientific_name="Gekko gecko"
    )

    service.create_species(request)

    result = service.get_species_by_id("1")

    assert result["common_name"] == "Gecko"


def test_get_species_not_found():
    service = SpeciesService(FakeUow())

    with pytest.raises(NotFoundError):
        service.get_species_by_id("10")