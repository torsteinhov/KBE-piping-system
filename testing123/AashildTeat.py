#from shapes.Block import Block
#from shapes.Cylinder import Cylinder
#from checkData import checkCustommerInput
import sys

sys.path.append('C:\\Users\\Hilde\\anaconda3\\envs\\tdt4265\\lib\\site-packages')
#import numpy as np

"""
import NXOpen
import numpy as np
if __name__ == "__main__":
    theSession = NXOpen.Session.GetSession()
    theUI = NXOpen.UI.GetUI()
    theLw = theSession.ListingWindow
    theLw.Open()
    #theLw.WriteLine(sys.version)
    theLw.WriteLine("The numpy version is: {}".format(np.version.version))
"""
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
"""
"""
for i in range(2):
    print("Hei123")
# cubes for testing
num_eq = 3
eq_size_list = [[70,70,70],[150,150,150],[1000,1000,1000]]
eq_pos = [[50,150,0],[150,1000,1000], [2000,1000,2000]]
env_size = [3000, 3000, 3000]
eq_in_out = [[40,0,40], [70,40,40],[100,0,100],[150,100,100],[500,0,500],[1000,500,500]]
startPoint = [0,1500,1500]
endPoint = [3000, 1500,1500]
pipeDia =  50.8

#feilmelding =checkCustommerInput(3, eq_size_list,eq_pos, eq_in_out, env_size, startPoint, endPoint, 10, 2)
#print(feilmelding)
#custommer = drawGivenInfo(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, pipeDia)
#custommer.run_model()
"""
"""
vek = [1,2,3]
midpoint = [vek[0], vek[1], vek[2]]
print(midpoint)

midpoint = [vek[0]+1,vek[1]+1,vek[2]+1]
print(midpoint)

#drawGivenInfo
 mP =[eq_pos[0],eq_pos[1],eq_pos[2]]

        # finding what side the mid point is on and calculating it in global points
        if(x == 0 and y<eq_size and y>0 and z<eq_size and z>0 ):
            midPoint = [mP[0]+0, mP[1]+eq_size/2, mP[2]+eq_size/2]
            dirInEq = [1,0,0]
        elif (x == eq_size and y<eq_size and y>0 and z<eq_size and z>0):
            midPoint = [mP[0]+eq_size, mP[1]+eq_size/2, mP[2]+eq_size/2]
            dirInEq = [-1,0,0]
        elif (x <eq_size and x>0 and y==0 and z<eq_size and z>0):
            midPoint = [mP[0]+eq_size/2, mP[1]+0, mP[2]+eq_size/2]
            dirInEq = [0,1,0]
        elif (x <eq_size and x>0 and y==eq_size and z<eq_size and z>0):
            midPoint = [mP[0]+eq_size/2, mP[1]+eq_size, mP[2]+eq_size/2]
            dirInEq = [0,-1,0]
        elif (x <eq_size and x>0 and y<eq_size and y>0 and z ==0):
            midPoint = [mP[0]+eq_size/2, mP[1]+eq_size/2, mP[2]+0]
            dirInEq = [0,0,1]
        elif (x <eq_size and x>0 and y<eq_size and y>0 and z == eq_size):
            midPoint = [mP[0]+eq_size/2, mP[1]+eq_size/2, mP[2]+eq_size]
            dirInEq = [0,0,-1]
        else:
            print("Not valid mid point on quipment!!!")
            print("equipment size: ", eq_size)
            print("Invalid side: ", side)
            print("Equipment position: ", eq_pos)
            midPoint = [0,0,0]
        return midPoint, dirInEq
"""

param_line = "envSizeX=1000&envSizeY=3000&envSizeZ=4000&startA=0%2C1500%2C2000&endB=1000%2C1500%2C2000&pipe_dia=6&eq1_sideX=500&eq1_sideY=500&eq1_sideZ=500&eq1_pos=500%2C500%2C500&eq1_in=0%2C250%2C250&eq1_out=500%2C250%2C250&eq2_sideX=300&eq2_sideY=300&eq2_sideZ=300&eq2_pos=300%2C700%2C500&eq2_in=0%2C150%2C150&eq2_out=300%2C150%2C150&eq3_sideX=700&eq3_sideY=700&eq3_sideZ=700&eq3_pos=700%2C1500%2C2000&eq3_in=0%2C350%2C350&eq3_out=700%2C350%2C350"
if param_line.find("%2C"):
    param_line = param_line.replace("%2C", ',')

key_val_pair = param_line.split('&')
print("key_val_pair: ", key_val_pair)

for i in range(len(key_val_pair)):
    if key_val_pair[i].find("%2C"):
        key_val_pair[i] = key_val_pair[i].replace("2%C", ",")
        print(key_val_pair[i])

print("key_val_pair: ", key_val_pair)


    def makePath(self):
        """
        # this could be function/calculated from num_nodes
        # num_nodes should take the properties of the pipe to consideration
        # we want number of nodes between two points to be equal in ration according to the distance
        num_nodes_A_eq1 = ... #number of nodes between A and eq1
        num_nodes_eq1_eq2 = ... # number of nodes between eq1 and eq2
        num_nodes_eq2_eq3 = ... # number of nodes between eq2 and eq3
        num_nodes_eq3_B = ... # nuber of nodes between eq3 and end point 
        num_nodes_between_2_points = [num_nodes_A_eq1, num_nodes_eq1_eq2, num_nodes_eq2_eq3, num_nodes_eq3_B]
        """
        """
        A_node = 
        eq1_node_in =
        eq1_node_out = 
        eq2_node_in = 
        eq2_node_out = 
        eq3_node_in = 
        eq3_node_out = 
        B_node =
        """