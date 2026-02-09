CREATE TABLE locations(
location_id INTEGER PRIMARY KEY,
city TEXT NOT NULL,
country TEXT NOT NULL
);

CREATE TABLE people (
person_id INTEGER PRIMARY KEY,
full_name TEXT NOT NULL
);

INSERT INTO locations(location_id, city, country) VALUES
(1, 'London', 'UK'),
(2, 'Paris', 'France'),
(3, 'Rome', 'Italy'),
(4, 'Cairo', 'Egypt');

INSERT INTO people (person_id, full_name) VALUES
(1, 'Mary')