import unittest
from tests_12_3 import RunnerTest, TournamentTest

class TestSuite(unittest.TestSuite):
    pass

# Используем TestLoader для добавления тестов в TestSuite
loader = unittest.TestLoader()
suite = TestSuite()
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
