## filename: HeapSort.py

## sortingAndSearching
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## TODO

####################################################

import math

class HeapSort:
    def __init__(self, dataList):
        self.heap = dataList
        self.length = len(dataList)-1
        self.heapSize = 0
        self.sortedList = [0]*self.length

    def parent(self,key):
        return int(math.floor(key/2))

    def left_child(self,key):
        return (2*key)

    def right_child(self,key):
        return ((2*key) + 1)

    def heapify(self,pos,isMax=True):
        l = self.left_child(pos)
        r = self.right_child(pos)

        largest = 0

        if l <= self.heapSize and self.heap[l] > self.heap[pos]:
            largest = l
        else:
            largest = pos
        
        if r <= self.heapSize and self.heap[r] > self.heap[largest]:
            largest = r

        if largest is not pos:
            temp = self.heap[pos]
            self.heap[pos] = self.heap[largest]
            self.heap[largest] = temp
            
            self.heapify(largest)

    def build_heap(self,isMax=True):
        self.heapSize = self.length
        mid = int(math.floor((self.length)/2))
        #print mid
        for i in xrange(mid,0,-1):
            self.heapify(i)
        
    def sort(self):
        self.build_heap()
        for i in xrange(self.length,1,-1):
            temp = self.heap[1]
            self.heap[1] = self.heap[i]
            self.heap[i] = temp
            self.heapSize = self.heapSize -1
            self.heapify(1)


    def display(self):
        print "SortedList:"
        print self.heap[1:]

if __name__ == '__main__':
    # assume arr[0] is the root 
    arr = [-1,4,1,3,2,16,9,10,14,8,7]
    hsort = HeapSort(arr)
    print "UnsortedList:"
    print arr[1:]
    hsort.sort()
    hsort.display()
