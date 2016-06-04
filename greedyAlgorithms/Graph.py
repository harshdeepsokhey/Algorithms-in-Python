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