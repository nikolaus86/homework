class Animal:
    def __init__(self, name):
        self.alive = True  # Живой
        self.fed = False   # Накормленный
        self.name = name   # Индивидуальное название

class Plant:
    def __init__(self, name):
        self.edible = False # Съедобность
        self.name = name    # Индивидуальное название

class Mammal(Animal):
    def eat(self, food):
        if food.edible:  # Проверяем, съедобен ли переданный объект
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:  # Проверяем, съедобен ли переданный объект
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    pass  # Цветы по умолчанию несъедобные

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем на съедобное

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка и вывод информации
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Волк пытается съесть цветок, а Хатико фрукт
a1.eat(p1)  # Волк не должен есть цветок
a2.eat(p2)  # Хатико должен съесть фрукт

print(a1.alive)
print(a2.fed)
