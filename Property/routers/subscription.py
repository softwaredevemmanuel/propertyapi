from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from Property import controllers
from Property.schemas.subscription import SubscriptionSchema, UpdateSubscriptionSchema

from App.database import get_db

subscription_router = APIRouter(prefix="/subscriptions")

@subscription_router.get("/")
async def get_subscriptions(db: Session = Depends(get_db)):
    return controllers.get_subscriptions(db)

@subscription_router.get("/{id}")
async def get_get_subscriptions_by_id(id:str, db: Session = Depends(get_db)):
    return controllers.get_subscriptions_by_id(id, db)

@subscription_router.post("/")
async def create_subscription(subscriptions:SubscriptionSchema, db:Session = Depends(get_db)):
    return controllers.create_subscription(db, subscriptions)

@subscription_router.delete("/{id}")
async def delete_subscription(id:str, db:Session = Depends(get_db)):
    return controllers.delete_subscription(id, db)

@subscription_router.patch("/{id}")
async def update_subscription(id:str, subscriptions_update: UpdateSubscriptionSchema, db:Session = Depends(get_db)):
    return controllers.update_subscription(id, subscriptions_update, db)