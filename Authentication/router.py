from fastapi import APIRouter,Depends,Request
from Authentication.controller import register,login,is_authorization
from Authentication.bases import get_db
from Authentication.pydantic_models import Pydantic,Pydantic_Response,Login_Schema
from sqlalchemy.orm import Session

user_router = APIRouter()

@user_router.post("/register",response_model=Pydantic_Response)
def register_router(body:Pydantic,db:Session=Depends(get_db)):
    return register(body,db)

@user_router.post("/login")
def login_router(body:Login_Schema,db:Session=Depends(get_db)):
    return login(body,db)

@user_router.get("/is_auth",response_model=Pydantic_Response)
def authentication(request:Request,db:Session=Depends(get_db),credentials:Session=Depends(is_authorization)):
    return is_authorization(request,db)