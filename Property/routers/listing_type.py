from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from Property import controllers
from App.models import ListingType
from Property.schemas.listing_type import ListingTypeSchema, ListingTypeUpdate

from App.database import get_db

listing_type_router = APIRouter(prefix="/listingtype")

@listing_type_router.get("/")
async def get_listing_type(db: Session = Depends(get_db)):
    return controllers.get_listing_type(db)

@listing_type_router.get("/{tag}")
async def get_brand_by_id(tag:str, db: Session = Depends(get_db)):
    return controllers.get_brand_by_id(tag,db)

@listing_type_router.post("/")
async def create_listing_type(listing:ListingTypeSchema, db:Session = Depends(get_db)):
    return controllers.create_listing_type(db,listing)

@listing_type_router.delete("/{tag}")
async def delete_listing_type(tag:str, db:Session = Depends(get_db)):
    return controllers.delete_listing_type(tag,db)

@listing_type_router.patch("/{tag}")
async def update_listing_type(tag:str, listing_type_update: ListingTypeUpdate, db:Session = Depends(get_db)):
    return controllers.update_listing_type(tag,listing_type_update, db)

# .................................... TOOGLE LISTING TYPE STATUS..........................
@listing_type_router.post("/{tag}/{enabled}")
def toogle_listing_type_status(tag : str, enabled: bool,  db: Session = Depends(get_db)):
    return controllers.toogle_listing_type_status(tag, enabled, db )

