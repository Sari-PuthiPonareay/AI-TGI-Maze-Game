from queue import PriorityQueue
from pyamaze import maze, agent, textLabel
def heuristic_fun(cell1, cell2): # to find the optimal solution
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1-x2) + abs(y1-y2) # manhatan distance 
def aStart_search(m):
    start = (m.rows, m.cols) # last row and last columns of the maze

    # dictionary comprehension
    g_of_n = {cell:float('inf') # inf = infinity, key = cell, value = infinity
                for cell in m.grid
                }
    g_of_n[start] = 0 # start cell 
    f_of_n = {cell:float('inf') 
              for cell in m.grid }

    f_of_n[start] = heuristic_fun(start,(1,1)) 


    priority_Q = PriorityQueue() 
    priority_Q.put((f_of_n[start]+0, f_of_n[start], start)) 
                # ((𝑓(𝑛) = h(𝑛) + g(𝑛), h(n), g(n))

    path = {} # reverse path 
    while not priority_Q.empty():

        current_Cell = priority_Q.get()[2] # [2] = start cell
        if current_Cell == (1,1):
            break
        for direction in 'ESNW': # East,south,North,west
            if m.maze_map[current_Cell][direction] == True:
                if direction == 'E':
                    neighbor_cell = (current_Cell[0], current_Cell[1]+1)
                                  # row of index same as current cell = 0, row of columns index will be one more than that
                if direction == 'W':
                    neighbor_cell = (current_Cell[0], current_Cell[1]-1)
                if direction == 'N':
                    neighbor_cell = (current_Cell[0]-1, current_Cell[1])
                if direction == 'S':
                    neighbor_cell = (current_Cell[0]+1, current_Cell[1])
                
                # once the neighbor is found, => new g(n) + 1
                new_g_of_n = g_of_n[current_Cell] + 1
                new_f_of_n = new_g_of_n + heuristic_fun(neighbor_cell,(1,1))

                if new_f_of_n < f_of_n[neighbor_cell]:
                    g_of_n[neighbor_cell] = new_g_of_n
                    f_of_n[neighbor_cell] = new_f_of_n

                    priority_Q.put((new_f_of_n, heuristic_fun(neighbor_cell,(1,1)), neighbor_cell))
                    path[neighbor_cell] = current_Cell
                        # key           = value 

    fwdpath = {} # invert part 
    cell = (1,1) # swap from the goal call 
    while cell != start:
        fwdpath[path[cell]] = cell
        cell = path[cell]

    return fwdpath

if __name__ == '__main__': # special variable : the point of execution for any program
    m = maze(10,10)

    m.CreateMaze()
    p = aStart_search(m)
    # print(m.maze_map)
    # print(m.grid) # print list of all cells inside the maze

    # create an agent
    a = agent(m, footprints = True)
    m.tracePath({a:p})
    l = textLabel(m, "A star path length : ", len(p)+1)

    m.run()