## filename: QuickSort.py

## sortingAndSearching
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## TODO
##
## TC : Best Case => O(n *log(n))  , Worst Case=> O(n^2)
## SC :
####################################################

class QuickSort:
    def __init__(self, arr):
        self.unsortedList = arr

    def sort(self, p, r):
        if p < r:
            q = self.partition(p,r)
            self.sort(p,q-1)
            self.sort(q+1,r)

    def swap(self,i,j):
        temp = self.unsortedList[i]
        self.unsortedList[i] = self.unsortedList[j]
        self.unsortedList[j] = temp

    def partition(self, p, r ):
        x = self.unsortedList[r]
        i = p-1
        for j in xrange(p,r):
            if self.unsortedList[j] <= x:
                i = i + 1
                self.swap(i,j)
        self.swap(i+1,r)
        return (i+1)

    def display(self):
        print "Sorted List:"
        print self.unsortedList

if __name__=='__main__':
    arr = [2,8,7,1,3,5,6,4]
    qsort = QuickSort(arr)
    qsort.sort(0,len(arr)-1)
    qsort.display()
