from sqlalchemy.orm import Session
from models.role import Role
from modules.error import handle_db_exception

class RoleHandler:
    def __init__(self, db: Session):
        self.db = db

    def read_roles(self):
        try:
            return Role.read_all(self.db)
        except Exception as e:
            handle_db_exception(e)

    def create_role(self, role_name: str):
        try:
            role = Role.create(role_name, self.db)
            return role
        except Exception as e:
            handle_db_exception(e)

    def update_role(self, role_id: int, role_name: str):
        try:
            return Role.update(role_id, role_name, self.db)
        except Exception as e:
            handle_db_exception(e)

    def delete_user(self, user_id: int):
        try:
            Role.delete(user_id, self.db)
            return
        except Exception as e:
            handle_db_exception(e)