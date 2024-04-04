from fastapi import APIRouter,Depends, Body, HTTPException
from sqlalchemy.orm import Session
from Auth.controllers.password_reset import verify_code as controllers
from App.database import get_db

verify_password_reset_code_router = APIRouter(prefix="/verify-password-reset-code")


# ................................. VERIFY PASSWORD TOKEN ...............................................
@verify_password_reset_code_router.post("/")
async def verify_password_reset_code(payload: dict = Body(...), db: Session = Depends(get_db)):
    return controllers.verify_password_reset_code(payload, db)

 