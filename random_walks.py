#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:08:36 2019

@author: Mauro Leoncini

Example usage:
    S = genParticles(100)
    plotData(S)
    Brownian(S,1000)
    plotData(S)
    # You are encouraged play with the possible moves.
    # For instance add another (1,0) move, i.e., change 
    # possibleMoves in the particle class to [(1,0),(-1,0),(0,1),(0,-1),(1,0)]
    # and see what happens
"""
import pylab
from random import sample

STEPSIZE = 0.01
gridsize = 50

class particle:
    ''' Class that implements a single particle '''
    def __init__(self, x=0, y=0):
        self.startx = x
        self.starty = y
        self.x = x
        self.y = y
        
    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'
    
    def move(self, particles, moveController):
        from random import choice
        possibleMoves = [(1,0),(-1,0),(0,1),(0,-1)]
        actualMove = choice(possibleMoves)
        x = self.x+actualMove[0]
        y = self.y+actualMove[1]
        if moveController(x,y,particles):
            self.x = x
            self.y = y

    def distanceCovered(self):
        from math import sqrt
        dx = self.x - self.startx
        dy = self.y - self.starty
        return sqrt(dx**2+dy**2)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

def genParticles(n,center=True):
    ''' Generate n particles and pace them into a square grid of 
        size gridsize ''' 
    global gridsize
    if center:
        disp=int(gridsize/4)
    else:
        disp=0
    grid = []
    for  i in range(disp,gridsize-disp):
            for j in range(disp,gridsize-disp):
                grid.append((i,j))
    initialPositions = sample(grid,n)
    particles = []
    for p in initialPositions:
        particles.append(particle(p[0],p[1]))
    # The following is more pythonic
    # particles = [particle(x,y) for x,y in sample(grid,n)]
    
    #But place one particle in each corner as well
    particles.append(particle(0,0))
    particles.append(particle(0,gridsize-1))
    particles.append(particle(gridsize-1,0))
    particles.append(particle(gridsize-1,gridsize-1))
    return particles

def viableMove(x,y,particles):
    ''' Returns true if (x,y) is a free position in the grid '''
    global gridsize
    if x<0 or y<0 or x>=gridsize or y >=gridsize:
        return False
    for p in particles:
        if x == p.getX() and y == p.getY():
            return False
    return True

def Brownian(particles,nSteps,controller=viableMove):
    ''' Simulates nSteps steps of random movements of the particles
        in the grid. Uses the function controller to checke whether the
        movo il legal'''
    n = len(particles)
    for _ in range(nSteps):
        randomOrder = sample(particles,n)
        for p in randomOrder:
            p.move(particles, controller)
  
def plotData(S):
    x = [p.getX() for p in S]
    y = [p.getY() for p in S]
    pylab.xticks(range(0,gridsize,10))
    pylab.plot(x, y, 'bo', label = 'Random Walk')
