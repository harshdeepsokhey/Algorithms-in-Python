## filename : ds_LinkedList_doubly.py 

## data structures ##
## Linked List: doubly LL ## 
## CS6101: Design of Analysis aand Algorothms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 

## Operations:
## Insert 
## Delete :
## Traverse
## Reversal : TODO
####################################################

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):

		# first node #
		new_node = Node(new_data)
		new_node.next = self.head

		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node

	def insertAfter(self, prev_node, new_data):
		
		# if LL is empty 
		if prev_node is None:
			print "The given prev node must be in LL"
			return 

		new_node = Node(new_data)

		new_node.next = prev_node.next
		prev_node.next = new_node
		new_node.prev = prev_node
		
		if new_node.next is not None:
			new_node.next.prev = new_node


	def insertAtEnd(self, new_data):

		new_node = Node(new_data)

		new_node.next = None

		# LL is empty
		if self.head is None:
			new_node.prev = None
			self.head = new_node
			return

		# traversal till the end 
		last = self.head
		
		while (last.next):
			last = last.next

		last.next = new_node

		new_node.prev = last
		
		return

	def deleteNodeByIndex(self, key):
		pass

	def deleteNodeByKey(self, key):

		temp = self.head
		prev = temp
		# key == head to be deleted
		if temp is not None:
			if temp.data == key:
				print "Deleting HEAD", temp.data
				self.head = temp.next
				self.head.prev = None
				temp = None
				return 


		while temp :
			if temp.data == key:
				break
			temp = temp.next


		if temp == None:
			print "Key Not Found!"
			return 
		else:
			print "Deleting ",temp.data

		temp.next.prev = temp.prev
		temp.prev.next = temp.next
		temp = None



	def traversal(self):

		temp = self.head
		while (temp):
			print temp.data,"<->", 
		 	temp = temp.next

		print "Null"

	def reverseTraversal(self):
		tail = self.head
		while (tail.next):
			tail = tail.next

		while (tail):
			print tail.data,"<->",
			tail = tail.prev

		print "Null"



if __name__ == '__main__':

	llist = DoublyLinkedList()
	
	llist.insertAtEnd(10)

	llist.push(25)

	llist.push(35)

	llist.insertAtEnd(40)

	llist.insertAfter(llist.head.next , 52)

	print "Forward Traversal :"
	llist.traversal()

	print "Reverse Traversal :"
	llist.reverseTraversal()

	print "Deleting HEAD node :"
	llist.deleteNodeByKey(35)

	print "LL after deleting node :"
	llist.deleteNodeByKey(52)

	print "Forward Traversal after Deletion :"
	llist.traversal()

	print "Reverse Traversal after Deletion :"
	llist.reverseTraversal()
