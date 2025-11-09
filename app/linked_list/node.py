"""
Node Module
"""


class Node:
    """
    Node for linked list
    """

    def __init__(self):
        """
        Constructor (Initalizer)
        """
        self.__data = None
        self.__next_node = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next_node

    def set_next(self, node):
        self.__next_node = node

    def __str__(self):
        """
        Object Representation
        """
        f"<Node {self.__data} points to {self.__next_node}>"
