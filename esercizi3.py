#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:08:36 2019

@author: Mauro Leoncini
"""

dnaseq = 'ACATGATGACCAAGAACCTGGCAGGAAAGACCCCGACGGACCTGGTGCA'+\
         'GCTCTGGCAGGCTGATACCCGGCACGCCCTGGAGCATCCTGAGCCGGGG'+\
         'GCTGAGCATAACGGGCTGGAGGGGCCTAATGATAGTGGGCGAGAGACCC'+\
         'CTCAGCCTGTGCCAGCCCAGTGAATGCGTCAATAAAAAAGCTGTTTTTG'+\
         'CTAAAAAAAAAAAAAAAAAAA'
  
def transcription(dnaseq, start, stop):
    rnaseq = ""
    for n in dnaseq[start:stop]:
        if n == 'T':
            rnaseq += 'U'
        else:
            rnaseq += n
    return rnaseq

def translation(rnaseq, start, stop):
    from mylib.biodata import GeneticCode
    proteinseq = ''
    stop = stop-(stop-start)%3
    for i in range(start,stop,3):
        proteinseq += GeneticCode[rnaseq[i:i+3]]
    return proteinseq

class dna():
    
    def __init__(self,sequence=''):
        self.sequence = sequence+'$'
        self.length = len(sequence)
        
    def __str__(self):
        return "5': "+self.sequence[:-1] + " 3'"
        
    def transcription(self,start=0,stop=-1):
        rnaseq = ""
        for n in self.sequence[start:stop]:
            if n == 'T':
                rnaseq += 'U'
            else:
                rnaseq += n
        return rnaseq
    
    def translation(self,start=0,stop=-1):
        from mylib.biodata import GeneticCode
        rnaseq = self.transcription(start,stop)
        stop = len(rnaseq)-len(rnaseq)%3
        proteinseq = ''
        for i in range(0,stop,3):
            codon = rnaseq[i:i+3]
            proteinseq  += GeneticCode[codon]
        return proteinseq
    
    def revcomp(self):
        seq = ''
        for i in range(self.length-1,-1,-1):
            seq += {'A':'T','C':'G','G':'C','T':'A'}[self.sequence[i]]
        return seq
    
    def k_nucleotide(self,k):
        d = {}
        for i in range(self.length-k+1):
            a = self.sequence[i:i+k]
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        return d
    
    def from_fasta(self,file):
        from Bio import SeqIO
        seq = str(next(SeqIO.parse(file, "fasta")).seq)
        self.__init__(seq)
        
    
def sommacomplessi(x,y):
    return complesso(x.re+y.re,x.img+y.img)          
       
class complesso():
    def __init__(self, re, img):
        self.re = re
        self.img = img
        
    def __str__(self):
        if self.img==0:
            return str(self.re)
        elif self.img<0:
            return str(self.re)+str(self.img)+'i'
        else:
            return str(self.re)+'+'+str(self.img)+'i'
        
    def __mul__(self,z):
        re = self.re*z.re-self.img*z.img
        img = self.re*z.img+self.img*z.re
        return complesso(re,img)
    
    def __add__(self,z):
        return complesso(self.re+z.re,self.img+z.img)
    
    def conjugate(self):
        z = complesso(self.re,-self.img)
        return z

    
