## filename: Kruskal.py

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

from UnionFind import UnionFind

class Node:
    def __init__(self,src,dest,cost):
        self.src = src
        self.dest = dest
        self.cost = cost

class Graph:
    def __init__(self,V):
        self.graph = []
        self.adjList = []
        self.V = V
        self.E = 0

    def getPosition(self,cost):
        pos = 0
        for n in self.graph:
            if cost <= n.cost:
                return pos
            pos = pos + 1
        # place at end
        return len(self.graph)

    def getGraph(self):
        return self.graph

    def getNumEdges(self):
        return self.E

    def addEdge(self,node):
        '''
        v: from node
        w: to node
        '''
        pos = self.getPosition(node.cost)
        self.graph.insert(pos,node)
        self.E += 1
    

class Kruskal:
    def __init__(self,graph,V,E):
        self.graph = graph 
        self.V = V
        self.E = E
        self.mst = []

    def checkCycle(self, uf, edge):
        x = uf.find(edge.src)
        y = uf.find(edge.dest)
        if (x != y):
            return True

        return False 

    def compute(self):
        #subsetList = [SubSet(i,0) for i in xrange(self.V)]
        uf = UnionFind(self.V, self.E)
        for edge in self.graph:
            if self.checkCycle(uf,edge):
                self.mst.append(edge)
                uf.union(edge.src,edge.dest)

    def display(self):
        print "Kruskal's Algorithm: "
        print "     U     |     V      |    cost      |"
        print "-----------+------------+--------------+"
        for node in self.mst:
            print "    ",node.src,"    |    ",node.dest,"     |      ",node.cost,"     |"


if __name__=='__main__':
    V = 6
    g = Graph(V)
    node = Node(0,1,6)
    g.addEdge(node)
    node = Node(0,2,1)
    g.addEdge(node)
    node = Node(0,3,5)
    g.addEdge(node)
    node = Node(1,0,6)
    g.addEdge(node)
    node = Node(1,2,5)
    g.addEdge(node)
    node = Node(1,4,3)
    g.addEdge(node)
    node = Node(2,1,5)
    g.addEdge(node)
    node = Node(2,3,5)
    g.addEdge(node)
    node = Node(2,4,6)
    g.addEdge(node)
    node = Node(2,5,4)
    g.addEdge(node)
    node = Node(3,0,5)
    g.addEdge(node)
    node = Node(3,2,5)
    g.addEdge(node)
    node = Node(3,5,2)
    g.addEdge(node)
    node = Node(4,1,3)
    g.addEdge(node)
    node = Node(4,2,6)
    g.addEdge(node)
    node = Node(4,5,6)
    g.addEdge(node)
    node = Node(5,3,2)
    g.addEdge(node)
    node = Node(5,2,4)
    g.addEdge(node)
    node = Node(5,4,6)
    g.addEdge(node)

    Gr = g.getGraph()
    E = g.getNumEdges()

    k = Kruskal(Gr,V,E)
    k.compute()
    k.display()
