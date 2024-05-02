from modules.session import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))

    def read_all(db: Session):
        try:
            roles = db.query(Role).all()
            return roles
        except Exception as e:
            raise e
    
    def create(role_name: str, db: Session):
        try:
            role = Role()
            role.name = role_name
            db.add(role)
            db.commit()
            db.refresh(role)
            return role
        except Exception as e:
            raise e
        
    def update(role_id: int, role_name: str, db: Session):
        try:
            return
        except Exception as e:
            raise e
        
    def delete(role_id: int, db: Session):
        try:
            return
        except Exception as e:
            raise e