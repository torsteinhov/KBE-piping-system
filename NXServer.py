#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import json
import math
import random
import css
#import style2

'''
from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere
from shapes.Cone import Cone
'''

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234

Torstein = "C:\\Kode\\GitHub\\KBE-piping-system\\" #location
Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\\\KBE-piping-system\\" #location
yourLocation = Torstein #must be changed after whom is using it

#defining parameters to be changed by the custommer
point_A = "starting point"
point_B = "end point"
pipe_dia = "pipe diameter"
eq1_size = "Equipment number 1 size"
eq1_point = "Equipment number 1 location"
eq2_size = "Equipment number 2 size"
eq2_point = "Equipment number 2 location"
eq3_size = "Equipment number 3 size"
eq3_point = "Equipment number 3 location"


custom_parameters = [point_A,point_B,pipe_dia,eq1_size,eq1_point,eq2_size,eq2_point,eq3_size,eq3_point] 

resultQuery = False

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):


	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()


	def do_GET(s):

		global point_A,point_B,pipe_dia,eq1_size,eq1_point,eq2_size,eq2_point,eq3_size,eq3_point

		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		
		if path.find("/") != -1 and len(path) == 1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title><style><link rel="stylesheet" type="text/css" href="style.css" media="screen"/></style></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/orderDesign") != -1:
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			s.wfile.write(bytes('<!DOCTYPE html><html><head>', 'utf-8'))
			
			#s.wfile.write(bytes('<title>Piping system optimization</title><link rel="stylesheet"  href="{{ url_for( filename="style2.css")}}"/>', 'utf-8'))
			s.wfile.write(bytes('<title>Piping system optimization</title><link rel="stylesheet"  href="style.css"/>', 'utf-8'))
			s.wfile.write(bytes('</head><body>', 'utf-8')) #style="'background-color:#26b6d9;'"
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

			"""
			#starting point
			s.wfile.write(bytes("<label for='point_A'>Starting point for the pipe [x,y,z] (drop the brackets, separate with comma): </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='point_A' name='point_A' value=" + str(point_A) +"><br><br>", 'utf-8'))
            #end point
			s.wfile.write(bytes("<label for='point_B'>End point for the pipe [x,y,z] (drop the brackets, separate with comma): </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='point_B' name='point_B' value=" + str(point_B) + "><br><br><br>", 'utf-8'))
            #eq1_size
			s.wfile.write(bytes("<h3>Equipment 1</h3><label for='eq1_size'>Equipment number 1 [mm] (cubloid): </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='eq1_size' name='eq1_size' value=" + str(eq1_size) + "><br><br>", 'utf-8'))
            #eq1_point
			s.wfile.write(bytes("<label for='eq1_point'>Equipment number 1 [x,y,z] location: </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='eq1_point' name='eq1_point' value=" + str(eq1_point) + "><br><br><br>", 'utf-8'))
            #eq2_size
			s.wfile.write(bytes("<h3>Equipment 2</h3><label for='eq2_size'>Equipment number 2 [mm] (cubloid): </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='eq2_size' name='eq2_size' value=" + str(eq2_size) + "><br><br>", 'utf-8'))
            #eq2_point
			s.wfile.write(bytes("<label for='eq2_point'>Equipment number 2 [x,y,z] location: </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='eq2_point' name='eq2_point' value=" + str(eq2_point) + "><br><br><br>", 'utf-8'))
            #eq3_size
			s.wfile.write(bytes("<h3>Equipment 3</h3><label for='eq3_size'>Equipment number 3 [mm] (cubloid): </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='eq3_size' name='eq3_size' value=" + str(eq3_size) + "><br><br>", 'utf-8'))
            #eq3_point
			s.wfile.write(bytes("<label for='eq3_point'>Equipment number 3 [x,y,z] location: </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='eq3_point' name='eq3_point' value=" + str(eq3_point) + "><br><br><br>", 'utf-8'))
			
			#pipe diameter option boxes
			s.wfile.write(bytes("<label for='pipe_dia'> Pipe diameter [inches]: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='pipe_dia' name='pipe_dia'>", 'utf-8'))
			s.wfile.write(bytes("<option value='2'>2''</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='4'>4''</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='6'>6''</option>", 'utf-8'))  
			s.wfile.write(bytes("</select> <br><br>", 'utf-8'))  
			"""
			#s.wfile.write(bytes("</fieldset><br>", 'utf-8'))
			s.wfile.write(bytes("<p>Click 'Submit' to design an optimized piping system", 'utf-8'))
			s.wfile.write(bytes("<input type='submit' value='Submit'></p>", 'utf-8'))
			s.wfile.write(bytes("</p>", 'utf-8'))
			s.wfile.write(bytes('</form>', 'utf-8'))
			s.wfile.write(bytes('</body></html>', 'utf-8'))

		elif path.find("/yourParameters") != -1:
			s.wfile.write(bytes('<html><body style="background-color:#FFD07E;"><h3>Piping system</h3>', 'utf-8'))
			s.wfile.write(bytes('<form action="/yourParameters" method="post">', 'utf-8'))
			s.wfile.write(bytes('<p>The following parameters line has arrived: ' + print_order +'</p>', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		elif path.find("/info") != -1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title><meta http-equiv="refresh" content="3"></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Info: Hello!.</p>" + str(i), "utf-8"))
			s.wfile.write(bytes('"</body></html>', "utf-8"))
			
	def do_POST(s):
		#allowing us to edit the custom parameters
		global custom_parameters

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		if path.find("/yourParameters") != -1:
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()

			#making a string to print
			global print_order, yourLocation
			print_order = ""
			#getting the parameter values
			key_val_pair = param_line.split('&')							#splitting the string at "&"
			for i in range(len(custom_parameters)): 						#itterating through the custom_parameter list
				print_order += str(custom_parameters[i]) 					#before changing the parameters, adding the to a string for printing
				print_order +=": "										#for a nice print
				custom_parameters[i] = key_val_pair[i].split('=')[1]		#spliting at "=" to only get the value
				if ' ' in custom_parameters[i]: 							#the last parameter has "HTTP/1.1" and we dont want it
					custom_parameters[i] = custom_parameters[i].split(" ")[0] #spliting to get rid of it ^
				print_order += str(custom_parameters[i])
				print_order += ", "

			s.do_GET() #this is not a optimal solution

		if path.find("/"):
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			s.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))

#IMPLEMENTATION WILL COME, FOR NOW LOGIC IS MADE IN systemDesigner.py
class makeSystem: 

    def __init__(self):

    #Cylinder(x, y, z, diameter, height, direction, color, material)
    #Cone(x, y, z, baseDiameter, topDiameter, height, direction, color, material)
        '''
        def run_model(self):
            return -1
        '''
        
	

 
if __name__ == '__main__':

	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()