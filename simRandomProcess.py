#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:08:36 2019

@author: mauro
"""
from random import choice
import matplotlib.pyplot as plt
import pylab
STEPSIZE = 0.01

def rollDie(): 
    """returns a random int between 1 and 6"""
    return choice([1,2,3,4,5,6])    

def testRoll(n = 10):
    """Ruturns a string with the results of 
       n die rolls
    """
    result = ''
    for i in range(n):
        result = result + ', ' + str(rollDie())
    return result[2:]

def runSim(goal, numTrials, txt):
    """ Simulates numTrials experiments, each one
        represented by len(goal) die rolls. Counts
        the number of experiments that give 
        goal as results in order to estimate its
        probability of occurrence. Prints estimated
        and theoretical probabilities.
    """
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=',
    round(1/(6**len(goal)), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated Probability of', txt, '=',
    round(estProbability, 8))
     
def checkCoin(N = 1000):
    """ Simulates N coin tosses """
    nH = 0  
    for _ in range(N):
        if rollDie() == 'H':
            nH += 1 
    return abs(nH/N-0.5)

def checkOnes(N=1000):
    """ Estimates the probability of the event
        'At least one 1 in five die rolls'
    """
    n = 0
    for _ in range(N):
        r = testRoll(5)
        if r.find('1')!=-1:
            n += 1
    return n/N
    
def sameDate(numPeople, numSame):
    """ Simulates the experiment of picking numPeople
        at random and checking if there is one or
        more subgroups of at least numSame people
        born the same day
    """
    possibleDates = list(range(366))
    birthdays = [0]*366
    for p in range(numPeople):
        birthDate = choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame
        
        
def findProb(N=1000, numPeople=20, numSame=2):
    """ Estimates the probability of having one or
        more subgroups of at least numSame people
        born the same day
    """ 
    nS = 0
    for _ in range(N):
        if sameDate(numPeople,numSame):
            nS += 1
    return nS/N

class particle:
    def __init__(self, x=0, y=0):
        self.startx = x
        self.starty = y
        self.x = x
        self.y = y
        
    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'
    
    def move(self, particles):
        from random import choice
        global STEPSIZE
        possibleMoves = [(STEPSIZE,0),(-STEPSIZE,0),(0,STEPSIZE),(0,-STEPSIZE)]
        actualMove = choice(possibleMoves)
        x = self.x+actualMove[0]
        y = self.y+actualMove[1]
        if particles.freeSpace(x,y):
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

'''
def distanceEstimation(numberOfMoves, numberOfExperiments):
    sumDistance = 0
    for i in range(numberOfExperiments):
        p = particle()
        for j in range(numberOfMoves):
            p.move()
        sumDistance += p.distanceCovered()
    return sumDistance/numberOfExperiments
'''

def distanceEstimation(numberOfMoves, numberOfExperiments):
    from math import sqrt
    distances = []
    for i in range(numberOfExperiments):
        p = particle()
        for j in range(numberOfMoves):
            p.move()
        distances.append(p.distanceCovered())
    average = sum(distances)/numberOfExperiments
    std = 0
    for d in distances:
        std = std + (d-average)**2
    std = sqrt(std/numberOfExperiments)
    return average, std

class SetOfParticles:
    
    def __init__(self, n, d, center=True):
        from random import sample
        global STEPSIZE
        if center:
            disp=int(d/4)
        else:
            disp=0
        SP = []
        for  i in range(disp,d-disp):
            for j in range(disp,d-disp):
                SP.append((i,j))
        I = sample(SP,n)
        #I = sample([(int(i/d),i%d) for i in range(d**2)],n)
        self.d = d*STEPSIZE
        self.particles = [particle(i*STEPSIZE,j*STEPSIZE) for i,j in I]
        #Also place one particle in each corner
        self.particles.append(particle(0,0))
        self.particles.append(particle(0,(d-1)*STEPSIZE))
        self.particles.append(particle((d-1)*STEPSIZE,0))
        self.particles.append(particle((d-1)*STEPSIZE,(d-1)*STEPSIZE))
        
    def freeSpace(self, x, y):
        """ - check whether position is not occupied by
              any particle
        """
        if x>=self.d or y>=self.d or x<0 or y<0:
            return False
        for p in self.particles:
            if x == p.getX() and y == p.getY():
                return False
        return True
    
    def getParticle(self,i):
        return self.particles[i]

    def Brownian(self, nSteps=1):
        from random import sample
        n = len(self.particles)
        for _ in range(nSteps):
            for i in sample(range(n),n):
                self.particles[i].move(self)
                
    def __str__(self):
        r = ''
        for p in self.particles:
            r += '<'+str(p.getX())+','+str(p.getY())+'>'
        return r    
  
def plotData(S):
    x = [S.particles[i].getX() for i in range(len(S.particles))]
    y = [S.particles[i].getY() for i in range(len(S.particles))]
    pylab.plot(x, y, 'bo', label = 'Random Walk')

def simulate(S, nSteps, animate=False, pltsize=8, slow=3):
    from time import sleep
    if not animate:
        S.Brownian(nSteps)
    else:
        plt.ion()
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111)
        x = [S.particles[i].getX() for i in range(len(S.particles))]
        y = [S.particles[i].getY() for i in range(len(S.particles))]
        line1, = ax.plot(x, y, 'bo')
        for _ in range(nSteps-1):
            sleep(2)
            S.Brownian()
            x = [S.particles[i].getX() for i in range(len(S.particles))]
            y = [S.particles[i].getY() for i in range(len(S.particles))]
            line1.set_xdata(x)
            line1.set_ydata(y)
            fig.canvas.draw()
              