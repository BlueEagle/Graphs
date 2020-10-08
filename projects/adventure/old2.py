def reverse_direction(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'


s = Stack()
traversal_graph = {}

# later pushes to the stack should all be directions
s.push([player.current_room.id])
starting_room = player.current_room.id
while s.size() > 0:
    last_room_id = player.current_room.id
    path = s.pop()

    travel_direction = path[-1] if not path[-1] == starting_room else None
    if travel_direction:
        player.travel(travel_direction)
        # print(
        #     f"Traveled to room {player.current_room.id}, direction: {travel_direction} and the graph for this room looks like {traversal_graph}")

        # add to traversal path
    current_room = player.current_room.id
    print(
        f"Last room {last_room_id} Current room {current_room} Traversal graph {traversal_graph}")

    if current_room not in traversal_graph:
        traversal_graph[current_room] = {
            exit: '?' for exit in player.current_room.get_exits()}
        if travel_direction:
            traversal_graph[last_room_id][travel_direction] = current_room

    # we will add this one before all the others, it will be the last one processed
    last_room = reverse_direction(travel_direction)
    s.push(last_room)  # this should be at the front of the stack
    for mystery_room in traversal_graph[current_room]:
        if not mystery_room == last_room:
            s.push(mystery_room)

            """
            Missing:
             - updates to the traversal path
             - More printouts...
             - 
            """

            """
            Strange behavior:
             - looping
             - on return, the traversal graph is not being updated for the last room.
             - it is noticeably only happening to the south direction.
            """
