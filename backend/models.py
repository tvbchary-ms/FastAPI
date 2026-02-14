from pydantic import BaseModel

class ProductCreate(BaseModel):
    #id : int
    name : str
    description: str
    price : float
    quantity : int


