from sqlalchemy.orm import Session
from Auth.models.user import User
from Auth.models.reset_password import ResetPassword
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Auth.controllers import config
import bcrypt


def reset_password(request, payload, db:Session):
        # Get the Authorization header from the request
    authorization_header = request.headers.get("Authorization")
      # Check if Authorization header exists
    if not authorization_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    # Extract the token from the header
    token = authorization_header.split("Bearer ")[-1]
  
    config.decode_token(token)

    # Token is valid, continue with further operations
    email = payload['email']
    reset_token = payload['reset_token']
    password = payload['password']
    confirm_password = payload['confirm_password']

    if password == confirm_password:

        user = db.query(ResetPassword).filter(ResetPassword.email == email).order_by(ResetPassword.created_at.desc()).first()
        if not user:
            raise HTTPException(status_code=401, detail= "User did not request for password change")



        if reset_token == user.code:

            # Hash the password before storing it
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            # Update is_verified in the database
            user = db.query(User).filter(User.email == email).first()
            if user:
                user.password = hashed_password.decode('utf-8')
                db.commit()
            else:
                raise ValueError("User not found")
        

            return {
                    "success": True, 
                    "message": "Password reset successfully!",
                    "data": {}
                }
        else:
            raise HTTPException(status_code=401, detail="Invalid Verification Code")

    else:
        raise HTTPException(status_code=401, detail="Password and Confirm Password do not match")