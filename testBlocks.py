from shapes.Block import Block
from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from util.Analyzer import Analyzer
from datetime import datetime
import time
import random

# Make product analysis after construction
analyze = True

"""
Do a block at the origin with corresponding length (20), width (20),
height (50), color (RED) and material (Aluminum_5086)
"""
b1 = Block(0.0, 0.0, 0.0, 20, 20, 50, "RED", "Aluminum_5086")
b1.initForNX() # Initialize the block in NX

"""
Do a cylinder having its origin at (10, 10, 50) with corresponding diameter (20),
height (30), direction ([0, 0, 1]), color (RED) and material (Aluminum_5086)
"""
c1 = Cylinder(10, 10, 50, 20, 30, [0, 0, 1], "RED", "Aluminum_5086")
c1.initForNX() # Initialize the cylinder in NX

"""
Do a sphere having its origin at (10, 10, 50) with corresponding diameter (50), 
color (BLUE) and material (Aluminum_5086)
"""
s1 = Sphere(10, 10, 50, 25, "BLUE", "Aluminum_5086")
s1.initForNX() # Initialize the sphere in NX

#Substract c1 from s1
#s1.subtract(c1) # one of the ways - just an illustration
c1.subtractFrom(s1) 
