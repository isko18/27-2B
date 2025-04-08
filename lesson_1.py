""" ООП - Объектно ориентированное программирование """

# hello_geeks = "Geeks" # Змеиный регистр

# HelloGeeks = "Geeks" # Верблюжий регистр


# class Car:
#     def __init__(self, motor, wheel, body): # __init__ - это конструктор
#         self.motor = motor # self - ссылка на текущий объект
#         self.wheel = wheel # атрибут класса
#         self.body = body 
        
#         self.bak = 20
#         self.is_start = False # Флажок
        
#     def info(self): # Функция внутри класса превращяется в метод
#         print(f"Мотор - {self.motor} Колесо - {self.wheel} Кузов - {self.body}")
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print("Машина заведена")
#         else:
#             print("У машины нет топлива")
            
#     def stop(self):
#         self.is_start = False
#         print("Машина заглушена")
        
#     def drive(self, city):
#         if self.is_start == True:
#             print(f'Машина едет в {city}')
#         else:
#             print("Машина не заведена")
        
# car = Car("V6", "R20", "Khan") # Экземпляр класса
# car.info()
# # car.start()
# car.stop()
# car.drive("Дубай")

""" Создать класс (Book).Передать параметры (avtor, book_name, year). Создать метод info. Вызвать переданный аргумент """

" Наследование "

class Animal:
    def __init__(self, name, color, year, type):
        self.name = name
        self.color = color
        self.year = year
        self.type = type
        
    def info(self):
        print(f"Название - {self.name} Цвет - {self.color} Возраст - {self.year} Виды - {self.type}")
        
class Cat(Animal):
    def __init__(self, name, color, year, type):
        super().__init__(name, color, year, type)
        # Animal().__init__(name, year)
        
    def info(self):
        return super().info()
    
    
animal = Animal("Кошка", "Рыжий", "40", "s22")
animal.info()

cat = Cat("Васька", "Черый", "18", "Ошлямский")
cat.info()