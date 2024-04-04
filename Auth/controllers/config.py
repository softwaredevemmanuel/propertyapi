from fastapi import APIRouter, HTTPException, Body, Depends, status, Request, Header
from datetime import datetime
import bcrypt
import random
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import jwt

# Load environment variables from .env file
load_dotenv()

# Secret key used to sign the JWT token
SECRET_KEY = os.getenv("SECRET_KEY")

# Algorithm used to sign the JWT token
ALGORITHM = os.getenv("ALGORITHM")

# Function to generate JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(days=7)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Generate a random 6 digits
def generate_6_digit_code():
    return ''.join(random.choices('123456789', k=6))



# Verify Token
def verify_token(token: str, secret_key: str) -> bool:
  
    try:
        # Decode the token without verifying the signature
        payload = jwt.decode(token, options={"verify_signature": False})

        # Extract expiration time from the payload
        expiration_time = payload.get('exp')

        # Convert expiration time to a datetime object
        expiration_datetime = datetime.utcfromtimestamp(expiration_time)

        if expiration_datetime < datetime.utcnow():
            return False
        else:
            return True


    except jwt.InvalidTokenError:
        print("Invalid token")



# Validate A JWT TOKEN
def decode_token(token: str):
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        # Invalid token
        raise HTTPException(status_code=401, detail="Invalid token")
   
    
def send_email(sender_email, recipient_email, subject, message):
    smtp_server = 'smtp-relay.brevo.com'
    smtp_port = 587
    smtp_login = 'unitimarket@outlook.com'
    smtp_password = 'sOk1YNQdJq3SBHyx'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_login, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)
    finally:
        server.quit()
