from sqlalchemy import Column, Integer, String  
from database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    pmid = Column(Integer, unique=True)
    language = Column(String)
    title = Column(String)
    abstract = Column(String)