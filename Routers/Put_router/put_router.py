from fastapi import APIRouter,Depends,status,HTTPException
from Database.database_engine import get_db
from Database.database_models import Patient_Database
from Pydantic.models import Update_Response,Update_Patient
from sqlalchemy.orm import Session
from Authentication.controller import is_authorization

router = APIRouter(prefix="/UPDATE")

@router.put("/update/{id}",response_model=Update_Response)
def update_router(id:str,patient:Update_Patient,db:Patient_Database=Depends(get_db),credentials:Session=Depends(is_authorization)):

    db_user = db.query(Patient_Database).filter(Patient_Database.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found !")

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

    