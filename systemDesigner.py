from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from shapes.Cone import Cone
from shapes.Block import Block
import math
import random
import NXOpen.CurveCollection.CreateLine

class pipeSystem: 

    def __init__(self, eq1_size, eq2_size, eq3_size):
        self.eq1_size = eq1_size
        self.eq2_size = eq2_size
        self.eq3_size = eq3_size

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
        line1 = CreateLine(startPoint,endPoint)
        line1.initForNX()

processSystem = pipeSystem(200, 100, 300)
processSystem.run_model()