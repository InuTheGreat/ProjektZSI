# Struktura projektu
 
## Stack
- Python 3.14
- FastAPI
- SQLAlchemy (ORM)
- Docker 
- Nginx
## Architektura
Projekt oparty o Domain-Driven Design (DDD) z podziałem na trzy warstwy: `application`, `domain`, `infrastructure`.
 
---
 
## Drzewo plików
 
```
/
├── backend/
│   ├── __pycache__/
│   │   ├── __init__.cpython-314.pyc
│   │   └── main.cpython-314.pyc
│   ├── application/
│   │   ├── api/
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-314.pyc
│   │   │   │   └── dependencies.cpython-314.pyc
│   │   │   ├── routers/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── __init__.cpython-314.pyc
│   │   │   │   │   ├── lizard_router.cpython-314.pyc
│   │   │   │   │   ├── lizard_vote_router.cpython-314.pyc
│   │   │   │   │   └── species_router.cpython-314.pyc
│   │   │   │   ├── __init__.py
│   │   │   │   ├── lizard_router.py
│   │   │   │   ├── lizard_vote_router.py
│   │   │   │   └── species_router.py
│   │   │   ├── __init__.py
│   │   │   └── dependencies.py
│   │   └── schemas/
│   │       ├── __pycache__/
│   │       │   ├── __init__.cpython-314.pyc
│   │       │   ├── lizard.cpython-314.pyc
│   │       │   ├── lizard_response.cpython-314.pyc
│   │       │   ├── lizard_vote.cpython-314.pyc
│   │       │   ├── lizard_vote_response.cpython-314.pyc
│   │       │   ├── species.cpython-314.pyc
│   │       │   └── species_response.cpython-314.pyc
│   │       ├── __init__.py
│   │       ├── lizard.py
│   │       ├── lizard_response.py
│   │       ├── lizard_vote.py
│   │       ├── lizard_vote_response.py
│   │       ├── species.py
│   │       └── species_response.py
│   ├── domain/
│   │   ├── entities/
│   │   │   ├── __pycache__/
│   │   │   │   ├── lizard.cpython-314.pyc
│   │   │   │   ├── lizard_vote.cpython-314.pyc
│   │   │   │   ├── lizard_vote_candidate.cpython-314.pyc
│   │   │   │   └── species.cpython-314.pyc
│   │   │   ├── __init__.py
│   │   │   ├── lizard.py
│   │   │   ├── lizard_vote.py
│   │   │   ├── lizard_vote_candidate.py
│   │   │   └── species.py
│   │   ├── exceptions/
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-314.pyc
│   │   │   │   └── custom_exceptions.cpython-314.pyc
│   │   │   ├── __init__.py
│   │   │   ├── custom_exceptions.py
│   │   │   └── global_handler_exceptions.py
│   │   └── services/
│   │       ├── __pycache__/
│   │       │   ├── __init__.cpython-314.pyc
│   │       │   ├── lizard_service.cpython-314.pyc
│   │       │   ├── lizard_vote_service.cpython-314.pyc
│   │       │   └── species_service.cpython-314.pyc
│   │       ├── __init__.py
│   │       ├── lizard_service.py
│   │       ├── lizard_vote_service.py
│   │       └── species_service.py
│   ├── infrastructure/
│   │   ├── core/
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-314.pyc
│   │   │   │   └── db.cpython-314.pyc
│   │   │   ├── __init__.py
│   │   │   └── db.py
│   │   ├── mappers/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── lizard_mapper.py
│   │   │   ├── lizard_vote_candidate_mapper.py
│   │   │   ├── lizard_vote_mapper.py
│   │   │   └── species_mapper.py
│   │   ├── orm/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── lizard_model.py
│   │   │   ├── lizard_vote_candidate_model.py
│   │   │   ├── lizard_vote_model.py
│   │   │   └── species_model.py
│   │   ├── repositories/
│   │   │   ├── __pycache__/
│   │   │   ├── lizard_repositories.py
│   │   │   ├── lizard_vote_repository.py
│   │   │   └── species_repositories.py
│   │   └── uow/
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       └── unit_of_work.py
│   ├── scripts/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── create_lizards.py
│   │   ├── create_species.py
│   │   ├── test_db.py
│   │   └── test_exceptions.py
│   ├── static/
│   │   └── index.html
│   ├── utils/
│   │   ├── __pycache__/
│   │   └── uuid.py
│   ├── __init__.py
│   └── main.py
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── nginx.conf
└── requirements.txt
```
 
---