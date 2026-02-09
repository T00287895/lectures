

CREATE TABLE movies (
    movie_id        SERIAL PRIMARY KEY,
    title           VARCHAR(150) NOT NULL,
    director        VARCHAR(100) NOT NULL,
    genre           VARCHAR(50),
    duration_mins   INTEGER NOT NULL CHECK (duration_mins > 0),
    tickets_sold    INTEGER NOT NULL CHECK (tickets_sold >= 0),
    release_year    INTEGER CHECK (release_year BETWEEN 1950 AND 2100)
);

INSERT INTO movies (title, director, genre, duration_mins, tickets_sold, release_year)
VALUES
    ('The Echoing Lights',         'Ava Nolan',         'Drama',      130, 180000, 2014),
    ('Cosmic Frequencies',         'Rory Byrne',        'Sci-Fi',     115, 220000, 2019),
    ('Hidden Strings',             'Ciara Walsh',       'Documentary',90,  80000,  2008),
    ('The Glass Empire',           'Donal Murphy',      'Action',     140, 340000, 2012),
    ('Midnight Feast',             'Eoin Kelly',        'Comedy',     105, 95000,  2003),
    ('Unwritten Paths',            'Clara Hayes',       'Drama',      128, 205000, 2020),
    ('Retro Dimensions',           'Liam Doyle',        'Sci-Fi',     160, 175000, 1998),
    ('The Artisan’s Table',        'Maeve Finn',        'Documentary',98,  67000,  2005);

SELECT COUNT(*) as "Total amount of movies"
FROM movies;

SELECT SUM(tickets_sold) as "Total tickets have been sold"
FROM movies;

SELECT AVG(duration_mins) as "Average duration", AVG(tickets_sold) as "Average tickets sold"
FROM movies;

SELECT MAX(release_year) as "The newest release", MIN(release_year) as "The earliest release"
FROM movies;

SELECT genre, COUNT(*)
FROM movies
GROUP BY genre;

SELECT genre, AVG(tickets_sold)
FROM movies
GROUP BY genre;

SELECT director, SUM(tickets_sold)
FROM movies
GROUP BY director;

SELECT *
FROM movies
WHERE tickets_sold > 200000;

SELECT *
FROM movies
WHERE release_year BETWEEN 2005 AND 2015;

SELECT *
FROM movies
WHERE genre = 'Drama' or genre = 'Sci-Fi';

SELECT *
FROM movies
WHERE genre != 'Action';

SELECT *
FROM movies
WHERE director = 'Rory Byrne';

SELECT *
FROM movies
WHERE duration_mins > 120 AND tickets_sold > 150000;

SELECT *
FROM movies
WHERE genre = 'Drama' or release_year < 2010;

SELECT *
FROM movies
WHERE genre = 'Drama' or genre = 'Sci-Fi' and tickets_sold > 150000;