# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:28:43 2020

@author: Romain

Index of coincidence
"""

import freqAnalysis
import rmSpaces

def index_of_coincidence(CT):
    CT = rmSpaces.rm_space(CT)
    N = len(CT)
    freq = freqAnalysis.freq_analysis(CT)
    IC = 0
    for i in freq:
        IC += (freq[i]*(freq[i] -1))
        
    IC = IC /(N*(N-1))
    
    typeCipher = ""
    
    if IC > 0.06 :
        typeCipher = "Monoalphabetic"
    elif (0.05 < IC) and (IC < 0.06):
        typeCipher = "either mono or poly alphabetic"
    elif (0.04 < IC) and (IC < 0.046):
        typeCipher = "Probably Vigenere"
    elif (IC < 0.05) and (typeCipher != "Probably Vigenere"):
        typeCipher = "Polyalphabetic"
        
            
    return (IC, typeCipher)

    
#if IC around 0.067 --> Monoalphabetic substitution

#if IC < 0.5 --> Polyalphabetic substitution
    
#if IC = 0.042 --> Vigenere Cipher
    
