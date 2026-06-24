# Struktura projektu
 
## Stos Technologiczny
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
│   ├── application/
│   │   ├── api/
│   │   │   ├── __pycache__/
│   │   │   ├── routers/
│   │   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── account_router.py
│   │   │   │   └── species_router.py
│   │   │   ├── __init__.py
│   │   │   └── dependencies.py
│   │   └── schemas/
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       ├── account.py
│   │       ├── account_response.py
│   │       ├── login.py
│   │       ├── role_update.py
│   │       ├── token_response.py
│   │       ├── species.py
│   │       └── species_response.py
│   ├── auth/
│   │   ├── __init__.py
│   │   └── auth_dependency.py
│   ├── domain/
│   │   ├── entities/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── account.py
│   │   │   └── species.py
│   │   ├── exceptions/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── custom_exceptions.py
│   │   │   └── global_handler_exceptions.py
│   │   └── services/
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       ├── account_service.py
│   │       ├── auth_service.py
│   │       ├── jwt_service.py
│   │       ├── password_service.py
│   │       └── species_service.py
│   ├── infrastructure/
│   │   ├── core/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── db.py
│   │   │   ├── redis_client.py
│   │   │   └── vote_rate_limiter.py
│   │   ├── mappers/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── account_mapper.py
│   │   │   └── species_mapper.py
│   │   ├── orm/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── account_model.py
│   │   │   ├── base.py
│   │   │   └── species_model.py
│   │   ├── repositories/
│   │   │   ├── __pycache__/
│   │   │   ├── account_repositories.py
│   │   │   └── species_repositories.py
│   │   └── uow/
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       └── unit_of_work.py
│   ├── scripts/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── create_species.py
│   │   ├── test_db.py
│   │   └── test_exceptions.py
│   ├── utils/
│   │   ├── __pycache__/
│   │   ├── uuid.py
│   │   └── user_role.py
│   ├── static/
│   │   └── index.html
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