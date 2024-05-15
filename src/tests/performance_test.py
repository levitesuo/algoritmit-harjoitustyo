import unittest
from random import seed, randint
from math import sqrt
from time import time

from map_generation.shape_functions import layered_noise
from map_generation.get_shape import get_shape
from map_generation.node_list_generator import node_list_generator
from functions.a_star import a_star
from functions.fringe_search import fringe_search
from functions.heurestic import heurestic, djikstra_heurestic


class TestAlgorithmAdvanced(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        num_of_maps = 20
        num_of_runs_per_map = 10
        data_resolution = 75

        super(TestAlgorithmAdvanced, cls).setUpClass()
        seed(10)

        cls.test_cases = []
        for i in range(num_of_maps):
            cls.test_cases.append({})
            cls.test_cases[i]['scenarios'] = []
            cls.test_cases[i]['node_list'] = node_list_generator(get_shape(data_resolution=data_resolution,
                                                                           shape_func=lambda x, y: layered_noise(
                                                                               random_seed=i,
                                                                               x=x, y=y,
                                                                               octaves=(
                                                                                   1, 5, 10),
                                                                               amplitudes=(
                                                                                   1, 0.2, 0.05)
                                                                           )), False)
            scenarios = []
            for _ in range(num_of_runs_per_map):
                start = (randint(0, data_resolution-1),
                         randint(0, data_resolution-1))
                goal = (randint(0, data_resolution-1),
                        randint(0, data_resolution-1))
                translated_start = start[1] * \
                    data_resolution + start[0]
                translated_goal = goal[1] * \
                    data_resolution + goal[0]
                scenarios.append(
                    {'start': translated_start, 'goal': translated_goal})
                cls.test_cases[i]['scenarios'] += scenarios

    def test_performance_on_generated_map(self):
        djikstra_time = 0
        fringe_search_time = 0
        a_star_time = 0
        for map_cases in self.test_cases:
            node_list = map_cases['node_list']
            for scenario in map_cases['scenarios']:
                a = time()
                djikstra_results = a_star(
                    scenario['start'], scenario['goal'], node_list, djikstra_heurestic)
                b = time()
                for node in node_list:
                    node.reset()
                c = time()
                a_star_results = a_star(
                    scenario['start'], scenario['goal'], node_list, heurestic)
                d = time()
                for node in node_list:
                    node.reset()
                e = time()
                fringe_search_results = fringe_search(scenario['start'],
                                                      scenario['goal'], node_list, heurestic)
                f = time()
                for node in node_list:
                    node.reset()
                djikstra_time += b - a
                a_star_time += d - c
                fringe_search_time += f - e

                self.assertAlmostEqual(
                    djikstra_results['cost'], a_star_results['cost'])
                self.assertAlmostEqual(
                    djikstra_results['cost'], fringe_search_results['cost'])
        print(
            f"\tfringe_search_time: {fringe_search_time}\ta_star_time: {a_star_time}\tdijkstra_time: {djikstra_time}")

        self.assertGreater(djikstra_time, a_star_time,
                           msg="A_star is slower tha dijkstra.")
