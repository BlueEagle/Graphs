from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


"""
WORKING AREA
# traversal_path = ['n', 'n']
"""


def reverse_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


traversal_graph = {}
bucket_list_stack = Stack()
breadcrumbs_stack = Stack()

bucket_list_stack.push([player.current_room.id])
breadcrumbs_stack.push(player.current_room.id)

starting_room = player.current_room.id
last_room_id = None

while bucket_list_stack.size() > 0:
    path = bucket_list_stack.pop()
    travel_direction = path[-1] if not path[-1] == starting_room else None

    if travel_direction:
        breadcrumbs_stack.push(travel_direction)
        player.travel(travel_direction)
    current_room = player.current_room.id
    # add new room ID to last room in graph, add last room ID to current room in graph.
    # where can we get the last room ID?

    # if last_room_id:
    #     print(f"BEFORE (Room {current_room}): {traversal_graph}")
    #     # I moved in what direction to get here? travel_direction
    #     # update the last room with current info.
    #     traversal_graph[current_room][travel_direction] = current_room
    #     # traversal_graph[current_room][reverse_direction(
    #     # travel_direction)] = last_room_id
    #     # print(
    #     #     f"UPDATE: new info for current room: {traversal_graph[current_room]}")
    #     # print(
    #     #     f"UPDATE: new info for current room: {traversal_graph[last_room_id]}")
    #     print(f"AFTER: {traversal_graph}")
    # last_room_id = current_room

    if current_room not in traversal_graph:
        # traversal_graph[current_room] = { n}
        exits = player.current_room.get_exits()
        traversal_graph[current_room] = {direction: '?' for direction in exits}
        print(
            f"You've entered a new room, the exits are: {exits}")
        print(
            f"Added {current_room} to traversal graph. It now looks like: {traversal_graph}")

    if travel_direction:
        last_room_id = breadcrumbs_stack.pop()
        traversal_graph[current_room][reverse_direction(
            travel_direction)] = last_room_id
        # traversal_graph[last_room_id][travel_direction] = current_room
        breadcrumbs_stack.push(last_room_id)

    # look in every direction from the room
    for direction in traversal_graph[current_room]:
        if traversal_graph[current_room][direction] == '?':
            print(
                f"In room {current_room}, found mysterious room to the {direction}")

            new_path = path + [direction]  # We do not have the id yet :(
            # we can figure out what direction needs to be taken by knowing the key and which path we took to get somewhere.
            bucket_list_stack.push(new_path)


"""
Try all this again tomorrow morning.

Final thoughts... 
    - Track the travel direction in the path.
    - The travel direction is what it took to get where we are currently.
    This means that the top of the path and current travel direction is what it took to get where we are.
    Reverse this to get back.
    - Instead of using visited to not add to stack/queue, we are searching at each stop to find mystery rooms.
    - When no mystery rooms are found, we can return on the path that got us where we are.
    If no mystery room is found, nothing is added to the path. Naturally, we begin eating off the top of the stack again.
    This is good except in a list like [n, n, n, n]. It becomes [n, n, n] and we travel north again, putting us in a loop.
    SOLUTION: 
    If no mystery room is found, pop the top off the stack and reverse it.
    [n, n, n, n] -> [n, n, n, s] and at the beginning of the next loop, we consume the 's'. Perform the check and find no mystery rooms?

    Do the numbers even matter? We don't just search for them. Could we use the number's relationships determine the shortest path to the next item in a queue?
    This may not be possible. It needs to have been visited to have a number.

    The normal stack is for the path that took us to where we are. It is a list of directions.

    What do we do when there are no more paths and we are at the starting point?
    if player.current_room.id == starting_room
    in the for loop where I check for rooms, check if any of the rooms are '?',
    I should do this anyway. If that condition is true and player.current_room.id == starting_room
    Nothing further should be added to the stack by default. But I can then return the traversal_path
"""

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
