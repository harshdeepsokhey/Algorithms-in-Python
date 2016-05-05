## filename: ActivitySelection.py

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
## Suppose we have a set S = {A1 .. An} of 'n' proposed activities,
## that wish to use a resource which can serve only one activity at a time. 
## Each activity 'Ai' has a start time 'Si' and a finish time 'Fi' where 0<=Si < Fi < inf.
## Select the maximum-size subset of mutually compatible activities. 
## 
## Assume: Activities are sorted in monotonically increasing order of finish time.
## 
####################################################

START_TIME = 0
FINISH_TIME = 1                    

class ActivitySelection:

    def __init__(self,activity):
        self.activity = activity
        self.length = len(activity)
        self.finalAct = {}
        
    def maxSubset(self):
        currentAct = self.activity[0]
        self.finalAct["1"] = self.activity[0]
        count = 1
        for nextAct in self.activity[1:]:
            count +=1
            if nextAct[START_TIME] >= currentAct[FINISH_TIME]:
                self.finalAct[str(count)] = nextAct
                currentAct = nextAct
    def display(self):
        print "Maximun Size Subset of Activities:"
        for key in self.finalAct.keys():
            print "Act#",key,":",self.finalAct[key]
if __name__ == "__main__":
    # Assume: All finish times are sorted. 
    # [s,f] : s = start time, f = finish time , index = activity number (act#1 is index 0)
    activity = [[1,4],[3,5],[0,6],[5,7],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]

    actSelect = ActivitySelection(activity)
    actSelect.maxSubset()
    actSelect.display()