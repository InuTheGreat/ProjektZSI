from backend.domain.entities.species import Species


class SpeciesMapper:

    @staticmethod
    def to_domain(model) -> Species:
        return Species(
            id=model.id,
            public_id=model.public_id,

            common_name=model.common_name,
            scientific_name=model.scientific_name,

            family=model.family,
            genus=model.genus,

            distribution=model.distribution,
            habitat=model.habitat,

            max_length_cm=model.max_length_cm,
            max_weight_g=model.max_weight_g,

            diet=model.diet,
            votes_count=model.votes_count,  

        )