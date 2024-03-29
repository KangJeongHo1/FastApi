from pydantic import BaseModel
from typing import Optional, List

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class SearchBook(BaseModel): # Detail - GET
    results: Optional[Book] # Book

class SearchBooks(BaseModel): # BookList - GET
    results: List[Book] # [Book, Book, Book]