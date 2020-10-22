# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:33:01 2020

@author: Romain

Cryptanalysis transposition cipher (without key for the moment)
"""
import affinecypherpy
import wordAppearence

def crypta_transpo(CT):
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
            
    
        
    return  pos_grid, PTs

"""
def transpo_key(CT):
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
        
    pos_grid = {} #toutes les grilles possibles
    for i in grid:
        pos_grid[i] = {}
        for j in range(i[0]):
            pos_grid[i][j] = []
            for k in range(i[1]):
                pos_grid[i][j].append(CT[k + j*i[1]])
    eff_grid = {} #les grilles réalistes
    for i in pos_grid:
        if (i == pos_grid[0]) or 
        (i == pos_grid[1]) or 
        (i == pos_grid[len(pos_grid) -1]) or
        (i == pos_grid[len(pos_grid)]):
            
    
    return pos_grid
"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
