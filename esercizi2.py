#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:26:07 2019

@author: mauro
"""



y = 10

def f(x):
    '''
        Funzione  di esempio per illustrare
        ambiente locale di una funzione 
        e ambiente globale dell'interprete
    '''
    x = x+1
    y = 2*x
    print('in f(x): x =', x)
    print('in f(x): y =', y)
    return x

DatiTemp = {'gen': ( 1.2, 4.2, 9.9, 3.5),
            'feb': (1.8, 4.0, 12.0, 3.9),
            'mar': (4.4, 3.5, 16.1, 4.5),
            'apr': (7.2, 3.0, 19.8, 4.3),
            'mag': (11.4, 2.8, 25.1, 4.2),
            'giu': (15.2, 2.8, 30.0, 4.3),
            'lug': (17.2, 2.5, 32.7, 3.8),
            'ago': (17.6, 2.6, 33.2, 3.8),
            'set': (13.9, 3.4, 27.0, 4.1),
            'ott': (10.3, 3.7, 21.8, 3.9),
            'nov': (6.0, 4.2, 14.6, 4.3),
            'dic': (2.5, 4.2, 10.5, 3.6)}

mesi = ('gen', 'feb', 'mar', 'apr', 'mag', 'giu',
        'lug', 'ago', 'set', 'ott', 'nov', 'dic')

def GenTemp(mese,N=12):
    '''
        Genera, "a caso" ma in modo realistico,
        temperature minime e massime per il 
        mese in questione
    '''
    from random import random
    from math import sqrt
    avgm,stdm,avgM,stdM = DatiTemp[mese]
    tmin = 0.0
    for _ in range(N):
        tmin += random()
    tmin = stdm*(tmin-N/2)/sqrt(N/12)+avgm
    tmax = 0.0
    for _ in range(N):
        tmax += random()
    tmax = stdM*(tmax-N/2)/sqrt(N/12)+avgM
    return round(tmin*100)/100, round(tmax*100)/100

