# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:13:28 2020

@author: Romain

Vigenere cryptanalysis

"""
import collections
import freqAnalysis
import indexOfCoincidence
import cesar
import itertools

def key_length(CT):
    quatuor = freqAnalysis.quatuor_analysis(CT)
    big4 = {}
    for i in quatuor:
        if quatuor[i] != 1:
            big4[i] = i
    
    #return rank when a quatuor of letter appears if it appears several times
    CT = CT.lower()
    occur = {}
    for i in big4:
        occur[i] = []
        for j in range(len(CT)-3):
            if CT[j] + CT[j+1] + CT[j+2] + CT[j+3] == i:
                occur[i].append(j)
    
    #return distance between the same quatuor for each quatuor
    dist = {}
    
    for i in occur:
        dist[i] = []
        for j in range(len(occur[i])-1):
            dist[i].append(occur[i][j+1] - occur[i][j])
      
    #return factors of the distance 
    fact = {}
    for i in dist:
        fact[i] = []
        for j in range(len(dist[i])):
            for k in range(2,dist[i][j]):
                if dist[i][j] % k == 0:
                    fact[i].append(k)
    
    #return factor by order of appearence between all of the quatuor
    l = []
    score = {}
    for i in fact:
        for j in range(len(fact[i])):
            if fact[i][j] in l:
                score[fact[i][j]] += 1
            else :
                l.append(fact[i][j])
                score[fact[i][j]] = 1
                
    sorted_score = collections.OrderedDict(sorted(score.items()))
    score = dict(sorted_score)
    
    best_occur = []
    max_val = max(score.values())
    for i in score:
        if score[i] == max_val:
            best_occur.append(i)
        
    
    return occur,dist, fact, score, best_occur


def sub_text(CT,keyL):
    subText ={}
    for j in range(keyL):
        subText[j] = ""
        for i in range(j,len(CT),keyL):
            subText[j] += CT[i]
    
    fr = {}
    freq = {}        
    IC = {}
    PTs = {}
    for i in subText:
        fr[i] = freqAnalysis.freq_analysis(subText[i])
        IC[i] = indexOfCoincidence.index_of_coincidence(subText[i])
        freq[i] = next(iter(freqAnalysis.freq_analysis(subText[i]).items()))
    
    
    dist = {}
    for i in freq:
        dist[i] = (ord('e')-ord(freq[i][0]))
        PTs[i] = cesar.cesar(subText[i],dist[i])
    
    
    freq2 = {}   
    for i in subText:
        freq2[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[1], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[1])
    dist2 = {} 
    PTs2 = {}
    for i in freq:
        dist2[i] = (ord('e') - ord(freq2[i][0]))
        PTs2[i] = cesar.cesar(subText[i],dist2[i])
        
    freq3 = {}   
    for i in subText:
        freq3[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[2], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[2])
    dist3 = {} 
    PTs3 = {}
    for i in freq:
        dist3[i] = (ord('e') - ord(freq3[i][0]))
        PTs3[i] = cesar.cesar(subText[i],dist3[i])
        
    freq4 = {}   
    for i in subText:
        freq4[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[3], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[3])
    dist4 = {} 
    PTs4 = {}
    for i in freq:
        dist4[i] = (ord('e') - ord(freq4[i][0]))
        PTs4[i] = cesar.cesar(subText[i],dist4[i])
    
    freq5 = {}   
    for i in subText:
        freq5[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[4], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[4])
    dist5 = {} 
    PTs5 = {}
    for i in freq:
        dist5[i] = (ord('e') - ord(freq5[i][0]))
        PTs5[i] = cesar.cesar(subText[i],dist5[i])
        
    freq6 = {}   
    for i in subText:
        freq6[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[5], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[5])
    dist6 = {} 
    PTs6 = {}
    for i in freq:
        dist6[i] = (ord('e') - ord(freq6[i][0]))
        PTs6[i] = cesar.cesar(subText[i],dist6[i])
    
    freq7 = {}   
    for i in subText:
        freq7[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[6], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[6])
    dist7 = {} 
    PTs7 = {}
    for i in freq:
        dist7[i] = (ord('e') - ord(freq7[i][0]))
        PTs7[i] = cesar.cesar(subText[i],dist7[i])
        
    freq8 = {}   
    for i in subText:
        freq8[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[7], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[7])
    dist8 = {} 
    PTs8 = {}
    for i in freq:
        dist8[i] = (ord('e') - ord(freq8[i][0]))
        PTs8[i] = cesar.cesar(subText[i],dist8[i])
        
        
    freq9 = {}   
    for i in subText:
        freq9[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[8], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[8])
    dist9 = {} 
    PTs9 = {}
    for i in freq:
        dist9[i] = (ord('e') - ord(freq9[i][0]))
        PTs9[i] = cesar.cesar(subText[i],dist9[i])
        
    freq10 = {}   
    for i in subText:
        freq10[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[9], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[9])
    dist10 = {} 
    PTs10 = {}
    for i in freq:
        dist10[i] = (ord('e') - ord(freq8[i][0]))
        PTs10[i] = cesar.cesar(subText[i],dist10[i])
        
    freq11 = {}   
    for i in subText:
        freq11[i] = (list(freqAnalysis.freq_analysis(subText[i]).keys())[10], 
             list(freqAnalysis.freq_analysis(subText[i]).values())[10])
    dist11 = {} 
    PTs11 = {}
    for i in freq:
        dist11[i] = (ord('e') - ord(freq11[i][0]))
        PTs11[i] = cesar.cesar(subText[i],dist11[i])
        
        
    P = {}
    P[0] = PTs[0] #sure
    P[1] = PTs3[1] #sure
    P[2] = PTs5[2] #sure
    P[3] = PTs[3] #sure
    P[4] = PTs[4] #sure
    P[5] = PTs[5] #sure
    P[6] = PTs9[6] 
    P[7] = PTs2[7] 
    P[8] = PTs[8]
    
    PT = ""
    for i in range(int(len(CT)/keyL)):
        for j in P:
            PT += P[j][i]
    
    ces = {}
    for i in subText:
        ces[i] = cesar.cesar_bf(subText[i])[1]
        
    
        
    return subText, ("P final : ", P), PT

     

