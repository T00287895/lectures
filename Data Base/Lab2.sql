CREATE TABLE students(
student_id INTEGER PRIMARY KEY,
student_name TEXT NOT NULL,
age INTEGER,
email TEXT UNIQUE,
enrolment_date DATE
);

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(1, 'Sarah Green', 21, 'sarah@example.com', '2024-09-10');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(2, 'John Murphy', 19, 'john@example.com', '2024-09-11'),
(3, 'Aisling Bryne', 22, 'aisling@example.com', '2024-09-09');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(4, 'Lian O"Connor', 20, 'liam.oconnor@example.com', '2024-09-12');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES
(5, 'Sally Brown', 21, 'sally@example.com', '2024-09-10');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(6, 'Sarah Smith', 20, 'sarahsmith@example.com', '2024-09-12');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(7, 'Fred Murphy', 20, 'fred@example.com', '2024-09-12');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(8, 'Alan Wallace', 20, 'alan"example.com', '2024-09-12');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(9, 'Brad Jones', 20, 'brad@example.com', '2024-09-12');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(10, 'Abdul Kahn', 21, 'abdul@example.com', '2024-09-12');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(11, 'Misha Soroka', 18, 'misha@example.com', '2024-09-12');

INSERT INTO students(student_id, student_name, age, email, enrolment_date)
VALUES 
(12, 'Walter White', 21, '', '2024-09-12');



SELECT * FROM students;

DROP TABLE IF EXISTS students;


CREATE TABLE employee(
employee_id INTEGER PRIMARY KEY,
employee_name TEXT NOT NULL,
age INTEGER,
email TEXT UNIQUE,
start_date DATE
);

INSERT INTO employee(employee_id, employee_name, age, email, start_date)
VALUES
(1, 'Emma Walsh', 34, 'Emma.walsh@example.com', '2021-02-15'),
(2, 'Liam Brown', 29, 'Liam.brown@example.com', '2023-06-01');

SELECT * FROM employee;