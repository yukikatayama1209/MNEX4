from sqlalchemy.orm import Session
from . import models

def get_prices(db: Session):
    return db.query(models.GasolinePrice).all()
