# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:44:35 2020

@author: Romain

Removing spaces from a text

"""

def rm_space(CT):
    CTwithoutspaces = ""
    for i in CT:
        if i != " ":
            CTwithoutspaces += i
    
    return CTwithoutspaces

            