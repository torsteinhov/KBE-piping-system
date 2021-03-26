#dfaUpdater to pipeSystemDesigner

templateForPipeSys = """#! NX/KF 4.0
DefClass: PipeSys_<customerName_company> (ug_base_part);
    (number parameter) environmentX: <envX>;
    (number parameter) environmentY: <envY>;
    (number parameter) environmentZ: <envZ>; 

#+
--------------PIPE-PROFILE---------------
#-

<PIPE_PROFILE_COMES_HERE>


#+
--------------PIPE-CLASS-----------------
#-

<PIPE_CLASS_COMES_HERE>

#+
Information about the customer:
    Name: <CUSTOMER_NAME>
    Company: <COMPANY_NAME>
    Number: <NUMBER>
    E-mail: <EMAIL>
#-

#+
---------------ENVIRONMENT-----------------
#-

(Child) environment_line1: {
 Class, ug_line; 
 Start_Point, Point(0,0,0); 
 End_Point, Point(environmentX:,0,0); 
}; 

(Child) environment_line2: {
 Class, ug_line; 
 Start_Point, Point(0,0,0); 
 End_Point, Point(0,environmentY:,0); 
}; 

(Child) environment_line3: {
 Class, ug_line; 
 Start_Point, Point(0,0,0); 
 End_Point, Point(0,0,environmentZ:); 
}; 

(Child) environment_line4: {
 Class, ug_line; 
 Start_Point, Point(environmentX:,0,0); 
 End_Point, Point(environmentX:,environmentY:,0); 
}; 

(Child) environment_line5: {
 Class, ug_line; 
 Start_Point, Point(environmentX:,0,0); 
 End_Point, Point(environmentX:,0,environmentZ:); 
}; 

(Child) environment_line6: {
 Class, ug_line; 
 Start_Point, Point(environmentX:,environmentY:,0); 
 End_Point, Point(environmentX:,environmentY:,environmentZ:); 
}; 

(Child) environment_line7: {
 Class, ug_line; 
 Start_Point, Point(0,environmentY:,0); 
 End_Point, Point(0,environmentY:,environmentZ:); 
}; 

(Child) environment_line8: {
 Class, ug_line; 
 Start_Point, Point(0,environmentY:,0); 
 End_Point, Point(environmentX:,environmentY:,0); 
}; 

(Child) environment_line9: {
 Class, ug_line; 
 Start_Point, Point(0,environmentY:,environmentZ:); 
 End_Point, Point(environmentX:,environmentY:,environmentZ:); 
}; 

(Child) environment_line10: {
 Class, ug_line; 
 Start_Point, Point(0,0,environmentZ:); 
 End_Point, Point(0,environmentY:,environmentZ:); 
}; 

(Child) environment_line11: {
 Class, ug_line; 
 Start_Point, Point(environmentX:,0,environmentZ:); 
 End_Point, Point(environmentX:,environmentY:,environmentZ:); 
}; 

(Child) environment_line12: {
 Class, ug_line; 
 Start_Point, Point(0,0,environmentZ:); 
 End_Point, Point(environmentX:,0,environmentZ:); 
}; 

#+
-------------EQUIPMENT----------
#-
<EQUIPMENT_COMES_HERE>

#+
-------------PIPE---------------
#-

<PIPES_COMES_HERE>

<PIPE_PATHS_COMES_HERE>

"""
equipmentTemplate = """
(Child) block_<Eq_index>: {
    class, ug_block;
    length, <Eq_L>;
    width, <Eq_W>;
    height, <Eq_H>;
    origin, Point(<Eq_X>,<Eq_Y>,<Eq_Z>);
};

# Body colored depending on the volume of the block
(Child) body_colored_<Eq_index>: { 
    class, ug_body; 
    feature, {block_<Eq_index>:};  
    layer, 1; 
    color, ug_askClosestColor(BLUE); 
};

"""

pipeTemplate ="""
(Child) <pipe_line>: {
    Class, ug_line; 
    Start_Point, Point(<Point_A>); 
    End_Point, Point(<Point_B>); 
}; 
"""

pipePathTemplate = """
(child) <pipe_path_number>: {
  Class, ug_curve_join;
  profile, {<Pipe_Path>};
};
"""

pipeProfileTemplate = """
(child) pipe_profile<profile_num>: {
class, ug_arc;
radius, <pipe_radius>;
start_angle, 0;
end_angle, 360;
center, Point(<start_point>);
#X_Axis, Vector(<X_axis>);
Y_Axis, Vector(<Y_axis>);
};
"""

pipePathTemplate = """
(child) <pipe_path_number>: {
Class, ug_curve_join;
profile, {<Pipe_Path>};
};
"""

pipeClassTemplate = """(child) pipe<pipe_num>: 
{ class, ug_swept;
  guide, {{forward, pipePath<pipePath_num>:}};
  section, {{forward, pipe_profile<pipeProfile_num>:}};
  scaling, {scale_constant, 1};
  alignment_init, parameter;
  orientation, {orientation_fixed};
  tolerances, {0, 0, 0};
};

"""

#Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-piping-system\\" #location
#Torstein = "C:\\Kode\\GitHub\\KBE-piping-system\\" #location
#yourLocation = Torstein #must be changed after whom is using it

endFolder = "GeneratedSystem\\" #folder to store the final dfa files

#gives the direction into the cuboid
def dirIntoEnvironment(point, eq_size): #takes in a point of a eq and the size of the eq and returns the midpoint on the point in world frame
		# point = [x,y,z] rrelative to the equipment -- this is the point
		# =================
		# possible points of a cube
		# (x=0, y, z), (x, y= 0, z), (x,y,z=0)
		# (x=eq_size, y, z), (x, y=eq_size, z), (x,y, z=eq_size)
		# The letter how dont have any nuymber should be between <0,eq_size>
		# ================
		# dirInEq is the direction from the point and into the box
		x = int(point[0])
		y = int(point[1])
		z = int(point[2])

		# finding what point the mid point is on and calculating it in global points
		if(x == 0 and y<int(eq_size[1]) and y>0 and z<int(eq_size[2]) and z>0 ):
			dirInEq = [1,0,0]
		elif (x == int(eq_size[0]) and y<int(eq_size[1]) and y>0 and z<int(eq_size[2]) and z>0):
			dirInEq = [-1,0,0]
		elif (x <int(eq_size[0]) and x>0 and y==0 and z<int(eq_size[2]) and z>0):
			dirInEq = [0,1,0]
		elif (x <int(eq_size[0]) and x>0 and y==int(eq_size[1]) and z<int(eq_size[2]) and z>0):
			dirInEq = [0,-1,0]
		elif (x <int(eq_size[0]) and x>0 and y<int(eq_size[1]) and y>0 and z ==0):
			dirInEq = [0,0,1]
		elif (x <int(eq_size[0]) and x>0 and y<int(eq_size[1]) and y>0 and z == int(eq_size[2])):
			dirInEq = [0,0,-1]
		else:
			dirInEq = [0,0,0]

		return dirInEq

#Takes in data from customer and the final processed path, and overwrites template and appends to a final DFA file				
def makeDFA(num_eq: int, eq_size_list: list, eq_pos: list, eq_in_out: list, env_size: list, startPoint: list, endPoint: list, pipDia: int, custommerInfo: list, path: list, yourLocation:str):
    global templateForPipeSys, equipmentTemplate, endFolder
    
    txt = templateForPipeSys # copy the template

    custommerInfoParams = ['<CUSTOMER_NAME>', '<NUMBER>', '<EMAIL>', '<COMPANY_NAME>']
    for i in range(len(custommerInfo)):
        txt = txt.replace(custommerInfoParams[i], custommerInfo[i])

    customerCompany = custommerInfo[3]
    customerName = custommerInfo[0]
    filename = customerCompany.replace(" ", "") +"_" +customerName.replace(" ", "")
    txt = txt.replace("<customerName_company>", filename)
    
    envParams = ["<envX>", "<envY>", "<envZ>"]
    
    '''CODE FOR ENVIRONMENT BELOW'''
    for i in range(len(envParams)):
        txt = txt.replace(str(envParams[i]), str(env_size[i]))
    

    '''CODE FOR EQUIPMENT BELOW'''
    eqResult =[] # a list with the equipments with inserted values
    for i in range(num_eq):
        eq = equipmentTemplate
        eqResult.append(eq)
        
    # må sette inn eqParams
    for x in range(len(eqResult)):
        eqResult[x] = eqResult[x].replace("<Eq_L>", str(eq_size_list[x][0]))
        eqResult[x] = eqResult[x].replace("<Eq_W>", str(eq_size_list[x][1]))
        eqResult[x] = eqResult[x].replace("<Eq_H>", str(eq_size_list[x][2]))
        eqResult[x] = eqResult[x].replace("<Eq_X>", str(eq_pos[x][0]))
        eqResult[x] = eqResult[x].replace("<Eq_Y>", str(eq_pos[x][1]))
        eqResult[x] = eqResult[x].replace("<Eq_Z>", str(eq_pos[x][2]))
        eqResult[x] = eqResult[x].replace("<Eq_index>", str(x+1))
    
    joinedEquipmentsCode =""
    for i in range(len(eqResult)):
        joinedEquipmentsCode += eqResult[i]
    
    # inserting the code for the equipments in the dfaCode
    txt = txt.replace("<EQUIPMENT_COMES_HERE>", joinedEquipmentsCode)
    
    '''CODE FOR PIPE BELOW'''
    # path = [[path1],[path2],[path3],[path4]]
    pipeResult = []

    # adds a template for each pipe element to the pipeResult
    for i in range(len(path)):
        for j in range(len(path[i])-1):
            pipeResult.append(pipeTemplate)

    # strips the point to x,y,z and overwrites pipeTemplate
    counter = 0
    pipe_list = []
    for localPath in path:
        pipe_string = ""
        for point in range(len(localPath)-1):
            pointStringA = str(localPath[point])
            pointStringA = pointStringA.strip("[")
            pointStringA = pointStringA.strip("]")
            pipeResult[counter] = pipeResult[counter].replace("<Point_A>",pointStringA)

            pointStringB = str(localPath[point+1])
            pointStringB = pointStringB.strip("[")
            pointStringB = pointStringB.strip("]")
            pipeResult[counter] = pipeResult[counter].replace("<Point_B>",pointStringB)

            pipeResult[counter] = pipeResult[counter].replace("<pipe_line>", "pipe_number_"+str(counter))
            
            pipe_string += "pipe_number_"+str(counter)+":,"

            counter += 1
        pipe_string = pipe_string[:-1]
        pipe_list.append(pipe_string)
        
    joinedPipesCode=""
    for i in range(len(pipeResult)):
        joinedPipesCode += pipeResult[i]

    txt = txt.replace("<PIPES_COMES_HERE>", joinedPipesCode)
    
    # making the pipe profile
    pipe_profile = ""
    counter = 0
    counter_out_side = -1
    for i in range(len(path)):
        pipe_radius = pipeDia * 25.4/2
        pipeProfile = pipeProfileTemplate
        pipeProfile = pipeProfile.replace("<pipe_radius>",str(pipe_radius))
        pipeProfile = pipeProfile.replace("<profile_num>",str(counter))

        if i == 0:
            pointVariable = path[i][0]
            Y_axis = str(dirIntoEnvironment(pointVariable,env_size))
        else:
            pointVariable = path[i][0]
            Y_axis = str(dirIntoEnvironment(pointVariable,eq_size_list[i-1]))

        pointVariable = str(pointVariable).strip("[")
        pointVariable = pointVariable.strip("]")
        pointVariable = pointVariable.replace("'","")
        pipeProfile = pipeProfile.replace("<start_point>",pointVariable)
        Y_axis = Y_axis.strip("[")
        Y_axis = Y_axis.strip("]")
        pipeProfile = pipeProfile.replace("<Y_axis>",Y_axis)

        pipe_profile += pipeProfile
        counter += 1
        counter_out_side +=2

    txt = txt.replace("<PIPE_PROFILE_COMES_HERE>", pipe_profile)

    pipe_class = ""
    for i in range(len(path)):
        pipeClass = pipeClassTemplate
        pipeClass = pipeClass.replace("<pipe_num>",str(i))
        pipeClass = pipeClass.replace("<pipePath_num>",str(i))
        pipeClass = pipeClass.replace("<pipeProfile_num>",str(i))
        pipe_class += pipeClass

    txt = txt.replace("<PIPE_CLASS_COMES_HERE>", pipe_class)

    # making a sammenhengende strek av alle linjene
    pipePaths = ""
    for i in range(len(pipe_list)):
        pipeLine = pipePathTemplate
        pipeLine = pipeLine.replace("<pipe_path_number>", "pipePath"+str(i))
        pipeLine = pipeLine.replace("<Pipe_Path>", pipe_list[i])
        pipePaths += pipeLine
    
    txt = txt.replace("<PIPE_PATHS_COMES_HERE>", pipePaths)

    f = open(yourLocation + endFolder + "PipeSys_"+filename+".dfa", "w")
    f.write(txt)
    f.close()

    return "PipeSys_"+filename+".dfa"

    
        
    
# testing environment
num_eq = 3
eq_size_list = [[200,100,300],[150,200,300],[300,300,300]]
eq_pos = [[500,500,500],[2000,1000,1000], [3000,2000,2500]]
env_size = [4000,4000,4000]
eq_in_out = [[0,35,35], [70,100,35],[0,75,75],[150,75,75],[0,250,250],[250,250,300]]
startPoint = [0,1500,1500]
endPoint = [4000, 2000,2000]
pipeDia =  2
#path = #sett inn path og poinst list type
customerName = "Aase"
customerCompany = "TorAS"
#path = [[[0,0,0],[100,100,100],[100,200,200]],[[200,200,200],[300,300,300],[300,400,400]],[[400,400,400],[500,500,500],[600,500,500]],[[600,600,600],[700,600,600],[700,700,700]]]
path = [[[0.0, 1480.0, 1480.0], [40.0, 1440.0, 1440.0], [80.0, 1400.0, 1400.0], [120.0, 1360.0, 1360.0], [120.0, 1320.0, 1320.0], [160.0, 1280.0, 1280.0], [160.0, 1240.0, 1240.0], [200.0, 1200.0, 1200.0], [200.0, 1160.0, 1160.0], [240.0, 1120.0, 1120.0], [240.0, 1080.0, 1080.0], [240.0, 1040.0, 1040.0], [280.0, 1000.0, 
1000.0], [280.0, 960.0, 960.0], [320.0, 920.0, 920.0], [320.0, 880.0, 880.0], [360.0, 840.0, 840.0], [360.0, 800.0, 800.0], [400.0, 760.0, 760.0], [400.0, 720.0, 720.0], [400.0, 680.0, 720.0], [440.0, 640.0, 680.0], [440.0, 600.0, 680.0], [480.0, 560.0, 640.0], [480.0, 520.0, 640.0]], [[600.0, 600.0, 640.0], [640.0, 600.0, 640.0], [680.0, 600.0, 640.0], [720.0, 600.0, 640.0], [760.0, 600.0, 640.0], [800.0, 600.0, 640.0], [840.0, 600.0, 640.0], [880.0, 600.0, 640.0], 
[920.0, 600.0, 640.0], [960.0, 640.0, 680.0], [1000.0, 640.0, 680.0], [1040.0, 680.0, 720.0], [1080.0, 680.0, 720.0], [1120.0, 720.0, 760.0], [1160.0, 720.0, 760.0], [1200.0, 720.0, 760.0], [1240.0, 760.0, 800.0], [1280.0, 760.0, 800.0], [1320.0, 800.0, 840.0], [1360.0, 800.0, 840.0], [1400.0, 840.0, 880.0], [1440.0, 840.0, 880.0], [1480.0, 840.0, 880.0], [1520.0, 880.0, 920.0], [1560.0, 880.0, 920.0], [1600.0, 920.0, 960.0], [1640.0, 920.0, 960.0], [1680.0, 960.0, 1000.0], [1720.0, 960.0, 1000.0], [1760.0, 960.0, 1000.0], [1800.0, 1000.0, 1040.0], [1840.0, 1000.0, 1040.0], [1880.0, 1040.0, 1080.0], [1920.0, 1040.0, 1080.0], [1960.0, 1040.0, 1080.0], [2000.0, 1080.0, 1120.0]], [[2120.0, 1080.0, 1120.0], [2160.0, 1120.0, 1160.0], [2200.0, 1160.0, 1200.0], [2240.0, 1200.0, 1240.0], [2280.0, 1240.0, 1280.0], [2320.0, 1280.0, 1320.0], [2360.0, 1320.0, 1360.0], [2400.0, 1360.0, 1400.0], [2440.0, 1400.0, 1440.0], [2480.0, 1440.0, 1480.0], [2520.0, 1480.0, 1520.0], [2560.0, 1520.0, 1560.0], [2600.0, 1560.0, 1600.0], [2640.0, 1600.0, 1640.0], [2640.0, 1640.0, 1680.0], [2640.0, 1680.0, 1720.0], [2680.0, 1720.0, 1760.0], [2680.0, 1720.0, 1800.0], [2680.0, 1720.0, 1840.0], [2720.0, 1760.0, 1880.0], [2720.0, 1760.0, 1920.0], [2760.0, 1800.0, 1960.0], [2760.0, 1800.0, 2000.0], [2760.0, 1840.0, 2040.0], [2760.0, 1840.0, 2080.0], [2800.0, 1880.0, 2120.0], [2800.0, 1880.0, 2160.0], [2840.0, 1920.0, 2200.0], [2840.0, 1920.0, 2240.0], [2880.0, 1960.0, 2280.0], [2880.0, 1960.0, 2320.0], [2880.0, 2000.0, 2360.0], [2880.0, 2000.0, 2400.0], [2920.0, 2040.0, 2440.0], [2920.0, 2040.0, 2480.0], [2960.0, 2080.0, 2520.0], [2960.0, 2080.0, 2560.0], [3000.0, 2120.0, 2600.0], [3000.0, 2120.0, 2640.0]], [[3120.0, 2120.0, 2800.0], [3160.0, 2120.0, 2760.0], [3200.0, 2120.0, 2720.0], [3240.0, 2120.0, 2680.0], [3280.0, 2120.0, 2640.0], [3320.0, 2120.0, 2600.0], [3360.0, 2120.0, 2560.0], [3400.0, 2120.0, 2520.0], [3440.0, 2120.0, 2480.0], [3480.0, 2120.0, 2440.0], [3520.0, 2120.0, 2400.0], [3560.0, 2120.0, 2360.0], [3600.0, 2120.0, 2320.0], 
[3640.0, 2120.0, 2280.0], [3680.0, 2120.0, 2240.0], [3720.0, 2120.0, 2200.0], [3760.0, 2080.0, 2160.0], [3800.0, 2080.0, 2120.0], [3840.0, 2040.0, 2080.0], [3880.0, 2040.0, 2040.0], [3920.0, 2000.0, 2000.0], [3960.0, 2000.0, 2000.0]]]

#makeDFA(num_eq, eq_size_list, eq_pos,eq_in_out, env_size, startPoint, endPoint, pipeDia, customerName, customerCompany, path)