## Basic Doubly Linked List ##

## TODO :  
## To be remove when able to import classes from different folders 
## ================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def createList(self, dataList):
        '''
        Usage:
        from LinkedList import LinkedList
        dataList = [<some data values here>]
        llist = LinkedList()
        newList = llist.createList(self, dataList)
        Creates a new list using data from dataList
        '''
        n = len(dataList)
        newLList = LinkedList()
        for i in xrange(n):
            newLList.push(dataList[i])
        return newLList


    def push(self, data):
        node = Node(data)
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev =  node

        self.head = node

    def pop(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        return temp.data

    def insertNode(self, beforeNode, keyNode):
        if beforeNode is None:
            print "Node doesnot exists in LinkedList"
            return

        # copy data in a new node
        newNode = Node(keyNode.data)

        flag = 0
        if beforeNode is self.head:
            flag = 1

        # delete the original node 
        self.deleteNode(keyNode)

        #insert new node in its sorted place
        if flag:
            newNode.next = beforeNode
            beforeNode.prev = newNode
            newNode.prev = None
            self.head = newNode
        else:
            newNode.next = beforeNode
            beforeNode.prev.next = newNode
            newNode.prev = beforeNode.prev
            beforeNode.prev = newNode 

        if newNode.next is not None:
            newNode.next.prev = newNode

    def deleteNode(self, key):
        temp = self.head
        # when deleting head node
        if temp is not None:
            if temp is key:
                self.head = temp.next
                self.head.prev = None
                temp = None
                return
        # when deleting last element        
        while(temp):
            if temp.data == key.data:
                break
            temp = temp.next

        if temp is None:
            print "Key not found"
            return
        else:
            if temp.next is not None:
               temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp = None


    def display(self):
        temp = self.head
        print "Forward Traversal:"
        while (temp):
            print temp.data, " -> ", 
            temp = temp.next
        print "Null"
        
        temp = self.head
        print "Reverse Traversal:"
        while temp.next is not None:
            temp = temp.next
        while(temp):
            print temp.data, " -> ",
            temp = temp.prev
        print "Null"



if __name__ == '__main__':

    llist = LinkedList()
    n = 10
    for i in xrange(n):
        llist.push(i*10)
    llist.display()
    newNode = Node(40)   
    llist.insertNode(llist.head, newNode)
    llist.display()
    newNode = Node(50)   
    llist.insertNode(llist.head.next.next, newNode)
    llist.display()