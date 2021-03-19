#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import json
import math
import random
import codecs
#import css


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
envSizeX="x"
envSizeY="y"
envSizeZ="z"
startA="x,y,z" #x%2Cy%2Cz
endB="x,y,z" #x%2Cy%2Cz
pipe_dia= "2''"
eq1_sideX= "x"
eq1_sideY= "y"
eq1_sideZ= "z"
eq1_pos="x,y,z" #x%2Cy%2Cz
eq1_in="x,y,z" #x%2Cy%2Cz
eq1_out= "x,y,z" #x%2Cy%2Cz
eq2_sideX= "x"
eq2_sideY= "y"
eq2_sideZ= "z"
eq2_pos= "x,y,z" #x%2Cy%2Cz
eq2_in= "x,y,z" #x%2Cy%2Cz
eq2_out= "x,y,z" #x%2Cy%2Cz
eq3_sideX= "x"
eq3_sideY= "y"
eq3_sideZ= "z"
eq3_pos= "x,y,z" #x%2Cy%2Cz
eq3_in= "x,y,z" #x%2Cy%2Cz
eq3_out= "x,y,z" #x%2Cy%2Cz

#Info about the customer:
name= "Your Name"
pNumber= "Your number"
eMail= "Your e-mail"
compName= "Your company"

custom_parameters = [envSizeX, envSizeY, envSizeZ, startA, endB, pipe_dia, eq1_sideX, eq1_sideY, eq1_sideZ, eq1_pos, eq1_in, eq1_out, eq2_sideX, eq2_sideY, eq2_sideZ, eq2_pos, eq2_in, eq2_out, eq3_sideX, eq3_sideY, eq3_sideZ, eq3_pos, eq3_in, eq3_out] 
custommerInfo = [name, pNumber, eMail, compName]

custommerInfoToChange = ['#name#', '#pNumber#', '#eMail#', '#compName#']
variablesToReplace = ['#envSizeX#', '#envSizeY#', '#envSizeZ#', '#startA#', '#endB#', '#pipe_dia#', '#eq1_sideX#', '#eq1_sideY#', '#eq1_sideZ#', '#eq1_pos#', '#eq1_in#','#eq1_out#', '#eq2_sideX#', '#eq2_sideY#', '#eq2_sideZ#', '#eq2_pos#', '#eq2_in#', '#eq2_out#', '#eq3_sideX#', '#eq3_sideY#', '#eq3_sideZ#', '#eq3_pos#', '#eq3_in#', '#eq3_out#']


resultQuery = False

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):


    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()


    def do_GET(s):
        global custom_parameters, custommerInfo, variablesToReplace, custommerInfoToChange
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
        elif path.find("/static/style2.css") != -1: # to handle the css
            # thanks to: https://stackoverflow.com/questions/28369758/python-not-finding-css-file
            stylefile = open("static/style2.css", "r")
            tekst = stylefile.read()
            s.wfile.write(bytes(tekst, 'utf-8'))
        elif path.find("/orderDesign") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            userInterface = open("userInterface.html", "r")
            UItext = userInterface.read()

            # changing the params displayed
            
            for i in range(len(variablesToReplace)):
                UItext = UItext.replace(variablesToReplace[i], str(custom_parameters[i]))
            
            
            for i in range(len(custommerInfoToChange)):
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i]))

            s.wfile.write(bytes(UItext, 'utf-8'))

        elif path.find("/yourParameters") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            userInterface = open("userInterface.html", "r")
            UItext = userInterface.read()

            for i in range(len(variablesToReplace)):
                if custom_parameters[i].find("%2C"):
                    custom_parameters[i] = custom_parameters[i].replace("%2C", ",")
                UItext = UItext.replace(variablesToReplace[i], str(custom_parameters[i]))
            
            for i in range(len(custommerInfoToChange)):
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i]))

            s.wfile.write(bytes(UItext, 'utf-8'))

        elif path.find("/sendOrder") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            
            # make a html-form for this 
            # Thank you for your order! A consulent in Aker Solution will soon get in thouch with you!

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
                """
				Vi må få kundens parametere på formen (på en sofistikert måte):
				num_eq = int
				eq_size_list = [eq1_size, eq2_size, eq3_size]
				eq_pos = [eq1_pos, eq2_pos, eq3_pos]
				eq_in_out = [eq1_in, eq1_out, eq2_in, eq2_out, eq3_in, eq3_out] #siden rørene skal gå inn og ut på
				env_size = int #lengden på kuben som definerer environmentet
				startPoint = [x,y,z]
				endpoint = [x,yz]
				num_node_ax = int # denne kan vi definere selv øverst i skriptet eller noe
				pipDia = float 
				"""
            print("string split: ", print_order)
				# check if input is valid

				#if not valid print beskjed, og la brukeren skrive inn nye verdier uten at de gamle forsvinner
            s.do_GET() #this is not a optimal solution

        if path.find("/sendOrder") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            
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