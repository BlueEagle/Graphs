traversal_graph = {}
s = Stack()
route_taken = Stack()
starting_room = player.current_room.id

s.push([starting_room])
route_taken.push([starting_room])
current_room = None

while s.size() > 0:
    path = s.pop()
    travel_direction = path[-1] if not path[-1] == starting_room else None

    if travel_direction:
        player.travel(travel_direction)
        current_room = player.current_room.id
        route_taken.push([current_room])  # updates route whenever we move
        print(current_room)

    if current_room not in traversal_graph:  # create the first entry for this room
        traversal_graph[current_room] = {
            direction: '?' for direction in player.current_room.get_exits()}

    if travel_direction:
        traversal_graph[]

    # if not current_room == starting_room:
        # print(route_taken.pop())
        # traversal_graph[]

    for direction in traversal_graph[current_room]:
        if traversal_graph[current_room][direction] == '?':
            s.push([direction])
