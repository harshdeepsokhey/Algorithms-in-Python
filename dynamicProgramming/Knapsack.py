## filename: Knapsack.py

## Dynamic Programming
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## Given weights and values of 'N' items, a Sack with maximum capacity of 'W'
## has to be filled such that the sum of values of the items in the sack is maximum.  
## 
## Time Complexity : O(N*W) 
## Space Complexity :
####################################################

import numpy as np

class Knapsack:
    def __init__(self,w,v,c):
        self.weight = w
        self.value = v
        self.capacity = c
        self.numItems = len(w)
        self.result = []

    def compute(self):
        auxArr = np.ones((self.numItems+1,self.capacity+1),dtype=np.int)
        auxArr = auxArr*(-32767)
        for w in xrange(self.capacity+1):
            auxArr[0][w] = 0

        for i in xrange(1,self.numItems+1):
            for w in xrange(self.capacity+1):
                if self.weight[i-1] <= w:
                    auxArr[i][w] = max([self.value[i-1]+ auxArr[i-1][w-self.weight[i-1]], auxArr[i-1][w]])
                else:
                    auxArr[i][w] = auxArr[i-1][w]

        self.result = auxArr[self.numItems][self.capacity]

    def display(self):
        print "Maximum Value =",self.result


if __name__=="__main__":
    v = [10,40,30,50]
    w = [5,4,6,3]
    c = 10
    ks = Knapsack(w,v,c)
    ks.compute()
    ks.display()
    