## filename: MinCostPath.py

## Dynamic Programming
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## 
##
## Time Complexity : 
## Space Complexity :
####################################################

import numpy as np

class MinCostPath:
    def __init__(self,cost,m,n):
        self.cost = cost
        self.rows = m
        self.cols = n
        self.mcp = 0

    def compute(self):
        auxArr = np.zeros((self.rows, self.cols),dtype=np.int)

        auxArr[0][0] = self.cost[0][0]

        for j in xrange(1,self.cols):
            auxArr[0][j] = self.cost[0][j] + auxArr[0][j-1]

        i =0
        j =0
        for i in xrange(1,self.rows):
            auxArr[i][0] = self.cost[i][0] + auxArr[i-1][0]
            for j in xrange(1,self.cols):
                auxArr[i][j] = self.cost[i][j] + min([auxArr[i-1][j],auxArr[i][j-1],auxArr[i-1][j-1]])
        
        self.mcp = auxArr[self.rows - 1][self.cols - 1]

    def display(self):
        print "Minimum Cost Path = ",self.mcp

if __name__=='__main__':
    m = 3
    n = 3
    cost = np.array([[1,2,3 ], [4,8,2], [1,5,3]])

    mcp = MinCostPath(cost,m,n)
    mcp.compute()
    mcp.display()