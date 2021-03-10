s.wfile.write(bytes("<!DOCTYPE html><html><head>", 'utf-8'))
s.wfile.write(bytes("<title>Piping system optimization</title>", 'utf-8'))
s.wfile.write(bytes("</head><body style="'background-color:#26b6d9;'">", 'utf-8'))
s.wfile.write(bytes("<h1>System parameters</h1>", 'utf-8'))
s.wfile.write(bytes("<p>Welcome to our optimization tool, please write in your system constrains, all values are in millimeters [mm]</p>", 'utf-8'))

s.wfile.write(bytes("<form action='/orderDesign' method='post'>", 'utf-8'))

#table for environment and pipe
s.wfile.write(bytes("<h3>Define environment and pipe </h3>", 'utf-8'))
s.wfile.write(bytes("<table><tr>", 'utf-8'))
s.wfile.write(bytes('<th><label for="envSize">Enviroment side [mm]:</label></th>', 'utf-8'))
s.wfile.write(bytes('<th><label for="startPointA">Starting point, A:</label></th>', 'utf-8'))
s.wfile.write(bytes('<th><label for="endPointB">End point, B:</label></th>', 'utf-8'))
s.wfile.write(bytes('<th><label for="pipSize">Pipe size [inches]:</label></th></tr>', 'utf-8'))

s.wfile.write(bytes('<tr><td><input type="text" id="envSize" name="envSize" value="400"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="startA" name="startA" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="endB" name="endB" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><select id="pipe_dia" name="pipe_dia">', 'utf-8'))
s.wfile.write(bytes('<option value="2">2''</option>', 'utf-8'))
s.wfile.write(bytes('<option value="4">4''</option>', 'utf-8'))
s.wfile.write(bytes('<option value="6">6''</option>', 'utf-8'))
s.wfile.write(bytes('</select> </td></tr></table>', 'utf-8'))

#table for eq.
s.wfile.write(bytes('<h3>Define equipment</h3>', 'utf-8'))
s.wfile.write(bytes('<table style="width:70%"><tr>', 'utf-8'))
s.wfile.write(bytes('<th>Equipment number:</th>', 'utf-8'))
s.wfile.write(bytes('<th>Cuboid side [mm]</th> ', 'utf-8'))
s.wfile.write(bytes('<th>Location in enviroment</th>', 'utf-8'))
s.wfile.write(bytes('<th>Input pose relative to eq:</th>', 'utf-8'))
s.wfile.write(bytes('<th>Output pose relative to eq:</th></tr>', 'utf-8'))

#values for eq1
s.wfile.write(bytes('<tr><td><label for="eq1">eq1:</label><br></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq1_side" name="eq1_side" value="300"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq1_pos" name="eq1_pos" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq1_in" name="eq1_in" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq1_out" name="eq1_out" value="x,y,z"></td></tr>', 'utf-8'))

#values for eq2
s.wfile.write(bytes('<tr><td><label for="eq2">eq2:</label><br></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq2_side" name="eq2_side" value="500"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq2_pos" name="eq2_pos" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq2_in" name="eq2_in" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq2_out" name="eq2_out" value="x,y,z"></td></tr>', 'utf-8'))

#values for eq3
s.wfile.write(bytes('<tr><td><label for="eq3">eq3:</label><br></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq3_side" name="eq3_side" value="400"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq3_pos" name="eq3_pos" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq3_in" name="eq3_in" value="x,y,z"></td>', 'utf-8'))
s.wfile.write(bytes('<td><input type="text" id="eq3_out" name="eq3_out" value="x,y,z"></td></tr></table>', 'utf-8'))

#end of inputvalues
s.wfile.write(bytes('<br><br>', 'utf-8'))
s.wfile.write(bytes('<input type="submit" value="Submit"></form></body></html>', 'utf-8'))


s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
s.wfile.write(bytes('', 'utf-8'))
  

  
    
    
    
    



