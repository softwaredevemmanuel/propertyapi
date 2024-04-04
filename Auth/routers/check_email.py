from fastapi import APIRouter,Depends, Body
from sqlalchemy.orm import Session
from Auth.controllers import check_email as controllers
from Auth.schemas.check_email import EmailCheckRequest
from App.database import get_db


check_email_router = APIRouter(prefix="/check-email")

# Verify email Code
@check_email_router.post("/")
async def check_email(request_data: EmailCheckRequest, db: Session = Depends(get_db)):
    return controllers.check_email(request_data, db)
    
@check_email_router.get("/")
async def get_investment_plan(db: Session = Depends(get_db)):
    return controllers.get_users(db)
