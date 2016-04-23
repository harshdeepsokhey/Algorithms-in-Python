## filename: bucketSort.py

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
from InsertionSort import InsertionSort

class BucketSort:
    def __init__(self, arrLList, length):
        self.unsortedList = arrLList
        self.length = length
        self.sortedList = []

    def sort(self):

        n = self.length
        ref2List = self.unsortedList.head	## reference to linkedList.head 
        temp = [LinkedList() for i in xrange(n)]

        i = 0 
        for i in xrange(n):
        	## valid intergral index
        	tempIdx = (int(math.floor(ref2List.data *n)) % n)
        	temp[tempIdx].push(ref2List.data)
        	ref2List = ref2List.next
      	
		i=0
        for i in xrange(n):
        	isort = InsertionSort(temp[i])
        	isort.sort()

        i=0
        sortedList = []
        for i in xrange(n):
        	count = temp[i].head
        	while  count is not None:
        		sortedList.append(count.data)
        		count = count.next
        sortedList.reverse()
        self.sortedList = LinkedList().createList(sortedList)
                	
        ## free 
        ref2List = None
        temp = []
        sortedList = []

    def display(self):
        print "Unsorted list "
        self.unsortedList.display()	# since its a linkedList
        print "Sorted List :"
        print self.sortedList.display()

if __name__ == '__main__':
	arr = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
	llist = LinkedList()
	arrLList = llist.createList(arr)
	bs = BucketSort(arrLList, len(arr))
	bs.sort()
	bs.display()

