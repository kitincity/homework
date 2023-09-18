# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

#подключаемся к БД
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()

# Создаем таблицу Students
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
Student_Id INTEGER PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL,
FOREIGN KEY (School_id) REFERENCES School(School_id)
)
''')

# Сохраняем изменения 
connection.commit()

records = [(201, 'Иван', 1),
           (202, 'Петр', 2),
           (203, 'Анастасия', 3),
           (204, 'Игорь', 4)]

sql= """INSERT INTO Students
      (Student_Id, Student_name, School_Id)
       VALUES (?, ?, ?);"""

cursor.executemany(sql, records)

print('Введите Id студента')

id = int(input())

cursor.execute('''SELECT Student_id, Student_name, School.School_id, School_name FROM Students,School
               where Students.School_Id = School.School_Id and Student_id = ?''',(id,))
students = cursor.fetchall()

# Выводим результаты
for student in students:
  print(student)

connection.close()