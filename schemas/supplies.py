from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    id : Optional[int] = None
    Supplier_ID: int = Field(ge=1, description="supplier id")
    Product_ID: int = Field(ge=1, description="product id ")
    Purchase_Price: float = Field(ge=1,le=50000,description="enter purchase price")
    class Config:
        schema_extra = {
            "example":{
                "Supplier_ID":0,
                "Product_ID":0,
                "Purchase_Price":1.50
            }
        }
        
        
        
        
        