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

        self.distanceBetweenNodes = max(int(env_size[0]),int(env_size[1]),int(env_size[2]))/num_node_ax


    # take in a point and give out the corresponding node
    def coordinate2node(self, point):
        pointInNode = (int(point[0])//self.distanceBetweenNodes, int(point[1])//self.distanceBetweenNodes, int(point[2])//self.distanceBetweenNodes)
        return pointInNode

    # takes inn a local point on the surface of a equipment, the size of the equipment and the position(global) of the equipment
    # and return the point on the surface in Global coordinates
    def eqInOutGlobalPoint(self, point, eq_size, eq_pos): #takes in a side of a eq and the size of the eq and returns the midpoint on the side in world frame
		# side = [x,y,z] rrelative to the equipment -- this is the point
		# =================
		# possible sides of a cube
		# (x=0, y, z), (x, y= 0, z), (x,y,z=0)
		# (x=eq_size, y, z), (x, y=eq_size, z), (x,y, z=eq_size)
		# The letter how dont have any nuymber should be between <0,eq_size>
		# ================
        # # dirInEq is the direction from the side and into the box
        x = int(point[0])
        y = int(point[1])
        z = int(point[2])

		# finding what side the mid point is on and calculating it in global points
        if(x == 0 and y<int(eq_size[1]) and y>0 and z<int(eq_size[2]) and z>0 ):
            midPoint = [int(eq_pos[0])+0, int(eq_pos[1])+int(eq_size[1])/2, int(eq_pos[2])+int(eq_size[2])/2]
            
        elif (x == int(eq_size[0]) and y<int(eq_size[1]) and y>0 and z<int(eq_size[2]) and z>0):
            midPoint = [int(eq_pos[0])+int(eq_size[0]), int(eq_pos[1])+int(eq_size[1])/2, int(eq_pos[2])+int(eq_size[2])/2]
			
        elif (x <int(eq_size[0]) and x>0 and y==0 and z<int(eq_size[2]) and z>0):
            midPoint = [int(eq_pos[0])+int(eq_size[0])/2, int(eq_pos[1])+0, int(eq_pos[2])+int(eq_size[2])/2]
			
        elif (x <int(eq_size[0]) and x>0 and y==int(eq_size[1]) and z<int(eq_size[2]) and z>0):
            midPoint = [int(eq_pos[0])+int(eq_size[0])/2, int(eq_pos[1])+int(eq_size[1]), int(eq_pos[2])+int(eq_size[2])/2]
			
        elif (x <int(eq_size[0]) and x>0 and y<int(eq_size[1]) and y>0 and z ==0):
            midPoint = [int(eq_pos[0])+int(eq_size[0])/2, int(eq_pos[1])+int(eq_size[1])/2, int(eq_pos[2])+0]
			
        elif (x <int(eq_size[0]) and x>0 and y<int(eq_size[1]) and y>0 and z == int(eq_size[2])):
            midPoint = [int(eq_pos[0])+int(eq_size[0])/2, int(eq_pos[1])+int(eq_size[1])/2, int(eq_pos[2])+int(eq_size[2])]
			
        else:
            print("Not valid mid point on equipment!")
            print("equipment size: ", eq_size)
            print("Invalid side: ", point)
            print("Equipment position: ", eq_pos)
            midPoint = [0,0,0]
		
        return midPoint
    # takes in a node and returns the Global point
    def node2point(self, node): #usikker p?? om dette er riktig
        nodeInPoint = [round(node[0]*self.distanceBetweenNodes,1), round(node[1]*self.distanceBetweenNodes,1), round(node[2]*self.distanceBetweenNodes,1)]
        return nodeInPoint

    # takes in a path of nodes and returs a path in Global points
    def nodePath2pointPath(self, nodePath): # takes in a list of nodes which describes the path between eq1 and eq2, and returnes the list in points(world frame coordinates)
        pointPath = []
        for i in range(len(nodePath)):
            point = self.node2point(nodePath[i])
            pointPath.append(point)
        return pointPath
    
    def makeSubEnv(self):
        ...

    # this function uses all the other function 
    # using all the functions and the given information and returns a list of lists
    # returning: [pointpath between A and eq1In, pointPath between eq1Out and eq2In, pointPath between eq2out and eq3In, pointpath between eq3Out and B]
    def makePath(self):

        # making a list of all the points (in global frame) to make pipe between
        points2reach = [self.startPoint] #first adding the startpoint to the list

        #eq_size_list=[[eq1_w,eq1_l,eq1_h],[eq2_w,eq2_l,eq2_h]]
        #eq_in_out=[[eq1_in_X,eq1_in_Y,eq1_in_Z],[eq1_out_X,eq1_out_Y,eq1_out_Z],[eq2_in_X,eq2_in_Y,eq2_in_Z],[eq2_out_X,eq2_out_Y,eq2_out_Z]]
        n = 0
        for i in range(self.num_eq):
            in_side = self.eq_in_out[n]
            out_side = self.eq_in_out[n+1]
            midPointIn = self.eqInOutGlobalPoint(in_side,self.eq_size_list[i],self.eq_pos[i])
            points2reach.append(midPointIn)
            midPointOut = self.eqInOutGlobalPoint(out_side,self.eq_size_list[i],self.eq_pos[i])
            points2reach.append(midPointOut)
            n+=2

        points2reach.append(self.endPoint) #finally adding the endpoint to the list of all points 2 reach globally

        if len(points2reach)%2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of points to reach is not even! Check this out!")


        # then we need to convert the points (global) to nodes
        nodes2reach = [] # a list of all nodes we want to reach
        # this is how it will look: nodes2reach = [A_node,eq1_node_in, eq1_node_out, eq2_node_in, eq2_node_out, eq3_node_in, eq3_node_out, B_node]

        for i in range(len(points2reach[-1])):
            value = max(self.env_size[0],self.env_size[1],self.env_size[2])
            if points2reach[-1][i] == value:
                points2reach[-1][i] = value - 1
            
        for j in points2reach:
            nodeOfPoint = self.coordinate2node(j)
            nodes2reach.append(nodeOfPoint)
        
        if int(len(nodes2reach))%2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of nodes is not even! Check this out!")

        # collecting all the paths between the nodes to reach in a list
        node_paths_all = []
        # iterates over every second step in nodes to reach, because we want the path between A and eq1In, eq1Out and eq2In. We do NOT want the path between eq1In and eq1Out
        for i in range(0,len(nodes2reach), 2):
            path_nodes = aStar(int(self.num_node_ax), nodes2reach[i], nodes2reach[i+1])
            node_paths_all.append(path_nodes)


        # now we have the wanted paths in nodes and we need them in point paths
        # changing the path from nodes to points (global)
        point_paths_all = [] # a list with the different paths, ex: [from A to eq1, form eq1 to eq2, form eq2 to eq3, form eq3 to B]
        for i in range(len(node_paths_all)):
            path_points = self.nodePath2pointPath(node_paths_all[i])
            point_paths_all.append(path_points)

        return point_paths_all