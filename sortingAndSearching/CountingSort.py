## filename: CountingSort.py

## sortingAndSearching
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## TODO

####################################################

class CountingSort:
    def __init__(self, dataList, maxElem):
            self.unsortedList = arr
            self.maxElement = maxElem
            self.length = len(self.unsortedList)
            self.sortedList = [0]*self.length

    def sort(self):
        k=self.maxElement
        auxArr = [0]*(k+1)

        for j in xrange(self.length):
            auxArr[self.unsortedList[j]] = auxArr[self.unsortedList[j]] +1

        for i in xrange(k+1):
            auxArr[i] = auxArr[i] + auxArr[i-1]
        i=0
        for i in xrange(k+1):
            auxArr[i] = auxArr[i] -1
        
        j=0
        for j in reversed(self.unsortedList):
            self.sortedList[auxArr[j]-1] = j
            auxArr[j] = auxArr[j] -1
    
    def display(self):
        print "UnSorted:"
        print self.unsortedList
        print "Sorted :"
        print self.sortedList

if __name__ == '__main__':
    arr = [2,5,3,0,2,3,0,3]
    csort = CountingSort(arr,max(arr))
    csort.sort()
    csort.display()



