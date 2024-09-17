class Human:
    def __init__(self, name, age): # Это специальный метод, который вызывается при создании объекта. Он
        # инициализирует атрибуты объекта.

        #Атрибуты - это переменные, принадлежащие объекту. Они хранят данные об объекте.
        self.name = name
        self.age = age
        self.say_info()
        #self - это специальный параметр в методах класса, который указывает на текущий объект.

    def say_info(self):  # это методы класса Human.
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):  #это методы класса Human.
        self.age += 1
        print(f'Мне исполнилось {self.age} лет')

    def change_name(self, new_name):  #это методы класса Human.
        old_name = self.name #ставим старое имя
        self.name = new_name #заменим имя на новое
        print(f'Предыдущее имя: {old_name}, новое имя: {self.name}')

    max.change_name('Михаил')

#Создание и использование объектов:
den = Human('Денис', 24)
max = Human('Максим', 25)
max.birthday()