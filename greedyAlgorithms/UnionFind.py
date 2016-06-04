## filename: UnionFind.py

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS
## Fundamentals of Computer Algorithms-Horowitz, Sahani, Rajasekaran

####################################################

# TODO: Update find and union for ranks 
class SubSet:
    def __init__(self, parent, cost):
        self.parent = parent
        self.cost = cost

class UnionFind:
    def __init__(self,V,E):
        self.V = V  # vertices 
        self.E = E  # edges
        self.parent = [-1]*self.V # initializw all vertices with -1

    def find(self,index):
        if self.parent[index] == -1:
            return index

        return self.find(self.parent[index])
        
    def union(self,x,y):
        set_X = self.find(x)
        set_Y = self.find(y)
        self.parent[set_X] = set_Y
        