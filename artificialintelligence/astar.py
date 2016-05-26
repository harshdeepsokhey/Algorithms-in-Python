# astar.py 


class Node:
    def __init__(self, posx,posy):
        # node id : string type ,(xy)
        self.nodeId = str(posx)+str(posy)
        # value of fcost
        self.fcost = 0
        # value of gcost
        self.gcost = 0
        # value of hcost
        self.hcost = 0
        # node id of parent
        self.parent = None

    def node2NodeId(self,posx,posy):
        return str(posx)+str(posy)

    def getNodeId(self):
        return self.nodeId

    def getNodeXY(self):
        return map(int, list(self.nodeId))

    def getFcost(self):
        return self.fcost

    def setFcost(self,fcost):
        self.Fcost = fcost

    def getGcost(self):
        return self.gcost

    def setGcost(self, gcost):
        self.gcost = gcost

    def getHcost(self):
        return self.hcost

    def setHcost(self,hcost):
        self.hcost = hcost

DIAG_DIST = 14
LINEAR_DIST = 10
class AStar:
    def __init__(self,xlim,ylim):
        # start node id
        self.start = None
        # end node id
        self.end = None
        # dimension of the arena
        self.dim = (xlim,ylim)
        # open list : for all nodes that are yet to be scanned 
        self.open = []
        # closed list: for all nodes that have been scanned
        self.closed = []

    def setStartNode(self, start):
        self.start = start

    def setEndNode(self,end):
        self.end = end

    def getStartNode(self):
        return self.start

    def getEndNode(self):
        return self.end

    def getNeighborNode(self, cnode):
        '''     
                Placing:
                 ___ ___ ___
                |_a_|_b_|_c_|
                |_h_|_X_|_d_|
                |_g_|_f_|_e_|

                Position:
                 ___________ _________ ___________
                |_(i-1,j-1)_|_(i-1,j)_|_(i-1,j+1)_|
                |__(i,j-1)__|__(i,j)__|__(i,j+1)__|
                |_(i+1,j-1)_|_(i+1,j)_|_(i+1,j+1)_|

                Cost : 
                 ____ ____ ____
                |_14_|_10_|_14_|
                |_10_|_X__|_10_|
                |_14_|_10_|_14_|

        '''
        tempNodeList = []
        tempNode = None
        nodeList = [(-1,-1),(-1,0),(-1,1),(0,1) ,(1,1),(1,0),(1,-1),(0,-1)]

        for (i,j) in nodeList:
            # TODO: check boundary conditions 
            [X,Y] = cnode.getNodeXY()

            tempNode = Node(X+i,Y+j)
            # gcost = distance from start node
            tempNode.gcost = self.getDistance(self.start,tempNode)
            #hcost = distance from end node
            tempNode.hcost = self.getDistance(self.end, tempNode)
            # fcost = gcost + hcost
            tempNode.fcost = tempNode.getGcost() + tempNode.getHcost()

            tempNodeList.append(tempNode)

        return tempNodeList


    def getDistance(self,goal,node):
        [gX,gY] = goal.getNodeXY()
        [nX,nY] = node.getNodeXY()
        dx = abs(nX - gX)
        dy = abs(nY - gY)
        D = 0
        if dx > dy:
            D = 14*dy + 10*(dx-dy)
        else:
            D = 14*dx - 10*(dy-dx)

        return D


    def compute(self):
        self.open = []
        self.close = []

        # add start node to open list
        self.open.append(self.startNode.getNodeId())

        # while open list is not empty
        while self.open:
            pass


    def display(self):
        pass



if __name__== '__main__':
    
    asr = AStar(10,10)
    startNode = Node(3,5)
    endNode = Node(5,3)

    asr.setStartNode(startNode)
    asr.setEndNode(endNode)

    asr.compute()

    asr.display()

