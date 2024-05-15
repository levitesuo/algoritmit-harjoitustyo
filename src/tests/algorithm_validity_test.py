import os
import unittest
from time import time
from map_generation.two_d_translator import two_d_translator
from functions.heurestic import djikstra_heurestic
from map_generation.node_list_generator import node_list_generator
from functions.a_star import a_star
from functions.fringe_search import fringe_search


class TestAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''
        These tests are run on movinai map AR0022SR.map. 
        The inputs_outputs list contains data parsed from the .map.scene file in a format ((start tuple), (goal tuple), (cost)).
        The list is 150 cases long. Witht the num_of_test_cases variable you can tune how meny run.
        150 cases might be a litle demanding for your machine.

        These test are designed to give a reasonable cerainty that the algorithms are running correctly.
        '''
        maps = ['AR0022SR']
        super(TestAlgorithms, cls).setUpClass()

        map_folder_path = os.path.join(
            os.getcwd(), "src/map_generation/maps/")

        test_cases = []
        for i, map in enumerate(maps):
            map_path = os.path.join(map_folder_path, map+".map")
            solutions_path = os.path.join(map_folder_path, map+".map.scen")
            test_cases.append({})
            with open(map_path, 'r') as map_file:
                test_cases[i]['node_list'] = node_list_generator(
                    map_file.read(), True)
            with open(solutions_path, 'r') as solutions_file:
                solution_rows = solutions_file.read().split("\n")[1:-1]
            test_cases[i]['scenarios'] = []
            for row in solution_rows:
                data = row.split()
                start = (int(data[4]), int(data[5]))
                goal = (int(data[6]), int(data[7]))
                cost = float(data[8])
                test_cases[i]['scenarios'].append(
                    {'start': start, 'goal': goal, 'cost': cost})
        cls.test_cases = test_cases

    def test_run_dijkstra(self):
        for map in self.test_cases:
            node_list = map['node_list']
            for scenario in map['scenarios']:
                generated_result = two_d_translator(
                    start=scenario['start'],
                    goal=scenario['goal'],
                    node_list=node_list,
                    algorithm=a_star
                )
                self.assertAlmostEqual(
                    scenario['cost'], generated_result['cost'], places=5, msg=f"s: {scenario['start']}, g:{scenario['goal']}, p:{generated_result['path']}")

    def test_run_frigne_search(self):
        for map in self.test_cases:
            node_list = map['node_list']
            for scenario in map['scenarios']:
                generated_result = two_d_translator(
                    start=scenario['start'],
                    goal=scenario['goal'],
                    node_list=node_list,
                    algorithm=fringe_search
                )
                self.assertAlmostEqual(
                    scenario['cost'], generated_result['cost'], places=5, msg=f"s: {scenario['start']}, g:{scenario['goal']}, p:{generated_result['path']}")

    def test_run_a_star(self):

        for map in self.test_cases:
            node_list = map['node_list']
            for scenario in map['scenarios']:
                generated_result = two_d_translator(
                    start=scenario['start'],
                    goal=scenario['goal'],
                    node_list=node_list,
                    algorithm=a_star,
                    heurestic=djikstra_heurestic
                )
                self.assertAlmostEqual(
                    scenario['cost'], generated_result['cost'], places=5, msg=f"s: {scenario['start']}, g:{scenario['goal']}, p:{generated_result['path']}")
