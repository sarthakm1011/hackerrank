class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		super(Node, self).__init__()
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next

	def insert_node(self, prev_node, new_data):
		# at any given position 
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node	
		

	def push(self, new_data):
		# at the beginning
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node


	def append(self, new_data):
		# at the end 
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next

		last.next = new_node


if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second
	second.next = third

	llist.printList()
