from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class PatientCreate(BaseModel):
    age: int
    gender: str
    blood_pressure: str
    cholesterol: int
    glucose: int
    heart_rate: int

class PatientUpdate(BaseModel):
    age: int
    gender: str
    blood_pressure: str
    cholesterol: int
    glucose: int
    heart_rate: int

class HeartPrediction(BaseModel):
    patient_id: int
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

class PredictionResponse(BaseModel):

    id:int

    patient_id:int

    prediction:str

    risk_level:str

    confidence:float

    created_at:datetime

    class Config:
        from_attributes=True