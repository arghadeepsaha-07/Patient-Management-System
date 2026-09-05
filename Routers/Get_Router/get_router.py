from fastapi import APIRouter,HTTPException,status,Depends
from Database.database_engine import get_db
from Database.database_models import Patient_Database
from Pydantic.models import Patient_Response
from sqlalchemy.orm import Session
from Authentication.controller import is_authorization


router = APIRouter(prefix="/GET")

@router.get("/greet")
def greet():
    return {"message":"Hi, Welcome to Patient Management API !"}

@router.get("/get",response_model=list[Patient_Response])
def get_all(db:Session = Depends(get_db),credentials:Session=Depends(is_authorization)):
    db_user = db.query(Patient_Database).order_by(Patient_Database.id).all()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found!")

    return db_user


@router.get("/get/{id}",response_model=Patient_Response)
def get_by_id(id:str,db:Session=Depends(get_db),credentials:Session=Depends(is_authorization)):
    db_user = db.query(Patient_Database).filter(Patient_Database.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found!")

    return db_user

