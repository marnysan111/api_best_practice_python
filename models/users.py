from modules.session import Base
from fastapi import HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))

    def create(user_name:str, db: Session):
        try:
            users = Users()
            users.name = user_name
            db.add(users)
            db.commit()
            db.refresh(users)
            return users
        except Exception as e:
            raise e
        
    def read_by_id(user_id: int, db: Session):
        try:
            users = db.query(Users).filter_by(id = user_id).first()
            return users
        except Exception as e:
            raise e
        
    def update(user_id: int, user_name: str, db: Session):
        try:
            user = db.query(Users).filter_by(id = user_id).first()
            if user is None:
                raise ValueError(f"User with ID {user_id} not found")
            user.name = user_name
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            raise e
        
    def delete(user_id: int, db: Session):
        try:
            db.query(Users).filter_by(id = user_id).delete()
            db.commit()
        except Exception as e:
            raise e
