# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:12:17 2018

@author: Groupe 12.36
"""
from SMR import *
from EnergieATR import *
na=1 #Débit CH4 in
nb=2.5#Débit H20 in
T_in=693
T_out=1100
P=30
E=0.5/100
Cm_SMR= 2900 #j/kg*k
Cm_comb=1200#j/kg*k

# a la sortie, il y aura (0.05+ 79/21 * 0. 05 mol d air +1 mol de H2O + 1 mol de CO2) ntotal =2,24
# et donc allons calculer une masse molaire moyenne= 68.95 (ou 51.91 si on prend les gaz de debut)

deltaH_comb=-803 #kj/molde CH4
deltaH_SMR=224 #kj/molde CH4
deltaH_WGS= -34 #kj/mol de CO

xi=Avan_SMR(na,nb,T_out,P,E)#Xi[0] = degre d'avancement de CH4+H20 // xi[1] = "" CO+H2O
debs=Out_SMR(na,nb,xi)# Débits en sortie de Vapo debs[0] = CH4 // debs[1] = H2O // 
#debs[2] = CO // debs[3] = H2 // debs[4] = CO2

debf=wgs(debs[2],debs[1],debs[4],debs[3])
print(' ')
print(' ')
print(' ')
print(' ')
print('degré d\'avancement vapo: ', xi[0])
print('degré d\'avancement WGS: ', xi[1])
print(' Débits final de CH4 = ', debs[0], ' [mol/s]')
print(' Débits final de H2 = ', debf[3], ' [mol/s]')
print(' Débits final de H2O = ', debf[1], ' [mol/s]')
print(' Débits final de CO = ', debf[0], ' [mol/s]')
print(' Débits final de CO2 = ', debf[2], ' [mol/s]')
print(' Energie consommée par la réaction' , E_In_SMR(na,nb,0,deltaH_SMR,deltaH_WGS,T_in,T_out) )