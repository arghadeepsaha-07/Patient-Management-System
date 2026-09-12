from fastapi import APIRouter,Depends,status,HTTPException
from Authentication.bases import get_db
from Routers.database_models import Patient_Database
from Routers.pydantic_models import Update_Patient
from sqlalchemy.orm import Session
from Authentication.database_models import Database

def update_router(id:str,patient:Update_Patient,db:Patient_Database,user:Database):

    db_user = db.query(Patient_Database).filter(Patient_Database.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found !")

    
    
    if db_user.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not allowed to delete this task")
    
    
    
    
    if patient.name is not None:
        db_user.name = patient.name

    if patient.age is not None:
        db_user.age = patient.age

    if patient.gender is not None:
        db_user.gender = patient.gender

    if patient.height is not None:
        db_user.height = patient.height

    if patient.weight is not None:
        db_user.weight = patient.weight

    if patient.problem is not None:
        db_user.problem = patient.problem

    if patient.email is not None:
        db_user.email = patient.email

    if patient.phone_no is not None:
        db_user.phone_no = patient.phone_no

    if patient.emergency_phone_no is not None:
        db_user.emergency_phone_no = patient.emergency_phone_no

    db.commit()
    db.refresh(db_user)

    return db_user

    