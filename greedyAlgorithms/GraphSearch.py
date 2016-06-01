## filename: GraphSearch.py

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
## 
## 
## Avergae Homology Score : TODO
## 
####################################################

class Graph:
    def __init__(self):
        self.graph = []

    def addEdge(self,node,edgeList):
        '''
        v: from node
        w: to node
        '''
        self.graph.insert(node,edgeList)

    def getList(self):
        return self.graph


class GraphSearch:
    def __init__(self, adjList, numVertices):
        self.adjList = adjList
        self.vertices = numVertices
        self.visited = []

    def breadthFirstSearch(self,start): 
        # add start node to the queue
        queue = [start]

        while queue:
            # dequeue
            currNode = queue.pop(0)

            if currNode not in self.visited:
                self.visited.append(currNode)
                for edge in self.adjList[currNode]:
                    queue.append(edge)
    
    def depthFirstSearch(self,start):
        pass

    def display(self,dfs=True):
        if dfs:
            print "Depth First Search:"
        else:
            print "Breadth First Search:"

        print self.visited

if __name__=='__main__':
    
    g = Graph()
    g.addEdge(0, [1,2,3,4]);
    g.addEdge(1, [0,3,4]);
    g.addEdge(2, [0,5,6]);
    g.addEdge(3, [0,1,4]);
    g.addEdge(4, [0,1,3]);
    g.addEdge(5, [2,6]);
    g.addEdge(6, [2,5]);
   
    adjList = g.getList()
    numVertices = 7

    dfs = GraphSearch(adjList,numVertices)
    dfs.depthFirstSearch(0)
    dfs.display()

    bfs = GraphSearch(adjList,numVertices)
    bfs.breadthFirstSearch(0)
    bfs.display(False)


