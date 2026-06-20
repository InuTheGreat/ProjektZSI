from pydantic import BaseModel
from pydantic import EmailStr


class AccountCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str