#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import json
import math
import random
from checkData import checkCustomerInput



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
            startPage = open("HTML/startPage.HTML", 'r')
            startPageText = startPage.read()
            s.wfile.write(bytes(startPageText, 'utf-8'))
            
        elif path.find("/static/style2.css") != -1: # to handle the css
            # thanks to: https://stackoverflow.com/questions/28369758/python-not-finding-css-file
            stylefile = open("static/style2.css", "r")
            tekst = stylefile.read()
            s.wfile.write(bytes(tekst, 'utf-8'))
        elif path.find("/orderDesign") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            userInterface = open("HTML/userInterface.html", "r") #reading the userinterface html-page
            UItext = userInterface.read()

            # changing the params displayed
            for i in range(len(variablesToReplace)):
                UItext = UItext.replace(variablesToReplace[i], str(custom_parameters[i])) # the data about the pipe-env

            for i in range(len(custommerInfoToChange)):
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i])) # the data about the custommer

            s.wfile.write(bytes(UItext, 'utf-8')) # writing to the local host

        elif path.find("/yourParameters") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            userInterface = open("HTML/userInterface.html", "r") #reading the userinterface html-page
            UItext = userInterface.read()

            # changing the params displayed
            for i in range(len(variablesToReplace)):
                if custom_parameters[i].find("%2C"):
                    custom_parameters[i] = custom_parameters[i].replace("%2C", ",") #taking care of the ","
                UItext = UItext.replace(variablesToReplace[i], str(custom_parameters[i])) # the data about the pipe-env
            
            for i in range(len(custommerInfoToChange)):
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i])) # the data about the customme

            s.wfile.write(bytes(UItext, 'utf-8')) # writing to the local host

        elif path.find("/sendOrder") != -1:
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            
            orderAcceptedMsg = open("HTML/orderAccepted.html", 'r')
            orderMsgText = orderAcceptedMsg.read()
            s.wfile.write(bytes(orderMsgText, 'utf-8'))# writing to the local host
            

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
            print("param line", param_line)
            #param line envSizeX=1000&envSizeY=3000&envSizeZ=4000&startA=0%2C1500%2C2000&endB=1000%2C1500%2C2000&pipe_dia=6&
            # eq1_sideX=500&eq1_sideY=500&eq1_sideZ=500&eq1_pos=500%2C500%2C500&eq1_in=0%2C250%2C250&eq1_out=500%2C250%2C250&eq2_sideX=300&eq2_sideY=300&eq2_sideZ=300&eq2_pos=300%2C700%2C500&eq2_in=0%2C150%2C150&eq2_out=300%2C150%2C150&eq3_sideX=700&eq3_sideY=700&eq3_sideZ=700&eq3_pos=700%2C1500%2C2000&eq3_in=0%2C350%2C350&eq3_out=700%2C350%2C350

			#making a string to print
            global print_order, yourLocation
            print_order = ""

            if param_line.find("%2C"): # replacing "%2C" with ','
                param_line = param_line.replace("%2C", ',')
			#getting the parameter values
            key_val_pair = param_line.split('&')							#splitting the string at "&"
            print("key_val_pair: ", key_val_pair)
            for i in range(len(custom_parameters)): 						#itterating through the custom_parameter list
                print_order += str(custom_parameters[i]) 					#before changing the parameters, adding the to a string for printing
                print_order +=": "										#for a nice print
                custom_parameters[i] = key_val_pair[i].split('=')[1]		#spliting at "=" to only get the value
                if ' ' in custom_parameters[i]: 							#the last parameter has "HTTP/1.1" and we dont want it
                    custom_parameters[i] = custom_parameters[i].split(" ")[0] #spliting to get rid of it ^
                    print_order += str(custom_parameters[i])
                print_order += ", "
            print("custom_parameters: ", custom_parameters)
            print("string split: ", print_order)

            # getting the data arranged i a sensable way
            env_size =[]
            startPoint = []
            endPoint = []
            pipDia = 0
            
            eq_size_list = []
            eq_pos = []
            eq_in_out = []
            
            num_eq = 3 # hardcoded
            num_node_ax = 0 # hardcoded

            # from reading the param line we know that the 6 first parameters are for the environment, 
            # then the 6 next params are for eq1, the 6 params after that for eq2, and so on

            # mulig disse må castes til int
            env_size = [custom_parameters[0], custom_parameters[1], custom_parameters[2]]
            startPoint = list(custom_parameters[3].split(","))
            endPoint = list(custom_parameters[4].split(","))
            pipDia = int(custom_parameters[5])

            for i in range(6,len(custom_parameters),6):
                eq_size_eqN = [custom_parameters[i], custom_parameters[i+1], custom_parameters[i+2]] # size of equipment number N
                eq_size_list.append(eq_size_eqN)

                eq_pos_eqN = list(custom_parameters[i+3].split(",")) # position of equipment number N
                eq_pos.append(eq_pos_eqN)

                eq_in_eqN = list(custom_parameters[i+4].split(",")) # in position of the pip on equipment number N (relative to equipment)
                eq_in_out.append(eq_in_eqN)

                eq_out_eqN = list(custom_parameters[i+5].split(",")) # out position of the pip on equipment number N (relative to equipment)
                eq_in_out.append(eq_out_eqN)

            print("env_size: ", env_size)
            print("startPoint: ", startPoint)
            print("endPoint: ", endPoint)
            print("pipDia: ", pipDia)
            print("eq_size_list: ", eq_size_list)
            print("eq_pos: ", eq_pos)
            print("eq_in_out: ", eq_in_out)

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
            
			# check if input is valid
            errorMsg = checkCustomerInput(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, num_node_ax, pipDia)
            print("Check if the input is valid: ", errorMsg)

            for i in errorMsg:
                if not i.find("ok"):
                    #be brukeren skrive inn på nytt og gi tilbakemelding på hva som er feil. 
                    # send brukeren til yourParameters"
                    ...

            # take oicture of the drawCustomerInfo
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

 
if __name__ == '__main__':

	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()