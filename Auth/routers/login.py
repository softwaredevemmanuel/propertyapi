from fastapi import APIRouter,Depends, Body, Request, HTTPException
from sqlalchemy.orm import Session
from Auth.controllers import login as controllers
from App.database import get_db

login_router = APIRouter(prefix="/login")

@login_router.post("/")
async def login(request: Request, payload: dict = Body(...), db: Session = Depends(get_db)):   
    return controllers.login(request, payload, db) 
