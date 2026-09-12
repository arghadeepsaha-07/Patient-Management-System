from fastapi import HTTPException,status,Depends
from Authentication.bases import get_db
from Routers.database_models import Patient_Database
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from Authentication.controller import is_authorization
from Authentication.database_models import Database


def delete(id:str,db:Session,user:Database):
    db_user = db.query(Patient_Database).filter(Patient_Database.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found!")

    
    if db_user.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not allowed to delete this task")
    
    
    db.delete(db_user)
    db.commit()

    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Patient Data is Deleted!"})
