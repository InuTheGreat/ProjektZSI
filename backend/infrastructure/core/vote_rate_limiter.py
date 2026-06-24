VOTE_TTL_SECONDS = 24 * 60 * 60

def build_vote_key(species_id: str, voter_id: str) -> str:
    return f"vote:{species_id}:{voter_id}"

def has_already_voted(redis_client, species_id: str, voter_id: str) -> bool:
    key = build_vote_key(species_id, voter_id)
    return redis_client.exists(key) == 1

def register_vote(redis_client, species_id: str, voter_id: str) -> None:
    key = build_vote_key(species_id, voter_id)
    redis_client.setex(key, VOTE_TTL_SECONDS, "1")