import os
import unittest
from functions.a_star import a_star
from functions.fringe_search import fringe_search
from functions.two_d_heurestic import two_d_heurestics
from functions.heurestic import djikstra_heurestic
from map_generation.node_list_generator import node_list_generator


class TestAlgorithmDot3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestAlgorithmDot3, cls).setUpClass()
        map_folder_path = os.path.join(
            os.getcwd(), "src/map_generation/maps/")

        dot_3_filename = "dot_3"
        dot_3_path = os.path.join(map_folder_path, dot_3_filename + ".map")

        with open(dot_3_path, "r") as f:
            dot_3 = node_list_generator(f.read(), True)

        cls.map = dot_3

    def setUp(self):
        for node in self.map:
            node.reset()

    def test_closed_0_2_dijkstra(self):
        result = a_star(0, 2, self.map, djikstra_heurestic)
        correct_closed = [1, 2, 3, 2, False, False,
                          False, False, False]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_0_2_a_star(self):
        result = a_star(0, 2, self.map, two_d_heurestics)
        correct_closed = [1, 2, 3, False, False, False,
                          False, False, False]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_0_2_fringe_search(self):
        result = fringe_search(0, 2, self.map, two_d_heurestics)
        correct_cache = [(0, None), (1, 0), (2, 1),
                         (1, 0), False, False, False, False, False, ]
        self.assertEqual(correct_cache, result['cache'])

    def test_closed_0_8_dijkstra(self):
        result = a_star(0, 8, self.map, djikstra_heurestic)
        correct_closed = [1, 2, 3, 2, False, 4,
                          3, 4, 5]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_0_8_a_star(self):
        result = a_star(0, 8, self.map, two_d_heurestics)
        correct_closed = [1, 2, 3, 2, False, 4,
                          3, 4, 5]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_0_8_fringe_search(self):
        result = fringe_search(0, 8, self.map, two_d_heurestics)
        correct_cache = [(0, None), (1, 0), (2, 1),
                         (1, 0), False, (3, 2), (2, 3), False, (4, 5)]
        self.assertEqual(correct_cache, result['cache'])

    def test_closed_5_3_dijkstra(self):
        result = a_star(5, 3, self.map, djikstra_heurestic)
        correct_closed = [4, 3, 2,
                          5, False, 1,
                          4, 3, 2]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_5_3_a_star(self):
        result = a_star(5, 3, self.map, two_d_heurestics)
        correct_closed = [4, 3, 2,
                          5, False, 1,
                          False, 3, 2]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_5_3_fringe_search(self):
        result = fringe_search(5, 3, self.map, two_d_heurestics)
        correct_cache = [(3, 1), (2, 2), (1, 5),
                         (4, 0), False, (0, None),
                         (3, 7), (2, 8), (1, 5)]
        self.assertEqual(correct_cache, result['cache'])
