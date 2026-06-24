from sqlalchemy.orm import sessionmaker
from backend.infrastructure.orm.base import Base
from backend.infrastructure.orm.lizard_model import LizardModel
from backend.infrastructure.orm.species_model import SpeciesModel
from backend.infrastructure.orm.account_model import AccountModel

from sqlalchemy import create_engine
import os

DATABASE_URL = (
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASS')}@"
    f"{os.getenv('DB_HOST')}:3306/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)


