from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(book):
    sql = "INSERT INTO table_of_books (title, author) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author]
    results = run_sql(sql, values)
    return results

def select_all():
    books = []
    
    sql = "SELECT * FROM table_of_books"
    results = run_sql(sql)
    
    for row_of_book in results:
        author = Author
        book = Book(row_of_book['title'], author, row_of_book['id'])
        books.append(book)
    return books
        

