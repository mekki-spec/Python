from math import *
import numpy as np
import matplotlib.pyplot as plt

def schema_explicite(T0,dx,dt=0.02,alpha=(385*8920)/389,beta=(2*155)/(0.001*389),Tint=340,Text=290,ItMax=500):
    n=len(T0)
    r=dt/(alpha*(dx)**2)
    rb=(beta*dt)/(alpha)
    new_T=T0
    if r<0.5:
        M=np.diag([r]*(n-1),-1)+np.diag([1-2*r-rb]*n,0)+np.diag([r]*(n-1),1)
        Vext=np.array([Text] for i in range(n))
        V=np.array([0] for i in range(n))
        V[0]=Tint
        V[n-1]=Text
        T_tous_k=np.zeros(n-1,ItMax)
        T_tous_k[:,0]=T0
        for k in range(1,ItMax):
            new_T=M*new_T+r*V+rb*Vext
            T_tous_k=[:,k]=new_T
    else:
        T_tous_k="Condition r<0.5 non respectée"
    return T_tous_k