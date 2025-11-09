"""
Queue Module
"""


class Queue:
    """
    Queue Module
    """

    __queue = None

    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def enqueue(self, element):
        self.__queue.append(element)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.__queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.__queue[0]

    def size(self):
        return len(self.__queue)
