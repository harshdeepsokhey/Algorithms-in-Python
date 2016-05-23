## filename: MaxScore.py

## GreedyAlgorithms
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS
## Fundamentals of Computer Algorithms-Horowitz, Sahani, Rajasekaran

## Topic Description :
## Greedy Algos:
## At each step,make an optimal(best) choice at that instant,
## so that we get the optimal solution for the complete problems
##  
## Problem Description
## Maximize the average homology score for all pairs in the set.
## 
## Avergae Homology Score : TODO
## 
####################################################

class MaxScore:
    def __init__(self,dataList):
        self.dataList = dataList
        self.maxScore = 0.0
        self.freqMat = {"AA":0,"CC":0,"GG":0,"TT":0,"AC":0, "AG":0,"AT":0,"CG":0,"CT":0,"GT":0}
        self.F =[0.0]*10
        self.bestAvg = 0.0
        
    def buildFreqMat(self):
        
        n = len(self.dataList)
        count = 0
        seqLen = len(self.dataList[0])
        for i in xrange(n-1):
            for j in xrange(i+1,n):
                #print i,j,self.dataList[i],self.dataList[j], len(self.dataList[i])
                y =[]
                for k in xrange(seqLen):
                    y.append(str(self.dataList[i][k]+self.dataList[j][k]))
                for x in y:
                    if x not in self.freqMat.keys():
                        x = x[::-1]
                    self.freqMat[x] += 1
        count = 0
        for k in ["AA","GG","CC","TT"]:
            self.F[count] = self.freqMat[k]
            count = count+1
       
        for k in ["AC","AG","AT","CG","CT","GT"]:
            self.F[count] = self.freqMat[k]
            count = count+1
            
        #self.F[4:] = sorted(self.F[4:])
        
                
    def maxAvg(self):
        self.buildFreqMat()
        n = len(self.dataList)
        comb = int(n*(n-1)/2)
        F = self.F
        #print F
        #print self.freqMat
        best = -32767
        S = [0]*10
        for a in xrange(1,11):
            for b in xrange(1,11):
                for c in xrange(1,11):
                    for d in xrange(1,11):
                        S[0] = a
                        S[1] = b
                        S[2] = c
                        S[3] = d
                        if ((a+b+c+d)%2 == 0):
                            S[4] = S[5] = 10
                            S[6] = 10 - (a+b+c+d)
                            S [7] = S [8] = S [9] = -10
                            score = (S[7]*F[7] + S[8]*F[8] + S[9]*F[9] + S[6]*F[6] + S[4]*F[4]+ S[5]*F[5] + a*F[0] + b*F[1]+ c*F[2]+ d*F[3])/comb
                            #print score
                            best = max(best, score)
        self.bestAvg = (best)

    def display(self):
        print "Max Score:",self.bestAvg
        
if __name__=='__main__':
    #arr = ["ACTAGAGAC", "AAAAAAAAA", "TAGTCATAC", "GCAGCATTC"]
    arr = ["AAA","AAA","AAC"]
    #arr = ["ACTGACTGACTG","GACTTGACCTGA"]
    mscore = MaxScore(arr)
    mscore.maxAvg()
    mscore.display()    
