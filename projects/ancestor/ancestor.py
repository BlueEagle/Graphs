from util import Queue

def earliest_ancestor(ancestors, starting_node):
    ancestor_list = ancestors
    # print(ancestors_list)

    # Unpack ancestors_list into dictionary
    ancestors = {}
    for item in ancestor_list:
        # add entry for ancestor
        if item[1] not in ancestors:
            ancestors[item[1]] = []
        
        # add ancestor to entry
        ancestors[item[1]].append(item[0])
    
    # Check that ancestors dict looks right (child: [ancestor1, ancestor2])
    # print(ancestors)

    # Returns early if the node is not found in the graph, or it it has no parents
    if starting_node not in ancestors or len(ancestors[starting_node]) == 0:
        return -1

    q = Queue()
    q.enqueue(starting_node)
    level = {}
    while q.size() > 0:
        current_node = q.dequeue()
        # print(f"Current node: {current_node} {level}")

        # If the current node does not have a level,
        # add one. This should only happen on the first run.
        if current_node not in level:
            level[current_node] = 1
            # print(f"Adding level to node: {level[current_node]}")

        if current_node in ancestors:
            for ancestor in ancestors[current_node]:
                level[ancestor] = level[current_node] + 1
                q.enqueue(ancestor)

    # Check to see if we have a dictionary with levels
    # print(level)

    highest_level = [-1, -1] # [key, level]
    for key in level:
        # print(level[key])
        # if current level is higher, update var. If they are the same and the current key is lower, update var
        if level[key] > highest_level[1] or (level[key] == highest_level and key < highest_level[0]): 
            highest_level = [key, level[key]]
    
    # print(highest_level[0])
    return highest_level[0]