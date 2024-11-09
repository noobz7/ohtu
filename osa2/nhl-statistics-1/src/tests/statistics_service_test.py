import unittest
from statistics_service import StatisticsService
from player import Player
from player_reader import PlayerReader

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_fullname(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")

    def test_search_no_one_found(self):
        self.assertEqual(self.stats.search("Pasi"), None)

    def test_team_search(self):
        self.assertEqual(self.stats.team("EDM")[2].team, "EDM")

    def test_sorting_points(self):
        self.assertEqual(len(self.stats.top(3)), 4)
