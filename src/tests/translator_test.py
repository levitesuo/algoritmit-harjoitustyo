import unittest
from time import sleep
from map_generation.translator import translator


class ResetObj:
    def reset(self):
        return


class TestLinkedList(unittest.TestCase):
    def test_path_translation1(self):
        args = {
            'start': (1, 1),
            'goal': (2, 2),
            'node_list': [ResetObj() for _ in range(16)]
        }

        def f(start, goal, function):
            return {'path': [0, 4, 8, 12]}

        result = translator(
            start=args['start'],
            goal=args['goal'],
            node_list=args['node_list'],
            algorithm=f
        )

        self.assertEqual(result['path'], [(0, 0), (0, 1), (0, 2), (0, 3)])

    def test_path_translation2(self):
        args = {
            'start': (1, 1),
            'goal': (2, 2),
            'node_list': [ResetObj() for _ in range(16)]
        }

        def f(start, goal, function):
            return {'path': [14, 2, 7, 6]}

        result = translator(
            start=args['start'],
            goal=args['goal'],
            node_list=args['node_list'],
            algorithm=f
        )

        self.assertEqual(result['path'], [(2, 3), (2, 0), (3, 1), (2, 1)])

    def test_timing(self):
        args = {
            'start': (1, 1),
            'goal': (2, 2),
            'node_list': [ResetObj() for _ in range(16)]
        }

        def f(start, goal, function):
            sleep(0.5)
            return {'path': [0, 4, 8, 12]}

        result = translator(
            start=args['start'],
            goal=args['goal'],
            node_list=args['node_list'],
            algorithm=f
        )

        self.assertAlmostEqual(0.5, result['time'], places=3)
