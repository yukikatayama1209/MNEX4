from pydantic import BaseModel

class GasolinePrice(BaseModel):
    week: str
    price: float

    class Config:
        orm_mode = True
