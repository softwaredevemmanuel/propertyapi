from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from Auth.models.verification_token import VerificationToken
from Auth.models.user import User
from Auth.controllers import config
from datetime import datetime


def update_user_verification_status(db: Session, email: str, is_verified: bool, verified_at: datetime) -> None:
    """
    Update the verification status of a user in the database.

    Args:
        db (Session): SQLAlchemy database session
        email (str): Email of the user to update
        is_verified (bool): New verification status

    Returns:
        None
    """
    user = db.query(User).filter(User.email == email).first()
    if user:
        user.is_verified = is_verified
        user.verified_at = verified_at
        db.commit()
    else:
        raise ValueError("User not found")


def verify_code(request, payload, db:Session):

# Get the Authorization header from the request
    authorization_header = request.headers.get("Authorization")
      # Check if Authorization header exists
    if not authorization_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    # Extract the token from the header
    token = authorization_header.split("Bearer ")[-1]
  
    user_info = config.decode_token(token)

    # Token is valid, continue with further operations
    user_email = user_info['user_email']
    code = payload['code']

    user = db.query(VerificationToken).filter(VerificationToken.email == user_email).order_by(VerificationToken.created_at.desc()).first()

    if code == user.code:

        # Update is_verified in the database
        verified_at = datetime.utcnow()  # Call the function to get the current datetime

        update_user_verification_status(db, email=user_email, is_verified=True, verified_at=verified_at)

        user_details = db.query(User).filter(User.email == user_email).first()

        # Fetch the user data with profile using joinedload
        filter_query = db.query(User).options(joinedload(User.profile)).filter(User.id == user_details.id).first()
         
         # ........ Removing the Password METHOD 2.......
        user_query_dict = filter_query.__dict__
        user_query_dict.pop("password", None)
    
        return {
                "success": True, 
                "message": "Email verified successfully",
                "data": user_query_dict,
            }
    else:
        raise HTTPException(status_code=401, detail="Invalid Code")