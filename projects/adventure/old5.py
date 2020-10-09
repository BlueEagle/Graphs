traversal_graph = {}
s = Queue()
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


while s.size() > 0:
    path = s.dequeue()
    travel_direction = path[-1] if not path[-1] == starting_room else None
    # travel_direction = path[-1]
    # print(travel_direction)

    if travel_direction:
        # print(travel_direction)
        # print(f"Travel direction {travel_direction}")
        player.travel(travel_direction)
        traversal_path.append(travel_direction)

    current_room = player.current_room.id
    visited.add(current_room)
    # print(current_room)
    # print(visited, current_room)

    if current_room not in traversal_graph:  # create the first entry for this room
        traversal_graph[current_room] = {
            direction: '?' for direction in player.current_room.get_exits()}

    if last_room:
        traversal_graph[current_room][reverse_direction(
            last_room[1])] = last_room[0]
        traversal_graph[last_room[0]][last_room[1]] = current_room
    last_room = (current_room, travel_direction)

    # print(traversal_graph[current_room], f"\n\n {current_room}")

    for direction in traversal_graph[current_room]:
        if traversal_graph[current_room][direction] not in visited:
            # print(traversal_graph[current_room][direction])
            # print(current_room, [direction])
            s.enqueue([direction])
