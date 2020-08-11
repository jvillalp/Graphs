"""
Write a function that takes a 2D binary array and returns the number of 1 islands. 

island_counter(islands) # returns 4

nodes: 1s
edge: connected n/s/w/e
islands: connecyed components

build our graph or just define getNeighbors()

visited = set((0,1))

Plan
## iterate through the matrix
### when we see a 1, if its not been visited
### increment our island counter
### run a traversal
### mark things as visited

- stretch goal: refactor Graph to use a matrix
"""

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def get_neighbors(node, matrix):
    row, col = node
    neighbors = []

    stepNorth = stepSouth = stepWest = stepEast = False
    ##take a step north
    if row > 0:
        stepNorth = row -1
    ##take a step south
    if row < len(matrix) -1:
        stepSouth = row +1
    ##take a step east
    if col < len(matrix[row]) -1:
        stepEast = col +1
    ##take a step west
    if col > 0:
        stepWest = col -1

    if stepNorth is not False and matrix[stepNorth][col] ==1:
        neighbors.append((stepNorth, col))

    if stepSouth is not False and matrix[stepSouth][col] ==1:
        neighbors.append((stepSouth, col))

    if stepEast is not False and matrix[stepEast][col] ==1:
        neighbors.append((stepEast, col))

    if stepWest is not False and matrix[stepWest][col] ==1:
        neighbors.append((stepWest, col))

    return neighbors

def dft_recursive(node, visited, matrix):
    ###if node not visited
    if node not in visited:
        ##add to visited
        visited.add(node)
        ##get  neighbors
        neighbors = get_neighbors(node, matrix)
        for neighbor in neighbors:
            #recurse
            dft_recursive(neighbor, visited, matrix)
    ### mark things as visited

def island_counter(isles): #2D array (list of lists)
    visited = set()
    number_islands = 0
    ## iterate through the matrix
    for row in range(len(isles)):
        for col in range(len(isles[row])):
            node = (row, col)

            ### when we see a 1, if its not been visited
            if node not in visited and isles[row][col] == 1:
                ### increment our island counter
                number_islands += 1
                ### run a traversal
                dft_recursive(node, visited, matrix)

    return number_islands
    
print(island_counter(islands))