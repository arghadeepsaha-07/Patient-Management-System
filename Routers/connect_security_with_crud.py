from fastapi import Request,Depends
from Authentication.controller import is_authorization
from Authentication.bases import get_db
from sqlalchemy.orm import Session
from Authentication.controller import security


def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
    credentials = Depends(security)
):
    return is_authorization(request, db, credentials)

