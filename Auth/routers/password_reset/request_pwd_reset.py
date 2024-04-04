from fastapi import APIRouter,Depends, Body, Request
from sqlalchemy.orm import Session
from Auth.controllers.password_reset import request_pwd_reset as controllers
from App.database import get_db

request_password_reset_router = APIRouter(prefix="/request-password-reset")


@request_password_reset_router.post("/")
async def request_password_reset(request: Request, payload: dict = Body(...), db: Session = Depends(get_db)):
    return controllers.request_password_reset(request, payload, db)

