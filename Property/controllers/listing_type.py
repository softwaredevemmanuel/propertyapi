from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from App.models import ListingType
from Property.schemas.listing_type import ListingTypeSchema, ListingTypeUpdate

def get_listing_type(db: Session):
    listing = db.query(ListingType).all()
    return {
    "success": True,
        "message": "Listing type added successfully",
        "data" : listing    
    }

def get_brand_by_id(tag: str, db: Session):
    
    listing_query = db.query(ListingType).filter(ListingType.tag == tag).first()
  

    if listing_query is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return {
        "success": True,
        "message": "Listing retrieved successfully",
        "data": listing_query
    }

def create_listing_type(db: Session, listing: ListingTypeSchema):

    if  db.query(ListingType).filter(ListingType.tag == listing.tag).first():
        raise HTTPException(status_code=401, detail="Listing type already exist")
    
    new_brand = ListingType(**listing.model_dump())
   
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return {
        "success": True,
        "message": "Listing type added successfully",
        "data" : new_brand
        }

def delete_listing_type(tag: str, db: Session):
    brand_to_delete = db.query(ListingType).filter(ListingType.tag == tag).first()
    if brand_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Listing type does not exist")
    
    db.delete(brand_to_delete)
    db.commit()
    return {
        "success": True,
        "message": "Listing type deleted successfully"
    }

def update_listing_type(tag: str, listing_type_update: ListingTypeUpdate, db: Session):

    listing_type = db.query(ListingType).filter(ListingType.tag == tag).first()
    
    if not listing_type:
        raise HTTPException(status_code=404, detail="Listing type not found")
    
    for field, value in listing_type_update.dict().items():
        setattr(listing_type, field, value)
    
    db.commit()
    
    return {
        "success": True,
        "message": "Listing type updated successfully"
    }


#............................... TOOGLE LISTING TYPE ENABLED STATUS ............................
def toogle_listing_type_status(tag: str, enabled: bool,  db: Session):
        
    listing_type = db.query(ListingType).filter(ListingType.tag == tag).first()

    if not listing_type:
        raise HTTPException(status_code=404, detail="Listing type not found")
    
   
    listing_type.enabled = enabled
    db.commit()


    return {
            "success": True,
            "message": "Status toggled successfully"
            }

