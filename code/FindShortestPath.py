from sys import maxsize
from itertools import permutations
 
# implementation of traveling Salesman Problem
def FindShortestPath(graph, startLoc):
    '''
    
    This function is to find the shortest path given the Graph object and start location

    Parameters:
    ---------- 
    graph: Graph object
        the Graph object that includes everything needed to find the shortest path
    
    startLoc: int
        the user's choice that want to start at

    Returns
    -------
    minPath: list
        the list that contains the shortest path

    shortestDistance: int
        the distance of the shortest path
    
    '''

    if (startLoc - 1) not in graph.nodes:
        print('The start location is not in the destination list! ')
        return [], maxsize

    startLocIndex = graph.nodes.index(startLoc - 1)
    numVertex = len(graph.nodes)
    # store all vertex apart from source vertex
    vertex = []
    for i in range(numVertex):
        if i != startLocIndex:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    shortestDistance = maxsize
    next_permutation=permutations(vertex)

    minPath = ()
    
    for i in next_permutation:
 
        # store current Path weight(cost)
        currentDistance = 0
 
        # compute current path weight
        k = startLocIndex
        for j in i:
            currentDistance += graph.edgeMatrix[k][j]
            k = j
        #currentDistance += graph.edgeMatrix[k][startLocIndex]
 
        # update minimum
        if currentDistance < shortestDistance:
            shortestDistance = currentDistance
            minPath = i
        
    minPath = [startLocIndex] + list(minPath)
    
    return minPath, shortestDistance