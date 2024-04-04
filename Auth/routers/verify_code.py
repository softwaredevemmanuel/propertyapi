from fastapi import APIRouter,Depends, Request, Body
from sqlalchemy.orm import Session
from Auth.controllers import verify_code as controllers
from App.database import get_db


verify_code_router = APIRouter(prefix="/verify-email")

# Verify email Code
@verify_code_router.post("/")
async def verify_code(request: Request, payload: dict = Body(...), db: Session = Depends(get_db)):  
    return controllers.verify_code(request, payload, db)
    
