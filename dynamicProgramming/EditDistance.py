## filename: EditDistance.py

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

class EditDistance:
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
        self.len1 = len(str1)
        self.len2 = len(str2)
        self.distance = 0
        self.trace = ["","",""]

    def trackChange(self,auxArr):
        i = self.len1
        j = self.len2

        while(i > 0 or j > 0):
            if (i > 0 and j > 0):
                d = auxArr[i-1][j-1]
                ch = '|'
                if self.str1[i-1] != self.str2[j-1]:
                    d = d+1
                    ch = ' '

                if (auxArr[i][j] == d):
                    self.trace[0] += self.str1[i-1]
                    self.trace[1] += ch
                    self.trace[2] += self.str2[j-1]
                    i = i-1
                    j = j-1
                elif (auxArr[i][j] == auxArr[i-1][j]+1):
                    self.trace[0]+= self.str1[i-1]
                    self.trace[1]+= " "
                    self.trace[2]+= "-"
                    i = i-1
                else :
                    self.trace[0]+= "-"
                    self.trace[1]+= " "
                    self.trace[2]+= self.str2[j-1]
                    j = j-1
            elif (i>0):
                self.trace[0]+= self.str1[i-1]
                self.trace[1]+= " "
                self.trace[2]+= "-"
                i = i-1
            elif (j>0):
                self.trace[0]+= "-"
                self.trace[1]+= " "
                self.trace[2]+= self.str1[j-1]
                j = j-1


    def compute(self):
        auxArr = np.zeros((self.len1+1,self.len2+1),dtype=np.int)
        for j in xrange(1,self.len2+1):
            auxArr[0][j] = j        
        i=0
        j=0
        for i in xrange(1,self.len1+1):
            auxArr[i][0] = i
            for j in xrange(1,self.len2+1):
                d = auxArr[i-1][j-1] # diagnol elements

                #last character is not same
                if self.str1[i-1] != self.str2[j-1]:
                    d = d+1

                auxArr[i][j] = min([d, auxArr[i-1][j]+1, auxArr[i][j-1]+1])

        self.trackChange(auxArr)
        self.distance = auxArr[self.len1][self.len2]

    def display(self):
        print "Trace:\n"
        print self.trace[0][::-1]
        print self.trace[1][::-1]
        print self.trace[2][::-1]
        print "\nedit distance =",self.distance

if __name__=='__main__':
    str1 = "sunday"
    str2 = "saturday"
    ed = EditDistance(str1,str2)
    ed.compute()
    ed.display()
