from backend.domain.entities.species import Species
from backend.domain.exceptions.custom_exceptions import NotFoundError,AlreadyVotedError


class SpeciesService:

    def __init__(self, uow):
        self.uow = uow

    def get_species(self) -> list[Species]:
        found_species = self.uow.species.get_all_species()
        if not found_species:
            raise NotFoundError("No species found")
        return found_species

    def get_species_by_id(self, species_id: str) -> Species:
        found_species = self.uow.species.get_species_by_id(species_id)
        if not found_species:
            raise NotFoundError("Species not found")
        return found_species

    def create_species(self, species_data) -> Species:
        result = self.uow.species.create_species(species_data)
        self.uow.commit()
        return result

    def update_species(self, species_id: str, species_data) -> Species:
        result = self.uow.species.update_species(species_id, species_data)
        if not result:
            raise NotFoundError("Species not found")
        self.uow.commit()
        return result

    def delete_species(self, species_id: str) -> bool:
        found = self.uow.species.get_species_by_id(species_id)
        if not found:
            raise NotFoundError("Species not found")

        result = self.uow.species.delete_species(species_id)
        self.uow.commit()
        return result

    def get_species_paginated(self, skip: int, limit: int):
        return self.uow.species.get_species_paginated(skip, limit)

    def vote(self, species_id: str, voter_id: str, redis_client) -> None:
        from backend.infrastructure.core.vote_rate_limiter import (
            has_already_voted,
            register_vote,
        )

        if has_already_voted(redis_client, species_id, voter_id):
            raise AlreadyVotedError("Już dzisiaj głosowałeś na tę jaszczurkę")

        success = self.uow.species.increment_vote(species_id)
        if not success:
            raise NotFoundError("Species not found")

        register_vote(redis_client, species_id, voter_id)