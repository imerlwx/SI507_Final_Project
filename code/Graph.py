from collections import defaultdict
from FindIndex import FindIndex
from OpenCache import OpenCache
from ReadFile import GetSizeOfFile

class Graph():
    '''

    This class is to define some attributes and methods for a graph
    
    '''

    def __init__(self, destinationList, distanceCacheName, totalLocationFile):
        
        """
        Parameters:
        ---------- 
        destinationList: list
            the destination list that contains some or all the destination index in the total destinations
        
        distanceCacheName: string
            the json name that contains all the distance information
        
        totalLocationFile: string
            the file that contains all the specfic locations

        Returns
        -------
        
        self.edges: default dict
            all possible next nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}

        self.weights: dict
            weights between two nodes, with the two nodes as a tuple as the key e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}

        self.nodes: list
            a list contains the destinations that will go

        self.totalDestinationNum: int
            the number of all the destinations that could choose
        
        self.edgeList: list
            a list that contain multiple tuples like (locationA, locationB, distanceBetweenAAndB)

        self.edgeMatrix: matrix
            a matrix that edgeMatrix[i][j] represent the distance between location[i] and location[j]

        self.edgeDict: dict
            same as self.edges
        """
        self.edges = defaultdict(list)
        self.nodes = [x - 1 for x in destinationList]
        self.totalDestinationNum = GetSizeOfFile(totalLocationFile)
        self.edgeList = self.GetEdges(distanceCacheName)
        self.edgeMatrix = self.GetNodeMatrix()
        self.weights = {}
        self.edgeDict = self.GetEdgesDict()
    
    def add_edge(self, from_node, to_node, weight):
        '''
        This function is to build all the edges for the graph

        Parameters:
        ---------- 
        from_node, to_node: int
            add a edge between edges[from_node] to edges[to_node]
        
        weight: int
            the distance between edges[from_node] to edges[to_node]

        Returns
        -------
        None
        
        '''
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def GetEdges(self, distanceCacheName):
        '''
        This function is to build all the edges for the graph

        Parameters:
        ---------- 
        distanceCacheName: string
            the json name that contains all the distance information

        Returns
        -------
        edges: default dict
            all possible next nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        
        '''
        edges = []
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                index = FindIndex(self.nodes[i], self.nodes[j], self.totalDestinationNum)
                distance = OpenCache(distanceCacheName, index)["rows"][0]["elements"][0]["distance"]["value"]
                edges.append((self.nodes[i], self.nodes[j], distance))

        return edges

    def GetNodeMatrix(self):
        '''
        This function is to build the node matrix for the graph

        Parameters:
        ---------- 
        None

        Returns
        -------
        self.edgeMatrix: matrix
            a matrix that edgeMatrix[i][j] represent the distance between location[i] and location[j]
        
        '''
        nodeMatrix = [[0 for val in range(len(self.nodes))] for val in range(len(self.nodes))]
        for x, y, val in self.edgeList:
            nodeMatrix[self.nodes.index(x)][self.nodes.index(y)] = nodeMatrix[self.nodes.index(y)][self.nodes.index(x)] =  val
        
        return nodeMatrix
    
    def GetEdgesDict(self):
        '''
        This function is to build the node dictionary for the graph

        Parameters:
        ---------- 

        Returns
        -------
        self.edges: default dict
            all possible next nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        
        '''
        for edge in self.edgeList:
            self.add_edge(*edge)

        return self.edges