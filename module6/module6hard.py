import math #импорт


class Figure:
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = color
        self.filled = True

    @property
    def color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    @property
    def sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)  # Периаметр, считая что стороны определяют длину

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]]
        else:
            self.__sides = [1]  # Соответствующее количество сторон

    @property
    def radius(self):
        return self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 3:
            self.__sides = list(sides)
        else:
            self.__sides = [1, 1, 1]  # Соответствующее количество сторон

    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.set_sides(*sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = [new_sides[0]] * self.sides_count
        elif len(new_sides) == self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count  # Иначе все единицы

    def get_volume(self):
        return self.__sides[0] ** 3


# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.color)
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.color)

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.sides)
circle1.set_sides(15)  # Изменится
print(circle1.sides)

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
