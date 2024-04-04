from fastapi import APIRouter,Depends, Body
from sqlalchemy.orm import Session
from Auth.controllers import register as controllers
from App.database import get_db

register_router = APIRouter()



# .................................... CREATE USER ......................................

@register_router.post("/register")
async def register_user_profile(payload: dict = Body(...), db: Session = Depends(get_db)):
    return controllers.register_user_profile(payload, db)
