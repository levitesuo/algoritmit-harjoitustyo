import unittest
from random import seed
from services.running_service import AppEngine


class TestAppEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AppEngine()

    def test_amplitudes_from_string(self):
        self.engine.set_amplitudes_from_string("11, 22, 33")
        self.assertEqual([11, 22, 33], self.engine.amplitudes)

    def test_octaves_from_string(self):
        self.engine.set_octaves_from_string("11, 22, 33")
        self.assertEqual([11, 22, 33], self.engine.octaves)

    def test_set_start_from_string(self):
        self.engine.set_start_from_string("11, 22")
        self.assertEqual((11, 22), self.engine.start)

    def test_set_goal_from_string(self):
        self.engine.set_goal_from_string("11, 22")
        self.assertEqual((11, 22), self.engine.goal)

    def test_init_empty_values_all_empty(self):
        seed(1)
        self.engine.init_empty_values()
        self.assertEqual(self.engine.get_values(), {
                         'data_resolution': 75, 'random_seed': 138, 'goal': (61, 65), 'start': (13, 10)})

    def test_init_empty_values_seed_filled(self):
        self.engine.random_seed = 10
        self.engine.init_empty_values()
        self.assertEqual(self.engine.get_values(), {
                         'data_resolution': 75, 'random_seed': 10, 'goal': (39, 65), 'start': (37, 10)})

    def test_init_empty_values_start_filled(self):
        seed(1)
        self.engine.start = (10, 10)
        self.engine.init_empty_values()
        self.assertEqual(self.engine.get_values(), {
                         'data_resolution': 75, 'random_seed': 138, 'goal': (49, 65), 'start': (10, 10)})

    def test_init_empty_values_goal_filled(self):
        seed(1)
        self.engine.goal = (10, 10)
        self.engine.init_empty_values()
        self.assertEqual(self.engine.get_values(), {
                         'data_resolution': 75, 'random_seed': 138, 'goal': (10, 10), 'start': (13, 10)})

    def test_init_empty_values_resolution_filled(self):
        self.engine.data_resolution = 101
        seed(1)
        self.engine.init_empty_values()
        self.assertEqual(self.engine.get_values(), {
                         'data_resolution': 101, 'random_seed': 138, 'goal': (74, 91), 'start': (13, 10)})
