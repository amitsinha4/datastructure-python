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

    def test_print_empyt_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.print_linked_list(), "List is empty.")

    def test_length_of_list(self):
        self.assertEqual(self.__linked_list.length_of_list(), 4)

    def test_insert_at_end(self):
        self.__linked_list.insert_at_end(23)

    def test_insert_at_end_in_empty_list(self):
        linked_list = LinkedList()
        linked_list.insert_at_end(10)
        self.assertIsInstance(linked_list, LinkedList)

    def test_insert_at(self):
        self.__linked_list.insert_at(23, 3)

    def test_insert_at_with_invalid_index(self):
        self.assertEqual(
            self.__linked_list.insert_at(10, 100),
            "Invalid index."
        )

    def test_insert_at_beginning(self):
        linked_list = LinkedList()
        node = linked_list.insert_at(10, 0)
        self.assertIsInstance(node.__str__(), str)
        self.assertEqual(node.get_data(), 10)

    def test_remote_at(self):
        self.__linked_list.insert_at_end(100)
        node = self.__linked_list.remove_at(3)
        self.assertEqual(node.get_data(), 4)

    def test_remove_at(self):
        msg = self.__linked_list.remove_at(-1)
        self.assertEqual(msg, "Invalid index.")

    def test_remove_at_second_last(self):
        self.__linked_list.remove_at(4)

    def test_remove_at_end(self):
        self.__linked_list.insert_at_end(100)
        node = self.__linked_list.remove_at_end()
        self.assertEqual(node.get_data(), 100)
        self.assertEqual(node.get_next(), None)

    def test_remove_at_end_in_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.remove_at_end(), "List is empty.")

    def test_traverse_list(self):
        self.__linked_list.traversing_list()
