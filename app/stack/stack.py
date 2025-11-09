"""
Stack Module
"""


class Stack:
    """
    Stack Module
    """
    __stack = []

    def __init__(self):
        self.__stack = []

    def push(self, element: int):
        self.__stack.append(element)

    def pop(self):
        return self.__stack.pop()

    def is_empty(self):
        return len(self.__stack) == 0

    def size(self) -> int:
        return len(self.__stack)

    def peek(self) -> int:
        if self.is_empty():
            print("Stack is empty.")
            return "Stack is empty."
        return self.__stack[-1]
