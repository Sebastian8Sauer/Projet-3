# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:55:11 2018

@author: Groupe 12.36
"""
from ATR import *

T_in=693
T_out=1300
P=50
E=0.5/100
Cm_SMR= 2900 #j/kg*k
Cm_comb=1200#j/kg*k

# a la sortie, il y aura (0.05+ 79/21 * 0. 05 mol d air +1 mol de H2O + 1 mol de CO2) ntotal =2,24
# et donc allons calculer une masse molaire moyenne= 68.95 (ou 51.91 si on prend les gaz de debut)

deltaH_comb=-803 #kj/molde CH4
deltaH_SMR=224 #kj/molde CH4
deltaH_WGS= -34 #kj/mol de CO
#T_Out>T_in

def E_Out_comb(nc,deltaH_comb,T_in,T_out):
    Cmol_comb= 1.2*0.06895#kJ/mol*K
    return (Cmol_comb*(T_out-T_in) +deltaH_comb)*nc

# on doit convertir Cp de massiqeue a molaire ==> on doir prendre en considération mes de gré d avancement
#n mol H2/ n mol total *2+ n mol CH4/ n mol total *16
def E_In_SMR(na,nb,nc,deltaH_SMR,deltaH_WGS,T_in,T_out):
    xi=Avan_ATR(na,nb,1,T_out,P,E)
    n_tot=n_total_out(xi[1],na,nb,nc)-2.24*nc# le dernier est pour le H2O
    Cmol_SMR= (0.002*(3*xi[0]+xi[1])+xi[1]*0.044+(xi[0]-xi[1])*0.028+0.018*(nb-nc-xi[0]-xi[1])+0.016*(3*xi[0]+xi[1]))*2.9/n_tot
    #verfier signe de xi[1]-xi[2]
    return (Cmol_SMR*(T_out-T_in) +deltaH_SMR)*na +deltaH_WGS*(xi[1])

# faire la fonction qui retoure le nombre de CH4 a bruler pour faire la reaction SMR dans la cas ATR
def funNc(na,nb,deltaH_SMR,deltaH_comb,deltaH_WGS,T_in,T_out):
    return -(E_In_SMR(na,nb,1,deltaH_SMR,deltaH_WGS,T_in,T_out))/E_Out_comb(1,deltaH_comb,T_in,T_out)
