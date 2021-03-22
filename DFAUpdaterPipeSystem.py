#dfaUpdater to pipeSystemDesigner

"""
				Vi må få kundens parametere på formen (på en sofistikert måte):
				num_eq = int
				eq_size_list = [eq1_size, eq2_size, eq3_size]
				eq_pos = [eq1_pos, eq2_pos, eq3_pos]
				eq_in_out = [eq1_in, eq1_out, eq2_in, eq2_out, eq3_in, eq3_out] #siden rørene skal gå inn og ut på
				env_size = [x,y,z] #lengden på kuben som definerer environmentet
				startPoint = [x,y,z]
				endpoint = [x,yz]
				num_node_ax = int # denne kan vi definere selv øverst i skriptet eller noe
				pipDia = float 
				"""
# def makeDFA(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, num_node_ax, pipDia):

templateForPipeSys = """#! NX/KF 4.0
DefClass: PipeSys_<customerName_company> (ug_base_part);
    #(number parameter) environmentX: <envX>;
    #(number parameter) environmentY: <envY>;
    #(number parameter) environmentZ: <envZ>; 

    
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

<PIPES_COMES_HERE>

# Methods of the class
(Method Number) getVolume:(Number $length, Number $width, Number $height) 
  @{
     $length * $width * $height;
   };

"""
equipmentTemplate = """(child) block_<Eq_index>: 
    {
        class, ug_block;
        length, <Eq_L>;
        width, <Eq_W>;
        height, <Eq_H>;
		Origin, Point(<Eq_X>,<Eq_Y>,<Eq_Z>);
    };

    # Body colored depending on the volume of the block
    (Child) body_colored_<Eq_index>: 
    { 
      Class, ug_body; 
      Feature, {block_<Eq_index>:};  
      Layer, 1; 
      color, ug_askClosestColor(BLUE); 
    };

    #Inlet, #Outlet

    """
    
pipeTemplate ="""Write it here"""


Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-piping-system\\" #location
yourLocation = Aashild #must be changed after whom is using it
				
def makeDFA(num_eq, eq_size_list, eq_pos, env_size, startPoint, endPoint, pipDia, customerName, customerCompany):
    global templateForPipeSys, equipmentTemplate, yourLoaction
    # kopierer block for antall equipment
    
    templatePath = yourLoaction + "template\\piping_system_template_test123.dfa"
    
    txt = templateForPipeSys
    print("before:", txt)
    envParams = ["<envX>", "<envY>", "<envZ>"]
    
    for i in range(len(envParams)):
        txt = txt.replace(envParams[i], env_size[i])
    print("Inserted evironment params \n:", txt)
    
    eqResult =[] # a list with the equipments with inserted values
    for i in range num_eq:
        eq = equipmentTemplate
        eqResult.append(eq)
        
    # må sette inn eqParams
    
    
    joinedEquipmentsCode =""
    for i in range(len(eqResult)):
        joinedEquipmentsCode += eqResult[i]
    
    # inserting the code for the equipments in the dfaCode
    txt = txt.replace("<EQUIPMENT_COMES_HERE>", joinedEquipmentsCode)
    
    #sette inn pipes
    pipeResult = []
    
    for i in range(len(
    txt = txt.replace("<PIPES_COMES_HERE>", joinedPipesCode)
    
        
    
