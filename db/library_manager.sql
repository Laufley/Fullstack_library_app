DROP TABLE IF EXISTS table_of_books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE table_of_books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255)
    author_id INT REFERENCES authors(id)
);





