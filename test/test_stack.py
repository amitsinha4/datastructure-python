"""
Test stack
"""
from unittest import TestCase
from app.stack.stack import Stack


class TestStack(TestCase):
    """
    Test stack
    """

    __stack = None

    def setUp(self):
        self.__stack = Stack()
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)

    def test_push_in_stack(self):
        self.__stack.push(4)
        self.assertEqual(self.__stack.peek(), 4)

    def test_peek_in_stack(self):
        self.assertEqual(self.__stack.peek(), 3)

    def test_pop_in_stack(self):
        self.assertEqual(self.__stack.pop(), 3)

    def test_size_of_stack(self):
        self.assertEqual(self.__stack.size(), 3)

    def test_size_of_empty_stack(self):
        stack = Stack()
        self.assertEqual(stack.peek(), "Stack is empty.")
