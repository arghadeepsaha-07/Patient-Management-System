from fastapi import HTTPException,status,Depends,Request
from Authentication.database_models import Database
from Authentication.pydantic_models import Pydantic,Login_Schema
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from Authentication.settings import settings
from datetime import datetime,timedelta
import jwt
from jwt.exceptions import InvalidTokenError
from Authentication.bases import get_db


security = HTTPBearer()

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password_hash(plain_password,hash_password):
    return password_hash.verify(plain_password,hash_password)

def register(body:Pydantic,db:Session=Depends(get_db)):
    user = db.query(Database).filter(Database.username == body.username).first()
    
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Username alrasy exists !")
    
    email = db.query(Database).filter(Database.email == body.email).first()
    
    if email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email Address already exists !")
    
    hash_password = get_password_hash(body.password)
    
    new_user = Database(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def login(body:Login_Schema,db:Session=Depends(get_db)):
    user = db.query(Database).filter(Database.username == body.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email Address alrady exists !")
    
    if not verify_password_hash(body.password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email Address alrady exists !")
    
    exp_time = datetime.now() + timedelta(minutes=int(settings.EXP_TIME))
    
    token = jwt.encode({"id":user.id,"exp":exp_time.timestamp()},settings.SECRET_KEY,settings.ALGORITHM)
    
    return {"token":token}


def is_authorization(request:Request,db:Session=Depends(get_db),secure:Session=Depends(security)):
    try:
        token = request.headers.get("authorization")
        
        if not token:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="You are un-Authorized!")
        
        token = token.split(" ")[-1]
        
        data = jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])        
        
        user_id = int(data.get("id"))
        
        user = db.query(Database).filter(Database.id == user_id).first()
        
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="You are un-Authorized!")
        
        return user
    
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="You are un-Authorized!")
