from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
from modules.session import Base

class UserRole(Base):
    __tablename__ = "user_role"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    user = relationship("Users", foreign_keys=[user_id], lazy="subquery")
    role = relationship("Role", foreign_keys=[role_id], lazy="subquery")

    def create(user_id: int, role_id: int, db: Session):
        try:
            userRole = UserRole()
            userRole.user_id = user_id
            userRole.role_id = role_id
            db.add(userRole)
            db.commit()
            db.refresh(userRole)
            return userRole
        except Exception as e:
            raise e
        
    def read_by_user_id(user_id: int, db: Session):
        try:
            userRole = db.query(UserRole).filter_by(user_id = user_id).first()
            return userRole
        except Exception as e:
            raise e
        

    def update_role_id(user_id: int, role_id: int, db: Session):
        try:
            userRole = db.query(UserRole).filter_by(user_id = user_id).first()
            userRole.role_id = role_id
            db.add(userRole)
            db.commit()
            db.refresh(userRole)
            return userRole
        except Exception as e:
            raise e
        
    def delete_by_user_id(user_id: int, db: Session):
        try:
            db.query(UserRole).filter_by(user_id = user_id).delete()
            db.commit()
            return
        except Exception as e:
            raise e