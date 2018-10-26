# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:35:13 2018

@author: Groupe 12.36
"""
from ATR import *
from EnergieATR import *

na=1 #Débit CH4 in

nb=2.5#Débit H20 in
T_in=693
T_out=1100#Temperature
P=30 #Pression
E=0.5/100#Taux d'erreur

deltaH_comb=-803 #kj/molde CH4
deltaH_SMR=224 #kj/molde CH4
deltaH_WGS= -34 #kj/mol de CO
nc= funNc(na,nb,deltaH_SMR,deltaH_comb,deltaH_WGS,T_in,T_out)
print('na + nc', na+nc)
print('nc = ', nc)

xi=Avan_ATR(na,nb,nc,T_out,P,E)#Xi[0] = degre d'avancement de CH4+H20 // xi[1] = "" CO+H2O
debs=Out_ATR(na,nb,nc,xi)# Débits en sortie de Vapo debs[0] = CH4 // debs[1] = H2O // 
#debs[2] = CO // debs[3] = H2 // debs[4] = CO2

debf=wgs(debs[2],debs[1],debs[4],debs[3])
E_in= E_Out_comb(nc,deltaH_comb,T_in,T_out)
E_needed=E_In_SMR(na,nb,nc,deltaH_SMR,deltaH_WGS,T_in,T_out)
print(' ')
print(' ')
print(' ')
print(' ')
print(' quantité de CH4 brulé',nc)
print('degré d\'avancement vapo: ', xi[0])
print('degré d\'avancement WGS: ', xi[1])
print(' Débits final de CH4 = ', debs[0], ' [mol/s]')
print(' Débits final de H2 = ', debs[3],debf[3], ' [mol/s]')
print(' Débits final de H2O = ', debs[1],debf[1], ' [mol/s]')
print(' Débits final de CO = ', debs[2],debf[0], ' [mol/s]')
print(' Débits final de CO2 = ', debs[4],debf[2], ' [mol/s]')
print('Esmr',E_needed)
print('Ecomb',E_in)

#quantité de CH4 brulé dependra si on prend en compte WGS. Un des probleme se retrouve à l initiatio car alors 
# WGS n 'a pas encore lieu et donc quantité de CH4 brulé sera plutot 0.33 car WGS est exothermique     