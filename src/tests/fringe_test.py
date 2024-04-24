import unittest
from random import randint, seed
from algorithms.fringe_search import fringe_search
from map_generation.get_shape import get_shape
from map_generation.shape_functions import *


class TestFringeSearch(unittest.TestCase):

    def setUp(self):
        seed(10)
        self.plane = get_shape(20, plane_function)
        self.zig_zag_plane = get_shape(20, zig_zag_plane_function)
        self.slope = get_shape(20, slope_function)
        self.corridor = get_shape(20, corridor_function)

    def test_plane(self):
        result = fringe_search((10, 0), (10, 19), self.plane)
        path = result['path']
        correct_path = [(10, 19), (10, 18), (10, 17), (10, 16), (10, 15), (10, 14), (10, 13), (10, 12), (10, 11),
                        (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (10, 0)]
        self.assertEqual(correct_path, path)

    def test_slope(self):
        result = fringe_search((10, 0), (10, 19), self.slope)
        path = result['path']
        correct_path = [(10, 19), (10, 18), (10, 17), (10, 16), (10, 15), (10, 14), (10, 13), (10, 12), (10, 11),
                        (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (10, 0)]
        self.assertEqual(correct_path, path)

    def test_zig_zag(self):
        result = fringe_search((10, 0), (10, 19), self.zig_zag_plane)
        path = result['path']
        correct_path = [(10, 19), (10, 18), (10, 17), (10, 16), (10, 15), (10, 14), (10, 13), (10, 12), (10, 11),
                        (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (10, 0)]
        self.assertEqual(correct_path, path)

    def test_corridor(self):
        result = fringe_search((1, 1), (18, 18), self.corridor)
        path = result['path']
        print(path)
        correct_path = [(18, 18), (17, 18), (16, 18), (15, 18), (14, 18), (13, 18), (12, 18), (11, 18), (10, 18), (9, 18), (8, 18), (7, 18), (6, 18), (5, 18), (4, 18), (
            3, 18), (2, 18), (1, 17), (1, 16), (1, 15), (1, 14), (1, 13), (1, 12), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1)]
        self.assertEqual(correct_path, path)
