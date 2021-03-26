# this script checks the geometry of the user inpu
# eg. if the equipments are insde of the environment
# eg. if the start and end point are on the surface of the environment

def pointOnSurface(env_size:list, point:list): #env__size=[x,y,z] - point=[x,y,z]
	x_e = int(env_size[0])
	y_e = int(env_size[1])
	z_e = int(env_size[2])
	x_p = int(point[0])
	y_p = int(point[1])
	z_p = int(point[2])

	onSureface = False

	if x_p == 0 and y_p>0 and y_p<y_e and z_p>0 and z_p<z_e:
		onSureface = True
	elif x_p == x_e and y_p>0 and y_p<y_e and z_p>0 and z_p<z_e:
		onSureface = True
	elif x_p>0 and x_p<x_e and y_p==0 and z_p>0 and z_p<z_e:
		onSureface = True
	elif x_p>0 and x_p<x_e and y_p==y_e and z_p>0 and z_p<z_e:
		onSureface = True
	elif  x_p>0 and x_p<x_e and y_p>0 and y_p<y_e and z_p ==0:
		onSureface = True
	elif  x_p>0 and x_p<x_e and y_p>0 and y_p<y_e and z_p ==z_e:
		onSureface = True

	return onSureface

def insideEnv(env_size:list, eq_size: list, eq_pos: list): #env_size=[x(width), y(length), z(height)] - eq_size = [x(width), y(length), z(height)] per eq. - eq_pos = eq_size = [x(width), y(length), z(height)]
# this function checks if the eq is inside the env. 
    messages = ""
    insideXdir = False
    insideYdir = False
    insideZdir = False
    eqInsideEnv = False

    if int(eq_pos[0]) >= 0 and int(eq_pos[0]) + int(eq_size[0]) <= int(env_size[0]): # check if the eq is inside the x-dir
        insideXdir = True
    else: 
        errorMsg = "Equipment is outside the environment in the width (x-direction). "
        messages += errorMsg

    if int(eq_pos[1]) >= 0 and int(eq_pos[1])+ int(eq_size[1])<= int(env_size[1]): # check if the eq is inside the y-dir
        insideYdir = True
    else:
        errorMsg = "Equipment is outside the environment in the length (y-direction)."
        messages += errorMsg
    if int(eq_pos[2]) >= 0 and int(eq_pos[2]) + int(eq_size[2]) <= int(env_size[2]): # check if the eq is inside the y-dir
        insideZdir = True
    else:
        errorMsg = " Equipment is outside the environment in the height (z-direction)."
        messages += errorMsg

    if insideXdir and insideYdir and insideZdir:
        eqInsideEnv = True
        messages = "ok"

    return eqInsideEnv, messages

#Checks wether the equipment crash with eachother
#ref https://www.geeksforgeeks.org/find-two-rectangles-overlap/ , extended for use in 3D.
def equipmentCrash(self_pos, self_size, other_pos, other_size):

	overlapXYleft = False
	overlapXYover = False
	overlapXZleft = False
	overlapXZover = False
	overlapYZleft = False
	overlapYZover = False

	l1xy = [self_pos[0],self_pos[1]]
	r1xy = [self_pos[0]+self_size[0],self_pos[1]+self_size[1]]
	l2xy = [other_pos[0],other_pos[1]]
	r2xy = [other_pos[0]+other_size[0],other_pos[1]+other_size[1]]


	if (l1xy[0] > r2xy[0] or l2xy[0] > r1xy[0]):
		overlapXYleft = False
	else:
		overlapXYleft = True
	
	if (l1xy[1] < r2xy[1] or l2xy[1] < r1xy[1]):
		overlapXYover = False
	else:
		overlapXYover = True


	l1xz = [self_pos[0],self_pos[2]]
	r1xz = [self_pos[0]+self_size[0],self_pos[2]+self_size[2]]
	l2xz = [other_pos[0],other_pos[2]]
	r2xz = [other_pos[0]+other_size[0],other_pos[2]+other_size[2]]

	if (l1xz[0] > r2xz[0] or l2xz[0] > r1xz[0]):
		overlapXZleft = False
	else:
		overlapXZleft = True

	if (l1xz[1] < r2xz[1] or l2xz[1] < r1xz[1]):
		overlapXZover = False
	else:
		overlapXZover = True


	l1yz = [self_pos[1],self_pos[2]]
	r1yz = [self_pos[1]+self_size[1],self_pos[2]+self_size[2]]
	l2yz = [other_pos[1],other_pos[2]]
	r2yz = [other_pos[1]+other_size[1],other_pos[2]+other_size[2]]

	if (l1yz[0] > r2yz[0] or l2yz[0] > r1yz[0]):
		overlapYZleft = False
	else:
		overlapYZleft = True

	if (l1yz[1] < r2yz[1] or l2yz[1] < r1yz[1]):
		overlapYZover = False
	else:
		overlapYZover = True

	overlapXY = (overlapXYleft or overlapXYover)
	overlapXZ = (overlapXZleft or overlapXZover)
	overlapYZ = (overlapYZleft or overlapYZover)

	if (overlapXY and overlapXZ and overlapYZ):
		messages = "colliding equipments"
		return True, messages

	messages = "ok"
	return False, messages 



def checkCustomerInput(num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: list, startPoint, endPoint, num_node_ax: int, pipeDia: int):

	messages = []

	pipeDia_mm = 25.4 * pipeDia

	for eq in range(len(eq_size_list)): # shuld check the side that the pip is entring, not all.
		for side in eq_size_list[eq]:
			if (pipeDia_mm < int(side)):#pipe diameter is smaller than all of the eq
				errorMsg = "ok"
				messages.append(errorMsg)
			else:
				errorMsg = "The pipe diameter is greater than the equipment"
				messages.append(errorMsg)
	
	if pointOnSurface(env_size,startPoint):# Need to have a function to check if point A and B is ond the surface of env.
		errorMsg = "ok"
		messages.append(errorMsg)
	else:
		errorMsg = "The start point, A, is not on the surface of the environment."
		messages.append(errorMsg)

	if pointOnSurface(env_size,endPoint):
		errorMsg = "ok"
		messages.append(errorMsg)
	else:
		errorMsg = "The end point, B, is not on the surface of the environment."
		messages.append(errorMsg)
	
	for i in range(num_eq):
		errorMsg = "for equipment number " + str(i+1)
		eqInsideEnv, text = insideEnv(env_size, eq_size_list[i], eq_pos[i]) 
		errorMsg += text
		messages.append(errorMsg)

	for i in range(num_eq): # check for colliding equipments
		for j in range(num_eq): # using double for-loop to check every equpiment to all off the other equipment, this is not neassescary for only 3 eq
			if i !=j: # do not check against it self
				colliding, errorMsg = equipmentCrash(eq_pos[i], eq_size_list[i],eq_pos[j], eq_size_list[j])  # it should also be a feedback of which eq that is colliding.
				collidingEq = "Equipments " + str(i + 1) + " and " + str(j + 1) +": "
				messages.append(collidingEq + errorMsg)
	
	return messages