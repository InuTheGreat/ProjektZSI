from dataclasses import dataclass


@dataclass
class Account:
    id: str
    first_name: str
    last_name: str
    email: str
    password_hash: str
    role: str