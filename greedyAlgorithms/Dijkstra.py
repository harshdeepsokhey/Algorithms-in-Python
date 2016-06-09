## filename: Dijkstra.py

## Greedy Algorithms
## CS6101: Design and Analysis of Algorithms

## Reference : 
## http://www.geeksforgeeks.org
## http://topcoder.com 
## Introduction to Algorithms, CLRS

## Description :
## Single Source Shortest Path Problem
##
## Given a weighted graph G, find the shortest path from a 
## source vertex (s) to a destination vertex (v)
## 
## Assumption :
## - All edges have non-negative weights
## - Graph must be connected
###################################################

from Graph import WeightedGraph,Node

MAX_INT16 = 32767

class Dijkstra:
    def __init__(self,wGraph,neighbours, E, V,src, dest):
        self.E = E
        self.V = V
        self.graph = wGraph
        self.neighbours = neighbours
        self.path = [-1]*self.V
        self.dist = 0
        self.src = src
        self.dest = dest

    def minDist(self,dist,visited):
        m = MAX_INT16
        for v in xrange(self.V):
            if (dist[v] <= m) and (v not in visited):
                m = dist[v]
                index = v

        return index


    def getEdge(self,u,v):
        for e in self.graph:
            if e.src == u and e.dest == v:
                return e

    def shortestPath(self):
        global MAX_INT16
        # initialize 
        dist = [MAX_INT16]*self.V
        dist[self.src] = 0

        visited = []
        q = range(self.V)

        while q:
            x = q.pop(0)
            u = self.minDist(dist,visited)
            visited.append(u)

            for v in self.neighbours[u]:
                e = self.getEdge(u,v)
                w = e.cost
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    self.path[u+1] = v

        self.dist = dist

    def display(self):
        print "Shortest Distance :",self.dist[self.dest]
        print "Shortest Path:"
        print self.src,
        for i in self.path:
            if i != -1:
                print "-->",
                print i,
        
if __name__=='__main__':
    V = 6
    wg = WeightedGraph(V)
    node = Node(0,1,2)
    wg.addEdge(node)
    node = Node(0,2,4)
    wg.addEdge(node)
    node = Node(1,2,1)
    wg.addEdge(node)
    node = Node(1,3,4)
    wg.addEdge(node)
    node = Node(1,4,2)
    wg.addEdge(node)
    node = Node(2,4,3)
    wg.addEdge(node)
    node = Node(3,5,2)
    wg.addEdge(node)
    node = Node(4,3,3)
    wg.addEdge(node)
    node = Node(4,5,2)
    wg.addEdge(node)

    wgr = wg.getGraph()
    E = wg.getNumEdges()
    n = wg.getNeighbours(-1)

    src = 0
    dest = 5
    
    dsp = Dijkstra(wgr,n,E,V,src,dest)
    dsp.shortestPath()
    dsp.display()