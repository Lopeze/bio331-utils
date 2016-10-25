'''
Erik Lopez

Graph Functions
-create_deg(nodes,edges)-> dictionary
-biggest_deg(nodes,node:value pair)-> node, node degree
-rm_dup(edges)-> edges
-rm_selfloop(edges)-> edges


'''

def create_deg(nodes, edges, directed = False):
    '''
    This function creates a dictionary of node:degree pairs for input graph

    Input:
        1. nodes
        2. edges
        3. if graph is directed or not
    Return:
        A dictionary that represents node and their degrees
        (nodes = key, degree = value)
    '''

    node_deg = {}
    for node in nodes:
        node_deg[node] = 0
        for edge in edges:
            if directed == False:
                if node in edge:
                    node_deg[node] += 1
            else:
                if node == edge[1]:
                    node_deg[node] += 1
    return node_deg

def biggest_deg(diction):
    '''
    This function looks at the list of nodes and finds the node with the largest
    degree
    
    Input:
        dictionary of node:degree pairs
    Return:
        the node from the dictionary with the highest degree
    '''
    highdeg = 0
    highnode = ''
    for n in diction:
        if diction[n] > highdeg:
            highdeg = diction[n]
            highnode = n
    return [highnode, highdeg]


def rm_dup(edges):
    '''
    This function goes through the list of edges deleting duplicate edges in
    the graph.

    Input:
        A list of edges
    Return:
        A list of edges with no duplicate entries
    '''
    for i in range(0,len(edges)):
        for x in edges[i::]:
            if edges[i] == x:
                edges.remove(x)
    return edges

def rm_selfloop(edges):
    '''
    This function goes through the list of edges deleting self loops in graph

    Input:
         A list of edges
    Return:
         A list of edges with no self loops
    '''
    print("Before removing self loops we have: %d edges" % len(edges))
    for edge in edges:
        if edge[0] == edge[1]:
            edges.remove(edge)
    print("After removing self loops we have: %d edges" % len(edges))
    return edges
