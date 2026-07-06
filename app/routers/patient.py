from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.connection import get_db
from app.models import Patient, User
from app.schemas import PatientCreate,PatientUpdate

router = APIRouter(
    prefix="/patient",
    tags=["Patient"]
)

@router.post("/")
def add_patient(patient: PatientCreate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == patient.user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_patient = Patient(
        user_id=patient.user_id,
        age=patient.age,
        gender=patient.gender,
        blood_pressure=patient.blood_pressure,
        cholesterol=patient.cholesterol,
        glucose=patient.glucose,
        heart_rate=patient.heart_rate
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient Added Successfully"
    }

@router.get("/")
def get_all_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()

    return patients

@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient Not Found"
        )

    return patient

@router.put("/{patient_id}")
def update_patient(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db)
):

    db_patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not db_patient:
        raise HTTPException(
            status_code=404,
            detail="Patient Not Found"
        )

    db_patient.age = patient.age
    db_patient.gender = patient.gender
    db_patient.blood_pressure = patient.blood_pressure
    db_patient.cholesterol = patient.cholesterol
    db_patient.glucose = patient.glucose
    db_patient.heart_rate = patient.heart_rate

    db.commit()
    db.refresh(db_patient)

    return {
        "message": "Patient Updated Successfully"
    }

@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient Not Found"
        )

    db.delete(patient)
    db.commit()

    return {
        "message": "Patient Deleted Successfully"
    }