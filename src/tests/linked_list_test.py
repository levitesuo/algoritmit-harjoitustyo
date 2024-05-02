import unittest
from objects.doubly_linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList(100, 0)

    def test_i_setup(self):
        self.assertEqual(0, self.list.i)

    def test_add(self):
        self.list.insert_after(11)
        self.assertEqual('[0, 11]', str(self.list))

    def test_add_false(self):
        self.assertEqual(False, self.list.iterate())

    def test_insert_2(self):
        self.list.insert_after(11)
        self.list.insert_after(22)
        self.assertEqual('[0, 22, 11]', str(self.list))

    def test_delete_middle(self):
        self.list.insert_after(11)
        self.list.insert_after(22)
        self.list.delete_if_able(22)
        self.assertEqual('[0, 11]', str(self.list))

    def test_iterate(self):
        self.list.insert_after(22)
        self.list.insert_after(11)
        self.list.iterate()
        self.assertEqual(self.list.get_i(), 11)

    def test_delete_iter_last(self):
        self.list.insert_after(22)
        self.list.insert_after(11)
        self.list.iterate()
        self.list.delete_if_able(0)
        self.assertEqual('[11, 22]', str(self.list))

    def test_delete_last(self):
        self.list.insert_after(22)
        self.list.insert_after(11)
        self.list.delete_if_able(22)
        self.assertEqual('[0, 11]', str(self.list))

    def test_del_cur_last(self):
        self.list.insert_after(22)
        self.list.insert_after(11)
        self.list.iterate()
        self.list.iterate()
        self.list.delete_current()
        self.assertEqual("[0, 11]", str(self.list))
