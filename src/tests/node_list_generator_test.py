import unittest
from map_generation.node_list_generator import node_list_generator
from map_generation.shape_functions import plane_function
from map_generation.get_shape import get_shape


class TestNodeListGenerator(unittest.TestCase):
    def setUp(self):
        plane = get_shape(3, plane_function)
        self.plane_node_list = node_list_generator(plane, False)

        two_d_map = "1\n2\n3\n4\n@@@@@\n@...@\n@...@\n@...@\n@@@@@\n"
        self.two_d_node_list = node_list_generator(two_d_map, True)

    def test_3d_positions(self):
        result = []
        for node in self.plane_node_list:
            result.append(node.position)
        self.assertEqual(
            result, [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)])

    def test_2d_positions(self):
        result = []
        for node in self.two_d_node_list:
            result.append(node.position)
        correct_result = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (
            2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(result, correct_result)

    def test_3d_edges_index_0(self):
        edges = self.plane_node_list[0].edges
        correct_result = [(1, 1), (1, 3), (1.4142135623730951, 4)]
        self.assertEqual(correct_result, edges)

    def test_3d_edges_index_5(self):
        edges = self.plane_node_list[4].edges
        correct_result = [(1, 1), (1, 3), (1, 5), (1, 7), (1.4142135623730951, 0), (
            1.4142135623730951, 2), (1.4142135623730951, 6), (1.4142135623730951, 8)]
        self.assertEqual(correct_result, edges)

    def test_2d_edges_index_0(self):
        edges = self.two_d_node_list[6].edges
        correct_result = [(1, 7), (1, 11), (1.41421356, 12)]
        self.assertEqual(correct_result, edges)

    def test_2d_edges_index_5(self):
        edges = self.two_d_node_list[12].edges
        correct_result = [(1, 7), (1, 11), (1, 13), (1, 17), (1.41421356, 6), (
            1.41421356, 8), (1.41421356, 16), (1.41421356, 18)]
        self.assertEqual(correct_result, edges)
