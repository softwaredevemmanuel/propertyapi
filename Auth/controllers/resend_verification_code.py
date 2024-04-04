from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Auth.models.verification_token import VerificationToken
from Auth.controllers import config



def resend_email_verification(request, db: Session):

    # Get the Authorization header from the request
    authorization_header = request.headers.get("Authorization")
      # Check if Authorization header exists
    if not authorization_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")
   
    token = authorization_header.split("Bearer ")[-1]
    

    # Token is valid, continue with further operations
    user_info = config.decode_token(token)

    user_email = user_info['user_email']
    six_digits_code = config.generate_6_digit_code()

    new_code = VerificationToken(
            email = user_email,
            code = six_digits_code,
        )



    db.add(new_code)
    db.commit()

    # sender_email = 'unitimarket@outlook.com'
    # subject = 'Email Verification Code'
    # message = f'Kindly use this code {six_digits_code} for your email verification.'

    # send_email(sender_email, user_email, subject, message)
    
    return {
            "success": True, 
            "message": "Email verification sent successfully"
            }
