# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:23:16 2020

@author: Romain

Frequency Analysis 


"""
import rmSpaces

# CTEZ = "XBCEDBIFXGHJKLOMDUBIFNPQADURYCSTGFHCENUTABQMSIPVYSIQCPQLVGWXWHMSZKXJZGJWJSR"
# frequency analysis
englishFreq = ['e','t','a','o','n','r','i','s','h','d','l','f','c','m','u','g','y','p','w','b','v','k','x','j','q','z']

voyelles = ['e', 'a', 'o', 'i', 'u', 'y']
consonnes = ['t', 'n', 'r', 's', 'h', 'd', 'l', 'f', 'c', 'm', 'g', 'p', 'w', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
bigrams = ['th', 'he', 'an', 're', 'er', 'in', 'on', 'at', 'nd', 'st', 'es', 'en', 'of', 'te', 'ed']

def bigram_analysis(CT):
    big = {}
    CT = CT.lower()
    for i in range(len(CT)-1):
        if CT[i] + CT[i+1] not in big.keys():
            big[CT[i]+CT[i+1]] = 1
        else : 
            big[CT[i]+CT[i+1]] += 1
        
    sortedDict = {}
    for w in sorted(big, key = big.get, reverse = True):
        sortedDict[w] = big[w]
    
    return sortedDict

def trigrams_analysis(CT):
    tri = {}
    CT = CT.lower()
    for i in range(len(CT)-2):
        if CT[i] + CT[i+1] + CT[i+2] not in tri.keys():
            tri[CT[i]+CT[i+1]+CT[i+2]] = 1
        else : 
            tri[CT[i]+CT[i+1]+CT[i+2]] += 1
        
    sortedDict = {}
    for w in sorted(tri, key = tri.get, reverse = True):
        sortedDict[w] = tri[w]
    
    return sortedDict

def quatuor_analysis(CT):
    qua = {}
    CT = CT.lower()
    for i in range(len(CT)-3):
        if CT[i] + CT[i+1] + CT[i+2] + CT[i+3] not in qua.keys():
            qua[CT[i]+CT[i+1]+CT[i+2]+CT[i+3]] = 1
        else : 
            qua[CT[i]+CT[i+1]+CT[i+2]+CT[i+3]] += 1
        
    sortedDict = {}
    for w in sorted(qua, key = qua.get, reverse = True):
        sortedDict[w] = qua[w]
    
    return sortedDict



def freq_analysis(CT):
    #alphabet = [0 for i in range(0,26)]
    alphabet = {}
    CT = CT.lower()
    CT =rmSpaces.rm_space(CT)
    for i in CT:
        if i not in alphabet.keys():
            alphabet[i] = 1
            
        else : 
            alphabet[i] += 1
    
    sortedDict = {}
    for w in sorted(alphabet, key=alphabet.get, reverse=True):
        sortedDict[w] = alphabet[w]   
                  
    return sortedDict

def english_compare(CT):
    
    """precisions = input('Les voyelles sont-elles claires ? (y/n) ' )
    if precisions == 'y':
        CTV = input('rentre les lettres correspondantes aux voyelles : ')
        CTV = CTV.lower()
        CTVS = ""
        for i in CT:
            if i in CTV:
                CTVS += i
            
        freqvoyelles = dict(zip(freq_analysis(CTVS), voyelles))
        CTC = ""
        for i in CT:
            if i not in CTV:
                CTC += i
            
        freqconsonnes = dict(zip(freq_analysis(CTC), consonnes))
        freq_all = freqconsonnes
        freq_all.update(freqvoyelles)
        
        sortedDict = {}
        for w in sorted(freq_all, key=freq_all.get, reverse=True):
            sortedDict[w] = freq_all[w] 
        
        CT = CT.lower()
        PT = ""
        for i in CT:
            PT += freq_all[i]
            
    else :"""
    
    CTl = CT.lower()
    zipped = dict(zip(freq_analysis(CTl), englishFreq))
    PT = ""
    for i in CTl:
        PT += zipped[i]
        
    return PT





