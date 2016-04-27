## filename: Queues.py

## dataStructures
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## Implements Queues in Python
##
## Operations:
## TODO
##
## Abbreviations :
## TC : Time Complexity
## SC : Space Complexity
## FIFO : Last In First Out
####################################################

from LinkedList import LinkedList,Node

class Queue:
    def __init__(self):
        self.queueList = None
        self.head = None # deletion
        self.tail = None # insertion
        self.queueMax = 10
        self.numElements = 0

    def createQueue(self, data):
        n = len(data)
        temp = LinkedList()
        temp.push(data[0])
        self.head = temp.head
        self.tail = temp.head
        self.numElements = self.numElements + 1

        for i in xrange(1,n):
            temp.push(data[i])
            self.tail = temp.head
            self.numElements = self.numElements + 1

        self.queueList = temp
        temp = None

    def isFull(self):
        if self.numElements >= self.queueMax:
            return True

        return False

    def isEmpty(self):
        if self.head == self.tail and self.numElements == 0 :
            return True
        return False

    def enQueue(self,data):
        if self.isFull():
            print "Queue OverFlow : Queue is Full!"
            return 

        node = Node(data)
        self.head.next = node
        node.prev = self.head
        self.head = node
        self.numElements = self.numElements + 1


    def deQueue(self):
        if self.isEmpty():
            print "Queue Underflow : Queue is Empty!"
            return

        print "Dequeuing", self.tail.data,"from the Queue"
        self.queueList.pop()
        self.tail = self.queueList.head
        self.numElements = self.numElements - 1

    def display(self):
        print "Queue:"
        self.queueList.display(False)

if __name__== '__main__':
    arr = [9,16,4,1]

    q_o = Queue()
    q_o.createQueue(arr)
    q_o.enQueue(100)
    q_o.display()
    q_o.enQueue(200)
    q_o.display()
    q_o.enQueue(300)
    q_o.display()
    q_o.enQueue(400)
    q_o.display()
    q_o.enQueue(500)
    q_o.display()
    q_o.deQueue()
    q_o.display()
    q_o.deQueue()    
    q_o.display()    
