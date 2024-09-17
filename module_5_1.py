class House:  # Класс дома
    # Конструктор дома
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Для перемещения лифта
    def go_to(self, new_floor):
        # Выводит этажи от текущего до нового
        if 1 <= new_floor <= self.number_of_floors:
            # Выводит этажи от текущего до нового
            for floor in range(1, new_floor + 1):
                # Выводит этаж
                print(floor)
        else:  # Выводит сообщение об ошибке, если этаж не существует
            # Выводит сообщение об ошибке
            print("Такого этажа не существует")

    # Для вывода информации о доме
    def __str__(self):  # Выводит информацию о доме
        # Выводит информацию о доме в виде строки в формате "Дом 'имя' с 'количество этажей' этажами"
        return f"Дом '{self.name}' с {self.number_of_floors} этажами"


# Вызовем метод __str__ для обоих домов
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print("ЖК Горский:")
h1.go_to(5)
print("Домик в деревне':")  # Выводит этажи от текущего до нового
h2.go_to(10)  #
