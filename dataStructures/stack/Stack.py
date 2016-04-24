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

class Stack:
    def __init__(self):
        self.top = None

    def createStack(self, dataList):
        '''
            createStack(dataList)
            Creates a stack with elements 
            from the dataList (index starts at 0)
            TC :
            SC :
        '''
        pass

    def push(self):
        '''
            push()
            Pushes elements on to the stack (LIFO)
            TC :
            SC :
        '''
        pass

    def pop(self):
        '''
            pop()
            Pop elements on to the stack (LIFO)
            TC :
            SC :
        '''
        pass

    def getTop(self):
        return self.top

    def isEmpty(self):
        pass

    def isFull(self):
        pass

    def getPostFix(self):
        pass

    def getPreFix(self):
        pass

    def display(self):
        pass


if __name__ == '__main__':
    arr = [15,6,2,9,17,3]
    o_stack = Stack()
    o_stack.createStack(arr)


