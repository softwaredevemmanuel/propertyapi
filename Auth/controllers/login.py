from sqlalchemy.orm import Session, joinedload
from Auth.models.user import User
from Auth.models.profile import Profile
from Auth.models.login_history import LoginHistory
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import bcrypt
from Auth.models.verification_token import VerificationToken
from Auth.models.user_token import UserToken
from Auth.models.user import User
from Auth.models.profile import Profile
from Auth.controllers import config
from Auth.schemas.user_schema import UserSchema
from datetime import datetime
from passlib.context import CryptContext

# Create a global variable for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    print(plain_password)
    print(hashed_password)
    """
    Verify the plain password against the hashed password.

    Parameters:
    - plain_password (str): The plain text password to verify.
    - hashed_password (str): The hashed password stored in the database.

    Returns:
    - bool: True if the plain password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def login(request, payload, db:Session):

    email=payload['email']
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User does not exist")
    
    if not user.is_verified:
        raise HTTPException(status_code=401, detail="User is not verified")
    
    if not verify_password(payload['password'], user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # Retrieve the associated profile for the user
    profile = db.query(Profile).filter(Profile.email == email).first()
    
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    # Generate JWT token with user data
    user_data = {"user_id": user.id, "user_email": user.email, "user_password": user.password}  # Customize as per your user schema
    access_token = config.create_access_token(data=user_data)

    # Get the client's IP address
    client_ip = request.client.host

    # Get the access client (if applicable)
    access_client = request.headers.get("User-Agent")

    # Create a login history record
    login_at = datetime.utcnow()
    new_login = LoginHistory(
        user_id=user.id,
        time_in=login_at,
        ip_address=client_ip,
        access_client=access_client
    )

    # Save the login history record to the database
    db.add(new_login)
    db.commit()

    # Fetch the user data with profile using joinedload
    user_query = db.query(User).options(joinedload(User.profile)).filter(User.id == user.id).first()
    
    if user_query is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Exclude the password field from the user object
    user_query_dict = user_query.__dict__
    if "password" in user_query_dict:
        del user_query_dict["password"]
    
         

    return {
        "success": True, 
        "message": "Logged in successfully", 
        "data": {
            "user": user_query
        }, 
        "token": access_token
    }
