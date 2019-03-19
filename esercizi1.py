#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:19:05 2019

@author: mauro
"""

def mysqrt(x,eps=0.001):
    guess = x/2
    while guess**2-x<-eps or guess**2-x>eps:
        guess = (guess+x/guess)/2
    return guess

def match(T,P):
    n = len(T)
    m = len(P)
    if m>n:
        print("Non ci possono essere match del pattern nel testo")
    else:
        i = 0 # i è la variabile usata come in 
        while i<= n-m:
            j = 0
            while j<m and T[i+j] == P[j]:
                j = j+1
            if j == m:
                print("Match alla posizione", i)
            i = i+1

'''
def palindroma(s):
    n = len(s)
    for i in range(int(n/2)):
        if s[i] != s[n-i-1]:
            return False
    return True


def ordina(a,b,c):
    if a<b:
        if b<c:
            return a,b,c
        elif a<c:
            return a,c,b
        else:
            return c,a,b
    else:
        if c<b:
            return c,b,a
        elif c<a:
            return b,c,a
        else:
            return b,a,c
'''

def reverse(s):
    srev = ''
    for c in s:
        srev = c+srev
    return srev

def palindroma(s):
    return s==reverse(s)

def isprime(n):
    from math import sqrt
    for i in range(2,int(sqrt(n))):
        if n%i==0:
            return False
    return True

# Try 3231231231112151

def ordina(a,b,c,precede):
    if precede(a,b):
        if precede(b,c):
            return a,b,c
        elif precede(a,c):
            return a,c,b
        else:
            return c,a,b
    else: 
        if precede(a,c):
            return b,a,c
        elif precede(b,c):
            return b,c,a
        else:
            return c,b,a
  
