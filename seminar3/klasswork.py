# Что за парадигма - числа?
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 ==0]
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("Квадраты чисел: ", squared_numbers)
print("Четные числа: ", even_numbers)
print("Удвоенные числа", doubled_numbers)
# Ответ: Использованы императивная и декларативная парадигмы!
# Почему это так: генераторы списков и метод map - признаки декларативной (если быть точным - функциональной) парадигмы, 
# а весь остальной код остаётся в рамках императивного стиля

# Что за парадигма - автомобиль
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.color} автомобиль {self.brand} завел двигатель.")

    def stop_engine(self):
        print(f"{self.color} автомобиль {self.brand} заглушил двигатель.")
# Ответ: это объектно-ориентированная парадигма.
# Почему это так: в данном коде определяются два класса Vehicle и Car и их методы __init__, start_engine, stop_engine.

#Что за парадигма: музыкальный плейлист
class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

def create_playlist(player:MusicPlayer, songs:list):
    for song in songs:
        player.add_song(song)

player = MusicPlayer()
create_playlist(player)
# Ответ: здесь использованы ООП, процедурная и структурная парадигмы.
# Почему это так: объявлен класс MusicPlayer, его конструктор и метод add_song. Для создания плейлиста
# используется стандартная процедура (НЕ метод), также используется цикл for, и нет goto.

# Задача. Реализовать класс Shape, содержащий пустые методы get_area и get_perimeter. Использовать библиотеку
# абстрактных классов “ABC” в данном случае - не обязательно.
class Shape:
    def get_perimeter(self):
        pass

    def get_area(self):
        pass

# Задача. Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса Circle.
# ○ get_area - метод для расчета площади круга
# ○ get_perimeter - метод для расчета периметра окружности
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2
    
# Задача. Реализовать дочерний от Shape класс Triangle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса.
# ○ get_area - метод для расчета площади
# ○ get_perimeter - метод для расчета периметра
import math

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))