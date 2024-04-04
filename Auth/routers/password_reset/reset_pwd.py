from fastapi import APIRouter,Depends, Body, HTTPException, Request
from sqlalchemy.orm import Session
from Auth.controllers.password_reset import reset_pwd as controllers
from App.database import get_db

reset_password_router = APIRouter(prefix="/reset-password")


# Reset Password
@reset_password_router.post("/")
async def reset_password(request: Request, payload: dict = Body(...), db: Session = Depends(get_db)):  
    return controllers.reset_password(request, payload, db)
    
