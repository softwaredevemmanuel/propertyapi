from sqlalchemy.orm import Session
from Auth.models.reset_password import ResetPassword
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime




def verify_password_reset_code(payload, db:Session):
       
    email = payload['email']
    code = payload['code']

    user = db.query(ResetPassword).filter(ResetPassword.email == email).order_by(ResetPassword.created_at.desc()).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Code")



    if  user.verified_at:
        return { 
                "details":"Token has been verified"
                }
    
    

    # # Update verified_at in the database
    verified_at = datetime.utcnow()  # Call the function to get the current datetime
    print(verified_at)
    
    user = db.query(ResetPassword).filter(ResetPassword.email == email).order_by(ResetPassword.created_at.desc()).first()
    if user:
        user.verified_at = verified_at
        db.commit()
    else:
        raise ValueError("Unable to update verification time")      



    return {
            "success": True, 
            "message": "Token verified successfully",
            "dat":{
                "reset_token": code
            }
            
        }
  