# -*- coding: utf-8 -*-
"""
Created on Thu Oct 4 17:17:09 2018

@author: Groupe 12.36
"""
# and = condition ET
# or = condition OU
import numpy as np
#Définition des constantes d'équilibres
def funK1(T): #SMR
    return 10**(-(11650/T)+13.076)
def funK2(T): #WGS
    return 10**((1910/T)-1.764)
def K1(X,Y,na,nb,P):
    return (((3*X+Y)**3)*(X-Y))*P**2/(((na+nb+2*X)**2)*(na-X)*(nb-X-Y))
def K2(X,Y,na,nb):
    return ((3*X+Y)*Y)/((nb-X-Y)*(X-Y))
#Fonction du programme d'avant
def Avan_SMR(na,nb,T,P,E):#Programme retournant un tableau sol dont sol[0]=Xi1 , sol[1]=Xi2
    M=min(na,nb)
    sol=np.empty(2)
    vK1=funK1(T)#Valeur K1
    vK2=funK2(T)#Valeur K2
    
    for X in np.linspace(0,M,5000) : 
        for Y in np.linspace(0,X,5000) :
            if (vK1 <= K1(X,Y,na,nb,P)*(1+E) and vK1 >= K1(X,Y,na,nb,P)*(1-E)) and (vK2 <= K2(X,Y,na,nb)*(1+E) and vK2 >= K2(X,Y,na,nb)*(1-E)) :
                sol[0] = X
                #print('sol de X : ', X)
                sol[1] = Y
                #print('sol de Y : ', Y)
            #on pourrait imprimer les valeurs, si on en obtient plusieurs -> on peut encore reduire l'erreur
    return sol
    
#Débits finaux
def Out_SMR(na,nb,deg):#'sol contient les débits de CH4...'
    sol= np.empty(5)
    sol[0]= na - deg[0] #CH4
    sol[1]= nb-deg[0]-deg[1]#H20
    sol[2]= deg[0]-deg[1]#CO
    sol[3]= 3*deg[0] + deg[1]#H2
    sol[4]= deg[0]#CO2
    return sol

#WGS complet
#na+nb-->nc+nd
def wgs(na,nb,nc,nd):
    sol=np.empty(4)
    limit=min(na,nb)
    sol[0] = na - limit#CO
    sol[1] = nb - limit#H20
    sol[2] = nc + limit#CO2
    sol[3] = nd + limit#H2
    return sol
