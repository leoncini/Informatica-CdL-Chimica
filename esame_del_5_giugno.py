#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:03:06 2019

@author: Mauro Leoncini
"""

def campione_casuale():
    from random import random
    from math import sqrt
    N = 12
    media = 34 #in migliaia di euro
    std = 8
    while True:
        r = 0.0
        for _ in range(N):
            r += random()
        r = std*(r-N/2)/sqrt(N/12)+media
        yield round(r*100000)/100
            
rilevazione = campione_casuale()

# Implementare la seguente funzione
def RedditoLaureati(n):
    ''' La funzione deve stimare la media del reddito dei laureati 
        italiani utilizzando un campione di n soggetti.
        Per ottenere una rilevazione, si utilizzi l'istruzione
        R = next(rilevazione)
        Bonus: calcolare anche la deviazione standard
    '''
    global rilevazione
    # Inserire qui il proprio codice
        