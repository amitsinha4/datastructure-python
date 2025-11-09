"""
Test linked list
"""
from unittest import TestCase
from app.linked_list.linked_list import LinkedList


class TestLinkedList(TestCase):
    """
    Test linked list
    """
    __linked_list = None

    def setUp(self):
        self.__linked_list = LinkedList()
        self.__linked_list.insert_at_begining(data=1)
        self.__linked_list.insert_at_begining(data=2)
        self.__linked_list.insert_at_begining(data=3)
        self.__linked_list.insert_at_end(data=4)

    def test_print_list(self):
        self.assertNotEqual(self.__linked_list.print_linked_list(), "")

    def test_length_of_list(self):
        self.assertEqual(self.__linked_list.length_of_list(), 4)

    def test_insert_at_end(self):
        self.__linked_list.insert_at_end(23)

    def test_insert_at(self):
        self.__linked_list.insert_at(23, 3)

    def test_remote_at(self):
        self.__linked_list.insert_at_end(100)
        node = self.__linked_list.remove_at(3)
        self.assertEqual(node.get_data(), 4)

    def test_remove_at_end(self):
        self.__linked_list.insert_at_end(100)
        node = self.__linked_list.remove_at_end()
        self.assertEqual(node.get_data(), 100)
        self.assertEqual(node.get_next(), None)
