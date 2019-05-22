#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:08:36 2019

@author: mauro
"""
from random import choice

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

        
        
        
        
        
        
        
        