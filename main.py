from fastapi import FastAPI,HTTPException,status
from Database.database_engine import engine
from Database.database_models import Base
from Routers.Get_Router.get_router import router as router_get
from Routers.Delete_Router.delete_router import router as router_delete
from Routers.Post_Router.post_router import router as router_create
from Routers.Put_router.put_router import router as router_update
from Authentication.router import user_router as authentication
from fastapi.security import HTTPBearer



Base.metadata.create_all(bind=engine)

security = HTTPBearer()

app = FastAPI(title="Patient Management System",description="This is a patient management system where we manage patients details !")

app.include_router(authentication)
app.include_router(router_get)
app.include_router(router_create)
app.include_router(router_update)
app.include_router(router_delete)
