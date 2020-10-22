# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:25:39 2020

@author: Romain
cesar cipher
"""
import rmSpaces
import wordAppearence

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

def cesar(CT, rot):
    CT = CT.lower()
    CT = rmSpaces.rm_space(CT)
    text = {}
    l = []
    for i in CT:
        l.append(chr((((ord(i)-97)+rot)%26)+97))
        
    a = listToString(l)
    return a
    
def cesar_bf(CT):
    CT = CT.lower()
    CT = rmSpaces.rm_space(CT)
    
    text = {}
        
    for j in range(26):
        l = []

        for i in CT:
            l.append(chr((((ord(i)-97)+j)%26)+97))
        
        a = listToString(l)
        text[j] = a
    score = 0
    PTi = ""
    for i in text:
        if wordAppearence.word_appearence(text[i]) > score:
            score = wordAppearence.word_appearence(text[i])
            PTi = i
            
    return (PTi, text, text[PTi])

