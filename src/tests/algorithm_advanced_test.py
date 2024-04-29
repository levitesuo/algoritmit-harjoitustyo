from map_generation.shape_functions import layered_noise
from map_generation.get_shape import get_shape
from algorithms.a_star import a_star
from algorithms.fringe_search import fringe_search
import unittest
from services.generated_map_translator import generated_map_translator
from algorithms.functions.heurestic_function import heurestic_function


class TestAlgorithmAdvanced(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        num_of_test_cases = 1

        super(TestAlgorithmAdvanced, cls).setUpClass()

        cls.test_maps = [get_shape(data_resolution=50,
                                   shape_func=lambda x, y: layered_noise(
                                       random_seed=seed,
                                       x=x, y=y,
                                       octaves=(1, 5, 10),
                                       amplitudes=(1, 0.2, 0.05)
                                   )) for seed in range(num_of_test_cases)]

        cls.outputs = [generated_map_translator(start=(1, 1),
                                                goal=(49, 49),
                                                grid=m,
                                                algorithm=lambda s, g, n: a_star(
                                                    start=s,
                                                    goal=g,
                                                    node_list=n,
                                                    heurestic_function=lambda x, y, z: 0
        )) for m in cls.test_maps]

    def test_a_star_advanced(self):
        for i, m in enumerate(self.test_maps):
            result = generated_map_translator(start=(1, 1),
                                              goal=(49, 49),
                                              grid=m,
                                              algorithm=lambda s, g, n: a_star(
                start=s,
                goal=g,
                node_list=n,
                heurestic_function=heurestic_function))
        self.assertEqual(self.outputs[i]['cost'], result['cost'])

    def test_fringe_search_advanced(self):
        for i, m in enumerate(self.test_maps):
            result = generated_map_translator(start=(1, 1),
                                              goal=(49, 49),
                                              grid=m,
                                              algorithm=lambda s, g, n: fringe_search(
                start=s,
                goal=g,
                node_list=n,
                heurestic_function=heurestic_function))
        self.assertEqual(self.outputs[i]['cost'], result['cost'])
