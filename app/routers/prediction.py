from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.connection import get_db

from app.schemas import HeartPrediction

from app.ml.predict import predict_heart

from app.models import Prediction

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post("/heart")
def predict(
        data: HeartPrediction,
        db: Session = Depends(get_db)
):

    result = predict_heart(data.dict())

    history = Prediction(

        patient_id=data.patient_id,

        prediction=result["prediction"],

        risk_level=result["risk_level"],

        confidence=result["confidence"]

    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return result

@router.get("/history")
def get_prediction_history(
    db: Session = Depends(get_db)
):

    history = db.query(Prediction).all()

    return history

@router.get("/history/{patient_id}")
def get_patient_history(
        patient_id: int,
        db: Session = Depends(get_db)
):

    history = db.query(Prediction).filter(
        Prediction.patient_id == patient_id
    ).all()

    if not history:

        raise HTTPException(
            status_code=404,
            detail="Prediction History Not Found"
        )

    return history