from email import message
from typing import Optional, List
\
from fastapi import FastAPI, HTTPException, Body,Response

app = FastAPI()  # Create a FastAPI instance


# BOOKS = [
#      {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Classic"},
#      {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
#      {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
#         {"title": "1994", "author": "George Orwell", "category": "Dystopian"},
#            {"title": "1974", "author": "George Orwell", "category": "Dystopian"},
# ]


class Book:
    id: int
    title: str
    author: str
    description: int
    rating: int
    """A simple Book class to represent book entries."""
    def __init__(self, id: int, title: str, author: str, description: int, rating: int):        
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel set in the Roaring Twenties, exploring themes of wealth, love, and the American Dream.", 4),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "A story of racial injustice and moral growth in the Deep South, seen through the eyes of young Scout Finch.", 5),
    Book(3, "1984", "George Orwell", "A dystopian novel depicting a totalitarian society under constant surveillance, where independent thought is suppressed.", 5),
    Book(4, "1994", "George Orwell", "A dystopian novel depicting a totalitarian society under constant surveillance, where independent thought is suppressed.", 5),
]  # In-memory list to store book entries  


@app.get("/")
async def root():
    """Root endpoint with a welcome message."""
    return {"message": "Welcome to the Book API! We have now started using multiple branches and pull requests to manage our code changes."}


@app.post("/books")
#Body() is used to indicate that the function expects a JSON body in the request. It allows FastAPI to automatically parse the incoming JSON data and convert it into a Python dictionary that can be used within the function.
async def create_book(book_request = Body()):
    """Create a new book entry.

    - Expects a JSON body with `title`, `author`, and optionally `category`.
    - Returns the created book with a 201 status code.
    """
    new_book = Book(book_request.get("id"), book_request.get("title"), book_request.get("author"), book_request.get("description"), book_request.get("rating"))
    BOOKS.append(new_book)

    return Response(content='{"message": "Book created"}', status_code=201)


@app.put("/books/")
#Body() is used to indicate that the function expects a JSON body in the request, which will be parsed and passed as the new_book parameter. 
#Body() allows FastAPI to automatically parse the incoming JSON data and convert it into a Python dictionary that can be used within the function. 
async def update_book(new_book=Body()):
    """Update an existing book entry.

    - Expects a JSON body with `title`, `author`, and `category`.
    - Finds the book by title and updates its details.
    - Returns the updated book with a 200 status code.
    - Returns 404 if the book to update is not found.
    """
    for b in BOOKS:
        if b.get("title") == new_book.get("title"):
            b.update(new_book)
            return b
        #HTTPException method is used to raise an HTTP error response when a specific condition is not met. In this case, if the book to be updated is not found in the BOOKS list, we raise a 404 Not Found error with a custom message "Book not found for update". This allows the API to communicate to the client that the requested resource (book) could not be found for updating.
        #details parameter provides additional information about the error which is passed as string in the JSON response.
        raise HTTPException(status_code=404, detail="Book not found for update")


@app.get("/books/all")
async def read_all_books(category: Optional[str] = None):
    """Return all books, or filter by category when the `category` query param is provided.

    - Returns 200 with a list of books when found.
    - Returns 404 when category is provided but no books match.
    """

    if category:
        results = [b for b in BOOKS if b.get("category") and b.get("category").lower() == category.lower()]
        #if not results:
        #    raise HTTPException(status_code=404, detail="No books found in this category")
        return results
    return BOOKS


@app.get("/books/{book_id}")
# This endpoint retrieves a single book by its index (book_id) passed as a path parameter. The function checks if the index is valid and returns the corresponding book or raises a 404 error if the index is out of range.
async def read_book(book_id: int):
    """Return a single book by index (book_id acts as a zero-based index).

    This validates the index and returns a 404 HTTP error when the index is out of range.
    """
    if 0 <= book_id < len(BOOKS):
        return BOOKS[book_id]
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/search")
# This endpoint allows searching for books by title, author, or category using query parameters.
# FastAPI will automatically handle the query parameters and pass them to the function.
#We must set default values to None for the query parameters to make them optional, allowing users to search by any combination of attributes.
async def read_book_by_attributes(book_title: str=None, book_author: str=None, category: str=None):
    """Return a list of books matching title, author, or category.

    Returns a (possibly empty) list of books that match any of the provided attributes.
    Does not raise 404 if no books match, but returns an empty list (mirrors read_all_books behavior).
    """
    results = []
    for book in BOOKS:
        if book_title and book.get("title").lower() == book_title.lower():
            results.append(book)
        if book_author and book.get("author").lower() == book_author.lower():
            results.append(book)
        if category and book.get("category").lower() == category.lower():
            results.append(book)
    return results
        
@app.delete("/books/{book_title}")
async def delete_book(book_title: str):
    """Delete a book by title.

    This validates the title and returns a 404 HTTP error when the title is not found.
    """
    for i, book in enumerate(BOOKS):
        if book.get("title").lower() == book_title.lower():
            deleted_book = BOOKS.pop(i)
            return {"message": "Book deleted", "book": deleted_book}
    raise HTTPException(status_code=404, detail="Book not found")       

   