# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:31:24 2020

@author: Romain

Affine cipher cryptanalysis

"""


import wordAppearence

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
        
           
def affine_cipher(string, a, result):
    
    
    for k in range(0,50):
        if (k*a)%26 == 1:        
            break
    
    textascii = []
    for L in string:
        textascii.append(ord(L.lower()) - 97)
    
    PT = []
    
    for p in textascii:
        PT.append(((p- result[a])*k)%26)
        
    for r in range(len(PT)):
        PT[r] = chr(PT[r] + 97)
            
    return listToString(PT)



def bf_affine(CTLetter, PTLetter, CT):
    
    PTLetter_value = ord(PTLetter.lower()) - 97
    CTLetter_value = ord(CTLetter.lower()) - 97
    
    possible_A = [1, 3, 5, 7, 9, 11,13, 15, 17, 19, 21, 23, 25]
    
    result = {}
    for i in possible_A:
        for j in range(0,26):
            if (i*PTLetter_value + j)%26 == CTLetter_value:
                result[i] = j
    
    allText= {}
    
    
    for a in possible_A:
        allText[a, result[a]] = affine_cipher(CT, a, result)
        
    score = 0
    PTi = ""
    
    for t in allText:
        if wordAppearence.word_appearence(allText[t]) > score:
            score = wordAppearence.word_appearence(allText[t])
            PTi = t
    
    return (PTi, allText, allText[PTi])



        
    
    