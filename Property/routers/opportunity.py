from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from Property import controllers
from Property.schemas.opportunity_schema import OpportunitySchema

from App.database import get_db

opportunity_router = APIRouter(prefix="/opportunities")

@opportunity_router.get("/")
async def get_opportunities(db: Session = Depends(get_db)):
    return controllers.get_opportunities(db)

@opportunity_router.get("/{id}")
async def get_opportunities_by_id(id:str, db: Session = Depends(get_db)):
    return controllers.get_opportunities_by_id(id, db)

@opportunity_router.post("/")
async def create_opportunities(opportunity:OpportunitySchema, db:Session = Depends(get_db)):
    return controllers.create_opportunities(db, opportunity)

@opportunity_router.delete("/{id}")
async def delete_opportunities(id:str, db:Session = Depends(get_db)):
    return controllers.delete_opportunities(id, db)

@opportunity_router.patch("/{id}")
async def update_opportunities(id:str, opportunity_update: OpportunitySchema, db:Session = Depends(get_db)):
    return controllers.update_opportunities(id, opportunity_update, db)

# .................................... TOOGLE OPPORTUNITY STATUS..........................
@opportunity_router.post("/{id}/{enabled}")
def toogle_opportunity_status(id : str, enabled: bool,  db: Session = Depends(get_db)):
    return controllers.toogle_opportunity_status(id, enabled, db )
