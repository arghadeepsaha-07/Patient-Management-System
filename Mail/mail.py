from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

load_dotenv()

from typing import List

conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD"),
    MAIL_FROM = os.getenv("MAIL_FROM"),
    MAIL_PORT = int(os.getenv("MAIL_PORT")),
    MAIL_SERVER = os.getenv("MAIL_SERVER"), #smtp->protocal of email
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME"),
    MAIL_STARTTLS = os.getenv("MAIL_STARTTLS") == "True",
    MAIL_SSL_TLS = os.getenv("MAIL_SSL_TLS") == "True",
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

'''
For Understanding:->
MAIL_USERNAME = "company@gmail.com"       # sender
MAIL_PASSWORD = "APP_PASSWORD"            # sender's Gmail App Password
MAIL_FROM     = "company@gmail.com"       # sender

================================

while the registration input contains:

{
    "email": "client@gmail.com",
    "password": "client_app_password"
}

Those are completely separate passwords.

'''



async def send_email(emails : List[str]) -> JSONResponse:
    html = """<p>Hi, Thanks for Registration. Our Team will connect with You Soon !</p> """

    message = MessageSchema(
        subject="Registration Confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
    