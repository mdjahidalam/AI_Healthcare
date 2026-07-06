from sqlalchemy import Column, Integer, String,Float,DateTime
from app.connection import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default="patient")


class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    age = Column(Integer)

    gender = Column(String(20))

    blood_pressure = Column(String(20))

    cholesterol = Column(Integer)

    glucose = Column(Integer)

    heart_rate = Column(Integer)

    user = relationship("User")



class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    prediction = Column(String(50))

    risk_level = Column(String(20))

    confidence = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)

    patient = relationship("Patient")