from fastapi import FastAPI
from .database import engine, SessionLocal
from .models import Base, GasolinePrice

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/prices/")
def read_prices():
    with SessionLocal() as session:
        prices = session.query(GasolinePrice).all()
        return prices
