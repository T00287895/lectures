CREATE TABLE students(
student_id INTEGER PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
age INTEGER,
email VARCHAR(100),
enrolment_date DATE
);

INSERT INTO students(student_id,first_name,last_name,age,email,enrolment_date)
VALUES
(1, 'Sarah', 'O"Brien', 21, 'sarah@example.com', '2024-09-10'),
(2, 'John', 'Murphy', 19, 'john@example.com', '2024-09-11'),
(3, 'Aisling', 'Bryne', 22, 'aisling@example.com', '2024-09-09'),
(4, 'Jane', 'Smith', 19, NULL, '2024-09-09');

SELECT * 
FROM students;

SELECT first_name, last_name 
FROM students;

SELECT * 
FROM students 
WHERE age>20;

SELECT * 
FROM students 
WHERE age <=19;

SELECT student_id, first_name, last_name 
FROM students 
WHERE age = 21;

SELECT * 
FROM students 
WHERE age BETWEEN 18 AND 21;

SELECT * 
FROM students 
WHERE age IN(19,22);

SELECT * 
FROM students 
WHERE age <> 19;

SELECT * 
FROM students 
WHERE email IS NULL;

SELECT * 
FROM students 
WHERE email IS NOT NULL;

SELECT first_name,last_name,age
FROM students
WHERE age >= 21;

CREATE TABLE courses(
course_id INTEGER PRIMARY KEY,
course_name TEXT NOT NULL,
credits INTEGER,
start_date DATE,
department TEXT,
);

INSERT INTO courses(course_id,course_name,credits,start_date,department)
VALUES
(1, 'Web Development', 10, '2024-09-15', 'Computing')
(2, 'Financial Accounting', 5, '2024-09-17', 'Business')
(3, 'Applied Statistics', 10, '2024-09-19', 'Science')
(4, 'Web Development', 5, NULL, 'Business')
(5, 'Web Development', 15, '2024-09-23', 'Computing')
(6, 'Web Development', 10, '2024-09-26', 'Science')