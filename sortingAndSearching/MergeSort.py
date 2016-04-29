## filename: MergeSort.py

## sortingAndSearching
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms - CLRS
## Fundamentals of Computer Algorithms-Horowitz, Sahani, Rajasekaran

## Description :
## TODO

####################################################
import math

class MergeSort:
    def __init__(self,data):
        self.dataList = data
        self.auxList = [0]*len(data)

    def sort(self,low,high):
        if ( low < high):
            mid = int(math.floor((low + high) /2))
            self.sort(low,mid)
            self.sort(mid+1, high)
            self.merge(low,mid,high)

    def merge(self, low, mid, high):
        h = low
        i = low
        j = mid+1
        
        while ((h <= mid) and (j <= high)):
            if self.dataList[h] <= self.dataList[j]:
                self.auxList[i] = self.dataList[h]
                h = h+1
            else:
                self.auxList[i] = self.dataList[j]
                j = j+1
            i = i+1

        if h > mid:
            k =0
            for k in xrange(j,high+1):
                self.auxList[i] = self.dataList[k]
                i = i+1
        else:
            k=0
            for k in xrange(h,mid+1):
                self.auxList[i] = self.dataList[k]
                i = i+1
        k = 0
        for k in xrange(low, high+1):
            self.dataList[k] = self.auxList[k]

    def display(self):
        print "SortedList:"
        print self.dataList


if __name__ == '__main__':
    arr = [310,285,179,652,351,423,861,254,450,520]
    msort = MergeSort(arr)
    print "UnSortedList:"
    print arr
    msort.sort(0,len(arr)-1)
    msort.display()
