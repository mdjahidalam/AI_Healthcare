from fastapi import FastAPI
from app.connection import engine, Base
from app.models import User
from app.routers.auth import router as auth_router
from app.routers.patient import router as patient_router
from app.routers.prediction import router as prediction_router
from app.routers.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Healthcare Platform"
)

app.include_router(auth_router)

app.include_router(patient_router)

app.include_router(prediction_router)

app.include_router(dashboard_router)

@app.get("/")
def home():
    return {
        "message": "AI Healthcare Platform Running Successfully 🚀"
    }

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)