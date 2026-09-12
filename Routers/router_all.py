from fastapi import APIRouter,HTTPException,status,Depends
from Authentication.bases import get_db
from Routers.database_models import Patient_Database
from Routers.pydantic_models import Patient_Create,Patient_Response,Update_Patient
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from Authentication.controller import is_authorization
from Authentication.database_models import Database
from Routers.get_router import get_all,get_by_id
from Routers.post_router import create_router
from Routers.put_router import update_router
from Routers.delete_router import delete
from Routers.connect_security_with_crud import get_current_user


user_router = APIRouter()


@user_router.get("/")
def greet_route():
    return {"message":"Hi, Welcome to Patient Management API !"}

@user_router.get("/get",response_model=list[Patient_Response])
def get_route(db:Session=Depends(get_db),user = Depends(get_current_user)):
    return get_all(db,user)

@user_router.get("/get_id/{id}",response_model=Patient_Response)
def get_route_id(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    return get_by_id(id,db,user)

@user_router.post("/create",response_model=Patient_Response)
def create_route(body:Patient_Create,db:Session=Depends(get_db),user:Database=Depends(get_current_user)):
    # print(user.id)
    return create_router(body,db,user)

@user_router.put("/update",response_model=Patient_Response)
def update_route(id:int,body:Update_Patient,db:Session=Depends(get_db),user:Database=Depends(get_current_user)):
    return update_router(id,body,db,user)

@user_router.delete("/delete/{id}")
def delete_route(id:str,db:Session=Depends(get_db),user: Database = Depends(get_current_user)):
    return delete(id,db,user)