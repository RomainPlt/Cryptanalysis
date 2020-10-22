# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:11:10 2020

@author: Romain
"""
import affinecypherpy
import freqAnalysis
import wordAppearence
import transpo

CT = "XBZPAFQVDOXZAAVVBVWTBDQQDEAVFEYEXQAYXYSPXLDYTDWLFVYYYDDOWNVWYEDAWPELBWVVDWLZESVXYBDDHDDTEQQFDWHOWEQVCDNYLQEW"

PTi, alltext, text = affinecypherpy.bf_affine('d','t',CT)
print(freqAnalysis.freq_analysis(CT))

posgrid ={}
PTs = {}

for i in alltext:
    posgrid[i], PTs[i] = transpo.crypta_transpo(alltext[i])
    
    
    
posgrid2 = {}
PTs2 = {}

for i in PTs:
    for j in PTs[i]:
        posgrid2[(i,j)], PTs2[(i,j)]  =  transpo.crypta_transpo(PTs[i][j])
       
print("PTS : \n")
score = 0
PT = ""
PTi = ""
for i in PTs:
    for j in PTs[i]:
        if wordAppearence.word_appearence(PTs[i][j]) > score:
            score = wordAppearence.word_appearence(PTs[i][j])
            PTi = (i,j)
            print(PTs[i][j], "\n")
        
print("PTS2 : \n")

score = 0
PT = ""
PTi = ""
for i in PTs2:
    for j in PTs2[i]:
        if wordAppearence.word_appearence(PTs2[i][j]) > score:
            score = wordAppearence.word_appearence(PTs2[i][j])
            PTi = (i,j)
            print(PTs2[i][j], "\n")

            
