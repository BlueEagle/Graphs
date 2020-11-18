def maze_explore(starting_room, last_room=None, visited=set(), traversal_graph={}):
    if not starting_room in visited:
        player.travel(starting_room)
        traversal_path.append(starting_room)

        print(starting_room)
        visited.add(starting_room)

        if starting_room not in traversal_graph:
            traversal_graph[starting_room] = {
                exit: '?' for exit in player.current_room.get_exits()}

        if last_room:
            pass

        for direction in player.current_room.get_exits():
            print(direction)
            if traversal_graph[player.current_room.id][direction] == '?':
                maze_explore(direction)


maze_explore(player.current_room.id)
