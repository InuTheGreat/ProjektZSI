from dataclasses import dataclass


@dataclass
class Species:
    id: str
    public_id: int | None

    common_name: str
    scientific_name: str

    family: str | None
    genus: str | None

    distribution: str | None
    habitat: str | None

    max_length_cm: str | None
    max_weight_g: str | None

    diet: str | None
    votes_count: int = 0 

    def __repr__(self) -> str:
        return f"Species(id={self.id}, public_id={self.public_id}, common_name={self.common_name}, scientific_name={self.scientific_name}, family={self.family}, genus={self.genus}, distribution={self.distribution}, habitat={self.habitat}, max_length_cm={self.max_length_cm}, max_weight_g={self.max_weight_g}, diet={self.diet}, votes_count={self.votes_count})"