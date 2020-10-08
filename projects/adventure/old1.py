def reverse_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


print(f"This is COLLIN's output: {player.current_room.id}")
traversal_graph = {}
bucket_list_stack = Stack()
breadcrumbs_stack = Stack()

bucket_list_stack.push([player.current_room.id])
breadcrumbs_stack.push(player.current_room.id)
starting_room = player.current_room.id
last_room_ID = None

while bucket_list_stack.size() > 0:
    path = bucket_list_stack.pop()
    # This may be able to replace breadcrumbs... Consider it later.
    travel_direction = path[-1]
    # if we are in the starting room, look around first.
    if not travel_direction == starting_room:
        breadcrumbs_stack.push(travel_direction)
        player.travel(travel_direction)
    current_room = player.current_room.id
    # add new room ID to last room in graph, add last room ID to current room in graph.
    # where can we get the last room ID?

    if last_room_ID:
        print(f"BEFORE (Room {current_room}): {traversal_graph}")
        # I moved in what direction to get here? travel_direction
        # update the last room with current info.
        traversal_graph[current_room][travel_direction] = current_room
        # traversal_graph[current_room][reverse_direction(
        # travel_direction)] = last_room_ID
        # print(
        #     f"UPDATE: new info for current room: {traversal_graph[current_room]}")
        # print(
        #     f"UPDATE: new info for current room: {traversal_graph[last_room_ID]}")
        print(f"AFTER: {traversal_graph}")
    last_room_ID = current_room

    """
    Knowing the current room, we can make our first breadcrumb.

    Cannot forget to travel...
    """

    if current_room not in traversal_graph:
        # traversal_graph[current_room] = { n}
        exits = player.current_room.get_exits()
        traversal_graph[current_room] = {direction: '?' for direction in exits}
        print(
            f"You've entered a new room, the exits are: {exits}")
        print(
            f"Added {current_room} to traversal graph. It now looks like: {traversal_graph}")

    # look in every direction from the room
    for direction in traversal_graph[current_room]:
        if traversal_graph[current_room][direction] == '?':
            print(
                f"In room {current_room}, found mysterious room to the {direction}")

            new_path = path + [direction]  # We do not have the id yet :(
            # we can figure out what direction needs to be taken by knowing the key and which path we took to get somewhere.
            bucket_list_stack.push(new_path)
