# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:23:43 2020

@author: Romain

Code 9
"""

import indexOfCoincidence
import freqAnalysis
import affinecypherpy
import transpo
import wordAppearence

CT = "XBZPAFQVDOXZAAVVBVWTBDQQDEAVFEYEXQAYXYSPXLDYTDWLFVYYYDDOWNVWYEDAWPELBWVVDWLZESVXYBDDHDDTEQQFDWHOWEQVCDNYLQEW"
englishFreq = ['e','t','a','o','n','r','i','s','h','d','l','f','c','m','u','g','y','p','w','b','v','k','x','j','q','z']

print("index of coincidence :",indexOfCoincidence.index_of_coincidence(CT), "\n")
freq = freqAnalysis.freq_analysis(CT)
print("frequency analysis : ", freqAnalysis.freq_analysis(CT), "\n")

i, alltextDE, theTextDE = affinecypherpy.bf_affine('d','e',CT)
grid = {}
texts = {}

grid2 = {}
texts2 = {}

for i in alltextDE:
    grid[('DE',i)], texts[('DE',i)] = transpo.crypta_transpo(alltextDE[i])
    for j in texts[('DE',i)]:
        grid2[('DE',i,j)], texts2[('DE',i,j)] = transpo.crypta_transpo(texts[('DE',i)][j])
       
i, alltextDT, theTextDT = affinecypherpy.bf_affine('d','t',CT)
for i in alltextDT:
    grid[('DT',i)], texts[('DT',i)] = transpo.crypta_transpo(alltextDT[i])
    for j in texts[('DT',i)]:
        grid2[('DT',i,j)], texts2[('DT',i,j)] = transpo.crypta_transpo(texts[('DT',i)][j])
    
i, alltextVE, theTextVE = affinecypherpy.bf_affine('v','e',CT)
for i in alltextVE:
    grid[('VE',i)], texts[('VE',i)] = transpo.crypta_transpo(alltextVE[i])
    for j in texts[('VE',i)]:
        grid2[('VE',i,j)], texts2[('VE',i,j)] = transpo.crypta_transpo(texts[('VE',i)][j])
    
i, alltextVT, theTextVT = affinecypherpy.bf_affine('v','t',CT)
for i in alltextVT:
    grid[('VT',i)], texts[('VT',i)] = transpo.crypta_transpo(alltextVT[i])
    for j in texts[('VT',i)]:
        grid2[('VT',i,j)], texts2[('VT',i,j)] = transpo.crypta_transpo(texts[('VT',i)][j])
    
i, alltextVA, theTextVA = affinecypherpy.bf_affine('v','a',CT)
for i in alltextVA:
    grid[('VA',i)], texts[('VA',i)] = transpo.crypta_transpo(alltextVA[i])
    for j in texts[('VA',i)]:
        grid2[('VA',i,j)], texts2[('VA',i,j)] = transpo.crypta_transpo(texts[('VA',i)][j])
    
i, alltextVO, theTextVO = affinecypherpy.bf_affine('v','o',CT)
for i in alltextVO:
    grid[('VO',i)], texts[('VO',i)] = transpo.crypta_transpo(alltextVO[i])
    for j in texts[('VO',i)]:
        grid2[('VO',i,j)], texts2[('VO',i,j)] = transpo.crypta_transpo(texts[('VO',i)][j])
    
i, alltextWT, theTextWT = affinecypherpy.bf_affine('w','t',CT)
for i in alltextWT:
    grid[('WT',i)], texts[('WT',i)] = transpo.crypta_transpo(alltextWT[i])
    for j in texts[('WT',i)]:
        grid2[('WT',i,j)], texts2[('WT',i,j)] = transpo.crypta_transpo(texts[('WT',i)][j])
    
i, alltextWA, theTextWA = affinecypherpy.bf_affine('w','a',CT)
for i in alltextWA:
    grid[('WA',i)], texts[('WA',i)] = transpo.crypta_transpo(alltextWA[i])
    for j in texts[('WA',i)]:
        grid2[('WA',i,j)], texts2[('WA',i,j)] = transpo.crypta_transpo(texts[('WA',i)][j])
    
i, alltextWO, theTextWO = affinecypherpy.bf_affine('w','o',CT)
for i in alltextWO:
    grid[('WO',i)], texts[('WO',i)] = transpo.crypta_transpo(alltextWO[i])
    for j in texts[('WO',i)]:
        grid2[('WO',i,j)], texts2[('WO',i,j)] = transpo.crypta_transpo(texts[('WO',i)][j])

score = 0
PTi = ""
for i in texts:
    for j in texts[i]:
        
        if wordAppearence.word_appearence(texts[i][j]) > score:
            score = wordAppearence.word_appearence(texts[i][j])
            PTi = i,j
            print(texts[i][j])
            
score2 = 0
PTi2 = ""
for i in texts2:
    for j in texts2[i]:
        if wordAppearence.word_appearence(texts2[i][j]) > score2:
            score2 = wordAppearence.word_appearence(texts2[i][j])
            print(texts2[i][j])
            PTi2 = i,j









