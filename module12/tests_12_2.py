import unittest

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
                    finishers[place] = participant.name  # Изменение здесь
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrey = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertEqual(result[max(result.keys())], "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertEqual(result[max(result.keys())], "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertEqual(result[max(result.keys())], "Ник")


if __name__ == '__main__':
    unittest.main()
