# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:54:11 2020

@author: Romain

Algorithm to solve transposition cipher

"""

CT = "HHWEHHISIQYSHVEDWTNTLNXTAORGDHTWNLITEHIAUISEWNRLTFEMKASINOYREUTUESYGXEEHRNIRITETORYSLHCRSDAXEONITINSNUIREERJIMTAAAXSDEIETADOTHMEWAIOHEHOIX"

import affinecypherpy
import wordAppearence

def crypta_transpo2(CT):
    p = len(CT)
    n = 1
    grid =  []
    for i in range(p):
        m = p

        for j in range(p):
            if m*n == p:
                grid.append((m,n)) 
            
            m = m - 1
        n = n + 1
        

    pos_grid = {}
    for i in grid:
        pos_grid[i] = {}
        for j in range(i[0]):
            pos_grid[i][j] = []
            for k in range(i[1]):
                pos_grid[i][j].append(CT[k + j*i[1]])
                
    for i in pos_grid:
        if (i[0] > 3) and (i[0] < 10) :
            grid = pos_grid[i]
            for j in range(len(grid[0])):
                l = []
                for k in range(len(grid)):
                    l.append(grid[k][j])
                    
                wordColumn = affinecypherpy.listToString(l)
                
                
                
    
    
    
    PTs = {}
    
    for i in pos_grid:
        PTs[i] = []
        for k in range(len(pos_grid[i][0])):
            for j in pos_grid[i]:
                PTs[i].append(pos_grid[i][j][k])
                
    for i in PTs:
        PTs[i] = affinecypherpy.listToString(PTs[i])
        PTs[i] = PTs[i].lower()
    
    score = 0
    PTi = ""
    
    for i in PTs:
        if wordAppearence.word_appearence(PTs[i]) > score:
            score = wordAppearence.word_appearence(PTs[i])
            PTi = i
            
    
        
    return pos_grid, PTs, PTs[PTi]











