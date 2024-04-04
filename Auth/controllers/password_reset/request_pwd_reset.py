from sqlalchemy.orm import Session
from Auth.models.user import User
from Auth.models.reset_password import ResetPassword
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Auth.controllers import config


def request_password_reset(request, payload, db:Session):
    email = payload['email']
     # Get the Authorization header from the request
    authorization_header = request.headers.get("Authorization")
    
    # Check if Authorization header exists
    if not authorization_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    
    # Extract the token from the header
    token = authorization_header.split("Bearer ")[-1]
  
    user_info = config.decode_token(token)
    print(user_info)

    # Check if the email exists in the database

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Email not found")

    # Generate a password reset token
    reset_token = config.generate_6_digit_code()
    
      # Generate JWT token with user data
    user_data = { "user_id": user_info['user_id'], "user_password": user_info['user_password'], "user_email": user_info['user_email']}  # Customize as per your user schema
    access_token = config.create_access_token(data=user_data)

    
    # You can send the token via email or any other method here
    new_code = ResetPassword(
            email = email,
            code = reset_token,
            token = access_token,
        )


    db.add(new_code)
    db.commit()

    # sender_email = 'unitimarket@outlook.com'
    # subject = 'Pass Reset Request'
    # message = f'Kindly use this code {reset_token} to reset your password.'

    # send_email(sender_email, email, subject, message)

    # Return the token
    return {
            "success": True, 
            "message": "Password verification code sent successfully"
            }

