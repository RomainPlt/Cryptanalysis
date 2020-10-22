# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:02:53 2020

@author: Romain
"""
import cesar
import transpo 


CT = "HZWPPWWWTYZEZDZWPOZYGSEASPEWERDWPCSGSQZQTCXCTPPSFTHZASZTDMEPPLMXQLPLPXCSPEYZFFPUYLPJCCGPPPRTOHLLZOZRYEENFSYQLZEPOEP"
CTenglishcompare = 'eafncestmooenaourytttrhtetddfpslasmiwnoiaaetsgteieeiraatcteernheoarlatluondehieg'
CTaffine = 'etlnrehvuccentckbxvvvbqvevpplfhmthudancdttevhivedeedbttvrveebnqectbmtvmkcnpeqdei'
   

n, texts, t = cesar.cesar_bf(CT)

posgrid = {}
PTs = {}
PTi = {}


for i in range(len(texts)):
    posgrid[i], PTs[i]= transpo.crypta_transpo(texts[i])
    
    
    
posgrid2 = {}
PTs2 = {}

for i in PTs:
    for j in PTs[i]:
        posgrid2[(i,j)], PTs2[(i,j)]  =  transpo.crypta_transpo(PTs[i][j])
        


CTen0, CTeng1 = transpo.crypta_transpo(CTenglishcompare)
CTaff0, CTaff1 = transpo.crypta_transpo(CTaffine)

