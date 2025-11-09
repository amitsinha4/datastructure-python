"""
Test of Queue
"""
from unittest import TestCase
from app.queue.queue import Queue


class TestQueue(TestCase):

    __queue = None

    def setUp(self):
        self.__queue = Queue()
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)

    def test_is_empty(self):
        self.assertEqual(self.__queue.is_empty(), False)

    def test_is_enqueue(self):
        self.__queue.enqueue(4)
        self.assertEqual(self.__queue.peek(), 1)

    def test_is_dequeue(self):
        self.assertEqual(self.__queue.dequeue(), 1)

    def test_dequeue(self):
        queue = Queue()
        self.assertEqual(queue.dequeue(), "Queue is empty")

    def test_size(self):
        self.assertEqual(self.__queue.size(), 3)

    def test_peek(self):
        queue = Queue()
        self.assertEqual(queue.peek(), "Queue is empty")
