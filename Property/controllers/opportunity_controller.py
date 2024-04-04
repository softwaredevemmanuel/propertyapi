from fastapi import HTTPException,status
from sqlalchemy.orm import Session, joinedload

from App.models import OpportunityModel
from Property.schemas.opportunity_schema import OpportunitySchema
from Property.models.property import Property
from uuid import UUID, uuid4


def get_opportunities(db: Session):
    opportunity_query = db.query(OpportunityModel).options(joinedload(OpportunityModel.property), joinedload(OpportunityModel.investment_plan)).all()

    return {
        "success": True,
        "message": "Opportunity retrieved successfully",
        "data": opportunity_query
    }

def get_opportunities_by_id(id:str, db: Session):

    try:
        uuid_obj = UUID(id, version=4)  # Attempt to convert the string to a UUID
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID format, must be a valid UUID")

    opportunity_query = db.query(OpportunityModel).filter(OpportunityModel.id == uuid_obj).options(joinedload(OpportunityModel.property), joinedload(OpportunityModel.investment_plan)).first()

    if opportunity_query is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return {
        "success": True,
        "message": "Opportunity retrieved successfully",
        "data": opportunity_query
    }

def create_opportunities(db: Session, opportunity: OpportunitySchema):

    if not db.query(Property).filter(Property.id == opportunity.property_id).first():
        raise HTTPException(status_code=401, detail="Property with the provided property_id does not exist")


    if  (db.query(OpportunityModel).filter(OpportunityModel.property_id == opportunity.property_id).first() and db.query(OpportunityModel).filter(OpportunityModel.listing_type == opportunity.listing_type).first()):
        raise HTTPException(status_code=401, detail="Opportunity already exist")
    
    new_brand = OpportunityModel(**opportunity.model_dump())
   
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return {
        "success": True,
        "message": "Opportunity added successfully",
        "data" : new_brand
        }




def delete_opportunities(id: str, db: Session):

    opportunity_to_delete = db.query(OpportunityModel).filter(OpportunityModel.id == id).first()

    if opportunity_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Opportunity does not exist")
    
    db.delete(opportunity_to_delete)
    db.commit()
    return {
        "success": True,
        "message": "Opportunity deleted successfully"
    }


def update_opportunities(id: str, opportunity_update: OpportunitySchema, db: Session):

    listing_type = db.query(OpportunityModel).filter(OpportunityModel.id == id).first()

    if not db.query(Property).filter(Property.id == opportunity_update.property_id).first():
        raise HTTPException(status_code=404, detail="Property with the provided property_id does not exist")

    
    if not listing_type:
        raise HTTPException(status_code=404, detail="Listing type not found")
    
    for field, value in opportunity_update.dict().items():
        setattr(listing_type, field, value)
    
    db.commit()
    
    return {
        "success": True,
        "message": "Opportunity updated successfully"
    }


#............................... TOOGLE OPPORTUNITY TYPE ENABLED STATUS ............................
def toogle_opportunity_status(id: str, enabled: bool,  db: Session):
        
    opportunity = db.query(OpportunityModel).filter(OpportunityModel.id == id).first()

    if not opportunity:
        raise HTTPException(status_code=404, detail="Opportunity type not found")
    
   
    opportunity.enabled = enabled
    db.commit()


    return {
            "success": True,
            "message": "Status toggled successfully"
            }
