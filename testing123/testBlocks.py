from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from shapes.Cone import Cone
from shapes.Block import Block

import NXOpen
import math
#from NXOpen.NXObject import NXOpen.DisplayableObject

#the size of the space (rectangualr cuboid)
space_length = 3000
space_width = 2000
space_height = 2500

#select the points A and B

#define the size of the equipments

#define where it should be, due to origin. #Here it could be nice with a picture of the box and origin for the custommer to see, after everye placement of something. 

space = Block(0,0,0, space_length, space_width, space_height, "RED", "SeeThrough")
#space.ModelingViews.WorkView.RenderingStyle = NXOpen.View.RenderingStyleType.WireframeWithDimEdges
space.initForNX()

space1 = Block(space_length, space_width,space_length, space_height, space_width, space_height, "RED", "Steel")
space1.initForNX()