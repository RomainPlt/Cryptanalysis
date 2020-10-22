# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:45:25 2020

@author: Romain

password cipher solver


"""

import numpy as np
import affinecypherpy
import wordAppearence
import operator

def man_bf(CT, key):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher = []
    CT = CT.lower()
    key = key.lower()
    for i in key:
        if i not in cipher:
            cipher.append(i)
    for j in alphabet:
        if j not in cipher:
            cipher.append(j)
                
    PT = []
    for k in CT:
        for i in range(len(cipher)):
            if cipher[i] == k:
                break
        PT.append(alphabet[i])
    
    text = ""
    for i in PT:
        text += i
        
    return text

def recursion(l, n, m, a):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if l[n-1] == "z":
        return (a,l) 
    else :
        for i in alphabet:
            for j in alphabet :
                l[m] = j
                a += l
            
            
        
        
        if l[n - 1] == 'z' :
            m += 1
            return recursion(l,n,m,a)
        
        else :
            for i in alphabet:
                l[m] = i
                a += l
            l[n-m-1] = chr(ord(l[n-m-1])+1)
            return recursion(l,n,m,a)
    
import pandas as pd

def bf(CT):
   
    df = pd.read_csv("E:/Users/Romain/Documents/CTU/Information security/words_alpha.csv")
    df['a'] = df['a'].apply(lambda x : str(x))  
    
    text = {}
    
    for i in df['a']:
        text[i] = man_bf(CT, i)
    
    score = 0
    PTi = ""
    results = []
    
    for i in text:
        result = []
        if wordAppearence.word_appearence(text[i]) > score:
            score = wordAppearence.word_appearence(text[i])
           
            result = [score, i, text[i]]
         
            results.append(result)
    
    results = sorted(results, key=lambda result: result[0], reverse = True)
            
    text1 = results[0][2]
    text2 = results[1][2]
    text3 = results[2][2]
    
    return (results)
        









def brute_force(CT,lenk):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    """
    l = ['a' for i in range(lenk)]
    (a,l) = recursion(l,lenk,1,[])
    print(a)
    p = []
    
    for i in range(0,len(a)-lenk,lenk):
        h = []
        for w in range(lenk):
            h.append(a[i+w])
        p.append(h)
      
    return p
    """
    
    l =["a","a","a","a","a"]
    a = []
    p = []
    for i in alphabet:
        l[0] = i
        for j in alphabet:
            l[1] = j
            for k in alphabet:
                l[2] = k
                for m in alphabet:
                    l[3] = m
                    for n in alphabet:
                        l[4] = n
                        a += l
                
    for i in range(0,len(a)-4,5):
        p.append(affinecypherpy.listToString([a[i],a[i+1],a[i+2],a[i+3],a[i+4]]))

    text = {}
    
    for i in p:
        text[i] = man_bf(CT, i)
    
    score = 0
    PTi = ""
    for i in text:
        if wordAppearence.word_appearence(text[i]) > score:
            score = wordAppearence.word_appearence(text[i])
            PTi = i
    
    return (score, PTi, text[PTi])
        
    
        
    
"""
a = []
p = []
for i in range(25):
    l[0] = i
    for j in range(25):
        l[1] = j
        for k in range(25):
            l[2] = k
            a += l
for i in range(0,len(a)-25,26):
    h = []
    for w in range(25):
        h.append(a[i+w])
    p.append(h)
            """
    
    
    
    
    
    
    
    
    
    
    
    
        
        