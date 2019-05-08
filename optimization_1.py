#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:48:33 2019

@author: mauro
"""

class Alimento:
    ''' Ogni alimento è caratterizzato da un nome, un valore e
        un numero di calorie per porzione. Il valore è un numero che
        indica una preferenza soggettiva. Quanto più è alto, tanto più
        l'alimento è gradito.
    '''
    def __init__(self, n, v, w):
        self.nome = n
        self.valore = v
        self.calorie = w
    def valrel(self):
        return self.valore/self.calorie
    def __str__(self):
        return self.nome + ': <' + str(self.valore)\
            + ', ' + str(self.calorie) + '>'
            
def Menu(file_alimenti):
    ''' Legge il file file_alimenti riga per riga.
        Si suppone che ogni riga contenga tre valori:
            nome del particolare alimento
            valore (un numero che costituisce preferenza "soggettiva")
            calorie per porzione
        Per ogni alimento (riga) viene creato un oggetto della
        classe Alimento e tutti tali oggetti vengono poi inseriti
        in una lista che è il valore restituito dalla funzione
    '''
    menu = []
    with open(file_alimenti) as f:
        for linea in f:
            nome,valore,calorie = linea.strip().split('\t')
            menu.append(Alimento(nome,float(valore),float(calorie)))
    return menu

def greedy(listaAlimenti, costoMax, criterio_di_preferenza):
    ''' Dapprima ordiniamo la lista degli alimenti secondo il
        criterio di preferenza, dal più alto al più basso
        (per questo viene secificato reverse=True).
        Poi, seguendo tale ordine, un determinato alimento
        viene aggiunto alla scelta se e solo se ci sono ancora
        abbastanza calorie disponibili
    '''
    listaOrdinata = sorted(listaAlimenti,key=criterio_di_preferenza,\
                           reverse=True)
    scelta = []
    valTotale, costoTotale = 0.0, 0.0
    for alimento in listaOrdinata:
        if costoTotale+alimento.calorie <= costoMax:
            scelta.append(alimento)
            costoTotale += alimento.calorie
            valTotale += alimento.valore
    return scelta, valTotale

def pref1(x):
    return x.valore

def pref2(x):
    return 1.0/x.calorie

def pref3(x):
    return x.valrel()

def powerSet(X):
    '''Data una lista X di n elementi, restituisce un generatore
       per il suo powerset, ovvero un "oggetto iterabile" I tale
       che, mediante successive chiamate next(I), restituisce tutti
       i possibili sottoinsiemi di X
       Utilizzo:
           Dapprima 
           I = powerSet(X)
       e, successivamente e ripetutamente,
           next(I)
    '''
    n = len(X)
    for i in range(2**n):
        S = []
        v = i
        j = 0
        while v != 0:
            if v%2 == 1:
                S.append(X[j])
            j += 1
            v = v >> 1
        yield S
        
def BruteForce(listaAlimenti, costoMax):
    ''' Determina la scelta ottimale analizzando tutte le
        possibili scelta, che sono in numero esponenziale
        rispetto al numero di alimenti
    '''
    n = len(listaAlimenti)
    valMax = 0.0
    for S in powerSet(listaAlimenti):
        val = 0.0
        cal = 0.0
        for a in S:
            val += a.valore
            cal += a.calorie
        if cal<=costoMax and val>valMax:
            scelta = S
            valMax = val
    return scelta, valMax

def timeAlgs(menu,calMax,pref):
    from time import perf_counter
    t0 =  perf_counter()
    scelta, valore = greedy(menu,calMax,pref)
    t1 = perf_counter() - t0
    print("Secondi impegati da greedy:",t1)
    t0 =  perf_counter()
    scelta, valore = BruteForce(menu,calMax)
    t1 = perf_counter() - t0
    print("Secondi impegati da BruteForce:",t1)
    
activities = [(6,10),(1,4),(12,16),(5,7),(8,12),(3,9),\
              (0,6),(5,9),(8,11),(3,5),(2,14)]