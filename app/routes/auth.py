from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=schemas.Token)
def login(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.username).first()
    
    if user:
        if utils.verify_password(credentials.password, user.password):
            access_token = oauth2.create_access_token({
                "user_id": user.id
            })
            return { "access_token": access_token, "token_type": "Bearer" }
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email or password")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")