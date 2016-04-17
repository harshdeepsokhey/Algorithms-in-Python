## filename: ds_LinkedList_singly.py

## data structures
## Linked List: singly LL
## CS6101: Design of Analysis aand Algorothms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 

## Operations:
## Insert 
## Delete
## Traverse
## Reversal : TODO
####################################################

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None


	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head

		self.head = new_node

	def insertAfterNode(self, prev_node, new_data):
		
		# if LL is empty 
		if prev_node is None:
			print "Node is not present in the LL "
			return 

		new_node = Node(new_data)

		new_node.next = prev_node.next
		prev_node.next = new_node

	def insertAtEnd(self, new_data):

		new_node = Node(new_data)

		# LL is empty
		if self.head is None:
			self.head = new_node
			return

		# traversal till the end 
		last = self.head
		
		while (last.next):
			last = last.next

		last.next = new_node


	def deleteNode(self, key):

		temp = self.head
		prev = temp
		# key == head to be deleted
		if temp is not None:
			if temp.data == key:
				print "Deleting HEAD ",temp.data
				self.head = temp.next
				temp = None
				return 


		while temp :
			if temp.data == key:
				break
			prev = temp
			temp = temp.next


		if temp == None:
			print "Key Not Found!"
			return 
		else:
			print "Deleting ",temp.data


		prev.next = temp.next
		temp = None


	def display(self):

		temp = self.head
		while (temp):
			print temp.data, " -> ", 
		 	temp = temp.next

		print "Null"

if __name__ == '__main__':

	llist = SinglyLinkedList()
	
	llist.insertAtEnd(10)

	llist.push(25)

	llist.push(35)

	llist.insertAtEnd(40)

	llist.insertAfterNode(llist.head.next , 52)

	print "Linked List : "
	llist.display()

	print "Deleting HEAD Node: "
	llist.deleteNode(35)
	llist.display()

	print "Linked List after deletion of Node :"
	llist.deleteNode(52)
	llist.display()

	
