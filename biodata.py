#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:59:58 2019

@author: Mauro Leoncini
"""

GeneticCode = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                  
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_', 
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W', 
    } 

aminoacid = {"A": ("alanine", "ala"),
    "R": ("arginine", "arg"),
    "N": ("asparagine", "asn"),
    "D": ("aspartic acid", "asp"),
    "B": ("asparagine or aspartic acid", "asx"),
    "C": ("cysteine", "cys"),
    "E": ("glutamic acid", "glu"),
    "Q": ("glutamine", "gln"),
    "Z": ("glutamine or glutamic acid", "glx"),
    "G": ("glycine", "gly"),
    "H": ("histidine", "his"),
    "I": ("isoleucine", "ile"),
    "L": ("leucine", "leu"),
    "K": ("lysine", "lys"),
    "M": ("methionine", "met"),
    "F": ("phenylalanine", "phe"),
    "P": ("proline", "pro"),
    "S": ("serine", "ser"),
    "T": ("threonine", "thr"),
    "W": ("tryptophan", "trp"),
    "Y": ("tyrosine", "tyr"),
    "V": ("valine", "val")
    }

