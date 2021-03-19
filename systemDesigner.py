import math
import random
from pathFinder import aStar
import numpy as np
#import NXOpen.PartCollection

class pipeSystem: 

    def __init__(self, num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: list, startPoint, endPoint, num_node_ax: int, pipeDia: float):
        
        self.num_eq = num_eq # number of equipments in the environment
        self.eq_size_list = eq_size_list # a list of the cube side of the eq. a list of ist, each eq can have different width, length and height. 
        self.eq_pos = eq_pos # a list of positon of the eq.
        self.eq_in_out = eq_in_out # list of in and out sides of eq. relative to eq.
        self.env_size = env_size #size of the environment, list[x,y,z][width,length,height]
        self.startPoint = startPoint # start point of the pipe
        self.endPoint = endPoint # end point of the pipe
        self.num_node_ax = num_node_ax # number of nodes to divide the environment into along one axis
        self.pipeDia = pipeDia

        self.ratioX = self.env_size[0]/self.num_node_ax
        self.ratioY = self.env_size[1]/self.num_node_ax
        self.ratioZ = self.env_size[2]/self.num_node_ax


    def coordinate2node(self, point): # takes in the a point and gives the node position
        pointInNode = (point[0]*self.ratioX, point[1]*self.ratioY, point[2]*self.ratioZ)
        return pointInNode

    def eqInOutWorldPoint(self, side, eq_sizeX, eq_sizeY, eq_sizeZ, eq_pos): #takes in a side of a eq and the size of the eq and returns the midpoint on the side in world frame
        # side = [x,y,z] rrelative to the equipment
        # =================
        # possible sides of a cube
        # (x=0, y, z), (x, y= 0, z), (x,y,z=0)
        # (x=eq_size, y, z), (x, y=eq_size, z), (x,y, z=eq_size)
        # The letter how dont have any nuymber should be between <0,eq_size>
        # ================
        x = side[0]
        y = side[1]
        z = side[2]
        midPoint = np.array([eq_pos[0],eq_pos[1],eq_pos[2]])
        print("Midpoint: ", midPoint)
        print("x: ", x)
        print("y: ", x)
        print("z: ", z)

        # finding what side the mid point is on and calculating it in global points
        if(x == 0 and y < eq_sizeY and y > 0 and z < eq_sizeZ and z > 0 ):
            np.add(midPoint, [0, eq_sizeY/2, eq_sizeZ/2], out=midPoint, casting="unsafe")

        elif (x == eq_sizeX and y < eq_sizeY and y > 0 and z < eq_sizeZ and z > 0):
            np.add(midPoint, [eq_sizeX, eq_sizeY/2, eq_sizeZ/2], out=midPoint, casting="unsafe")

        elif (x < eq_sizeX and x > 0 and y==0 and z < eq_sizeZ and z > 0):
            np.add(midPoint, [eq_sizeX/2, 0, eq_sizeZ/2], out=midPoint, casting="unsafe")

        elif (x < eq_sizeX and x > 0 and y==eq_sizeY and z < eq_sizeZ and z > 0):
            np.add(midPoint, [eq_sizeX/2, eq_sizeY, eq_sizeZ/2], out=midPoint, casting="unsafe")

        elif (x < eq_sizeX and x > 0 and y < eq_sizeY and y > 0 and z ==0):
            np.add(midPoint, [eq_sizeX/2, eq_sizeY/2, 0], out=midPoint, casting="unsafe")

        elif (x < eq_sizeX and x > 0 and y < eq_sizeY and y > 0 and z == eq_sizeZ):
            np.add(midPoint, [eq_sizeX/2, eq_sizeY/2, eq_sizeZ], out=midPoint, casting="unsafe")

        else:
            print("Not valid mid point on quipment!!!")
            midPoint = np.array([0,0,0])
        return midPoint

    def node2point(self, node): #usikker på om dette er riktig
        nodeInPoint = [node[0]/self.ratioX, node[1]/self.ratioY, node[2]/self.ratioZ]
        return nodeInPoint

    def nodePath2pointPath(self, nodePath): # takes in a list of nodes which describes the path between eq1 and eq2, and returnes the list in points(world frame coordinates)
        pointPath = []
        for i in range(nodePath):
            point = self.node2point(nodePath[i])
            pointPath.append(point)
        return pointPath
    
    def makeSubEnv(self):
        ...

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

        # making a list of all the points (in world frame) to make pipe between
        points2reach = [self.startPoint]
        n = 0
        for i in range(0, len(self.eq_size_list), 2):
            in_side = self.eq_in_out[n] #in to eq
            out_side = self.eq_in_out[n+1] #out from eq
            midpoint = self.eqInOutWorldPoint(in_side, self.eq_size_list[i][0],self.eq_size_list[i][1],self.eq_size_list[i][2],self.eq_pos[i])
            points2reach.append(midpoint)
            midpoint =self.eqInOutWorldPoint(out_side, self.eq_size_list[i][0],self.eq_size_list[i][1],self.eq_size_list[i][2],self.eq_pos[i])
            points2reach.append(midpoint)
        points2reach.append(self.endPoint)

        print("points2reach: ", points2reach)
        if int(len(points2reach))//2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of points to reach is not even! Check this out!")

        nodes2reach = [] # a list of all nodes we want to reach
        #nodes2reach = [A_node,eq1_node_in, eq1_node_out, eq2_node_in, eq2_node_out, eq3_node_in, eq3_node_out, B_node]
        for i in range(len(points2reach)):
            nodeOfPoint = self.coordinate2node(points2reach[i])
            nodes2reach.append(nodeOfPoint)
        
        if int(len(nodes2reach))//2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of nodes is not even! Check this out!")

        print("nodes2reach: ", nodes2reach)
        print("len(nodes2reach): ", len(nodes2reach)/2)
        node_paths_all = [] # collecting all the paths between the nodes to reach in a list
        #k=0 # counting variable to get the correct nomber of nodes between to points
        for i in range(0,len(nodes2reach)//2, 2): # iterates over every second step in nodes to reach
            #path_nodes = aStar(num_nodes_between_2_points[k], nodes2reach[i], nodes2reach[i+1])
            path_nodes = aStar(max(env_size[0],env_size[1],env_size[2]), nodes2reach[i], nodes2reach[i+1]) #ble dette riktig??
            node_paths_all.append(path_nodes)
            #k+=1

        #print("node_paths_all: ",node_paths_all)

        # changing the path to points from coordinates
        point_paths_all = [] # a list with the different paths, ex: [from A to eq1, form eq1 to eq2, form eq2 to eq3, form eq3 to B]
        for i in range(len(node_paths_all)):
            path_points = self.nodePath2pointPath(node_paths_all[i])
            point_paths_all.append(path_points)

        return point_paths_all

        #make a actual path of the points

#def __init__(self, num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: list, startPoint, endPoint, num_node_ax: int, pipeDia: float):
num_eq = 3
eq_size_list = [[5,5,5],[15,15,15],[20,20,20]]
eq_pos = [[5,15,0],[15,100,100],[200,100,200]]
env_size = [300,200,200]
eq_in_out = [[4,0,4], [7,4,4],[10,0,10],[15,10,10],[50,0,50],[100,50,50]]
startPoint = [0,150,150]
endPoint = [300, 150,150]
pipeDia =  5

processSystem = pipeSystem(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, 100, pipeDia)
print(processSystem.makePath())
#processSystem.run_model()

