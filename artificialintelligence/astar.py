## A* Search Algorithm ##

class Node:
    def __init__(self):
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.parent = None

    def getNodeInfo(self):
        return [self.g, self.h,self.f, self.parent]
    
    def setNodeInfo(self,gcost=0, hcost=0,parent=None):
        self.g = gcost
        self.h = hcost
        self.parent = parent
        
class AStar:
    def __init__(self):
        self.path = None
        self.visted = None
        self.notVisited = None
        
    def compute(self):
        pass
     
if __name__=="__main__":
    pass