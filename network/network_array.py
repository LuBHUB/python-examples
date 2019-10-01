#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represent a simple network of nodes and connections between nodes.
This implementation uses a numpy array of ints as the main data structure.
"""

import numpy


class Network:
    """
    Simple representation of a network as an adjacency matrix.
    
    The attribute Network.adjMat stores the matrix as a numpy array.
    
    Add nodes and connections using methods:
    Network.add_node()
    Network.add_connection()
    """
    
    def __init__(self, nNodes):
        """
        Required arguments:
        nNodes -- int number of nodes in the network
        
        Nodes are initialized without connections.
        Add connections with Network.add_connection().
        """
        self.nNodes = nNodes
        self.adjMat = numpy.zeros((nNodes, nNodes), dtype=int)
    
    def __repr__(self):
        """
        Show the network's adjacency matrix.
        """
        return str(self.adjMat)
    
    def add_nodes(self, nNodes):
        """
        Add nNodes new nodes to the network.
        
        Required arguments:
        nNodes -- int number of nodes to add to the network
        
        Nodes are initialized without connections.
        Add connections with Network.add_connection().
        """
        for ax in range(2):
            shape = [nNodes, nNodes]
            shape[1-ax] = self.nNodes
            newPart = numpy.zeros(shape, dtype=int)
            self.adjMat = numpy.concatenate((self.adjMat, newPart), axis=ax)
            self.nNodes += nNodes
    
    def add_connection(self, nodeA, nodeB):
        """
        Add a new connection between nodeA and nodeB.
        
        Required arguments:
        nodeA, nodeB -- int ID numbers of nodes to connect
        """
        self.adjMat[nodeA, nodeB] = 1
        self.adjMat[nodeB, nodeA] = 1


class DirectedNetwork(Network):
    """
    Simple representation of a directed network as an adjacency matrix.
    
    Inherits from Network class (which represents an undirected network).
    Only the method DirectedNetwork.add_connection() differs.
    """
    
    def add_connection(self, nodeA, nodeB):
        """
        Add a new connection from nodeA to nodeB.
        
        Required arguments:
        nodeA, nodeB -- int ID numbers of nodes to connect
        """
        self.adjMat[nodeA, nodeB] = 1
