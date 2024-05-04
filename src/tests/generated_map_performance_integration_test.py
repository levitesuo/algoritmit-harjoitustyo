import unittest
from random import seed, randint
from time import time

from map_generation.shape_functions import layered_noise
from map_generation.get_shape import get_shape
from map_generation.translator import translator
from map_generation.node_list_generator import node_list_generator
from functions.a_star import a_star
from functions.fringe_search import fringe_search
from functions.heurestic import heurestic


class TestAlgorithmAdvanced(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        num_of_maps = 5
        num_of_runs_per_map = 5
        data_resolution = 50

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
            for j in range(num_of_runs_per_map):
                start = (randint(0, data_resolution-1),
                         randint(0, data_resolution-1))
                goal = (randint(0, data_resolution-1),
                        randint(0, data_resolution-1))
                cost = translator(start=start,
                                  goal=goal,
                                  node_list=cls.test_cases[i]['node_list'],
                                  algorithm=lambda s, g, m: a_star(
                                      start=s,
                                      goal=g,
                                      node_list=m,
                                      heurestic_function=lambda x, y, z: 0
                                  ),
                                  ignore_path=True)['cost']
                scenarios.append({'start': start, 'goal': goal, 'cost': cost})
                cls.test_cases[i]['scenarios'] += scenarios

    def run_a_star(self):
        # pylint: disable=all
        start_time = time()
        for i in range(len(self.test_cases)):
            node_list = self.test_cases[i]['node_list']
            for j in range(len(self.test_cases[i]['scenarios'])):
                generated_cost = translator(
                    start=self.test_cases[i]['scenarios'][j]['start'],
                    goal=self.test_cases[i]['scenarios'][j]['goal'],
                    node_list=node_list,
                    algorithm=lambda s, g, m: a_star(
                        start=s, goal=g, node_list=m, heurestic_function=heurestic),
                    ignore_path=True)['cost']
                self.assertAlmostEqual(
                    self.test_cases[i]['scenarios'][j]['cost'], generated_cost)
        end_time = time()
        return end_time-start_time

    def run_dijkstar(self):
        # pylint: disable=all
        start_time = time()
        for i in range(len(self.test_cases)):
            node_list = self.test_cases[i]['node_list']
            for j in range(len(self.test_cases[i]['scenarios'])):
                generated_cost = translator(
                    start=self.test_cases[i]['scenarios'][j]['start'],
                    goal=self.test_cases[i]['scenarios'][j]['goal'],
                    node_list=node_list,
                    algorithm=lambda s, g, m: a_star(
                        start=s, goal=g, node_list=m, heurestic_function=lambda x, y, z: 0),
                    ignore_path=True)['cost']
                self.assertAlmostEqual(
                    self.test_cases[i]['scenarios'][j]['cost'], generated_cost)
        end_time = time()
        return end_time-start_time

    def run_fringe_search(self):
        # pylint: disable=all
        start_time = time()
        for i in range(len(self.test_cases)):
            node_list = self.test_cases[i]['node_list']
            for j in range(len(self.test_cases[i]['scenarios'])):
                generated_cost = translator(
                    start=self.test_cases[i]['scenarios'][j]['start'],
                    goal=self.test_cases[i]['scenarios'][j]['goal'],
                    node_list=node_list,
                    algorithm=lambda s, g, m: fringe_search(
                        start=s, goal=g, node_list=m, heurestic_function=lambda x, y, z: 0),
                    ignore_path=True)['cost']
                self.assertAlmostEqual(
                    self.test_cases[i]['scenarios'][j]['cost'], generated_cost)
        end_time = time()
        return end_time-start_time

    def test_performance_on_generated_map(self):
        djikstra_time = self.run_dijkstar()
        fringe_search_time = self.run_a_star()
        a_star_time = self.run_a_star()
        print(
            f"\tfringe_search_time: {fringe_search_time}\ta_star_time: {a_star_time}\tdijkstra_time: {djikstra_time}")
        self.assertGreater(djikstra_time, fringe_search_time,
                           msg="Fringe search is slower than dijkstra.")
        self.assertGreater(djikstra_time, a_star_time,
                           msg="A_star is slower tha dijkstra.")
