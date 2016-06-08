# Helper Class for Graphs #
###########################
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


class Node:
    def __init__(self,src,dest,cost):
        self.src = src
        self.dest = dest
        self.cost = cost


class WeightedGraph:
    def __init__(self,V):
        self.graph = []
        self.adjList = []
        self.neighbours = [ [] for i in xrange(V)]
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

    def getNeighbours(self,n):
        return self.neighbours[n]

    def addEdge(self,node):
        '''
        v: from node
        w: to node
        '''
        pos = self.getPosition(node.cost)
        self.graph.insert(pos,node)
        self.neighbours[node.src].append(node.dest)
        self.E += 1

