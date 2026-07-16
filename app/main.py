from fastapi import FastAPI
from app.core.database import engine, Base
from app import models
from app.routers import user as user_router
from app.routers import organization as org_router
from app.routers import team as team_router
from app.routers import task as task_router
from app.routers import org_member as org_member_router
from app.routers import team_member as team_member_router
from app.routers import auth as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router.router)
app.include_router(org_router.router)
app.include_router(team_router.router)
app.include_router(task_router.router)
app.include_router(org_member_router.router)
app.include_router(team_member_router.router)
app.include_router(auth_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
