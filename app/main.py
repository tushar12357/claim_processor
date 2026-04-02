from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Claim Processing API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for assignment it's fine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api")