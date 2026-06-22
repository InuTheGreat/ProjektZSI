from backend.infrastructure.uow.unit_of_work import UnitOfWork
from backend.domain.services.species_service import SpeciesService
from backend.application.schemas.species import SpeciesCreateRequest


def main():
    uow = UnitOfWork()
    service = SpeciesService(uow)

    print("Tworzę species...")

    payload = SpeciesCreateRequest(
        common_name="Leopard Gecko",
        scientific_name="Eublepharis macularius",
        family="Eublepharidae",
        genus="Eublepharis",
        distribution="Pakistan",
        habitat="Dry areas",
        max_length_cm="28",
        max_weight_g="90",
        diet="Insects",
    )

    created = service.create_species(payload)

    print("UTWORZONO:")
    print(created)

    uow.close()


if __name__ == "__main__":
    main()