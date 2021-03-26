# KBE-piping-system

In this project, we were challenged with making an automated piping design system. Based on parameters given in to the UI provided, an A* algorithm computes the shortest-path in 3D from start node, between equipment and to an end node. KBE was in focus for capture and systematically reuse of engineering knowledge, with the final goal of reducing time and costs of repetitive product development tasks. During the development of the program and algorithm, scalability was an aspect we wanted to strive for, and the solution we ended up with, may be adjusted to be used on other shortest-path tasks. This project challenged us with combining knowledge in artificial intelligence algorithms, web design, geometry and software development. From last time we recognized how important the geometry and architecture was from the start of the project to prevent misunderstandings, which leads to time and resource consumption.

   Example 1  |  Example 2  |  Example 3    
:----------------------------:|:----------------------------:|:----------------------------:
![](https://github.com/torsteinhov/KBE-piping-system/blob/main/imagesOfGeneratedSystems/example%201/ex1.jpg)  |  ![](https://github.com/torsteinhov/KBE-piping-system/blob/main/imagesOfGeneratedSystems/example%204/ex4.jpg)   |   ![](https://github.com/torsteinhov/KBE-piping-system/blob/main/imagesOfGeneratedSystems/example%203/ex3.jpg)

<h2>User interface</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/77832956/112614911-1fe3ff00-8e22-11eb-8792-86f2b0b1a3ba.png">
</p>

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

When choosing which algorithm to base our solution on, we were challenged with different aspects. We are very well aware that the shortest path between two points is the eucledian distance. But for an environment that may have obstacles as other pipes or equipment, this solution would not be feasible. We therefore needed a pathfinding algorithm that operated step-for-step. We ended up with choosing a 3D node environment, and the A* algorithm. By choosing this algorithm with our current implementation, its only the user-interface that sets the boundaries for the amount of equipment and obstacles that the algorithm will have to process. It is therefore very scalable and adaptable to new circumstances.
The A* Algorithm is using numpy arrays to display a workable environment, and the algorithm therefore has to consider 26 different potential paths for its next move. Accordingly, the weight of the different paths is calculated using Pythagoras theorem. Move along one axis => path cost = 1, two axis => path cost = sqrt(2), three axis => path cost = sqrt(3). The time complexity of the algorithm is very dependent on the success of the heuristic, and never better then O(|V|+|E|). The heuristic for this algorithm is the euclidean distance to the end node. This is a great solution for this problem since it allows for the algorithm to prune away many of the nodes an uninformed search would expand.

<h2>Program files with corresponding methods</h2>
<br>
<h3>NXServer.py</h3>

**Main coordinating unit behind this application. Uses HTTP Requests to retrieve data from the userinterface.html. Calls on pathInterpreter.py with the data and recieves a path in coordinates. Based on these result, calls on DFAUpdaterPipeSystem.py to write the final DFA**

| Method | Functionality |
| --- | --- |
| do_HEAD | sends the headers it would send for the equivalent GET request |
| do_GET | Gets a request from the path given |
| do_POST | Posts a request to the path given |
| stringSplit | Parses the input params from the customer and gives workable information for us to process |

<h3>pathInterpreter.py</h3>

**Translates path from pathFinder to coordinates in CAD environment and adjust to input/outlet positions on equipment. Calls on pathFinder to get the different paths between start-eq1-eq2-eq3-end, in node format and translates to coordinates in real environment**

| Method | Functionality |
| --- | --- |
| coordinate2node | **help function**: Takes in a point in the environment and gives out corresponding node |
| node2point | **help function**: Takes in a node and gives out corresponding point in the environment |
| nodePath2pointPath | **help function**: Takes in a path of nodes and returns a path in environment coordinates |
| eqInOutGlobalPoint | Takes in information regarding the equipment, size, position and inlet/outlet. Returns the midpoint of the correct side to connect inlet/outlet. |
| makePath | Uses all the help functions to actually process the data from pathFinder. Returns a path with coordinates related to the environment and the equipment. |

<h3>pathFinder.py</h3>

**Finds the shortest path between two nodes in 3D, using an A* algorithm. Consists of a Node class and the actual algorithm that parses through the open list and explores all possible paths with a heuristic of the euclidean distance to the end goal as a guide**

| Method | Functionality |
| --- | --- |
| aStar | Returns a list of 3D tuples which makes up the path from start node to end node |

<h3>DFAUpdaterPipeSystem.py</h3>

**Based on data given from NXServer regarding the path, environment and equipment. Strings of template Knowledge Fusion childs are declared and for loops iterates through the data, overwrites the template child and appends to the final DFA. The result is a piping system that has the shortest path between start-, equipment- and end position**

| Method | Functionality |
| --- | --- |
| dirIntoEnvironment | Gives the direction into the cuboid. This is for the pipe_profile child in the DFA code, which needs information regarding the X and Y axis to draw the circular profile of the pipe to be extruded. We have struggled a bit with the implementation of getting correct orientation for the profiles. |
| makeDFA | Takes in all the processed data, overwrites template strings and appends to the DFA. |

<h2>How to run:</h2>

+ Run NXServer.py **interact with webpage**.
+ DFA file ready to open in NX.

<h2>Further development</h2>

+ The capturing and reuse of knowledge in this KBE system is something that still has great potential. There should be some way of guiding the pipe to not change direction that often. Since the complexity of the resulting pipe will probably not work in an real life situation.

+ The algorithm is already capable of handling obstacles, therefore there should be functionality in the userinterface to submit obstacles(other equipment or pipes that is not to be connected with the corresponding pipe), and the nodes the obstacles occupy should be weighted to infinity for the algorithm, therefore it will never cross the section.

+ Userinterface should have a more detailed typing error checker, so that the program is 100% dummy proof.

+ There should be a much more sophisticated use of classes in the program. As the project stands now it is to often indexation of environment, equipment and etc. This is something we realised late in the project but is recognized as something we want to improve on.

+ More sophisticated piping modules. Now it is just an extruded line that creates a cylinder object. This should be a much more detailed and correct piping element. Luckily this is an easy modification since the architecture for adding this specific module to the DFA is already in place.

+ The "preview" button has a file associated with it, drawGivenInfo.py which is not activated right now but lays ready for implementation. As the program is right now you have to press the "preview" button for the information to be passed on before ordering, this is also an adjustment that can be made.

+ Create a manufChecker that submits which pipe sizes are available.

+ Have all the data from the user uploaded to a database.

+ Right now there are som quick fixes regarding the pathInterpreter, as forexample integer divison which may make the pipe to be some millimeters off the input/output on the equipment. This should be fixed.
