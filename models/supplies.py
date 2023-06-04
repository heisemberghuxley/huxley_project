from sqlalchemy import column, ForeignKey, Integer

from config import base 

class Supplies(base):
    __tablename__ = "supplies"

    id=column(Interger,primary_key=true)
    Supplies_ID = column(Integer,ForeignKey("Supplier_ID"))
    Product_ID = column(Integer,ForeignKey("Product_ID"))
    Purchase_Price = Column (Integer)