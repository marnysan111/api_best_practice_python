from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlite.db', connect_args={"check_same_thread": False}) 
Base = declarative_base()
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base.query = db_session.query_property()
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()