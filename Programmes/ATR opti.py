# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:41:51 2018

@author: robbe
"""

from scipy.optimize import *
from ATR import *
from EnergieATR import *
from numpy import *

na=1 #Débit CH4 in

nb=2.5#Débit H20 in
T_in=693
T_out=1300#Temperature
P=50 #Pression
E=0.1/100#Taux d'erreur

deltaH_comb=-803 #kj/molde CH4
deltaH_SMR=224 #kj/molde CH4
deltaH_WGS= -34 #kj/mol de CO
nc=funNc(na,nb,deltaH_SMR,deltaH_comb,deltaH_WGS,T_in,T_out,P,E)
def Avanopti_ATR(na,nb,nc,T_out,P):
    avan_1= lambda x,y : funK1(T_out)-K1(x,y,na,nb,nc,P)
    avan_2= lambda x,y : funK2(T_out)-K2(x,y,na,nb,nc)

    roots1= fsolve(avan_1,linspace(0,3,100),linspace(0,3,100),dtype=float)
    roots2= fsolve(avan_2,linspace(0,3,100),linspace(0,3,100),dtype=float)

    solution=zeros(2)
    for i in range(min(len(roots1),len(roots2))):
        if i/2==0:
            if roots1[i]==roots2[i] and roots1[i+1]==roots2[i+1]:
                solution[0]=roots1[i]
                solution[1]=roots1[i+1]
    return solution       
    
print(Avanopti_ATR(na,nb,nc,T_out,P))