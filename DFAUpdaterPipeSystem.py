#dfaUpdater to pipeSystemDesigner

templateForPipeSys = """#! NX/KF 4.0
DefClass: PipeSys_<customerName_company> (ug_base_part);
    (number parameter) environmentX: <envX>;
    (number parameter) environmentY: <envY>;
    (number parameter) environmentZ: <envZ>; 

    
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

<EQUIPMENT_COMES_HERE>
"""
equipmentTemplate = """(Child) block_<Eq_index>: {
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
    
pipeTemplate ="""Write it here"""


Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-piping-system\\" #location
Torstein = "C:\\Kode\\GitHub\\KBE-piping-system\\" #location
yourLocation = Torstein #must be changed after whom is using it

endFolder = "GeneratedSystem\\" #folder to store the final dfa files
				
def makeDFA(num_eq: int, eq_size_list: list, eq_pos: list, env_size: list, startPoint: list, endPoint: list, pipDia: int, customerName: str, customerCompany: str, path: list):
    global templateForPipeSys, equipmentTemplate, yourLoaction, endFolder
    # kopierer block for antall equipment
    
    filename = customerCompany +"_" +customerName
    
    txt = templateForPipeSys
    print("before:", txt)
    txt = txt.replace("<customerName_company>", filename)
    envParams = ["<envX>", "<envY>", "<envZ>"]
    
    for i in range(len(envParams)):
        txt = txt.replace(str(envParams[i]), str(env_size[i]))
    print("Inserted evironment params \n:", txt)
    
    eqResult =[] # a list with the equipments with inserted values
    for i in range(num_eq):
        eq = equipmentTemplate
        eqResult.append(eq)
        
    # må sette inn eqParams
    for x in range(len(eqResult)):
        eqResult[x] = equipmentTemplate.replace("<Eq_L>", str(eq_size_list[x][0]))
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
    
    #sette inn pipes
    pipeResult = [] #må endres!!

    #txt = txt.replace("<PIPES_COMES_HERE>", joinedPipesCode)

    print("done dfa file:", txt)

    f = open(yourLocation + endFolder + "PipeSys_"+filename+".dfa", "w")
    f.write(txt)
    f.close()

    
        
    
# testing environment
num_eq = 3
eq_size_list = [[70,70,70],[150,150,150],[1000,1000,1000]]
eq_pos = [[50,50,50],[150,150,150], [1000,1000,1000]]
env_size = [3000,3000,3000]
eq_in_out = [[0,35,35], [70,35,35],[0,75,75],[150,75,75],[0,500,500],[1000,500,500]]
startPoint = [0,1500,1500]
endPoint = [3000, 1500,1500]
pipeDia =  2
#path = #sett inn path og poinst list type
customerName = "torstein"
customerCompany = "TorAS"
path = [0,0,0]

makeDFA(num_eq, eq_size_list, eq_pos, env_size, startPoint, endPoint, pipeDia, customerName, customerCompany, path)