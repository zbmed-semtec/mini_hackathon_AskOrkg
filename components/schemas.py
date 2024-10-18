from pydantic import BaseModel

class Books(BaseModel):
    pmid: int
    language: str
    title: str
    abstract: str