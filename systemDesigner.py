from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from shapes.Cone import Cone
from shapes.Block import Block
import math
import random
from pathFinder import a_star
#import NXOpen.PartCollection

class pipeSystem: 

    def __init__(self, eq1_size, eq2_size, eq3_size, env_size, eq1_pos, eq2_pos, eq3_pos, startPoint, endPoint, num_node_ax):
        self.eq1_size = eq1_size
        self.eq2_size = eq2_size
        self.eq3_size = eq3_size
        self.env_size = env_size
        self.eq1_pos = eq1_pos
        self.eq2_pos = eq2_pos
        self.eq3_pos = eq3_pos
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.num_node_ax = num_nodes_ax


    #Cylinder(x, y, z, diameter, height, direction, color, material)
    #Cone(x, y, z, baseDiameter, topDiameter, height, direction, color, material)
    #Block(x, y, z, length, width, height, color, material)
    def run_model(self):

        eq1 = Block(0,0,0,self.eq1_size,self.eq1_size,self.eq1_size,"RED","Steel")
        eq1.initForNX()
        eq2 = Block(500,500,500,self.eq2_size,self.eq2_size,self.eq2_size,"BLUE","Steel")
        eq2.initForNX()
        eq3 = Block(0,300,100,self.eq3_size,self.eq3_size,self.eq3_size,"YELLOW","Steel")
        eq3.initForNX()
        #https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.CurveCollection.html#NXOpen.CurveCollection.CreateLine
        #line1 = CreateLine((0,0,0),(100,0,0))
        #line1.initForNX()

    def coordinate2node(self, point): # takes in the a point and gives the node position
        ratio = self.env_size/self.num_node_ax
        pointInNode = (point[0]*ratio, point[1]*ratio, point[2]*ratio)
        return pointInNode
    
    def makeSubEnv(self):

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
        nodes2reach = [] # a list of all nodes we want to reach
        #nodes2reach = [A_node,eq1_node_in, eq1_node_out, eq2_node_in, eq2_node_out, eq3_node_in, eq3_node_out, B_node]
        num_points = len(given_points)
        for i in range(num_points):
            nodeOfPoint = coordinate2node(num_points[i])
            nodes2reach.append(nodeOfPoint)
        
        if nodes2reach//2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of nodes is not even! Check this out!")

        node_paths_all = [] # collecting all the paths between the nodes to reach in a list
        k=0 # counting variable to get the correct nomber of nodes between to points
        for i in range(0,len(nodes2reach/2), 2): # itterates over every second step in nodes to reach
            path_nodes = a_star(num_nodes_between_2_points[k], nodes2reach[i], nodes2reach[i+1])
            node_paths_all.append(path_nodes)
            k+=1

        #define sub env
        # find path in xyz coords

processSystem = pipeSystem(130, 100, 160)
processSystem.run_model()
