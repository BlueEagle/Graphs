
def earliest_ancestor(ancestors, starting_node):
    # print(ancestors[0][1])

    # Unpack ancestors into dictionary
    g = {}
    for ancestor in ancestors:
        # add entry for ancestor
        if ancestor[1] not in g:
            g[ancestor[1]] = []
        
        # add ancestor to entry
        g[ancestor[1]].append(ancestor[0])
    
    # Check that ancestors dict looks right (child: [ancestor1, ancestor2])
    print(g)