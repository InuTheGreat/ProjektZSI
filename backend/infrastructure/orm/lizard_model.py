from backend.utils.uuid import generate_uuid
from sqlalchemy import DateTime
from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from backend.infrastructure.orm.base import Base

class LizardModel(Base):
    __tablename__ = "lizards"

    id = Column(String(36), primary_key=True, default=generate_uuid)

    public_id = Column(Integer, unique=True, nullable=True)


    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    species_id = Column(String(36), ForeignKey("species.id"))

    species = relationship("SpeciesModel", back_populates="lizards")
