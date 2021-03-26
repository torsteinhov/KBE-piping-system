# KBE-piping-system

In this project, we were challenged with making an automated piping design system. Based on parameters given in to the UI provided, an A* algorithm computes the shortest-path in 3D from start node, between equipment and to an end node. KBE was in focus for capture and systematically reuse of engineering knowledge, with the final goal of reducing time and costs of repetitive product development tasks. During the development of the program and algorithm, scalability was an aspect we wanted to strive for, and the solution we ended up with, may be adjusted to be used on other shortest-path tasks.

   Example 1  |  Example 2 (tested with fewer nodes)   |  Example 3    
:----------------------------:|:----------------------------:|:----------------------------:
![](https://github.com/torsteinhov/KBE-piping-system/blob/main/imagesOfGeneratedSystems/HundredNodes/hundredNodes.jpg)  |  ![](https://github.com/torsteinhov/KBE-piping-system/blob/main/imagesOfGeneratedSystems/FortyNodes/FortyNodes.jpg)   |   ![](https://user-images.githubusercontent.com/77832956/107939730-6d4d9080-6f87-11eb-8647-1d85c32ee681.png)


<h2>Architecture</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/77832956/112598690-3fbdf780-8e0f-11eb-8aab-5587ec60fea2.png">
</p>

The information flow starts when the customer submits data through the User Interface [HTML], which is styled by the CSS stylesheet. From here the NXServer.py parses the data from the HTTP Requests and sends the data to the pathInterpreter.py. Based on this data, it calls on the pathFinder.py to find shortest path in 3D from start to end node. Then it translates this node path to the coordinates in the actual CAD environment, also regarding the in- and outlets of the equipment for which side it shall connect. This calculation could have been done in the pathFinder but we wanted the actual algorithm to stay as general as possible for reusability and scalability. When the path is translated to coordinates in the environment, this path is sent to DFAUpdaterPipeSystem.py, which overwrites a DFA file based on the ug_swept feature, to produce the piping system. By using templates for each module needed to create a pipe, for loops are used to overwrite all the necessary data and add to the DFA. From here it is ready for demonstration in the Siemens NX software, which from there will be available for further modelling and modifying.

<h2>UML sequence diagram</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/77832956/112602024-74cc4900-8e13-11eb-8fac-b3aaf2e0a1cb.png">
</p>


<h2>A* Algorithm for the pathFinder.py</h2>

   Potential Paths  |  Path cost
:----------------------------:|:----------------------------:
![](https://user-images.githubusercontent.com/77832956/111148182-9dd71900-858b-11eb-8d45-45eeb49e906a.png) |  ![](https://user-images.githubusercontent.com/77832956/111148221-aa5b7180-858b-11eb-9230-e338ec759257.png)

The A* Algorithm works in an 3D environment. It is using numpy arrays to display a workable environment, and the algorithm therefore has to consider 26 different potential paths for its next move. Accordingly, the weight of the different paths is calculated using Pythagoras theorem. Move along one axis => path cost = 1, two axis => path cost = sqrt(2), three axis => path cost = sqrt(3). The time complexity of the algorithm is very dependent on the success of the heuristic, and never better then O(|V|+|E|). The heuristic for this algorithm is the euclidean distance to the end node. This is a great solution for this problem since it allows for the algorithm to prune away many of the nodes an uninformed search would expand.

<h3>NXServer.py</h3>

**Main coordinating unit behind this application. Uses HTTP Requests to retrieve data from the userinterface.html. Calls on pathInterpreter.py with the data and recieves a path in coordinates. Based on these result, calls on DFAUpdaterPipeSystem.py to write the final DFA.**

| Method | Functionality |
| --- | --- |
| do_HEAD | sends the headers it would send for the equivalent GET request |
| do_GET | Gets a request from the path given |
| do_POST | Posts a request to the path given |
| stringSplit | Parses the input params from the customer and gives workable information for us to process |

<h3>pathInterpreter.py</h3>

**Translates path from pathFinder to coordinates in CAD environment and adjust to input/outlet positions on equipment. Calls on pathFinder to get the different paths between start-eq1-eq2-eq3-end, in node format and translates to coordinates in real environment.**

| Method | Functionality |
| --- | --- |
| coordinate2node | **help function**: Takes in a point in the environment and gives out corresponding node |
| node2point | **help function**: Takes in a node and gives out corresponding point in the environment |
| nodePath2pointPath | **help function**: Takes in a path of nodes and returns a path in environment coordinates |
| eqInOutGlobalPoint | Takes in information regarding the equipment, size, position and inlet/outlet. Returns the midpoint of the correct side to connect inlet/outlet. |
| makePath | Uses all the help functions to actually process the data from pathFinder. Returns a path with coordinates related to the environment and the equipment. |

<h3>pathFinder.py</h3>

**Finds the shortest path between two nodes in 3D, using an A* algorithm. Consists of a Node class and the actual algorithm that parses through the open list and explores all possible paths with a heuristic of the euclidean distance to the end goal as a guide.**

| Method | Functionality |
| --- | --- |
| aStar | Returns a list of 3D tuples which makes up the path from start node to end node |

<h3>DFAUpdaterPipeSystem.py</h3>

**Based on data given from NXServer regarding the path, environment and equipment. Strings of template Knowledge Fusion childs are declared and for loops iterates through the data, overwrites the template child and appends to the final DFA. The result is a piping system that has the shortest path between start-, equipment- and end position.**

| Method | Functionality |
| --- | --- |
| dirIntoEnvironment | Gives the direction into the cuboid. This is for the pipe_profile child in the DFA code, which needs information regarding the X and Y axis to draw the circular profile of the pipe to be extruded. We have struggled a bit with the implementation of getting correct orientation for the profiles. |
| makeDFA | Takes in all the processed data, overwrites template strings and appends to the DFA. |

<h2>How to run:</h2>

+ Run NXServer.py **interact with webpage**.
+ DFA file ready to open in NX.

<h2>Further development</h2>

We have learned many things in the development of this project. First of all we have experienced the importance of agreeing and fully complete a geometry that meets our
design requirements. The hassle of changing ontology and DFA files while still developing software is something we would like to avoid for future projects because of its time cost.

+ The capturing and reuse of knowledge in this KBE system is something that still has great potential. Thoughts we have had regarding this is forexample automation of adding new constrains from the manufacturing side, or more enthusiastic, a genetic algorithm that proposes more creative designs based on a customers style preferences (modern, chic, conservative, baroque etc.).

+ Making the feasibilityChecker independent of the DFAServer is also something we would have implemented if this project was developed further 
and scaled for bigger usage.

+ Adding material choice for the different components in the DFA file, all the infrastructure for material choice in the database is already established.
