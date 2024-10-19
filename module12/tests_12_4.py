import logging
import unittest

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Usain', -5)  # Передаем отрицательную скорость
            runner.walk()
        except ValueError as e:
            logging.exception('Ошибка в test_walk')
            self.assertIsInstance(e, ValueError)  # Убедитесь, что ошибка действительно ValueError
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(12345, 10)  # Передаем что-то кроме строки
            runner.run()
        except TypeError as e:
            logging.exception('Ошибка в test_run')
            self.assertIsInstance(e, TypeError)  # Убедитесь, что ошибка действительно TypeError
        else:
            logging.info('"test_run" выполнен успешно')

if __name__ == '__main__':
    unittest.main()
