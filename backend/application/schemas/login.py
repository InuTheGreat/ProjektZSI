from pydantic import BaseModel, Field
from pydantic import EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)