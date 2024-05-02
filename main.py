from fastapi import FastAPI, HTTPException, Depends, APIRouter
from router import user, role
from modules.session import get_db
from sqlalchemy.orm import Session

app = FastAPI()
router = APIRouter()
router.include_router(user.router, prefix="/user")
router.include_router(role.router, prefix="/role")
app.include_router(router)

