## filename: RadixSort.py

## sortingAndSearching
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS
## Fundamentals of Computer Algorithms-Horowitz, Sahani, Rajasekaran

## Description :
## TODO

####################################################

class CountingSort:
    '''
        Using a stable sorting mechanism for sorting the elements digit wise. 
    '''
    def __init__(self, dataList):
        self.unsortedList = dataList
        self.length = len(self.unsortedList)

    def getDigit(self,number, sortingDigit):
        x = 0
        count = 1
        while count <= sortingDigit:
            x = number %10
            number = number // 10
            count += 1
        return x

    def sort(self, sortingDigit):
        '''
            This version of the Counting Sort is different
            from the original version as it sorts the elements
            based on the digits. 

            returns : digit-wise sorted list 
        '''
        sortedList= [0]* self.length
        k=10
        auxArr = [0]*(10)

        for j in xrange(self.length):
            x = self.getDigit(self.unsortedList[j],sortingDigit)
            auxArr[x] = auxArr[x] +1

        for i in xrange(k-1):
            auxArr[i+1] = auxArr[i+1] + auxArr[i]

        for j in reversed(self.unsortedList):
            y = self.getDigit(j, sortingDigit)
            sortedList[auxArr[y]-1] = j
            #print y,j, sortedList
            auxArr[y] = auxArr[y] -1          

        return sortedList


class RadixSort:
    def __init__(self, dataList):
            self.unsortedList = dataList
            self.sortedList = [0]*len(dataList)
    
    def sort(self):
        '''
        Algo:
        1. extract the maximum number of digits
        2. use a stable sort mechanism to sort 
        them based on the digits

        Example:
        We first sort the numbers based on the zero's place, 
        then one's place, then hundredth's place and so on. 
        '''
        d = len(str(abs(max(self.unsortedList))))
        usort = self.unsortedList
        for i in xrange(1,d+1):
            r_csort = CountingSort(usort)
            self.sortedList = r_csort.sort(i)
            usort = self.sortedList
            r_csort = None

    def display(self):
        print "Unsorted List:"
        print self.unsortedList
        print "Sorted List:"
        print self.sortedList

if __name__ == '__main__':
    arr = [329,457,657,839,436,720,355]
    rsort = RadixSort(arr)
    rsort.sort()
    rsort.display()

