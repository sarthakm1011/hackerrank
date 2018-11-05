class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		super(Node, self).__init__()
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def prinntList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next



if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second
	second.next = third

	llist.prinntList()
