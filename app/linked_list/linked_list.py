"""
Linked List
"""
from app.linked_list.node import Node


class LinkedList:
    """
    Linked List
    """

    def __init__(self):
        """
        Constructor
        """
        self.__head = None

    def insert_at_begining(self, data):
        """
        Insert At Begining
        """
        node = Node()
        node.set_data(data)
        if self.__head is None:
            self.__head = node
        else:
            node.set_next(self.__head)
            self.__head = node
        return node

    def insert_at_end(self, data):
        if self.__head is None:
            self.insert_at_begining(data)

        current = self.__head
        while current.get_next() is not None:
            current = current.get_next()
        node = Node()
        node.set_data(data)
        # node.set_next(None)
        current.set_next(node)
        return node

    def insert_at(self, data, index):
        if index < 0 or index > self.length_of_list():
            print("Invalid index.")
            return "Invalid index."
        if index == 0:
            node = self.insert_at_begining(data)
            return node
        count = 0
        current = self.__head
        while current:
            if count == index - 1:
                node = Node()
                node.set_data(data)
                node.set_next(current.get_next())
                current.set_next(node)
                return node
            else:
                current = current.get_next()
                count += 1

    def remove_at(self, index):
        if index < 0 or index > self.length_of_list():
            print("Invalid index.")
            return "Invalid index."
        current = self.__head
        count = 0
        while current:
            if count == index - 1:
                next_node = current.get_next()
                if next_node:
                    current.set_next(next_node.get_next())
                    return next_node
                else:
                    current.set_next(None)
            count += 1
            current = current.get_next()

    def remove_at_end(self):
        if self.__head is None:
            print("List is empty.")
            return "List is empty."
        current = self.__head
        while current.get_next():
            prev = current
            current = current.get_next()

        # Removing last element
        prev.set_next(None)
        return current

    def length_of_list(self) -> int:
        current = self.__head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def traversing_list(self):
        current = self.__head
        while current is not None:
            print(self.__head.get_data())
            current = current.get_next()
        return None

    def print_linked_list(self) -> str:
        if self.__head is None:
            print("List is empty.")
            return "List is empty."

        current = self.__head
        final_list = ""
        while current:
            final_list += f"{str(current.get_data())} --->"
            current = current.get_next()
        print(final_list)
        return final_list
