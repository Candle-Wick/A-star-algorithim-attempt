from math import sqrt,pow

class node():
    def __init__(self,name,x,y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.p = {}
        self.h = 0 # The heuristics number.
        self.d = 100 # should be infinity, so any arbitary high number
        self.last = [] # record of which node touched which first.

    def addp(self,node): #add to self.p another node as a key and the distence between self and the other node as the element.
        xchange = pow(self.x + node.x,2)
        ychange = pow(self.y + node.y,2)
        self.p[node] = sqrt(ychange + xchange)


def Astar(listy): #This is expecting a list of every node within the graph.
    origin = input("Name:")     #set up of the A* algorithm
    target = input("Destin:")
    for i in listy:     #finds the target and original node
        if i.name == target:
            tarnode = i
        elif i.name == origin:
            orinode = i
            orinode.d = 0
            orinode.last = [0]
    for i in listy:     #Assigns each node a heuristic distence from the target node
        xchange = pow(i.x + tarnode.x,2)
        ychange = pow(i.y + tarnode.y,2)
        i.h = sqrt(ychange + xchange)
    nodal = orinode
    queue = []
    final = []
    
    while nodal != tarnode: #The actual A* algorithm
        for i in nodal.p.keys():
            if i not in final:
                i.last.append(nodal)
                queue.append(i)
            if nodal.d + nodal.p[i] + nodal.h <= nodal.p[i]: #This accesses the connected nodes to the current node, and replaces the distence from the target node if the new distence is lower
                nodal.p[i] = nodal.d + nodal.p[i] + nodal.h

        final.append(nodal)
        nodal = queue.pop(0)
        queue.sort(key = lambda x: x.d)
        
    x = True    #Displaying the output
    truefi = []
    while x:
        try:
            truefi.insert(0,tarnode.name)
            tarnode = tarnode.last[0]
        except AttributeError:  #If the tarnode.last is not a list (when it is 0), then the original node has been found.
            x = False
    print(truefi)

'''
#The following is the code used to create a graph for testing purposes.

A = node("a",0,0)
B = node("b",4,0)
C = node("c",0,3)
D = node("d",4,3)
E = node("e",6,1)
F = node("f",5,1)

A.addp(B)
A.addp(C)
A.addp(F)

B.addp(A)
B.addp(D)

C.addp(A)
C.addp(D)

D.addp(C)
D.addp(F)
D.addp(B)
D.addp(E)

listy = [A,B,C,D,E,F]
Astar(listy)
'''
