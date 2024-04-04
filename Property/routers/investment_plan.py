from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from Property import controllers
from Property.schemas.investment_plan import InvestmentPlanSchema

from App.database import get_db

investment_plan_router = APIRouter(prefix="/investmentplans")

@investment_plan_router.get("/")
async def get_investment_plan(db: Session = Depends(get_db)):
    return controllers.get_investment_plan(db)

@investment_plan_router.get("/{id}")
async def get_investment_plan_by_id(id:str, db: Session = Depends(get_db)):
    return controllers.get_investment_plan_by_id(id, db)

@investment_plan_router.post("/")
async def create_investment_plan(opportunity:InvestmentPlanSchema, db:Session = Depends(get_db)):
    return controllers.create_investment_plan(db, opportunity)

@investment_plan_router.delete("/{id}")
async def delete_investment_plan(id:str, db:Session = Depends(get_db)):
    return controllers.delete_investment_plan(id, db)

@investment_plan_router.patch("/{id}")
async def update_investment_plan(id:str, opportunity_update: InvestmentPlanSchema, db:Session = Depends(get_db)):
    return controllers.update_investment_plan(id, opportunity_update, db)


# .................................... TOOGLE INVESTMENT PLAN STATUS..........................
@investment_plan_router.post("/{id}/{enabled}")
def toogle_investmentplan_status(id : str, enabled: bool,  db: Session = Depends(get_db)):
    return controllers.toogle_investmentplan_status(id, enabled, db )