import math as Math
import random
import numpy as np

#Node class for the A*
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        #distance between current node and start node
        self.g = 0
        #euclidean estimated distance to end node, heuristic aspect of the algorithm
        self.h = 0
        #f=g+h, total cost of the node
        self.f = 0

    #gets called when using the == operator
    def __eq__(self,other):
        return self.position == other.position

#Had a logic error further down where I wanted to break out of the inner loop but continuing the outer loop,
#This combined with try, except catch fixed this.
class ContinueI(Exception):
    pass

def aStar(amount,start,end):
    #returns a list of 3D tuples, that makes the path from start to end
    #ex: [(1,1,0),(2,1,1),(3,2,2),(3,2,3),(4,3,3),(5,4,3),(5,5,4),(5,5,5)]

    #creates environment cubloid with amount*amount*amount
    #much more scalable, since it allows the customer/process engineer to trade more computing in return for a more accurate design
    maze = []
    for i in range(amount):
        x = np.zeros((amount,amount))
        maze.append(x)

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    #initializes the open and closed list
    closed_list = []
    open_list = []
    open_list.append(start_node)


    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, value in enumerate(open_list):
            if value.f < current_node.f:
                current_node = value
                current_index = index

        #picks out top element from open_list and removes it from the open_list
        open_list.pop(current_index)
        closed_list.append(current_node)

        #checks whether we are done
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            #since it iterates back when reaching final node, we get the path from end -> start, we therefore want to flip it
            #print("Path: ", path[::-1])
            return path[::-1]

        children = []
        #Checks each possible path relative to current position(set as origo)
        #Has to check all the positions above, but also the layer above and below, illustrated below
        #is the positions for the current layer, with the other layers, the amount of positions that must be checked is
        #8+9+9=26 possible path relative to the current position.
        '''
            N.W    N    N.E
               \   |   /
                \  |  /
             W----Cell----E
                  / | \
                /   |  \
             S.W    S   S.E
        '''
        possible_paths = [(1,-1,-1),(1,0,-1),(1,1,-1),(1,-1,0),(1,0,0),(1,1,0),(1,-1,1),(1,0,1),(1,1,1),(0,-1,-1),(0,0,-1),(0,1,-1),(0,-1,0),(0,1,0),(0,-1,1),(0,0,1),(0,1,1),(-1,-1,-1),(-1,0,-1),(-1,1,-1),(-1,-1,0),(-1,0,0),(-1,1,0),(-1,-1,-1),(-1,0,1),(-1,1,1)]
        for new_position in possible_paths:

            #node position
            node_pos = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])

            #checks if its within range
            if node_pos[0] > (len(maze)-1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze)-1]) -1) or node_pos[1] < 0 or node_pos[2] < 0 or node_pos[2] > (len(maze[len(maze[len(maze)-1])-1])-1):
                continue

            if maze[int(node_pos[0])][int(node_pos[1])][int(node_pos[2])] != 0:
                continue
            
            #creates new node
            new_node = Node(current_node, node_pos)

            #Weighs the g based on the eucledian distance to the new position, by using pythagoras theorem we get either 1, sqrt(2) or sqrt(3), and
            #here it is weighted accordingly
            if new_position in [(0,-1,0),(-1,0,0),(0,1,0),(1,0,0),(0,0,1),(0,0,-1)]:
                new_node.g += 1
            elif new_position in [(1,-1,0),(-1,-1,0),(-1,1,0),(1,1,0),(1,0,1),(0,-1,1),(-1,0,1),(0,1,1),(0,1,-1),(1,0,-1),(0,-1,-1),(-1,0,-1)]:
                new_node.g += Math.sqrt(2)
            elif new_position in [(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,1,1),(-1,-1,-1),(-1,1,-1),(1,1,-1),(1,1,1)]:
                new_node.g += Math.sqrt(3)
            #adds new node to children
            children.append(new_node)

        #instance for the inner-loop break
        continue_i = ContinueI()

        for child in children:
            try:
                for closed_child in closed_list:
                    if child == closed_child:
                        raise continue_i
            
            except ContinueI:
                continue
            
            #We now want to calculate the f-total_value, g-weight_of_travel and h-distance_to_end values
            #the h parameter is what separates this algorithm from the Dijkstra-algorithm.
            #In our case, we know the location of the end_node, we therefore want to exploit that, and the
            #A* algorithm is heuristic in the sense that it uses this information when evaluating its path options.

            #calculates euclidean distance, if we only want straight pipes, we could simplify the algorithm by removing
            #some of the alternative path nodes and using a manhattan distance calculation here.
            child.h = Math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2) + ((child.position[2] - end_node.position[2]) ** 2))
            child.f = child.g + child.h

            #Child is already in the open list
            try:
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        raise continue_i
            except ContinueI:
                continue

            #Adds child to open list
            open_list.append(child)


if __name__ == '__main__':
    
    start = (25,31,31)
    end = (99,50,50)

    aStar(100, start, end)
    