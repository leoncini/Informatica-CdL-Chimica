#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:33:10 2019

@author: mauro
"""

class studente:
    def __init__(self,nome,cognome,matricola,cds):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.cds = cds
        self.carriera = {}  # Dizionario le cui chiavi dovranno essere
                            # i nomi dei singoli esami
        
    def __str__(self):
        return 'Nome: '+self.nome+'\n'\
               'Cognome: '+self.cognome+'\n'\
               'Matricola: '+str(self.matricola)+'\n'\
               'Corso di Studio: '+self.cds
               
    def registra_esame(self, esame, voto, lode=False, CFU=None):
        pass
    
    def stampa_libretto(self):
        for esame in self.carriera:
            if self.carriera[esame][1]:
                print(esame+': 30 e lode')
            else:
                print(esame+': '+str(self.carriera[esame][0]))
                
    def cfu_conseguiti(self):
        pass