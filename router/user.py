from fastapi import FastAPI, HTTPException, Depends, APIRouter
from modules.session import get_db
import logging
from handler.user import UserHandler
from handler.user_role import UserRoleHandler

router = APIRouter(
    tags=["user"],
    responses={404: {"description": "Not found"}},
)
logger = logging.getLogger(__name__)


def get_user_handler(db = Depends(get_db)):
    return UserHandler(db)

@router.get("/{user_id}")
def read_user(user_id: int, handler = Depends(get_user_handler)):
    user = handler.read_user(user_id)
    return {"result": "success", "user": user}

@router.post("")
def create_user(user_name: str, role_id: int, handler = Depends(get_user_handler)):
    user = handler.create_user(user_name, role_id)
    return {"result": "success", "user": user}

@router.put("/{user_id}")
def update_user(user_id: int, user_name: str, role_id: int, handler = Depends(get_user_handler)):
    user = handler.update_user(user_id, user_name, role_id)
    return {"result": "success", "user": user}


@router.delete("/{user_id}")
def delete_user(user_id: int, handler = Depends(get_user_handler)):
    handler.delete_user(user_id)
    return {"result": "success"}


def get_user_role_handler(db = Depends(get_db)):
    return UserRoleHandler(db)

@router.get("/{user_id}/role")
def read_user_role(user_id: int, handler = Depends(get_user_role_handler)):
    userRole = handler.read_user_role(user_id)
    return {"result": "success", "userRole": userRole}