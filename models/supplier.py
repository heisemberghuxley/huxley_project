from sqlalchemy import Column, Integer, String

from config.database import Base


class Supplier(Base):
    
    __tablename__= "product"
    
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Address = Column(String)
    Phone= Column(Integer)
    Price = Column(Integer)
    Email = Column(string)
    