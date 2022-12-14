import pdb

from models.book import Book

import repositories.book_repository as book_repository





book1 = Book("meditations")
book_repository.save(book1)




