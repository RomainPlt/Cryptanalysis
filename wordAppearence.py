# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:22:53 2020

@author: Romain

Score table for detecting words in texts

"""

wordList = ['the','are','is','we','they',
            'it','for','one','two','three',
            'end','and','then','why','will',
            'was','were', 'them', 'now', 'his',
            'her', 'mine', 'after', 'before',
            'during', 'over', 'hand', 'arm',
            'mouth', 'nose', 'head', 'eye', 
            'with', 'without', 'all', 'almost',
            'far', 'near', 'close', 'open', 'good', 
            'bad', 'ok', 'speak', 'walk', 'talk',
            'think', 'thing', 'able', 'lot', 'i',
            'you', 'he', 'she', 'parent', 'child', 
            'children', 'family', 'police', 'had', 
            'have', 'got', 'get', 'come', 'way', 'sex', 
            'number', 'thought', 'come', 'become']

def word_appearence(string):
    score = 0
    for i in wordList:
        if i in string:
            score += 1
            
    return score

