from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from Auth.models.verification_token import VerificationToken
from Auth.models.user import User
from Auth.controllers import config
from datetime import datetime


def check_email(request_data, db:Session):

    email = request_data.email
    user = db.query(User).filter(User.email == email).first()

    if user:
        all_query = db.query(User).options(joinedload(User.profile))

        filter_query = all_query.filter(User.email == request_data.email).first()
        
        # ........ Removing the Password METHOD 1.......
        # user_query_dict = filter_query.__dict__
        # if "password" in user_query_dict:
        #     del user_query_dict["password"]
        
        # ........ Removing the Password METHOD 2.......
        user_query_dict = filter_query.__dict__
        user_query_dict.pop("password", None)
        
        return {
            "success": True,
            "message": "Email found",
            "data": user_query_dict,
        }
    else:
        raise HTTPException(status_code=404, detail="Email not found")
    

def get_users(db: Session):
    investment_query = db.query(User).all()

    return {
        "success": True,
        "message": "Investment Plans retrieved successfully",
        "data": investment_query
    }