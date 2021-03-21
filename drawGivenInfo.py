from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from shapes.Cone import Cone
from shapes.Block import Block
import math
import random
#from pathFinder import a_star
#import numpy as np
#import NXOpen.PartCollection

class drawGivenInfo: 

    def __init__(self, num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: int, startPoint, endPoint, pipeDia: float):
        
        self.num_eq = num_eq # number of equipments in the environment
        self.eq_size_list = eq_size_list # a list of the cube side of the eq. 
        self.eq_pos = eq_pos # a list of positon of the eq.
        self.eq_in_out = eq_in_out # list of in and out sides of eq. relative to eq.
        self.env_size = env_size #size of the environment
        self.startPoint = startPoint # start point of the pipe
        self.endPoint = endPoint # end point of the pipe
        self.pipeDia = pipeDia

        #for the holes symolizing in/out
        self.height = 5
        self.color = "BLUE"
        self.material = "Wood"


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
        #env.makeSeeThrough(95)

        # Illustrate placement of A as a cylinder
        #startPoint = Cylinder(self.startPoint[0], self.startPoint[1], self.startPoint[2], self.pipeDia, height, ##direction, self.color, self.material)
        #startPoint.initForNX()
        #env.subtract(startPoint)
        
        # Illustrate placement of B 
        #endPoint = Cylinder(self.endPoint[0], self.endPoint[1], self.endPoint[2], self.pipeDia, self.height, direction, self.color, self.material)
        #endPoint.initForNX()
        #env.subtract(endPoint)

        """ If the part with only blocks works then try this one istead.
        # Illustrate plasement of inlet and outlet on the eq.
        mpWF, mpD = self.midPointsGlobal() # midpointsWorldFrame, midpintDirection
        if len(mpWF)/2 != len(self.num_eq):
            print("Number of midpoints is not twice as much as number of equipments. Fix it!")
        k = 0
        for i in range(mpWF):
            if i//2 ==0:
                eq = Block(self.eq_pos[k][0], self.eq_pos[k][1], self.eq_pos[k][2], self.eq_size_list[k], self.eq_size_list[k], self.eq_size_list[k],"RED", "Steel") # color and material could be extended
                eq.initForNX()
                k += 1
        
            hole = Cylinder(mpWF[i][0], mpWF[i][1], mpWF[i][2], self.pipeDia, self.height, mpD[i],self.color, self.material)
            hole.initForNX()
            eq.subtract(hole)
        """
        #need to find the direction into the cube

        # make cirles for start and endpoint with diameter = pipe-dia

        #https://docs.plm.automation.siemens.com/data_services/resources/nx/10/nx_api/en_US/custom/nxopen_python_ref/NXOpen.CurveCollection.html#NXOpen.CurveCollection.CreateLine
        #line1 = CreateLine((0,0,0),(100,0,0))
        #line1.initForNX()

    """
    def eqInOutWorldPoint(self, side, eq_size, eq_pos): #takes in a side of a eq and the size of the eq and returns the midpoint on the side in world frame
        # side = [x,y,z] rrelative to the equipment
        # =================
        # possible sides of a cube
        # (x=0, y, z), (x, y= 0, z), (x,y,z=0)
        # (x=eq_size, y, z), (x, y=eq_size, z), (x,y, z=eq_size)
        # The letter how dont have any nuymber should be between <0,eq_size>
        # ================
        # dirInEq is the direction from the side and into the box
        x = side[0]
        y = side[1]
        z = side[2]
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
    
    def midPointsGlobal(self): # making a list of all the points (in world frame) to make pipe between
        points2reach = []
        dirInEq = []
        n = 0
        for i in range(0, len(self.eq_size_list), 2):
            in_side = self.eq_in_out[n] #in to eq
            out_side = self.eq_in_out[n+1] #out from eq
            midpoint, dirInEq_ = self.eqInOutWorldPoint(in_side, self.eq_size_list[i], self.eq_pos[i])
            points2reach.append(midpoint)
            dirInEq.append(dirInEq_)
            midpoint, dirInEq_ = self.eqInOutWorldPoint(out_side, self.eq_size_list[i], self.eq_pos[i])
            points2reach.append(midpoint)
            dirInEq.append(dirInEq_)
        
        if points2reach//2 !=0 : #if the number of elements in nodes2reach not is even, there is an error
            print("Number of points to reach is not even! Check this out!")

        if len(points2reach) != len(dirInEq):
            print("Number of midpoints is not the same as number of directions atached to midpoints. Fix it!")

        return points2reach, dirInEq #resturns a list of the midpoints given in coordinates of the global frame
    """

# for testing
#if __name__ == '__main__':
num_eq = 3
eq_size_list = [[70,70,70],[150,150,150],[1000,1000,1000]]
eq_pos = [[50,150,0],[150,1000,1000], [2000,1000,2000]]
env_size = [3000,3000,3000]
eq_in_out = [[40,0,40], [70,40,40],[100,0,100],[150,100,100],[500,0,500],[1000,500,500]]
startPoint = [0,1500,1500]
endPoint = [3000, 1500,1500]
pipeDia =  50.8

custommer = drawGivenInfo(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, pipeDia)
custommer.run_model()


