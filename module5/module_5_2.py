class House:
    def __init__(self, name, number_of_floors):
        self.name = name          # имя дома
        self.number_of_floors = number_of_floors  # количество этажей

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors  # возвращаем количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # строковое представление

# Создаем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to у объектов
h1.go_to(5)
h2.go_to(10)

# Пример использования __str__ и __len__
print(h1)  # Название: ЖК Горский, кол-во этажей: 18
print(h2)  # Название: Домик в деревне, кол-во этажей: 2
print(len(h1))  # 18
print(len(h2))  # 2
