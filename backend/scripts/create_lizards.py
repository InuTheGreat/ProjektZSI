from backend.infrastructure.core.db import SessionLocal
from backend.infrastructure.repositories.lizard_repositories import LizardRepository
from backend.domain.services.lizard_service import LizardService
from backend.application.schemas.lizard import LizardCreateRequest


def main():
    db = SessionLocal()

    repo = LizardRepository(db)
    service = LizardService(repo)

    print("Tworzę lizard...")

    payload = LizardCreateRequest(
        name="Test Lizard",
        age=3,
        species_id="bad2e247-8f18-48d9-bd2f-e989bfbb2d4c"
    )

    created = service.create_lizard(payload)

    print("UTWORZONO:")
    print(created)

    db.close()


if __name__ == "__main__":
    main()