""" ООП - Объектно ориентированное программирование """
" Абстракция "


class It:
    def direction(self):
        pass 
    
    def language(self):
        pass 
    
    def db(self):
        pass 
    
class WebDeveloper(It):
    def direction(self):
        return f"Backend"
    
    def language(self):
        return f"Python"
    
    def db(self):
        return f"Yes"
    
class Vercel(It):
    def direction(self):
        return f"Frontend"
    
    def language(self):
        return f"JS"
    
    def db(self):
        return f"No"
    
class Server(It):
    def direction(self):
        return f"Devops"
    
    def language(self):
        return f"Linux/Python"
    
    def db(self):
        return f"Yes"
    
    
    '''Задание: "Система управления транспортом"
Цель:
Закрепить понимание наследования, полиморфизма и абстракции без использования модуля abc.

Описание задания:
Представь, что ты создаешь систему для управления различными видами транспорта. В этой системе есть общие характеристики для всех видов транспорта, но каждый вид транспорта имеет свои особенности.

Требования:
Создать базовый класс Transport:

У класса должны быть свойства brand (марка) и speed (скорость).
Добавь метод info(), который возвращает строку с информацией о транспорте (марка и скорость).
Создай метод move(), который просто выводит строку "Транспорт движется".
Создать классы-наследники Car, Bicycle, Airplane:

Каждый класс должен переопределить метод move(), чтобы он выводил уникальное сообщение о том, как этот вид транспорта движется:
Car — "Машина едет по дороге".
Bicycle — "Велосипед едет по тропинке".
Airplane — "Самолет летит в небе".
Добавь уникальные методы:
Car — метод honk(), который выводит "Машина сигналит".
Bicycle — метод ring_bell(), который выводит "Велосипед звенит звонком".
Airplane — метод take_off(), который выводит "Самолет взлетает".
Создать список транспортных средств и продемонстрировать полиморфизм:

Создай список с разными объектами: Car, Bicycle, Airplane.
Пройдись по списку и вызови метод move() для каждого транспорта.
Покажи использование уникальных методов для каждого вида транспорта.'''



""" БД - База Данных """
""" СУБД - Система управлением базы данных """
""" CRUD - CREATE, RETRIVE, UPDATE, DELETE """


import sqlite3

connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()

cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR (50) NOT NULL,
            age INT DEFAULT NULL, 
            direction TEXT,
            is_have BOOLEAN NOT NULL DEFAULT FALSE,
            birth_date DATE,
            rating DOUBLE (4,2) DEFAULT (0.0)        
        )                       
""")

def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    birth_date = input("Введите дату рождения: ")
    rating = float(input("Введите свой рейтинг: "))
    
    # cursor.execute(f""" INSERT INTO users
    #                (full_name, age, direction, is_have, birth_date, rating)
    #                VALUES ('{full_name}', {age}, '{direction}', {is_have}, '{birth_date}', {rating})""")
    
    # connect.commit() # Сохранение измения в бд
    
     #Использование форматированных строк (f"") для вставки значений в SQL-запрос может привести к уязвимости типа SQL-инъекция, если пользователь вводит специальные символы в текстовые поля.
    
    cursor.execute(""" INSERT INTO users
                   (full_name, age, direction, is_have, birth_date, rating)
                   VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, direction, is_have, birth_date, rating))
    
    connect.commit()    
    
    
# def all_students():
#     cursor.execute("SELECT * FROM users")
#     students = cursor.fetchall()
#     print(students)

def all_students(id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    students = cursor.fetchone()
    print(students)
    
def delete_students(id):
    cursor.execute("DELETE FROM users WHERE id=?",(id,))
    connect.commit()
    print(f"Пользователь {id}, был успешно удален")

delete_students(1)
# all_students(3)
# register()


