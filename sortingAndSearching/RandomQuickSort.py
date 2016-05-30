## filename: RandomQSort.py

## sortingAndSearching
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## TODO
##
## TC :
## SC :
####################################################

from random import randint

class RandomQuickSort:
    def __init__(self,arr):
        self.dataList = arr

    def swap(self,i,j):
        temp = self.dataList[i]
        self.dataList[i] = self.dataList[j]
        self.dataList[j] = temp

    def partition(self,p,r):
        x = self.dataList[r]
        i = p-1
        for j in xrange(p,r):
            if self.dataList[j] <= x:
                i = i + 1
                self.swap(i,j)
        self.swap(i+1,r)
        return (i+1)

    def random_partition(self,p,r):
        i = randint(p,r)
        self.swap(r,i)
        return self.partition(p,r)

    def random_quick_sort(self,p,r):
        if p<r:
            q = self.random_partition(p,r)
            self.random_quick_sort(p,q-1)
            self.random_quick_sort(q+1,r)

    def display(self):
        print "Random Quick Sort:"
        print "Sorted Array : ",self.dataList

if __name__=='__main__':
    arr = [2,8,7,1,3,5,6,4]
    rqsort = RandomQuickSort(arr)
    rqsort.random_quick_sort(0,len(arr)-1)
    rqsort.display()