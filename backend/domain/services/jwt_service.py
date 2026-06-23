from datetime import datetime
from datetime import timedelta

from jose import jwt


class JwtService:

    SECRET_KEY = "CHANGE_ME"

    ALGORITHM = "HS256"

    @classmethod
    def generate_token(
        cls,
        account_id: str,
        role: str,
    ):
        payload = {
            "sub": account_id,
            "role": role,
            "exp": datetime.utcnow()
            + timedelta(hours=12),
        }

        return jwt.encode(
            payload,
            cls.SECRET_KEY,
            algorithm=cls.ALGORITHM,
        )