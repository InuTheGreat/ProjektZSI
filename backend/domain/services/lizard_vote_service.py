from backend.utils.uuid import generate_uuid



class LizardVoteService:

    def __init__(self, uow):
        self.uow = uow

    def create_vote(self, title: str, species_ids: list[str]) -> str:
        if len(species_ids) != 4:
            raise ValueError("Exactly 4 lizards required")

        vote_id = generate_uuid()
        self.uow.lizard_votes.create_vote(vote_id, title)

        for species_id in species_ids:
            self.uow.lizard_votes.add_candidate(
                candidate_id=generate_uuid(),
                vote_id=vote_id,
                species_id=species_id,
            )

        return vote_id

    def vote(self, candidate_id: str) -> None:
        self.uow.lizard_votes.increment_vote(candidate_id)
        

    def get_results(self, vote_id: str):
        vote = self.uow.lizard_votes.get_vote(vote_id)
        candidates = self.uow.lizard_votes.get_candidates(vote_id)

        return {
            "vote": vote,
            "candidates": candidates,
        }