from fastapi import APIRouter
from typing import List, Optional
from models import Book, CreateBook, SearchBook, SearchBooks


route = APIRouter()
books: List[Book] = [] # [Book, Book, Book ....]

@route.post('/')
def create_book(book: CreateBook) -> Book:
    book = Book(id=len(books)+1, **book.model_dump())
    books.append(book)

    return book

@route.get('/search/')
def search_books(keyword: Optional[str], max_results: int = 10) -> SearchBooks:
    search_result = [book for book in books if keyword in book.title] if keyword else books

    # max_results: pagenation을 위한 옵션
    return SearchBooks(results=search_result[:max_results])



