from sqlalchemy.orm import Session
from Auth.models.user import User
from Auth.models.profile import Profile
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import bcrypt
from Auth.models.verification_token import VerificationToken
from Auth.models.user_token import UserToken
from Auth.models.user import User
from Auth.models.profile import Profile
from Auth.controllers import config
from Auth.schemas.user_schema import UserSchema



def register_user_profile(payload, db:Session):
    try:
        # Check if User with the provided email already exists
        email = payload['email']
        password = payload['password']

        existing_user = db.query(User).filter(User.email == email).first()
        
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Profile with this email already exists")
        
        # Hash the password before storing it
        hashed_password = bcrypt.hashpw(payload['password'].encode('utf-8'), bcrypt.gensalt())

        # Generate a 6-digit code
        six_digits_code = config.generate_6_digit_code()

       

         # Generate JWT token with user data
        user_data = {"user_password": password, "user_email": email}  # Customize as per your user schema
        access_token = config.create_access_token(data=user_data)

        new_code = VerificationToken(
            email = payload['email'],
            code = six_digits_code,
        )
        db.add(new_code)
        db.commit()

        new_token = UserToken(
            email = payload['email'],
            token = access_token,
        )

        db.add(new_token)
        db.commit()


        new_profile = Profile(
            first_name=payload['first_name'],
            last_name=payload['last_name'],
            email=payload['email'],
            phone=payload['phone']
        )

        db.add(new_profile)
        db.commit()  # Commit the transaction to generate the primary key id

        # Retrieve the id value after committing to the database
        id = new_profile.id

        new_user = User(
            profile_id=id,
            email=payload['email'],
            phone=payload['phone'],
            password=hashed_password.decode('utf-8'),  # Store the hashed password in the database
        )

        # Add user instance to session
        db.add(new_user)
        db.commit()
        db.refresh(new_user)


        # Refresh the profile instance to make sure it's properly bound to the session
        db.refresh(new_profile)

        # Create schema instances from the newly created profile and user objects
        #user_query = db.query(User).options(joinedload(User.profile))


        # Send verification code to the user
        # sender_email = 'unitimarket@outlook.com'
        # subject = 'Email Verification Code'
        # message = f'Registration succesfull! \n Kindly use this code below for your email verification. \n\n<b>{six_digits_code}</b>'

        # config.send_email(sender_email, email, subject, message)
        
        
        # Create schema instances from the newly created user objects
        user = db.query(User).filter(User.email == email).first()
        
        user_schema = UserSchema.from_orm(user)


        # Return the profile and user schemas in the response
        return {
            "success": True, 
            "message": "Account created successfully", 
            "data": {
                "user": user_schema,
            },
            "token": access_token
           
        }
    except Exception as e:
        # Rollback changes in case of error
        db.rollback()
        raise e
    finally:
        # Close the session
        db.close()
