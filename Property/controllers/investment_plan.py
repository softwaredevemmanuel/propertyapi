from fastapi import HTTPException,status
from sqlalchemy.orm import Session, joinedload

from App.models import InvestmentPlan
from Property.schemas.investment_plan import InvestmentPlanSchema
from Property.models.opportunity_model import OpportunityModel

def get_investment_plan(db: Session):
    investment_query = db.query(InvestmentPlan).options(joinedload(InvestmentPlan.opportunity)).all()

    return {
        "success": True,
        "message": "Investment Plans retrieved successfully",
        "data": investment_query
    }

def get_investment_plan_by_id(id:str, db: Session):

    investment = db.query(InvestmentPlan).filter(InvestmentPlan.id == id).options(joinedload(InvestmentPlan.opportunity)).first()
    
    if investment is None:
        raise HTTPException(status_code=404, detail="Investment not found")

    return {
        "success": True,
        "message": "Investment retrieved successfully",
        "data": investment
    }


def create_investment_plan(db: Session, opportunity: InvestmentPlanSchema):

    if not db.query(OpportunityModel).filter(OpportunityModel.id == opportunity.opportunity_id).first():
        raise HTTPException(status_code=401, detail="Opportunity with the provided opportunity does not exist")


    if  db.query(InvestmentPlan).filter(InvestmentPlan.opportunity_id == opportunity.opportunity_id).first():
        raise HTTPException(status_code=401, detail="Opportunity already exist")
    
    new_brand = InvestmentPlan(**opportunity.model_dump())
   
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand


def delete_investment_plan(id: str, db: Session):
    
    opportunity_to_delete = db.query(InvestmentPlan).filter(InvestmentPlan.id == id).first()

    if opportunity_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Investment plan does not exist")
    
    db.delete(opportunity_to_delete)
    db.commit()
    return {
        "success": True,
        "message": "Investment plan deleted successfully"
    }


def update_investment_plan(id: str, opportunity_update: InvestmentPlanSchema, db: Session):

    listing_type = db.query(InvestmentPlan).filter(InvestmentPlan.id == id).first()

    if not db.query(OpportunityModel).filter(OpportunityModel.id == opportunity_update.opportunity_id).first():
        raise HTTPException(status_code=404, detail="Opportunity with the provided opportunity_id does not exist")

    
    if not listing_type:
        raise HTTPException(status_code=404, detail="Opportunity type not found")
    
    for field, value in opportunity_update.dict().items():
        setattr(listing_type, field, value)
    
    db.commit()
    
    return {
        "success": True,
        "message": "Opportunity updated successfully"
    }


#............................... TOOGLE INVESTMENT PLAN STATUS ............................
def toogle_investmentplan_status(id: str, enabled: bool,  db: Session):
        
    opportunity = db.query(InvestmentPlan).filter(InvestmentPlan.id == id).first()

    if not opportunity:
        raise HTTPException(status_code=404, detail="Investment plan not found")
    
   
    opportunity.enabled = enabled
    db.commit()


    return {
            "success": True,
            "message": "Status toggled successfully"
            }
