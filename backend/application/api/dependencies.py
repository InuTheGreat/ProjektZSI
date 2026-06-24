from backend.infrastructure.uow.unit_of_work import UnitOfWork
from backend.infrastructure.core.redis_client import redis_client

def get_uow():
    uow = UnitOfWork()
    try:
        yield uow
    finally:
        uow.close()

def get_redis():
    return redis_client