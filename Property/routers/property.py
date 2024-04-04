from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from Property import controllers
from Property.schemas.property_schema import PropertySchema

from App.database import get_db

property_router = APIRouter(prefix="/properties")

@property_router.get("/")
async def get_properties(db: Session = Depends(get_db)):
    return controllers.get_properties(db)

@property_router.get("/{id}")
async def get_properties_by_id(id:str, db: Session = Depends(get_db)):
    return controllers.get_properties_by_id(id, db)

@property_router.post("/")
async def create_properties(property:PropertySchema, db:Session = Depends(get_db)):
    return controllers.create_properties(db, property)

@property_router.delete("/{id}")
async def delete_properties(id:str, db:Session = Depends(get_db)):
    return controllers.delete_properties(id, db)

@property_router.patch("/{id}")
async def update_properties(id:str, property_update: PropertySchema, db:Session = Depends(get_db)):
    return controllers.update_properties(id, property_update, db)

# .................................... TOOGLE PROPERTY STATUS..........................
@property_router.post("/{id}/{enabled}")
def toogle_property_status(id : str, enabled: bool,  db: Session = Depends(get_db)):
    return controllers.toogle_property_status(id, enabled, db )
