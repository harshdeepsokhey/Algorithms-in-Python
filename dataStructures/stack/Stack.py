## filename: Stack.py

## dataStructures
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## Implements Stack in Python
##
## Operations:
## push into the stack
## pop from the stack
## get TOP of the stack
## Check if stack is EMPTY
## Check if stack is FULL
## postFix of an expression
## preFix of an expression
## Infix of an expression
##
## Abbreviations :
## TC : Time Complexity
## SC : Space Complexity
## LIFO : Last In First Out
####################################################
from LinkedList import LinkedList,Node

class Stack:
    def __init__(self):
        self.top = None
        self.stackList = None
        self.stackMAX = 10
        self.numElements = 0

    def createStack(self, dataList, stackMax):
        '''
            createStack(dataList)
            Creates a stack with elements 
            from the dataList (index starts at 0)
            TC :
            SC :
        '''
        n = len(dataList)
        tempList = LinkedList()
        for i in xrange(n):
            if i >= stackMax:
                print "Stack MAX Limit reached!"
                break
            tempList.push(dataList[i])
            self.numElements += 1

        self.stackList = tempList
        self.top = tempList.head

    def push(self, data):
        '''
            push()
            Pushes elements on to the stack (LIFO)
            TC :
            SC :
        '''
        if (self.top is None) and (self.stackList is None) :
            print "No Stack Exist!"
            return

        if self.isFull():
            print "Stack Overflow: Cannot add (",data,"), Stack is FULL! "
            return

        node = Node(data)
        node.next = self.stackList.head
        self.stackList.head = node
        node.prev = None
        self.top = node
        self.numElements += 1
        print "Adding ", self.top.data


    def pop(self):
        '''
            pop()
            Pop elements on to the stack (LIFO)
            TC :
            SC :
        '''
        if (self.top is None) and (self.stackList is None) :
            print "No Stack Exist!"
            return

        if self.isEmpty():
            print "Stack Underflow: Stack is EMPTY!"
            return

        temp = self.top
        print "Deleting ",temp.data
        self.stackList.head = temp.next
        self.top = temp.next
        temp.next = None
        self.numElements -= 1

    def getTop(self):
        return self.top

    def isEmpty(self):
        if self.numElements is 0:
            return True
        return False

    def isFull(self):
        if self.numElements >= self.stackMAX:
            return True
        return False

    def getPostFix(self):
        pass

    def getPreFix(self):
        pass

    def display(self):
        temp = self.stackList.head

        while(temp):
            print temp.data,"->",
            temp = temp.next
        print "Null"


if __name__ == '__main__':
    arr = [15,6,2,9,17,3]
    o_stack = Stack()
    o_stack.createStack(arr,10)
    o_stack.display()
    o_stack.push(10)
    o_stack.push(20)
    o_stack.push(30)
    o_stack.push(40)
    o_stack.push(50)
    o_stack.display()
    for i in xrange(10):
        o_stack.pop()
        o_stack.display()
    o_stack.pop()
    o_stack.push(60)
    o_stack.display()


