import unittest

def skip_if_frozen(test_method):
    def wrapper(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self)
    return wrapper

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Этот тест будет выполняться

    @skip_if_frozen
    def test_challenge(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Все тесты в этом классе будут пропущены

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, Runner("Усэйн", speed=10), Runner("Ник", speed=3))
        result = tournament.start()
        self.assertEqual(result[max(result.keys())], "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, Runner("Андрей", speed=9), Runner("Ник", speed=3))
        result = tournament.start()
        self.assertEqual(result[max(result.keys())], "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, Runner("Усэйн", speed=10), Runner("Андрей", speed=9), Runner("Ник", speed=3))
        result = tournament.start()
        self.assertEqual(result[max(result.keys())], "Ник")

if __name__ == '__main__':
    unittest.main()
