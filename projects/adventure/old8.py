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
q = Queue()
visited = set()

q.enqueue(['s']) # this can be the first item of the list of exits.
# for exit in player.current_room.get_exits():
#             q.enqueue(exit)

while q.size() > 0:
    path = q.dequeue()
    direction = path[-1]
    print(direction)


    if player.current_room.id not in visited:
        visited.add(player.current_room.id)

    last_room_id = player.current_room.id
    player.travel(direction)
    print(f"Visited: {player.current_room.id} Set: {visited}")
    
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {direction: '?' for direction in player.current_room.get_exits()}

    traversal_graph[player.current_room.id][reverse_direction(direction)] = last_room_id
    print(traversal_graph)


    exit_found = False
    for exit in player.current_room.get_exits():
        if traversal_graph[player.current_room.id][exit] == '?':
            q.enqueue(path + [exit])
            exit_found = True

    print(path)
    new_path = []
    if not exit_found and not player.current_room.id == 0 :
        
        # for unit in path:
        #     new_path.append(reverse_direction(unit))
        # new_path.reverse()
        # q.enqueue(new_path)
        # print(new_path)