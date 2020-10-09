from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
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


traversal_graph = {}
s = Queue()
breadcrumbs = Stack()
visited = set()

starting_room = player.current_room.id
s.enqueue([starting_room])

last_room = None


def reverse_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


def walk(direction):
    if direction in player.current_room.get_exits():
        player.travel(direction)
        traversal_path.append(direction)
        breadcrumbs.push(direction)
    # else:
    #     walk(reverse_direction(breadcrumbs))
        # walk(direction)
        # reverse the queue?
        # Where are the extra queue instructions coming from?
        # probably the unexplored paths that are currently out of reach.
        # steps reverse: e,e,e,s -> n,w,w,w
        # a queue can be reversed with a stack...
        # backtrack iwth a stack


iter = 1
last_room_id = starting_room
while s.size() > 0:
    # pull the latest path and direction from the queue
    path = s.dequeue()
    travel_direction = path[-1] if not path[-1] == starting_room else None
    print(
        f"\n\nTravel direction {travel_direction}\nLast room {last_room}\nIteration {iter}\nCurrent room {player.current_room.id}\nVisited {visited}")
    # travel_direction = path[-1]

    # visit the currently queued room
    current_room = player.current_room.id
    visited.add(current_room)
    # print(visited, current_room)

    if current_room not in traversal_graph:  # create the first entry for this room
        traversal_graph[current_room] = {
            direction: '?' for direction in player.current_room.get_exits()}

    # If the travel_directions are not None
    # 0, n
    """
    Current room is the same as the first arg
    Last room id needs to come from the last loop

     - The first iteration is trying to add to the graph
     - The second iteration doesn't even try.
     - The third iteration thinks south is north and north is itself.
    """
    print(f"Iteration {iter} Last room id {last_room_id}")
    last_room = (last_room_id, travel_direction)
    if travel_direction:
        # traversal_graph[current_room][reverse_direction(
        #     last_room[1])] = last_room[0]
        traversal_graph[last_room[0]][last_room[1]] = current_room
        print("Iteration", iter, "Traversal graph",
              traversal_graph[current_room])
    #

    # print(traversal_graph[current_room], f"\n\n {current_room}")

    # if this is at least the second loop through, travel and add to reversal path
    if travel_direction:
        walk(travel_direction)

    for direction in traversal_graph[current_room]:
        if traversal_graph[current_room][direction] not in visited:
            s.enqueue([direction])

    last_room_id = current_room
    iter += 1


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
