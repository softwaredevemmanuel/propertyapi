from fastapi import HTTPException,status
from sqlalchemy.orm import Session, joinedload

from App.models import Subscription, OpportunityModel
from Property.schemas.subscription import SubscriptionSchema, UpdateSubscriptionSchema

def get_subscriptions(db: Session):
    subscriptions_query = db.query(Subscription).options(joinedload(Subscription.opportunity)).all()

    return {
        "success": True,
        "message": "Subscription Plans retrieved successfully",
        "data": subscriptions_query
    }

def get_subscriptions_by_id(id:str, db: Session):

       # Query the database to retrieve the investment plan with the given ID
    subscriptions_query = db.query(Subscription).filter(Subscription.id == id).options(joinedload(Subscription.opportunity)).first()
    
    # Check if the investment plan exists
    if subscriptions_query is None:
        raise HTTPException(status_code=404, detail="Investment not found")

    # Return the retrieved investment plan
    return {
        "success": True,
        "message": "Investment retrieved successfully",
        "data": subscriptions_query
    }


def create_subscription(db: Session, subscriptions: SubscriptionSchema):

      # Check if the property_id exists in the Property database
    if not db.query(OpportunityModel).filter(OpportunityModel.id == subscriptions.opportunity_id).first():
        raise HTTPException(status_code=404, detail="Opportunity with the provided opportunity does not exist")


    if  db.query(Subscription).filter(Subscription.opportunity_id == subscriptions.opportunity_id).first():
        raise HTTPException(status_code=404, detail="Opportunity already exist")
    
    subscriptions_query = Subscription(**subscriptions.model_dump())
   
    db.add(subscriptions_query)
    db.commit()
    db.refresh(subscriptions_query)
    return subscriptions_query


def delete_subscription(id: str, db: Session):
    
    opportunity_to_delete = db.query(Subscription).filter(Subscription.id == id).first()

    if opportunity_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Investment plan does not exist")
    
    db.delete(opportunity_to_delete)
    db.commit()
    return {
        "success": True,
        "message": "Investment plan deleted successfully"
    }


def update_subscription(id: str, subscriptions_update: UpdateSubscriptionSchema, db: Session):

    # Retrieve the listing type from the database
    subscriptions_type = db.query(Subscription).filter(Subscription.id == id).first()

    
    # Check if the listing type exists
    if not subscriptions_type:
        raise HTTPException(status_code=404, detail="Subscription type not found")
    
    # Update the listing type attributes with the provided values
    for field, value in subscriptions_update.dict().items():
        setattr(subscriptions_type, field, value)
    
    # Commit the changes to the database
    db.commit()
    
    # Return a success message
    return {
        "success": True,
        "message": "Subscription updated successfully"
    }

