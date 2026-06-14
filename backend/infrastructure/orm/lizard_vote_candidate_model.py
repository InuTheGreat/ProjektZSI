from sqlalchemy import Column, ForeignKey, Integer, String

from backend.utils.uuid import generate_uuid
from backend.infrastructure.orm.base import Base
from sqlalchemy.orm import relationship

class LizardVoteCandidateModel(Base):
    __tablename__ = "lizard_vote_candidates"

    id = Column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    vote_id = Column(
        String(36),
        ForeignKey("lizard_votes.id"),
        nullable=False,
    )

    species_id = Column(
        String(36),
        ForeignKey("species.id"),
        nullable=False,
    )

    votes_count = Column(
        Integer,
        nullable=False,
        default=0,
    )

    vote = relationship(
        "LizardVoteModel",
        back_populates="candidates",
    )

    species = relationship(
        "SpeciesModel",
    )
