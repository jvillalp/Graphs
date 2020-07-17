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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
current_room = player.current_room


room_to_path_taken = {current_room: []}
stack = []
for dir in player.current_room.get_exits():
    next_room = current_room.get_room_in_direction(dir)
    stack.append((next_room, [dir]))

while stack:
    next_room, path_taken = stack.pop()
    if next_room not in room_to_path_taken:
        current_room = player.current_room
        # print(current_room.id)
        travel_to_next_room = False
        for dir in current_room.get_exits():
            adjacent_room = current_room.get_room_in_direction(dir)
            if adjacent_room == next_room:
                player.travel(dir)
                traversal_path.append(dir)
                travel_to_next_room = True
                break
            for dir2 in adjacent_room.get_exits():
                if adjacent_room.get_room_in_direction(dir2) == next_room:
                    player.travel(dir)
                    player.travel(dir2)
                    traversal_path.extend([dir, dir2])
                    travel_to_next_room = True

        
        if not travel_to_next_room:
            path_to_next_node = []
            path_found = False
            for dir in traversal_path[::-1]:
                inversed_dir = inverse(dir)
                path_to_next_node.append(inversed_dir)
                player.travel(inversed_dir)
                current_room = player.current_room
                for dir2 in current_room.get_exits():
                    if current_room.get_room_in_direction(dir2) == next_room:
                        path_to_next_node.append(dir2)
                        player.travel(dir2)
                        path_found = True
                        break
                if path_found:
                    break
            traversal_path.extend(path_to_next_node)



            # inverse_path = [inverse(dir) for dir in room_to_path_taken[current_room]]
            # directions = inverse_path[::-1] + path_taken
            # traversal_path.extend(directions)
            # for dir in directions:
            #     player.travel(dir)
        
        # print(traversal_path)
        room_to_path_taken[next_room] = path_taken
        for dir in next_room.get_exits():
            next = next_room.get_room_in_direction(dir)
            stack.append((next, path_taken + [dir]))
            next_room.connect_rooms(dir, next)

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
