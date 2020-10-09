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

starting_room = player.current_room.id
last_room_id = None
mystery_room_found = True

while bucket_list_stack.size() > 0:
    path = bucket_list_stack.pop()
    travel_direction = path[-1] if not path[-1] == starting_room else None

    if travel_direction:
        if mystery_room_found:
            breadcrumbs_stack.push((travel_direction, player.current_room.id))
        player.travel(travel_direction)
    current_room = player.current_room.id

    if current_room not in traversal_graph:
        # traversal_graph[current_room] = { n}
        exits = player.current_room.get_exits()
        traversal_graph[current_room] = {direction: '?' for direction in exits}
        # print(
        #     f"You've entered a new room, the exits are: {exits}")
        # print(
        #     f"Added {current_room} to traversal graph. It now looks like: {traversal_graph}")

    if travel_direction and breadcrumbs_stack.size() > 0:
        last_room = breadcrumbs_stack.pop()
        last_room_direction = last_room[0]
        last_room_id = last_room[1]
        # print(
        #     f"Current room {current_room} Last room {last_room_id} Traversal graph {traversal_graph}")

        # traversal_graph[current_room][reverse_direction(
        #     travel_direction)] = last_room_id
        print(
            f"Last room id {last_room_id} Last room direction {last_room_direction} Current room {current_room}\n\n{traversal_graph}\n")
        traversal_graph[last_room_id][last_room_direction] = current_room
        traversal_graph[current_room][reverse_direction(
            last_room_direction)] = last_room_id

        # traversal_graph[last_room_id][travel_direction] = current_room
        breadcrumbs_stack.push(last_room)

    mystery_room_found = False
    # look in every direction from the room
    for direction in traversal_graph[current_room]:
        if traversal_graph[current_room][direction] == '?':  # if it is a mystery room
            new_path = path + [direction]
            bucket_list_stack.push(new_path)
            mystery_room_found = True

    if not mystery_room_found:
        last_room = breadcrumbs_stack.pop()
        move_direction = reverse_direction(last_room[0])
        bucket_list_stack.push(move_direction)

        # while bucket_list_stack.size() > 0:
        #     print(bucket_list_stack.pop())


print("\nBreadcrumbs:")
while breadcrumbs_stack.size() > 0:
    print(breadcrumbs_stack.pop())
