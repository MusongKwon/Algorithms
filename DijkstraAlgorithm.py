# Musong Kwon
# April 29, 2024
# Dijkstra's Algorithm

# make adjacency distance matrix
G = [[0, 0, 0, 0, 1, 0, 0, 10, 0, 0], # a
     [0, 0, 2, 0, 0, 0, 0,  0, 0, 0], # b
     [0, 0, 0, 0, 0, 0, 0,  0, 0, 0], # c
     [4, 0, 0, 0, 0, 0, 0,  1, 0, 0], # d
     [0, 0, 0, 0, 0, 3, 0,  0, 0, 0], # e
     [0, 1, 3, 0, 0, 0, 7,  0, 1, 0], # f
     [0, 0, 0, 0, 0, 0, 0,  0, 0, 0], # g
     [0, 0, 0, 0, 5, 0, 0,  0, 9, 0], # h
     [0, 0, 0, 0, 0, 0, 0,  0, 0, 2], # i
     [0, 0, 0, 0, 0, 0, 1,  0, 0, 0]] # j

# get user input for source node
source_node = int(input("Enter a source node(0 for a, 1 for b, ... , 9 for j) : "))

no_parent = -1
def dijkstra_algorithm(G, s):
    # initialize current distance and visited nodes
    currDist = [float("inf") for _ in range(len(G))]
    visited = [False for _ in range(len(G))]

    # initialize current distance of source node
    currDist[s] = 0

    # for printing path
    parents = [-1 for _ in range(len(G))]
    parents[s] = no_parent

    for i in range (1, len(G)):
        # min distance vertex
        vDist = float("inf")
        v = -1
        for i in range(len(G)):
            if currDist[i] < vDist and not visited[i]:
                vDist = currDist[i]
                v = i
        
        # mark the one visited
        visited[v] = True

        # update current distance
        for u in range(len(G[v])):
            if G[v][u] > 0 and currDist[u] > currDist[v] + G[v][u]:
                parents[u] = v
                currDist[u] = currDist[v] + G[v][u]
    
    # print result
    print_sol(s,currDist, parents)
        
    
def print_sol(s, currDist, parents):
    for i in range(len(G)):
        if i != s:
            print("Distance from source node, ", s, " to node ", i, ": ", currDist[i])
            print("Path: ")
            print_path(i, parents)
            print("------------------------------------------------")


def print_path(i, parents):
    if i == no_parent:
        return
    print_path(parents[i], parents)
    print(i)
    

dijkstra_algorithm(G, source_node)