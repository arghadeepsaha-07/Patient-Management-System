from fastapi import FastAPI
from Authentication.engines import engine
from Authentication.bases import Base
from Authentication.router import user_router as authentication
from Routers.router_all import user_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patient Management System",description="This is a patient management system where we manage patients details !")

app.include_router(authentication)
app.include_router(user_router)
