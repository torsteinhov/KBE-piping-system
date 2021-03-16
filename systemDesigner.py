from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from shapes.Cone import Cone
from shapes.Block import Block
import math
import random
from pathFinder import a_star
import numpy as np
#import NXOpen.PartCollection

class pipeSystem: 

    def __init__(self, num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: list, startPoint, endPoint, num_node_ax: int, pipeDia: float):
        
        self.num_eq = num_eq # number of equipments in the environment
        self.eq_size_list = eq_size_list # a list of the cube side of the eq. a list of ist, each eq can have different widt,length and height. 
        self.eq_pos = eq_pos # a list of positon of the eq.
        self.eq_in_out = eq_in_out # list of in and out sides of eq. relative to eq.
        self.env_size = env_size #size of the environment, list[x,y,z]
        self.startPoint = startPoint # start point of the pipe
        self.endPoint = endPoint # end point of the pipe
        self.num_node_ax = num_node_ax # number of nodes to divide the environment into along one axis
        self.pipeDia = pipeDia

        self.ratio = self.env_size/self.num_node_ax


    #Cylinder(x, y, z, diameter, height, direction, color, material)
    #Cone(x, y, z, baseDiameter, topDiameter, height, direction, color, material)
    #Block(x, y, z, length, width, height, color, material)

    def run_model(self):
        
        for i in range(self.num_eq):
            # here the code could have a if-else-statement to handle different shapes of the equipment

            eq = Block(self.eq_pos[i][0], self.eq_pos[i][1], self.eq_pos[i][2], self.eq_size_list[i], self.eq_size_list[i], self.eq_size_list[i],"RED", "Steel") # color and material could be extended
            eq.initForNX()
        
        env = Block(0,0,0,self.env_size, self.env_size, self.env_size, "RED", "Steel")
        env.initForNX()

        # make cirles for start and endpoint with diameter = pipe-dia

        #https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.CurveCollection.html#NXOpen.CurveCollection.CreateLine
        #line1 = CreateLine((0,0,0),(100,0,0))
        #line1.initForNX()

    def coordinate2node(self, point): # takes in the a point and gives the node position
        pointInNode = (point[0]*self.ratio, point[1]*self.ratio, point[2]*self.ratio)
        return pointInNode

    def eqInOutWorldPoint(self, side, eq_size, eq_pos): #takes in a side of a eq and the size of the eq and returns the midpoint on the side in world frame
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

        # finding what side the mid point is on and calculating it in global points
        if(x == 0 and y<eq_size and y>0 and z<eq_size and z>0 ):
            midPoint += [0, eq_size/2, eq_size/2]
        elif (x == eq_size and y<eq_size and y>0 and z<eq_size and z>0):
            midPoint += [eq_size, eq_size/2, eq_size/2]
        elif (x <eq_size and x>0 and y==0 and z<eq_size and z>0):
            midPoint += [eq_size/2, 0, eq_size/2]
        elif (x <eq_size and x>0 and y==eq_size and z<eq_size and z>0):
            midPoint += [eq_size/2, eq_size, eq_size/2]
        elif (x <eq_size and x>0 and y<eq_size and y>0 and z ==0):
            midPoint += [eq_size/2, eq_size/2, 0]
        elif (x <eq_size and x>0 and y<eq_size and y>0 and z == eq_size):
            midPoint += [eq_size/2, eq_size/2, eq_size]
        else:
            print("Not valid mid point on quipment!!!")
            print("equipment size: ", eq_size)
            print("Invalid side: ", side)
            print("Equipment position: ", eq_pos)
            midPoint = np.array([0,0,0])
        return midPoint

    def node2point(self, node): #usikker på om dette er riktig
        nodeInPoint = [node[0]/self.ratio, node[1]/self.ratio, node[2]/self.ratio]
        return nodeInPoint

    def nodePath2pointPath(self, nodePath): # takes in a list of nodes which describes the path between eq1 and eq2, and returnes the list in points(world frame coordinates)
        pointPath = []
        for i in range(nodePath):
            point = self.node2point(nodePath[i])
            pointPath.append(point)
        return pointPath
    
    def makeSubEnv(self):
        ...

    def make_pipe(self):
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
            midpoint = self.eqInOutWorldPoint(in_side, self.eq_size_list[i], self.eq_pos[i])
            points2reach.append(midpoint)
            midpoint =self.eqInOutWorldPoint(out_side, self.eq_size_list[i], self.eq_pos[i])
            points2reach.append(midpoint)
        points2reach.append(self.endPoint)

        if points2reach//2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of points to reach is not even! Check this out!")

        nodes2reach = [] # a list of all nodes we want to reach
        #nodes2reach = [A_node,eq1_node_in, eq1_node_out, eq2_node_in, eq2_node_out, eq3_node_in, eq3_node_out, B_node]
        for i in range(points2reach):
            nodeOfPoint = self.coordinate2node(points2reach[i])
            nodes2reach.append(nodeOfPoint)
        
        if nodes2reach//2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of nodes is not even! Check this out!")

        node_paths_all = [] # collecting all the paths between the nodes to reach in a list
        #k=0 # counting variable to get the correct nomber of nodes between to points
        for i in range(0,len(nodes2reach/2), 2): # itterates over every second step in nodes to reach
            #path_nodes = a_star(num_nodes_between_2_points[k], nodes2reach[i], nodes2reach[i+1])
            path_nodes = a_star(self.num_node_ax, nodes2reach[i], nodes2reach[i+1]) #ble dette riktig??
            node_paths_all.append(path_nodes)
            #k+=1

        # changing the path to points from coordinates
        point_paths_all = [] # a list with the different paths, ex: [from A to eq1, form eq1 to eq2, form eq2 to eq3, form eq3 to B]
        for i in range(len(node_paths_all)):
            path_points = self.nodePath2pointPath(node_paths_all[i])
            point_paths_all.append(path_points)

        #make a actual path of the points

processSystem = pipeSystem(130, 100, 160)
processSystem.run_model()
