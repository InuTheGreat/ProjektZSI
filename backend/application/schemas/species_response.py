from pydantic import BaseModel


class SpeciesResponse(BaseModel):
    id: str
    common_name: str
    scientific_name: str

    family: str | None = None
    genus: str | None = None
    distribution: str | None = None
    habitat: str | None = None
    max_length_cm: str | None = None
    max_weight_g: str | None = None
    diet: str | None = None
    votes_count: int = 0