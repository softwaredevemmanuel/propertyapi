from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from App.models import Property
from Property.schemas.property_schema import PropertySchema
from uuid import UUID, uuid4


def get_properties(db: Session):
    property_query =  db.query(Property).all()
    return {
        "success": True,
        "message": "Properties retrieved successfully",
        "data": property_query
    }

def get_properties_by_id(id: str, db: Session):
    try:
        uuid_obj = UUID(id, version=4)  # Attempt to convert the string to a UUID
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID format, must be a valid UUID")

    property_query = db.query(Property).filter(Property.id == uuid_obj).first()

    if not property_query:
        raise HTTPException(status_code=404, detail="Property does not exist")

    return {
        "success": True,
        "message": "Property retrieved successfully",
        "data": property_query
    }

def create_properties(db: Session, property: PropertySchema):

    if  db.query(Property).filter(Property.label == property.label).first():
        raise HTTPException(status_code=404, detail="Property already exist")
    
    new_brand = Property(**property.model_dump())
   
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand

def delete_properties(id: str, db: Session):
    property_to_delete = db.query(Property).filter(Property.id == id).first()
    if property_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Property does not exist")
    
    db.delete(property_to_delete)
    db.commit()
    return {
        "success": True,
        "message": "Property deleted successfully"
    }

def update_properties(id: str, property_update: PropertySchema, db: Session):

    listing_type = db.query(Property).filter(Property.id == id).first()
    
    if not listing_type:
        raise HTTPException(status_code=404, detail="Listing type not found")
    
    for field, value in property_update.dict().items():
        setattr(listing_type, field, value)
    
    db.commit()
    
    return {
        "success": True,
        "message": "Propery updated successfully"
    }



#............................... TOOGLE A PROPERTY ENABLED STATUS ............................
def toogle_property_status(id: str, enabled: bool,  db: Session):
        
    property = db.query(Property).filter(Property.id == id).first()

    if not property:
        raise HTTPException(status_code=404, detail="Listing type not found")
    
   
    property.enabled = enabled
    db.commit()


    return {
            "success": True,
            "message": "Status toggled successfully"
            }