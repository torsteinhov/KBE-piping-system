# KBE-piping-system

In this project, we were challenged with making an automated piping design system. Based on parameters given in to the UI provided, an A* algorithm computes the shortest-path in 3D from start node, between equipment and to an end node. KBE was in focus for capture and systematically reuse of engineering knowledge, with the final goal of reducing time and costs of repetitive product development tasks. During the development of the program and algorithm, scalability was an aspect we wanted to strive for, and the solution we ended up with, may be adjusted to be used on other shortest-path tasks.

   Example 1  |  Example 2   |  Example 3    
:----------------------------:|:----------------------------:|:----------------------------:
![](https://github.com/torsteinhov/KBE-piping-system/blob/main/imagesOfGeneratedSystems/HundredNodes/hundredNodes.jpg)  |  ![](https://user-images.githubusercontent.com/77832956/109148159-2705e780-7766-11eb-8c0c-71c2c576eb49.png)   |   ![](https://user-images.githubusercontent.com/77832956/107939730-6d4d9080-6f87-11eb-8647-1d85c32ee681.png)


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
