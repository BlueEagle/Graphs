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
    print(f"Iteration {iter} Last room id {last_room_id} Direction {travel_direction} Current room {current_room}")
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