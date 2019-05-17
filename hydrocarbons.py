#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:54:03 2019

@author: mauro
"""

class Carbon:
    def __init__(self,id):
        self.id = id
        self.free_bonds = 4
        
    def identity(self):
        return 'C'+str(self.id)
    
    def __str__(self):
        return self.identity()
    
    def getFreeBonds(self):
        return self.free_bonds
    
    def reduceFreeBonds(self):
        if self.free_bonds>0:
            self.free_bonds = self.free_bonds-1 
            
class Hydrogen:
    def __init__(self,id):
        self.id = id
        self.free_bonds = 1
        
    def identity(self):
        return 'H'+str(self.id)
    
    def __str__(self):
        return self.identity()
    
    def getFreeBonds(self):
        return self.free_bonds
    
    def reduceFreeBonds(self):
        if self.free_bonds>0:
            self.free_bonds = self.free_bonds-1    
    
class Hydrocarbon:
    def __init__(self,name,nC=0,nH=0):
        self.name = name
        self.bonds = {}
        for i in range(1,nC+1):
            c = Carbon(i)
            self.bonds[c] = []
        for i in range(1,nH+1):
            h = Hydrogen(i)
            self.bonds[h] = []
    
    def getAtom(self,identity):
        for atom in self.bonds.keys():
            if atom.identity() == identity:
                return atom
    
    def getBonds(self):
        for atom,bonds in self.bonds.items():
            s = atom.identity()+': '
            for a in bonds:
                s = s+a.identity()+', '
            print(s[:-2])
            
    def addBond(self,atom1,atom2):
        a1 = self.getAtom(atom1)
        a2 = self.getAtom(atom2)
        if a1.getFreeBonds() == 0 or\
           a2.getFreeBonds() == 0:
            raise ValueError('No other bond admitted')
        self.bonds[a1].append(a2)
        self.bonds[a2].append(a1)
        a1.reduceFreeBonds()
        a2.reduceFreeBonds()
        
    def checkBonds(self):
        for atom in self.bonds.keys():
            if atom.getFreeBonds()>0:
                return False
        return True