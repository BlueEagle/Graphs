# from adventure.old8 import reverse_direction
from room import Room
from player import Player
from world import World
from util import Queue, Stack
import random

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

"""
WORKING AREA
# traversal_path = ['n', 'n']
"""

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
map = {}
def explore(player, moves):
    q = Queue()

    q.enqueue([player.current_room.id])

    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        current_room = path[-1]

        if current_room not in visited:
            visited.add(current_room)

            for exit in map[current_room]:
                if map[current_room][exit] == "?":
                    return path
                else:
                    new_path = list(path)
                    new_path.append(map[current_room][exit])
                    q.enqueue(new_path)
    
    return []

new_moves = Queue()
def unexplored(player, new_moves):
    exits = map[player.current_room.id]
    untried = []

    for direction in exits:
        if exits[direction] == "?":
            untried.append(direction)

    if len(untried) == 0:
        not_explored = explore(player, new_moves)
        new_room = player.current_room.id
        
        for room in not_explored:
            for direction in map[new_room]:
                if map[new_room][direction] == room:
                    new_moves.enqueue(direction)
                    new_room = room
                    break

    else:
        new_moves.enqueue(untried[random.randint(0, len(untried)-1)])

unexplored_room = {}
for direction in player.current_room.get_exits():
    unexplored_room[direction] = "?"

map[world.starting_room.id] = unexplored_room

unexplored(player, new_moves)

reverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

while new_moves.size() > 0:
    current_room = player.current_room.id
    move = new_moves.dequeue()
    player.travel(move)
    traversal_path.append(move)
    next_room = player.current_room.id
    map[current_room][move] = next_room
    
    if next_room not in map:
        map[next_room] = {}

        for exit in player.current_room.get_exits():
            map[next_room][exit] = '?'
    
    map[next_room][reverse_directions[move]] = current_room

    if new_moves.size() == 0:
        unexplored(player, new_moves)

# paths = Queue()
# backtrace = Stack()
# visited = set()

# paths.enqueue([player.current_room])
# while paths.size() > 0:
#     path = paths.dequeue()
#     current_room = path[-1]

#     if current_room not in visited:
#         visited.add(current_room)

#         # add exits to the current room
#         if player.current_room not in places:
#             places[player.current_room.id] = {direction: '?' for direction in player.current_room.get_exits()}

#         # explore surrounding rooms and get their id's
#         for room in player.current_room.get_exits():
#             player.








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
