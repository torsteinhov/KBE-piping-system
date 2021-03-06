#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import json
import math
import random

from checkData import checkCustomerInput
from DFAUpdaterPipeSystem import makeDFA
import pathInterpreter

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234

Torstein = "C:\\Kode\\GitHub\\KBE-piping-system\\" #location
Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\KBE-piping-system\\" #location
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

messageToCustomer ="" # error message to the customer about typos

#Info about the customer:
name= "Ola Nordmann"
pNumber= "12345678"
eMail= "ola.nordmann@mail.com"
compName= "Nordmann AS"

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
            stylefile = open("HTML/static/style2.css", "r")
            tekst = stylefile.read()
            s.wfile.write(bytes(tekst, 'utf-8'))

        elif path.find("Aker_Solutions.png") != -1:
			#Make right headers
            #s.send_response(200)
            #s.send_header("Content-type", "image/png")
            #s.end_headers()
			#Read the file
			#Write file.
            bReader = open(yourLocation + "HTML\\webImg\\"+"Aker_Solutions.png", "rb")
            theImg = bReader.read()
            s.wfile.write(theImg)
            
        elif path.find("search_50px.png") != -1:
			#Make right headers
            #s.send_response(200)
            #s.send_header("Content-type", "image/png")
            #s.end_headers()
			#Read the file
			#Write file.
            bReader = open(yourLocation + "HTML\\webImg\\"+"search_50px.png", "rb")
            theImg = bReader.read()
            s.wfile.write(theImg)
            
        elif path.find("heavy_piping_system.png") != -1:
			#Make right headers
            #s.send_response(200)
            #s.send_header("Content-type", "image/png")
            #s.end_headers()
			#Read the file
			#Write file.
            bReader = open(yourLocation + "HTML\\webImg\\"+"heavy_piping_system.png", "rb")
            theImg = bReader.read()
            s.wfile.write(theImg)
            
    

        elif path.find("exampleSystem.png") != -1:
			#Make right headers
            #s.send_response(200)
            #s.send_header("Content-type", "image/png")
            #s.end_headers()
			#Read the file
			#Write file.
            bReader = open(yourLocation + "HTML\\webImg\\"+"exampleSystem.png", "rb")
            theImg = bReader.read()
            s.wfile.write(theImg)
            
        
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
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i])) # the data about the customer

            UItext = UItext.replace('#messageToCustomer#', messageToCustomer) # handeling error messages to the customer

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
                UItext = UItext.replace(custommerInfoToChange[i], str(custommerInfo[i])) # the data about the customer

            UItext = UItext.replace('#messageToCustomer#', messageToCustomer) # handeling error messages to the customer

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
        global custom_parameters, messageToCustomer, custommerInfo, yourLocation
        global env_size, startPoint, endPoint, pipDia, eq_size_list, eq_pos, eq_in_out, num_eq, num_node_ax
        
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        

		# Check what is the path
        path = s.path
        if path.find("/yourParameters") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            #print("param line", param_line)
            #param line envSizeX=1000&envSizeY=3000&envSizeZ=4000&startA=0%2C1500%2C2000&endB=1000%2C1500%2C2000&pipe_dia=6&
            # eq1_sideX=500&eq1_sideY=500&eq1_sideZ=500&eq1_pos=500%2C500%2C500&eq1_in=0%2C250%2C250&eq1_out=500%2C250%2C250&eq2_sideX=300&eq2_sideY=300&eq2_sideZ=300&eq2_pos=300%2C700%2C500&eq2_in=0%2C150%2C150&eq2_out=300%2C150%2C150&eq3_sideX=700&eq3_sideY=700&eq3_sideZ=700&eq3_pos=700%2C1500%2C2000&eq3_in=0%2C350%2C350&eq3_out=700%2C350%2C350

			#making a string to print
            global print_order, yourLocation
            print_order = ""

            custom_parameters = stringSplit(custom_parameters, param_line)

            # getting the data arranged i a sensable way
            """
				Vi m?? f?? kundens parametere p?? formen (p?? en sofistikert m??te):
				num_eq = int
				eq_size_list = [eq1_size, eq2_size, eq3_size]
				eq_pos = [eq1_pos, eq2_pos, eq3_pos]
				eq_in_out = [eq1_in, eq1_out, eq2_in, eq2_out, eq3_in, eq3_out] #siden r??rene skal g?? inn og ut p??
				env_size = [x,y,z] #lengden p?? kuben som definerer environmentet
				startPoint = [x,y,z]
				endpoint = [x,yz]
				num_node_ax = int # denne kan vi definere selv ??verst i skriptet eller noe
				pipDia = float 
				"""
            
            env_size =[]
            startPoint = []
            endPoint = []
            pipDia = 0

            eq_size_list = []
            eq_pos = []
            eq_in_out = []

            num_eq = 3 # hardcoded
            num_node_ax = 100 # hardcoded

            # from reading the param line we know that the 6 first parameters are for the environment, 
            # then the 6 next params are for eq1, the 6 params after that for eq2, and so on

            # mulig disse m?? castes til int
            env_size = [int(custom_parameters[0]), int(custom_parameters[1]), int(custom_parameters[2])]
            startPoint = list(custom_parameters[3].split(","))
            startPoint = [int(x) for x in startPoint] # casting to int
            endPoint = list(custom_parameters[4].split(","))
            endPoint = [int(x) for x in endPoint]
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
            

            
			# check if input is valid
            errorMsg = checkCustomerInput(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, num_node_ax, pipDia)

            messageToCustomer = "Something wrong has happened.<br>"
            inputError = False
            for i in errorMsg: # going through the error messages
                if "ok" not in i:
                    inputError = True
                    messageToCustomer += i + " "
                    #be brukeren skrive inn p?? nytt og gi tilbakemelding p?? hva som er feil. 
                    # send brukeren til yourParameters"
                    ...
            if not inputError:
                messageToCustomer = "Your system is accepted."


            # take picture of the drawCustomerInfo 
                # calling drawGivenInfo.py
                # tegne noe i nx av seg selv
                # picture function m?? lages
                # send image to web
            
            

            s.do_GET() #this is not a optimal solution

        elif path.find("/sendOrder") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            
            # string parsing av customer info ( name, number..)
            custommerInfo = stringSplit(custommerInfo, param_line)
            name= custommerInfo[0]
            pNumber= custommerInfo[1]
            eMail= custommerInfo[2]
            compName= custommerInfo[3]

            systemPathObject = pathInterpreter.pipeSystem(num_eq, eq_size_list, eq_pos, eq_in_out, env_size, startPoint, endPoint, num_node_ax, pipDia)
            systemPath = systemPathObject.makePath()
            

            # give new path to dfa template:
                # input params: new path list, env_size, eq_size_list, eq_pos, pipDia, company_name, custommer name.
            # save a file with new 
            filename = makeDFA(num_eq, eq_size_list, eq_pos,eq_in_out, env_size, startPoint, endPoint, pipDia, custommerInfo, systemPath, yourLocation)

            print("The order from ", name, ", ", compName, " is now stored in the folder 'GeneratedSystems' as ", filename, ".")
            s.do_GET()


        elif path.find("/"):
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            s.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))

def stringSplit(paramContainer, param_line):
    if param_line.find("%2C"): # replacing "%2C" with ','
        param_line = param_line.replace("%2C", ',')
    if param_line.find("%40"):
        param_line = param_line.replace("%40", "@")
    
    #getting the parameter values
    key_val_pair = param_line.split('&')							#splitting the string at "&"
    for i in range(len(paramContainer)): 						#itterating through the custom_parameter list
        paramContainer[i] = key_val_pair[i].split('=')[1]		#spliting at "=" to only get the value
        if "+" in paramContainer[i]:
            paramContainer[i]= paramContainer[i].replace("+", " ")

    return paramContainer
	
 
if __name__ == '__main__':

	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()