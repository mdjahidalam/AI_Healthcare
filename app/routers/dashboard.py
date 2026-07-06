from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.connection import get_db
from app.models import User, Patient, Prediction

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/summary")
def dashboard_summary(
        db: Session = Depends(get_db)
):

    total_users = db.query(User).count()

    total_patients = db.query(Patient).count()

    total_predictions = db.query(Prediction).count()

    high_risk = db.query(Prediction).filter(
        Prediction.risk_level == "High"
    ).count()

    low_risk = db.query(Prediction).filter(
        Prediction.risk_level == "Low"
    ).count()

    return {

        "total_users": total_users,

        "total_patients": total_patients,

        "total_predictions": total_predictions,

        "high_risk": high_risk,

        "low_risk": low_risk

    }

@router.get("/recent-predictions")
def recent_predictions(
        db: Session = Depends(get_db)
):

    predictions = db.query(Prediction)\
        .order_by(Prediction.created_at.desc())\
        .limit(10)\
        .all()

    return predictions

@router.get("/high-risk")
def high_risk_patients(
        db: Session = Depends(get_db)
):

    data = db.query(Prediction).filter(
        Prediction.risk_level == "High"
    ).all()

    return data

@router.get("/statistics")
def statistics(
        db: Session = Depends(get_db)
):

    high = db.query(Prediction).filter(
        Prediction.risk_level == "High"
    ).count()

    low = db.query(Prediction).filter(
        Prediction.risk_level == "Low"
    ).count()

    total = db.query(Prediction).count()

    return {

        "total_predictions": total,

        "high_risk": high,

        "low_risk": low

    }