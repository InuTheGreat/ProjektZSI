from fastapi import FastAPI
from backend.application.api.routers.lizard_vote_router import router as lizard_vote_router
from backend.application.api.routers.lizard_router import router as lizard_router
from backend.application.api.routers.species_router import router as species_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lizard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lizard_router)
app.include_router(species_router)
app.include_router(lizard_vote_router)
