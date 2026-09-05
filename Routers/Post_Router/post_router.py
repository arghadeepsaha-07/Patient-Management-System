from fastapi import APIRouter,HTTPException,status,Depends
from Database.database_engine import get_db
from Database.database_models import Patient_Database
from Pydantic.models import Patient_Create,Patient_Response
from sqlalchemy.orm import Session
from Authentication.controller import is_authorization


router = APIRouter(prefix="/CREATE")


@router.post("/create",response_model=Patient_Response)
def create_router(patient:Patient_Create,db:Session=Depends(get_db),credentials:Session=Depends(is_authorization)):

    db_user = Patient_Database(**patient.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return db_user

