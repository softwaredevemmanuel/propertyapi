from fastapi import APIRouter,Depends, Request
from sqlalchemy.orm import Session
from Auth.controllers import resend_verification_code as controllers
from App.database import get_db


resend_email_verification_router = APIRouter(prefix="/resend-email-verification")


# Resend Email Verificaion Code
@resend_email_verification_router.post("/")
async def resend_email_verification(request: Request, db: Session = Depends(get_db)):
    return controllers.resend_email_verification(request, db)
    
