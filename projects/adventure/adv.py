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


# path we want to print
traversal_path = []
#variable equal to current_room of player when going through walkthrough
start_room = player.current_room
dfs_stack = []
visited = {}

while len(visited.keys()) < len(world.rooms):
    nodes_to_traverse = []
    current_room = player.current_room
    for dir in current_room.get_exits():
        if current_room.get_room_in_direction(dir) not in visited:
            nodes_to_traverse.append(dir)

    visited[current_room] = True

    if nodes_to_traverse:
        next_move = random.randint(0, len(nodes_to_traverse) - 1)
        dfs_stack.append(nodes_to_traverse[next_move])
        player.travel(nodes_to_traverse[next_move])
        traversal_path.append(nodes_to_traverse[next_move])
    else:
        last_seen = dfs_stack.pop()
        inversed_dir = inverse(last_seen)
        player.travel(inversed_dir)
        traversal_path.append(inversed_dir)
#Queue
#at each room, check for directions an in 
#four rooms you see in four directions, see relationship
#room south, goes to room 4...
#visited each node and all relationship
# print("Length of visiting rooms: " + str(len(room_to_path_taken.keys())))
# print(room_to_path_taken)
# print(traversal_path)



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