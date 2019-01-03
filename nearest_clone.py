#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#


from collections import defaultdict

def createGraph(graph_from, graph_to):
    g = defaultdict(list)
    for i, n in enumerate(graph_from):
        g[n].append(graph_to[i])
        g[graph_to[i]].append(n)
    return g


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    
    # Return -1 if no other val exists in ids
    if ids.count(val) < 2:
        return -1

    # Create a graph if 2 or more 'val' present in ids
    g = createGraph(graph_from, graph_to)
    sp = float("inf") # initialise path_length = infinity
    starts = [] # list of nodes with color 'val'

    for i, x in enumerate(ids):
        # i+1 is the node
        # x is the color of the node
        if x == val:
            starts.append(i+1)

    # Find nodes which 'val' is connected to for each node with color 'val' 
    # Keep traversing until all nodes have been visited
    for s in starts:
        visited = set([s])
        queue = []
        # g is the whole graph
        # g[s] is each part(which in itself is a list) of the graph's dict connections
        for n in g[s]:
            queue.append((n,1)) 

        print(queue)
        while queue:
            
            n,d = queue.pop(0)
            if n in visited:
                continue
            visited.add(n)

            # check the path length when same colour is found
            # n is the node position
            # ids[n-1] because list starts from 0 whereas node position from 1
            if ids[n-1] == val:
                sp = min(sp,d)  # Take the smaller path
                break
            
            # check in that node 'n' for any further connection
            # appending those connections in the queue
            for nn in g[n]:
                queue.append((nn,d+1))
                
    return sp

        
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
