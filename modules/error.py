from fastapi import HTTPException
from sqlalchemy.exc import OperationalError, DataError, IntegrityError, SQLAlchemyError, DBAPIError
import logging

def handle_db_exception(e):
    logging.error(e)

    if isinstance(e, OperationalError):
        raise HTTPException(status_code=503, detail="DB connection error")
    elif isinstance(e, DataError):
        raise HTTPException(status_code=400, detail="Provided data is too long")
    elif isinstance(e, IntegrityError):
        raise HTTPException(status_code=400, detail="Referenced data does not exist")
    elif isinstance(e, SQLAlchemyError):
        raise HTTPException(status_code=500, detail="DB processing error")
    elif isinstance(e, ValueError):
        raise HTTPException(status_code=404, detail=str(e))
    else:
        raise HTTPException(status_code=500, detail="Server processing error")
    # detail はエラーコードを自作してそれを使いたい
    # loggingにもエラーコードを使いたい