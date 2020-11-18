traversal_graph = {}
s = Stack()
visited = set()

starting_room = player.current_room.id
s.push([starting_room])

while s.size() > 0:
    path = s.pop()
    # travel_direction = path[-1] if not path[-1] == starting_room else None
    travel_direction = path[-1]
    # print(travel_direction)

    if travel_direction:
        # print(travel_direction)
        player.travel(travel_direction)

    current_room = player.current_room.id
    visited.add(current_room)
    # print(current_room)
    print(visited, current_room)

    if current_room not in traversal_graph:  # create the first entry for this room
        traversal_graph[current_room] = {
            direction: '?' for direction in player.current_room.get_exits()}

    for direction in traversal_graph[current_room]:
        if traversal_graph[current_room][direction] not in visited:
            s.push([direction])
