from fastapi import APIRouter,HTTPException,status,Depends
from Authentication.bases import get_db
from Routers.database_models import Patient_Database
from Routers.pydantic_models import Patient_Response
from sqlalchemy.orm import Session
from Authentication.database_models import Database





def get_all(db:Session,user:Database):
    db_user = db.query(Patient_Database).filter(Patient_Database.id==user.id).all()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found!")

    return db_user



def get_by_id(id:str,db:Session,user:Database):
    db_user = db.query(Patient_Database).filter(Patient_Database.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found!")

    return db_user

