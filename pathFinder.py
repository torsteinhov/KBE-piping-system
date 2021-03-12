import math as Math
import random

l1 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l2 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l3 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l4 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l5 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l6 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l7 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l8 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l9 =    [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

l10 =   [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

maze = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]

class Node():
    #Node class for the A*
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        #weight of actual move
        self.g = 0
        #heuristic euclidean distance to end node
        self.h = 0
        #f=g+h, total value
        self.f = 0

class astar_pathfinder:

    def a_star(self,maze,start,end):
        #returns a list of 3D tuples, that makes the path from start to end
        #ex: [(1,1,0),(2,1,1),(3,2,2),(3,2,3),(4,3,3),(5,4,3),(5,5,4),(5,5,5)]

        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = []
        closed_list = []

        open_list.append(start_node)

        while len(open_list) > 0:
            print("Vi er inne i open_list")

            current_node = open_list[0]
            current_index = 0
            for index, value in enumerate(open_list):
                if value.f < current_node.f:
                    current_node = value
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            #checks whether we are done
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current_position)
                    current = current.parent
                #return reversed path
                return path[::-1]

            children = []
            for new_position in [(1,-1,-1),(1,0,-1),(1,1,-1),(1,-1,0),(1,0,0),(1,1,0),(1,-1,1),(1,0,1),(1,1,1),(0,-1,-1),(0,0,-1),(0,1,-1),(0,-1,0),(0,1,0),(0,-1,1),(0,0,1),(0,1,1),(-1,-1,-1),(-1,0,-1),(-1,1,-1),(-1,-1,0),(-1,0,0),(-1,1,0),(-1,-1,-1),(-1,0,1),(-1,1,1)]:
                print("Sjekker ny position:", new_position)
                #node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])

                #checks if its within range
                if node_position[0] > (len(maze)-1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0 or node_position[2] < 0 or node_position[2] > (len(maze[len(maze[len(maze)-1])-1])-1):
                    continue

                if maze[node_position[0]][node_position[1]][node_position[2]] != 0:
                    continue
                
                #creates new node
                new_node = Node(current_node, node_position)

                #adds new node to children
                children.append(new_node)

            for child in children:

                for closed_child in closed_list:
                    if child == closed_child:
                        break
                
                #We now want to calculate the f-total_value, g-weight_of_travel and h-distance_to_end values
                #the h parameter is what separates this algorithm from the Dijkstra-algorithm.
                #In our case, we know the location of the end_node, we therefore want to exploit that, and the
                #A* algorithm is heuristic in the sense that it uses this information when evaluating its path options.

                child.g = current_node.g + 1
                #calculates euclidean distance, if we only want straight pipes, we could simplify the algorithm by removing
                #some of the alternative path nodes and using a manhattan distance calculation here.
                child.h = Math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2) + ((child.position[2] - end_node.position[2]) ** 2))
                child.f = child.g + child.h
                print(child.h)

                #Child is already in the open list

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                #Adds child to open list
                open_list.append(child)



            

if __name__ == '__main__':

    start = (0,0,0)
    end = (1,1,1)

    x = astar_pathfinder()
    print(x.a_star(maze,start,end))

