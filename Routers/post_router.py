from fastapi import APIRouter,HTTPException,status,Depends
from Authentication.bases import get_db
from Routers.database_models import Patient_Database
from Routers.pydantic_models import Patient_Create,Patient_Response
from sqlalchemy.orm import Session
from Authentication.database_models import Database


def create_router(patient:Patient_Create,db:Session,user:Database):

    db_user = Patient_Database(**patient.model_dump(),user_id=user.id)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return db_user

