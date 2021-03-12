#from shapes.Block import Block
#from shapes.Cylinder import Cylinder

import numpy as np
"""
def eqNameNumber(num_eq):
        eqName = []
        for i in range(num_eq):
            global ""
            name = "eq" + str(i+1)
            eqName.append(name)
        return eqName

eqName = eqNameNumber(3)
print(eqName)
"""
"""
#Test run model - fungerer
num_eq = 3
eq_size_list = [70,150,1000]
eq_pos = [[50,150,0],[150,1000,1000], [2000,1000,2000]]
env_size = 3000

def run_model(num_eq, eq_size_list, eq_pos, env_size):
    for i in range(num_eq):
            eq = Block(eq_pos[i][0], eq_pos[i][1], eq_pos[i][2], eq_size_list[i], eq_size_list[i], eq_size_list[i],"RED", "Steel") # color and material could be extended
            eq.initForNX()
            if i==0:
                midpoint = Cylinder(85,150,35, 10, 10,[0,1,0], "Red", "Steel")
                midpoint.initForNX()
                eq.subtract(midpoint)
    
    env = Block(0,0,0,env_size, env_size, env_size, "RED", "Steel")
    env.initForNX()

run_model(num_eq, eq_size_list, eq_pos, env_size)
"""
"""
test = np.array([1,2,3])
test += [1,1,1]
print(test)
# this function need testing
eqInOutWorldPoint(self, side, eq_size, eq_pos)
"""
#test node2point
def node2point(node): #usikker på om dette er riktig
    env_size = 1000
    num_nodes = 100
    ratio = env_size/num_nodes
    nodeInPoint = [node[0]/ratio, node[1]/ratio, node[2]/ratio]
    return nodeInPoint

node = (1,1,1)
point = node2point(node)
print("node ", str(node), " til pkt: ", point)