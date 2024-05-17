import os
import unittest
from functions.a_star import a_star
from functions.fringe_search import fringe_search
from functions.two_d_heurestic import two_d_heurestics
from functions.heurestic import djikstra_heurestic
from map_generation.node_list_generator import node_list_generator


class TestAlgorithmBlank3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestAlgorithmBlank3, cls).setUpClass()
        map_folder_path = os.path.join(
            os.getcwd(), "src/map_generation/maps/")

        blank_3_filename = "blank_3"
        blank_3_path = os.path.join(map_folder_path, blank_3_filename + ".map")

        with open(blank_3_path, "r") as f:
            blank_3 = node_list_generator(f.read(), True)

        cls.map = blank_3

    def setUp(self):
        for node in self.map:
            node.reset()

    def test_closed_1_2_dijkstra(self):
        result = a_star(1, 2, self.map, djikstra_heurestic)
        correct_closed = [False, 1, 2, False, 2, False, False, False, False]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_1_2_a_star(self):
        result = a_star(1, 2, self.map, two_d_heurestics)
        correct_closed = [False, 1, 2, False, False, False,
                          False, False, False]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_1_2_fringe_search(self):
        result = fringe_search(1, 2, self.map, two_d_heurestics)
        correct_cache = [(1, 1), (0, None), (1, 1),
                         (1.41421356, 1), (1, 1), (1.41421356, 1), False, False, False, ]
        self.assertEqual(correct_cache, result['cache'])

    def test_closed_4_1_dijkstra(self):
        result = a_star(4, 1, self.map, djikstra_heurestic)
        correct_closed = [False, 2, False, 2, 1, 2, False, 2, False]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_4_1_a_star(self):
        result = a_star(4, 1, self.map, two_d_heurestics)
        correct_closed = [False, 2, False,
                          False, 1, False, False, False, False]
        self.assertEqual(correct_closed, result['closed'])

    def test_closed_4_1_fringe_search(self):
        result = fringe_search(4, 1, self.map, two_d_heurestics)
        correct_cache = [(1.41421356, 4), (1, 4), (1.41421356, 4),
                         (1, 4), (0, None), (1, 4),
                         (1.41421356, 4), (1, 4), (1.41421356, 4)]
        self.assertEqual(correct_cache, result['cache'])

    def test_path_0_8_dijkstra(self):
        result = a_star(0, 8, self.map, djikstra_heurestic)
        correct_paht = [8, 4, 0]
        self.assertEqual(correct_paht, result['path'])

    def test_path_0_8_a_star(self):
        result = a_star(0, 8, self.map, two_d_heurestics)
        correct_paht = [8, 4, 0]
        self.assertEqual(correct_paht, result['path'])

    def test_path_0_8_frigne_search(self):
        result = fringe_search(0, 8, self.map, two_d_heurestics)
        correct_paht = [8, 4, 0]
        self.assertEqual(correct_paht, result['path'])

    def test_path_6_2_dijkstra(self):
        result = a_star(6, 2, self.map, djikstra_heurestic)
        correct_paht = [2, 4, 6]
        self.assertEqual(correct_paht, result['path'])

    def test_path_6_2_a_star(self):
        result = a_star(6, 2, self.map, two_d_heurestics)
        correct_paht = [2, 4, 6]
        self.assertEqual(correct_paht, result['path'])

    def test_path_6_2_frigne_search(self):
        result = fringe_search(6, 2, self.map, two_d_heurestics)
        correct_paht = [2, 4, 6]
        self.assertEqual(correct_paht, result['path'])
