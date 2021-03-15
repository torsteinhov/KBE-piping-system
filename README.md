# KBE-piping-system

In this project, we were challenged with making an automated piping design system. Based on parameters given in to the UI provided, an A* algorithm computes the shortest-path in 3D from start node, between equipment and to an end node. KBE was in focus for capture and systematically reuse of engineering knowledge, with the final goal of reducing time and costs of repetitive product development tasks. During the development of the program and algorithm, scalability was an aspect we wanted to strive for, and the solution we ended up with, may be adjusted to be used on other shortest-path tasks.

   Problem  |  Illustration   |
:----------------------------:|:----------------------------:
Since the algorithm works in 3D, we were met with 26 possible coombinations<br /> for paths, as illustrated here. This meant that the algorithm had to process a wast amount<br /> of possible paths for each node it visited. Thankfully, because of the heuristic, <br /> it processes pretty rapidly in the correct direction and the running time therefore keeps at a stable level. |  ![](https://user-images.githubusercontent.com/77832956/111148182-9dd71900-858b-11eb-8d45-45eeb49e906a.png)
Since the algorithm had 26 different possible paths for each position, <br />we had to change the weighing of each path cost. By moving along 1,2 or 3 axes <br /> the weight of each move had to be accordingly. Illustrated in code below |  ![](https://user-images.githubusercontent.com/77832956/111148221-aa5b7180-858b-11eb-9230-e338ec759257.png)
 ```python
            if new_position in [(0,-1,0),(-1,0,0),(0,1,0),(1,0,0),(0,0,1),(0,0,-1)]:
                new_node.g += 1
            elif new_position in [(1,-1,0),(-1,-1,0),(-1,1,0),(1,1,0),(1,0,1),(0,-1,1),(-1,0,1),(0,1,1),(0,1,-1),(1,0,-1),(0,-1,-1),(-1,0,-1)]:
                new_node.g += Math.sqrt(2)
            elif new_position in [(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,1,1),(-1,-1,-1),(-1,1,-1),(1,1,-1),(1,1,1)]:
                new_node.g += Math.sqrt(3)```


