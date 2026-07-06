from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.connection import get_db
from app.models import User
from app.schemas import UserRegister, UserLogin
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    # Check if email already exists
    
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Create new user
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role="patient"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    # Check Email
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Verify Password
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    # Create JWT Token
    token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": db_user.id,
        "name": db_user.name
    }

from jose import JWTError, jwt

def decode_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None