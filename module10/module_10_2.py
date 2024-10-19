import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_remaining = 100
        self.days = 0
        self.victory = False

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies_remaining > 0:
            time.sleep(1)  # Обозначаем 1 день сражения
            self.days += 1
            self.enemies_remaining -= self.power

            # Корректируем количество оставшихся врагов
            if self.enemies_remaining < 0:
                self.enemies_remaining = 0

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies_remaining} воинов.")

        self.victory = True
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание экземпляров класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидаем, пока оба потока завершатся
first_knight.join()
second_knight.join()

# Вывод окончательной строки
print("Все битвы закончились!")
