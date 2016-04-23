## filename: InsertionSort.py

## sortingAndSearching
## CS6101: Design of Analysis aand Algorothms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## TODO

####################################################
import math
from LinkedList import LinkedList

class InsertionSort:
    def __init__(self, dataList):
        self.unsortedList = dataList

    def sort(self):
        ref2List = self.unsortedList.head   # element 0
        while (ref2List):
            key = ref2List.next                 # element 1
            while((ref2List is not None ) and (key is not None)and (ref2List.data > key.data)):
                self.unsortedList.insertNode(ref2List,key)
                ref2List = ref2List.prev.prev

            if key is None or key.next is None:
                break
            else:
                key = key.next
            ref2List = key.prev


    def display(self, msg):
        print msg
        self.unsortedList.display()

if __name__ == '__main__':
    arr = [3,1,6,4,2,5]
    llist = LinkedList()
    arrList = llist.createList(arr)
    isort = InsertionSort(arrList)
    isort.display("UnsortedList: ")
    isort.sort()
    isort.display("SortedList: ")
    
    
