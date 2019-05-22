#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:59:45 2019

@author: mauro
"""

class Node:
    def __init__(oggetto, name):
        """Assumes name is a string"""
        oggetto.name = name
        
    def getName(oggetto):
        return oggetto.name
    
    def __str__(oggetto):
        return oggetto.name
    
class Arc:
    def __init__(self, src, dest, weight=None):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
        self.weight = weight
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        repr = self.src.getName() + '->'\
            + self.dest.getName()
        if self.weight:
            repr += ' ('+self.weight+')'
        return repr
            
class Digraph:
    """arcs is a dict mapping each node to the list of adjacent nodes"""
    
    def __init__(self):
        self.arcs = {}
        
    def addNode(self, node):
        if node in self.arcs.keys():
            raise ValueError('Duplicate node')
        else:
            self.arcs[node] = []
            
    def addArc(self, arc):
        src = arc.getSource()
        dest = arc.getDestination()
        if not (src in self.arcs and dest in self.arcs):
            raise ValueError('Node not in graph')
        if dest in self.arcs[src]:
            raise ValueError('Duplicate arc')
        self.arcs[src].append(dest)
        
    def getNode(self, name):
        for node in self.arcs:
            if node.getName() == name:
                return node
        
    def connectedTo(self, node):
        return self.arcs[node]
        
    def __str__(self):
        result = ''
        for src in self.arcs:
            for dest in self.arcs[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1] # omit final newline

class Queue:
    def __init__(self):
        self.Q = []
    
    def isEmpty(self):
        return self.Q == []
    
    def enqueue(self,x):
        self.Q.append(x)
        
    def dequeue(self):
        return self.Q.pop(0)
    
    def __str__(self):
        return 'Head <- '+str(self.Q)+' <- Tail'
    
def buildCityGraph():
    g = Digraph()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',\
                 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addArc(Arc(g.getNode('Boston'), g.getNode('Providence')))
    g.addArc(Arc(g.getNode('Boston'), g.getNode('New York')))
    g.addArc(Arc(g.getNode('Providence'), g.getNode('Boston')))
    g.addArc(Arc(g.getNode('Providence'), g.getNode('New York')))
    g.addArc(Arc(g.getNode('New York'), g.getNode('Chicago')))
    g.addArc(Arc(g.getNode('Chicago'), g.getNode('Denver')))
    g.addArc(Arc(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addArc(Arc(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addArc(Arc(g.getNode('Denver'), g.getNode('New York')))
    g.addArc(Arc(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def printPath(path):
    if len(path) >= 1:
        print(path[0].getName(),end=' ')
    for i in range(1,len(path)):
        print('-> '+path[i].getName(),end=' ')
    print()

def BFS(G,start,end,verbose=False):
    ''' Uses a Queue to store and retrieve all the possible paths
        from start node, until one is found that leads to the end node
    '''
    # The Queue initially holds a path with the start node
    initialPath = [start]
    Q = Queue()
    Q.enqueue(initialPath)
    # End initialization of the Queue
    while not Q.isEmpty():  # If the Queue is not empty
        path = Q.dequeue()  # ... get the earliest inserted path 
        if verbose:
            print('Current path:', end=' ')
            printPath(path)
        last = path[-1]     
        if last == end:     # Check if the path is complete
            return path
        for succ in G.connectedTo(last): # Otherwise continue the path with
            if succ not in path:         # a suitable adjacent node to last
                Q.enqueue(path+[succ])
    return None

class Carbon:
    def __init__(self,id):
        self.id = id
        self.free_bonds = 4
    
    def identity(self):
        return 'C'+str(self.id)
    
    def __str__(self):
        return self.identity()
    
class Hydrogen:
    def __init__(self,id):
        self.id = id
        self.free_bonds = 1
    
    def identity(self):
        return 'H'+str(self.id)
    
    def __str__(self):
        return self.identity()
        
class Hydrocarbon:
    def __init__(self,name,nC=0,nH=0):
        self.name = name
        self.bonds = {}
        for i in range(1,nC+1):
            c = Carbon(i)
            self.bonds[c]=[]
        for i in range(1,nH+1):
            h = Hydrogen(i)
            self.bonds[h]=[]
    
    def getBonds(self):
        for b in self.bonds:
            print("{}: {}".format(b,self.bonds[b]))
        
    def getAtom(self,name):
        for atom in self.bonds:
            if atom.identity() == name:
                return atom
        return None
        
    def addBond(self,atom1,atom2):
        atom1 = self.getAtom(atom1)
        atom2 = self.getAtom(atom2)
        self.bonds[atom1].append(atom2)
        self.bonds[atom2].append(atom1)
            