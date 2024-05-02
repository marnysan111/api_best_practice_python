from sqlalchemy.orm import Session
from modules.error import handle_db_exception
from models.user_role import UserRole

class UserRoleHandler:
    def __init__(self, db: Session):
        self.db = db
    
    def read_user_role(self, user_id: int):
        try:
            return UserRole.read_by_user_id(user_id, self.db)
        except Exception as e:
            handle_db_exception(e)