q = [[player.current_room]]
visited = set()

def reverse_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


while q.size() > 0:
    current_room = q[-1]

    if player.current_room.id not in visited:
        visited.add(player.current_room.id)

    exits = player.current_room.get_exits()
    
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {direction: '?' for direction in exits}
    
    """
        add the item to the path
        add the item to the traversal graph if it is not there.

        

        
        
    """

    # add the exits to the q
    
    # 