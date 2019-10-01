#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Represent a simple network of nodes and connections between nodes.
This implementation uses a dict of sets as the main data structure.
"""


class Network:
    """
    Simple representation of a network as a dictionary of nodes.
    
    The attribute Network.dict stores the network data as a dictionary.
    
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
        self.dict = {node:set() for node in range(nNodes)}
    
    def __repr__(self):
        """
        Show the network's dictionary of nodes.
        """
        return str(self.dict)
    
    def add_nodes(self, nNodes):
        """
        Add nNodes new nodes to the network.
        
        Required arguments:
        nNodes -- int number of nodes to add to the network
        
        Nodes are initialized without connections.
        Add connections with Network.add_connection().
        """
        self.dict.update({node:set() for node in range(self.nNodes, self.nNodes+nNodes)})
        self.nNodes += nNodes
    
    def add_connection(self, nodeA, nodeB):
        """
        Add a new connection between nodeA and nodeB.
        
        Required arguments:
        nodeA, nodeB -- int ID numbers of nodes to connect
        """
        self.dict[nodeA].add(nodeB)
        self.dict[nodeB].add(nodeA)


class DirectedNetwork(Network):
    """
    Simple representation of a directed network as a dictionary of nodes.
    
    Inherits from Network class (which represents an undirected network).
    Only the method DirectedNetwork.add_connection() differs.
    """
    
    def add_connection(self, nodeA, nodeB):
        """
        Add a new connection from nodeA to nodeB.
        
        Required arguments:
        nodeA, nodeB -- int ID numbers of nodes to connect
        """
        self.dict[nodeA].add(nodeB)


#%% Tests

if __name__ == '__main__':
    
    # Network.
    myNet = Network(2)
    print(myNet)
    myNet.add_nodes(2)
    print(myNet)
    myNet.add_connection(0, 2)
    print(myNet)
    
    # DirectedNetwork
    myDirNet = DirectedNetwork(4)
    print(myDirNet)
    myDirNet.add_connection(0, 2)
    print(myDirNet)
