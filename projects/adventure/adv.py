from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


def inverse(dir):
    if dir == "n":
        return "s"
    elif dir == "s":
        return "n"
    elif dir == "e":
        return "w"
    else:
        return "e"
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


#Understand, Plan
#Stack
#at each room, check for directions an in 
#four rooms you see in four directions, see relationship
#room south, goes to room 4...
#visited each node and all relationship
# print("Length of visiting rooms: " + str(len(room_to_path_taken.keys())))
# print(room_to_path_taken)
# print(traversal_path)


# path we want to print
traversal_path = []
# keep a stack for DFS, and a dict of visited rooms.
dfs_stack = []
visited = {}

# DFS. If we hit a dead end (no more nodes_to_traverse), keep going back until
# we can explore another path.
while len(visited.keys()) < len(world.rooms):
    # nodes we can directly traverse to from current node.
    nodes_to_traverse = []
    current_room = player.current_room
    # for valid dir
    for dir in current_room.get_exits():
        if current_room.get_room_in_direction(dir) not in visited:
            # if node has not been visited before, add it as a node we can directly traverse to.
            nodes_to_traverse.append(dir)

    # Visit the current room.
    visited[current_room] = True

    # if there are nodes to traverse from here, randomly choose one,
    # travel there, and add to traversalpath.
    if nodes_to_traverse:
        next_move = random.randint(0, len(nodes_to_traverse) - 1)
        #append next node to traverse-to to the stack
        dfs_stack.append(nodes_to_traverse[next_move])
        #move player to that random node needed to traverse
        player.travel(nodes_to_traverse[next_move])
        #append next_move of node to the traversal_path which is what we will want counted for moves
        traversal_path.append(nodes_to_traverse[next_move])
    # else pop from stack and go backwards until we find a node that has nodes
    # it can directly traverse to.
    else:
        #pop from stoack
        last_seen = dfs_stack.pop()
        #go in inverse dir until we find a node we can traverse to
        inversed_dir = inverse(last_seen)
        #move player
        player.travel(inversed_dir)
        #append to traversal path
        traversal_path.append(inversed_dir)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")