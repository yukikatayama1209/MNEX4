from sqlalchemy import Column, Integer, Float, String
from .database import Base

class GasolinePrice(Base):
    __tablename__ = "gasoline_prices"
    
    id = Column(Integer, primary_key=True, index=True)
    week = Column(String, index=True)
    price = Column(Float)
