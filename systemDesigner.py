from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from shapes.Cone import Cone
from MyGA_lamp_v2 import MyGA_lamp
import math
import random

class makeLamp: 

    def __init__(self, base_diameter, leg_length, origin_point, point):
        self.base_diameter = base_diameter
        self.leg_length = leg_length
        self.point = point
        self.origin_point = origin_point


    #Made help functions to define x and y coordinates, had to drop because of complications
    '''
    def calculate_katetX(self, hypotenus, angle):
        x = (math.cos(math.radians(90-angle))) * hypotenus
        return x

    def calculate_katetZ(self, hypotenus, angle):
        z = math.sin(math.radians(90-angle))*hypotenus
        return z
    '''



    #Cylinder(x, y, z, diameter, height, direction, color, material)
    #Cone(x, y, z, baseDiameter, topDiameter, height, direction, color, material)
    def run_model(self):

        #tried to have an angle on the upper part of the leg, but we had to drop because of complications.
        '''
        if (point[0] >= 0 and point[1] >= 0) or (point[0] >= 0 and point[1] < 0):
            angle = angle
        elif (point[0] < 0 and point[1] >= 0) or (point[0] < 0 and point[1] < 0):
            angle = -angle

        setxVector = math.tan(math.radians(angle))
        '''

        hood_base_z = self.leg_length + self.base_diameter
        hood_base_x = 0
        hood_base_length = float(self.leg_length/7)
        hood_z = hood_base_z     # - self.calculate_katetZ(hood_base_length, angle)
        hood_x = hood_base_x     # + self.calculate_katetX(hood_base_length, angle)

        base1 = Cylinder(0, 0, 0, self.base_diameter/2, 15, [0, 0, 1], "YELLOW", "Wood")
        base1.initForNX()
        base2 = Cylinder(0, 0, 15, self.base_diameter/5, 5, [0, 0, -1], "YELLOW", "Wood")
        base2.initForNX()
        base1.subtract(base2)
        leg1 = Cylinder(0, 0, 0, self.base_diameter/20, float(self.base_diameter), [0, 0, 1], "YELLOW", "Wood")
        leg1.initForNX()
        sphere_connector = Sphere(0, 0, float(self.base_diameter), self.leg_length/(self.base_diameter/30), "GREEN", "Wood")
        sphere_connector.initForNX()
        leg2 = Cylinder(0, 0, self.base_diameter, self.base_diameter/20, float(self.leg_length), [0, 0, 1], "YELLOW", "Wood")
        leg2.initForNX()
        hood_base = Cylinder(hood_base_x,0,hood_base_z, self.leg_length/10, hood_base_length, self.point, "GREEN", "Wood")
        hood_base.initForNX()
        hood = Cone(hood_x, 0, hood_z, self.leg_length/10, self.leg_length/3, self.leg_length/3, self.point, "BLUE", "PLASTIC")
        hood.initForNX()
        hoodCutout = Cone(hood_x, 0, hood_z, self.leg_length/12, self.leg_length/4, self.leg_length/3, self.point, "BLUE", "PLASTIC")
        hoodCutout.initForNX()
        hood.subtract(hoodCutout)