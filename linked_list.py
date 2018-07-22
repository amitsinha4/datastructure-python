class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		self.data = arg
		self.nextNode = None

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None
		self.size = 0


	def insertStart(self, data):
		self.size += 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode


	def size(self):
		return self.size


	def insetEnd(self, data):
		self.size += 1
		newNode = Node(data)
		actualNode = self.head

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode


	def traverseList(self):
		actualNode = self.head

		while actualNode is not None:
			print('{0} ---> {1}'.format(actualNode.data, actualNode.nextNode))
			actualNode = actualNode.nextNode


	def remove(self, data):
		
		if self.head is None:
			return

		self.size -= 1
		currentNode = self.head
		previousNone = None

		while currentNode.data != data:
			previousNone = currentNode
			currentNode = currentNode.nextNode

		if previousNone is None:
			self.head = currentNode.nextNode
		else:
			previousNone.nextNode = currentNode.nextNode
