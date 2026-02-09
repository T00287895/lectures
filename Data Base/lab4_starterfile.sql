--DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id         INTEGER PRIMARY KEY,
    title           VARCHAR(120) NOT NULL,
    author          VARCHAR(80)  NOT NULL,
    genre           VARCHAR(40),
    copies          INTEGER NOT NULL CHECK (copies >= 0),  -- check constraint 
    borrow_count    INTEGER NOT NULL CHECK (borrow_count >= 0), -- check constraint
    published_year  INTEGER CHECK (published_year BETWEEN 1800 AND 2100)
);

INSERT INTO books (book_id, title, author, genre, copies, borrow_count, published_year)
VALUES
    (1, 'The Silent Archive',      'Nora Keane',     'Fiction',  5,  72, 2011),
    (2, 'Data in the Wild',        'Owen Walsh',     'Science',  3,  49, 2018),
    (3, 'A History of Cork',       'Maeve Doyle',    'History',  2,  18, 1999),
    (4, 'Quantum for Beginners',   'Liam O''Brien',  'Science',  4,  55, 2007),
    (5, 'Garden Crafts',           'Siobhan Flynn',  'Hobby',    6,   9, 2003),
    (6, 'Fictional Cities',        'Aisling Byrne',  'Fiction',  1, 120, 2015),
    (7, 'Medieval Myths',          'Ciaran Murray',  'History',  2,  64, 2001),
    (8, 'Modern Cooking Basics',   'Eimear Kelly',   'Lifestyle',8,  33, 2020);

SELECT *
FROM books;


SELECT COUNT(book_id) as "total number of books"
FROM books;

SELECT SUM(borrow_count) as "Total nmber of books have been borrowed"
FROM books;

SELECT AVG(borrow_count) as "Average borrow count"
FROM books;

SELECT MAX(borrow_count) as "Highest Lowest borrow count", MIN(borrow_count) as "Lowest borrow count"
FROM books;

SELECT MAX(published_year) as "The earliest published book" , MIN(borrow_count ) as "The most recent published book"
FROM books;

SELECT genre, COUNT(*)
FROM books
GROUP BY genre;

SELECT genre, AVG(borrow_count)
FROM books
GROUP BY genre;

SELECT author, SUM(borrow_count)
FROM books
GROUP BY author;

SELECT *
FROM books
WHERE borrow_count > 50;

SELECT *
FROM books
WHERE published_year BETWEEN 2000 AND 2015;

SELECT *
FROM books
WHERE genre = 'Fiction' or genre = 'Science';

SELECT *
FROM books
WHERE genre != 'History';

