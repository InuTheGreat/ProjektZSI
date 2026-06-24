from pydantic import BaseModel, Field


class LizardCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int = Field(gt=0)
    species_id: str