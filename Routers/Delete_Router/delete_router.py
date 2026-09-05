from fastapi import APIRouter,HTTPException,status,Depends
from Database.database_engine import get_db
from Database.database_models import Patient_Database
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from Authentication.controller import is_authorization


router = APIRouter(prefix="/DELETE")

@router.delete("/delete/{id}")
def delete(id:str,db:Session=Depends(get_db),credentials:Session=Depends(is_authorization)):
    db_user = db.query(Patient_Database).filter(Patient_Database.id == id).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Patient Data not Found!")

    db.delete(db_user)
    db.commit()

    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Patient Data is Deleted!"})
