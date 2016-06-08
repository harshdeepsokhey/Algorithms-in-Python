## filename: Dijkstra.py

## Artificial Intelligence
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

class Dijkstra:
    def __init__(self,wGraph, E, V):
        self.E = E
        self.V = V
        self.graph = wGraph

    def shortestPath(self):
        pass

    def display(self):
        pass
        
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
    node = Node(2,3,5)
    wg.addEdge(node)
    node = Node(3,5,2)
    wg.addEdge(node)
    node = Node(4,3,3)
    wg.addEdge(node)
    node = Node(4,5,2)
    wg.addEdge(node)

    wgr = wg.getGraph()
    E = wg.getNumEdges()
    
    for i in xrange(6):
        print wg.getNeighbours(i)

    dsp = Dijkstra(wgr,E,V)
    dsp.shortestPath()
    dsp.display()