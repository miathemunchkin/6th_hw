#6th_hw.py

#Крок 1: Встановлення Залежностей

pip install faker

#Крок 2: Створення Схеми Бази Даних

-- create_schema.sql
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY(group_id) REFERENCES groups(id)
);

CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date DATE,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);
#Крок 3: Заповнення Бази Даних Випадковими Даними

import sqlite3
from faker import Faker
from random import choice, randint
from datetime import datetime, timedelta

# Налаштування бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиць
with open('create_schema.sql', 'r') as file:
    cursor.executescript(file.read())

# Ініціалізація Faker
fake = Faker()

# Додавання груп
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (group,))

# Додавання студентів
student_ids = []
for _ in range(50):  # 50 студентів
    name = fake.name()
    group_id = randint(1, 3)
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))
    student_ids.append(cursor.lastrowid)

# Додавання викладачів
teacher_ids = []
for _ in range(5):  # 5 викладачів
    name = fake.name()
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (name,))
    teacher_ids.append(cursor.lastrowid)

# Додавання предметів
subjects = ['Math', 'Physics', 'Chemistry', 'History', 'Literature', 'Biology', 'Geography', 'Art']
for subject in subjects:
    teacher_id = choice(teacher_ids)
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

# Додавання оцінок
for student_id in student_ids:
    for subject_id in range(1, len(subjects) + 1):
        for _ in range(randint(5, 20)):  # до 20 оцінок
            grade = randint(1, 100)
            date = fake.date_between(start_date='-2y', end_date='today')
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                           (student_id, subject_id, grade, date))

conn.commit()
conn.close()
# Крок 4: Створення SQL Запитів

# query_1.sql: 5 студентів із найбільшим середнім балом

-- query_1.sql
SELECT students.name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 5;
#query_2.sql: Студент із найвищим середнім балом з певного предмета

-- query_2.sql
SELECT students.name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = (SELECT id FROM subjects WHERE name = 'Math')
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;
#query_3.sql: Середній бал у групах з певного предмета

-- query_3.sql
SELECT groups.name AS group_name, AVG(grades.grade) AS average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = (SELECT id FROM subjects WHERE name = 'Math')
GROUP BY groups.id;

#query_4.sql: Середній бал на потоці (по всій таблиці оцінок)

-- query_4.sql
SELECT AVG(grade) AS average_grade
FROM grades;

#query_5.sql: Курси, які читає певний викладач

-- query_5.sql
SELECT subjects.name
FROM subjects
WHERE teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe');

#query_6.sql: Список студентів у певній групі

-- query_6.sql
SELECT students.name
FROM students
WHERE group_id = (SELECT id FROM groups WHERE name = 'Group A');

#query_7.sql: Оцінки студентів у окремій групі з певного предмета

-- query_7.sql
SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = (SELECT id FROM groups WHERE name = 'Group A')
AND grades.subject_id = (SELECT id FROM subjects WHERE name = 'Math');

#query_8.sql: Середній бал, який ставить певний викладач зі своїх предметів

-- query_8.sql
SELECT AVG(grades.grade) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe');

#query_9.sql: Список курсів, які відвідує студент

-- query_9.sql
SELECT DISTINCT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = (SELECT id FROM students WHERE name = 'Jane Smith');

#query_10.sql: Курси, які певному студенту читає певний викладач

-- query_10.sql
SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = (SELECT id FROM students WHERE name = 'Jane Smith')
AND subjects.teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe');