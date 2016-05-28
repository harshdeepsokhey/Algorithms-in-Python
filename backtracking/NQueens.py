## filename: NQueens.py

## Backtracking
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## 
## 
####################################################

import numpy as np

class NQueens:
    def __init__(self,N):
        self.N = N
        self.result =  np.zeros((self.N, self.N),dtype=np.int)

    def compute(self,qc):

        if (qc >= self.N):
            return True
        
        for qr in xrange(self.N):
            if self.validate(qr,qc):
                self.result[qr][qc] = 1

                if self.compute(qc+1):
                    return True

            self.result[qr][qc] = 0

        return False


    def validate(self,qrow,qcol):
        
        # check forward/backward Diagonal 
        delta = (qcol - qrow)
        y = np.sum(np.diagonal(self.result,delta))
        
        delta1 = ((qcol+1)%self.N - qrow)

        yflip = np.sum(np.diagonal(np.fliplr(self.result), delta1))

        if (y >= 1 or yflip >= 1) and ((np.size(y) != 0) or (np.size(yflip) != 0)):
            return False 

        #check row
        y = np.sum(self.result[qrow,:])
        if y >= 1:
            return False
        
        return True

    def display(self):
        print "-----------------"
        print "N Queens Problem"
        print "-----------------"
        print "Solution: N = ",self.N
        for i in xrange(self.N):
            for j in xrange(self.N):
                if self.result[i][j] == 1:
                    print "Q",
                else:
                    print ".",
            print ""


if __name__=="__main__":
    N = 4
    nq = NQueens(N)
    if not nq.compute(0):
        print "No Solution exists!"
    else:
        nq.display()