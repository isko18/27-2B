""" ООП - Объектно ориентированное программирование """
" Инкапсуляция "

# class PublicExample: # Публичный класс
#     def __init__(self, value):
#         self.value = value # Публичный атрибут
        
#     def info(self):
#         return self.value # Публичный метод
    
# # public = PublicExample("Публичный класс")
# # print(public.info()) # Вызов публичного метода
# # print(public.value) # Доступ к публичному атрибуту


# class ProtectedExample: # Защищенный класс
#     def __init__(self, value):
#         self._value = value # Защищенный атрибут
        
#     def _info(self):
#         return self._value # Защищенный метод

# protected = ProtectedExample("Защищенный класс")

# print(protected._info()) # Это работает, но противоречит принципам инкапсуляции
# print(protected._value) # Можно получить занчение напрямую, но это рекомендуется


# class PrivateExample: # Приватный класс
#     def __init__(self, value):
#         self.__value = value # Приватный атрибут
        
#     def __info(self):
#         return self.__value # Приватный метод
    
#     def access_private(self):
#         return self.__info() # Публичный метод, где мы получаем доступ к приватному методу или атрибуту
   
# private = PrivateExample("Приватный класс")

# # Прямой вызов приватного метода вызовет ошибку
# # print(private.__info())

# # Прямой вызов атрибута вызовет ошибку 
# # print(private.__value)

# # print(private.access_private())

# # Доступ к приватному атрибуту либо методу через name mangling
# print(private._PrivateExample__info())



" Полиморфизм  "

# num1 = 1
# num2 = 2
# print(num1 + num2)

# string1 = "Hello"
# string2 = "Geeks"
# print(string1 + string2)


# print(len("Geeks"))
# print(len(['python', 'js', 'php', 'react']))
# print(len({'python': 'django', 'js': 'react'}))


class Cat:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def info(self):
        print(f"Я кот. Меня зовут {self.name}. Мне {self.age} года")

    def make_sound(self):
        print("Мяу!")
        
class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def info(self):
        print(f"Я собака. Меня зовут {self.name}. Мне {self.age} года")

    def make_sound(self):
        print("Гаф!")
        
cat = Cat("Васька", 2)
dog = Dog("Мухтар", 3)

for animal in (cat, dog):
    animal.info()
    animal.make_sound()