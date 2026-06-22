# Naprawa błędów krytycznych — gałąź `fix/critical-issues`

## 1. Skrypty seedujące (`create_lizards.py`, `create_species.py`)

### Problem
Oba skrypty tworzyły obiekt repozytorium (`LizardRepository` / `SpeciesRepository`) i przekazywały go bezpośrednio do serwisu:

```python
# BYŁO (błąd)
repo = LizardRepository(db)
service = LizardService(repo)
```

`LizardService` i `SpeciesService` oczekują obiektu `UnitOfWork`, bo odwołują się do `self.uow.lizards` / `self.uow.species`. Przekazanie repozytorium powodowało `AttributeError` przy pierwszym wywołaniu metody serwisu.

### Naprawa
```python
# JEST (poprawnie)
uow = UnitOfWork()
service = LizardService(uow)
# ...
uow.close()
```

**Pliki:** `backend/scripts/create_lizards.py`, `backend/scripts/create_species.py`

---

## 2. `increment_vote` ignoruje brakujący kandydat

### Problem
`LizardVoteRepository.increment_vote()` kończyło działanie bez żadnego efektu gdy `candidate_id` nie istniał w bazie:

```python
# BYŁO (błąd)
if not candidate:
    return  # cicha porażka
```

Router obsługuje `NotFoundError` w endpointcie `POST /votes/{candidate_id}/vote`, ale nigdy go nie dostawał — odpowiedź była zawsze `200 OK` nawet dla nieistniejącego kandydata.

### Naprawa
```python
# JEST (poprawnie)
if not candidate:
    raise NotFoundError(f"Candidate {candidate_id} not found")
```

**Plik:** `backend/infrastructure/repositories/lizard_vote_repository.py`

---

## 3. `get_results` nie rzuca `NotFoundError`

### Problem
`LizardVoteService.get_results()` zwracało `{"vote": None, "candidates": [...]}` gdy głosowanie o danym `vote_id` nie istniało. Router próbował potem dostać się do `result["vote"].id` na obiekcie `None`, co powodowało `AttributeError` i odpowiedź `500 Internal Server Error` zamiast `404 Not Found`.

```python
# BYŁO (błąd)
def get_results(self, vote_id: str):
    vote = self.uow.lizard_votes.get_vote(vote_id)
    # brak sprawdzenia — vote może być None
    candidates = self.uow.lizard_votes.get_candidates(vote_id)
    return {"vote": vote, "candidates": candidates}
```

### Naprawa
```python
# JEST (poprawnie)
def get_results(self, vote_id: str):
    vote = self.uow.lizard_votes.get_vote(vote_id)
    if not vote:
        raise NotFoundError(f"Vote {vote_id} not found")
    candidates = self.uow.lizard_votes.get_candidates(vote_id)
    return {"vote": vote, "candidates": candidates}
```

**Plik:** `backend/domain/services/lizard_vote_service.py`

---

## Podsumowanie zmian

| Plik | Zmiana |
|---|---|
| `backend/scripts/create_lizards.py` | Zastąpiono `LizardRepository(db)` → `UnitOfWork()` |
| `backend/scripts/create_species.py` | Zastąpiono `SpeciesRepository(db)` → `UnitOfWork()` |
| `backend/infrastructure/repositories/lizard_vote_repository.py` | `increment_vote` rzuca `NotFoundError` zamiast `return` |
| `backend/domain/services/lizard_vote_service.py` | `get_results` rzuca `NotFoundError` gdy głosowanie nie istnieje |

Commit: `136405b` na gałęzi `fix/critical-issues`.
