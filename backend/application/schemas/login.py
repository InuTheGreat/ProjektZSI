from pydantic import BaseModel, Field
from pydantic import EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
<<<<<<< HEAD
    password: str 
=======
    password: str = Field(min_length=8, max_length=100)
>>>>>>> origin/feature/AddNewErrorsAndWalidation
