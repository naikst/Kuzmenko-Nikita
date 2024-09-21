class Human:  # Класс Human, который описывает человека.

    head = True

    def __init__(self, name, age):  # Это специальный метод, который вызывается при создании объекта. Он
        # инициализирует атрибуты объекта.

        # Атрибуты - это переменные, принадлежащие объекту. Они хранят данные об объекте.
        self.name = name
        self.age = age
        self.say_info()
        # self - это специальный параметр в методах класса, который указывает на текущий объект.

    def say_info(self):  # это методы класса Human.
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):  # это методы класса Human.
        self.age += 1
        print(f'Мне исполнилось {self.age} лет')

    def _str__(self):  # это специальный метод, который вызывается при преобразовании объекта в строку.
        return f'{self.name}'  # Возвращает строку с информацией о человеке.

    def __len__(self):
        return self.age  # Возвращает возраст человека.

    def __lt__(self, other):
        return self.age < other.age  # Возвращает True, если возраст текущего человека меньше возраста other, иначе False.

    def __gt__(self, other):
        return self.age > other.age  # Возвращает True, если возраст текущего человека больше возраста other, иначе False.

    def __eq__(self, other):
        return self.age == other.age  # Возвращает True, если возраст текущего человека ра��ен возрасту other, иначе False.

    def __bool__(self):
        return bool(self.age > 0)  # Возвращает True, если возраст человека положительный, иначе False.

    def __del__(self):
        print(f'{self.name} ушёл')  # Выводит сообщение об удалении объекта.




# Создание и использование объектов:
den = Human('Денис', 24)
max = Human('Максим', 25)
a = 6

print(Human.head)
