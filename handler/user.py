from sqlalchemy.orm import Session
from models.users import Users
from models.role import Role
from models.user_role import UserRole
from modules.error import handle_db_exception

class UserHandler:
    def __init__(self, db: Session):
        self.db = db

    def read_user(self, user_id: int):
        try:
            user = Users.read_by_id(user_id, self.db)
            userRole = UserRole.read_by_user_id(user_id, self.db)
            userJson = {
                "id": user.id,
                "name": user.name,
                "role": userRole.role.name
            }
            return userJson
        except Exception as e:
            handle_db_exception(e)

    def create_user(self, user_name: str, role_id: id):
        try:
            user = Users.create(user_name, self.db)
            userRole = UserRole.create(user.id, role_id, self.db)
            userJson = {
                "id": user.id,
                "name": user.name,
                "role": userRole.role.name
            }
            return userJson
        except Exception as e:
            handle_db_exception(e)

    def update_user(self, user_id: int, user_name: str, role_id: int):
        try:
            user = Users.update(user_id, user_name, self.db)
            userRole = UserRole.update_role_id(user_id, role_id, self.db)
            userJson = {
                "id": user.id,
                "name": user.name,
                "role": userRole.role.name
            }
            return userJson
        except Exception as e:
            handle_db_exception(e)

    def delete_user(self, user_id: int):
        try:
            Users.delete(user_id, self.db)
            UserRole.delete_by_user_id(user_id, self.db)
            return
        except Exception as e:
            handle_db_exception(e)