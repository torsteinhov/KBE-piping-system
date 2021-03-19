# this script checks the geometry of the user inpu
# eg. if the equipments are insde of the environment
# eg. if the start and end point are on the surface of the environment

def pointOnSurface(env_size:list, point:list): #env__size=[x,y,z] - point=[x,y,z]
	x_e =env_size[0]
	y_e = env_size[1]
	z_e = env_size[2]
	x_p = point[0]
	y_p = point[1]
	z_p = point[2]

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

    if eq_pos[0] > 0 and eq_pos[0] + eq_size <= env_size[0]: # check if the eq is inside the x-dir
        insideXdir = True
    else: 
        errorMsg = "Equipment is outside the environment in the width (x-direction). "
        messages += errorMsg

    if eq_pos[1] >0 and eq_pos[1]+ eq_size[1]<= env_size[1]:
        insideYdir = True
    else:
        errorMsg = " Equipment is outside the environment in the length (y-direction)."
        messages += errorMsg
    if eq_pos[2] >0 and eq_pos[2]+eq_size[2] <= env_size[2]:
        insideZdir = True
    else:
        errorMsg = " Equipment is outside the environment in the height (z-direction)."
        messages += errorMsg

    if insideXdir and insideYdir and insideZdir:
        eqInsideEnv = True
        messages = "ok"

    return eqInsideEnv, messages

def equpmentCrash(eqN_pos, eqN_size, eqM_pos, eqM_size): #check if the equipments crashes into eachother
	...



def checkCustommerInput(num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: list, startPoint, endPoint, num_node_ax: int, pipeDia: float):
	messages = []
	pipeDia_mm = 25.4 * pipeDia

	if all(pipeDia_mm < i for i in eq_size_list ):#pipe diameter is smaller than all of the eq
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
		errorMsg = "for equpment number " + (i+1)
		eqInsideEnv, text = insideEnv(env_size, eq_size_list[i], eq_pos[i]) 
		errorMsg += text
		messages.append(errorMsg)
	
	return messages


	