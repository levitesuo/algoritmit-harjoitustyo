import unittest
from doubly_linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList(10, (0, 0))

    def test_i_setup(self):
        self.assertEqual(0, self.list.i)

    def test_add(self):
        self.list.insert_after((2, 2))
        self.assertEqual('[(0, 0), (2, 2)]', str(self.list))

    def test_add_false(self):
        self.assertEqual(False, self.list.iterate())

    def test_insert_2(self):
        self.list.insert_after((1, 1))
        self.list.insert_after((2, 2))
        self.assertEqual('[(0, 0), (2, 2), (1, 1)]', str(self.list))

    def test_delete_middle(self):
        self.list.insert_after((1, 1))
        self.list.insert_after((2, 2))
        self.list.delete_if_able((2, 2))
        self.assertEqual('[(0, 0), (1, 1)]', str(self.list))

    def test_iterate(self):
        self.list.insert_after((2, 2))
        self.list.insert_after((1, 1))
        self.list.iterate()
        self.assertEqual(self.list.get_i(), (1, 1))

    def test_delete_iter_last(self):
        self.list.insert_after((2, 2))
        self.list.insert_after((1, 1))
        self.list.iterate()
        self.list.delete_if_able(self.list._l_to_t(
            self.list.l[self.list.i]['past']))
        self.assertEqual('[(1, 1), (2, 2)]', str(self.list))

    def test_delete_last(self):
        self.list.insert_after((2, 2))
        self.list.insert_after((1, 1))
        self.list.delete_if_able((2, 2))
        self.assertEqual('[(0, 0), (1, 1)]', str(self.list))
