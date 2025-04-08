""" ООП - Объектно ориентированное программирование """
" Наследование "

class Game: # Родительский класс
    def __init__(self, game_name, game_year, company, graphics):
        self.game_name = game_name
        self.game_year = game_year
        self.company = company
        self.graphics = graphics
        
    def info(self):
        print(f"Game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics}")
        
# game = Game("Minecraft", 2017, "Mojang", "Full HD")
# game.info()

class Roblox(Game):
    def __init__(self, game_name, game_year, company, graphics, multiplayer):
        super().__init__(game_name, game_year, company, graphics)
        self.multiplayer = multiplayer
        
        self.name = "Player"
        self.gender = "None"
        self.skin = "None"
        self.hp = 100
        
    def info(self):
        print(f"Game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics} -  {self.multiplayer}")
        
    def info_player(self):
        print(f"Игрок - {self.name} - {self.gender} - {self.skin}, {self.hp}")
        
    def edit_player(self):
        name = input("Ввдите свое имя: ")
        gender = input("Введите свой пол: ")
        skin = input("Введиье свой облик: ")
        self.name = name
        self.gender = gender
        self.skin = skin
    
roblox = Roblox("Roblox", 2006, "Roblox corp.", "ULTRA", "4")
roblox.info()
roblox.edit_player()
roblox.info_player()

class Strike(Roblox):
    def __init__(self, game_name, game_year, company, graphics, multiplayer):
        super().__init__(game_name, game_year, company, graphics, multiplayer)
        
    def edit_player(self):
        return super().edit_player()
    
    def info_player(self):
        return super().info_player()
    
strike = Strike()

''''Задание: Симуляция Зоопарка с Конструкторами
Создайте классы, которые будут моделировать разных животных в зоопарке, используя множественное наследование и конструкторы для инициализации объектов.

Базовые классы:

Создайте класс Animal, который будет представлять общее животное. У этого класса должен быть конструктор __init__(), который принимает параметр name для имени животного. Также добавьте методы eat() и sleep(), которые выводят сообщения, например, "{name} ест" и "{name} спит".

Создайте класс Walker, который будет представлять животных, которые могут ходить. У этого класса должен быть метод walk(), который выводит сообщение "{name} ходит".

Создайте класс Swimmer, который будет представлять животных, которые могут плавать. У этого класса должен быть метод swim(), который выводит сообщение "{name} плавает".

Создайте класс Flyer, который будет представлять животных, которые могут летать. У этого класса должен быть метод fly(), который выводит сообщение "{name} летает".

Комбинированные классы:
                                            
Создайте класс Penguin, который наследуется от Animal, Walker, и Swimmer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что пингвин может ходить и плавать.

Создайте класс Duck, который наследуется от Animal, Walker, Swimmer, и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что утка может ходить, плавать и летать.

Создайте класс Bat, который наследуется от Animal и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что летучая мышь может летать.

Тестирование:

Создайте экземпляры каждого из созданных вами классов, передавая им имена, и вызовите для них методы describe(), а также методы, относящиеся к их поведению (например, walk(), swim(), fly()).'''