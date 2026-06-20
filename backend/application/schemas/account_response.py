from pydantic import BaseModel


class AccountResponse(
    BaseModel
):
    id: str
    first_name: str
    last_name: str
    email: str
    role: str