from pydantic import BaseModel, Field
from pydantic import EmailStr


class AccountCreateRequest(BaseModel):
<<<<<<< HEAD
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
=======
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)
>>>>>>> origin/feature/AddNewErrorsAndWalidation
