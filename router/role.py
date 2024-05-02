from fastapi import FastAPI, HTTPException, Depends, APIRouter
from modules.session import get_db
import logging
from handler.role import RoleHandler


router = APIRouter(
    tags=["role"],
    responses={404: {"description": "Not found"}},
)
logger = logging.getLogger(__name__)


def get_role_handler(db = Depends(get_db)):
    return RoleHandler(db)

@router.get("")
def read_role(handler = Depends(get_role_handler)):
    roles = handler.read_roles()
    return {"result": "success", "roles": roles}

@router.post("")
def create_role(role_name: str, handler = Depends(get_role_handler)):
    role = handler.create_role(role_name)
    return {"result": "success", "role": role}

@router.put("/{role_id}")
def update_role(role_id: int, role_name: str, handler = Depends(get_role_handler)):
    user = handler.update_role(role_id, role_name)
    return {"result": "success", "user": user}


@router.delete("/{role_id}")
def delete_role(role_id: int, handler = Depends(get_role_handler)):
    handler.delete_role(role_id)
    return {"result": "success"}

