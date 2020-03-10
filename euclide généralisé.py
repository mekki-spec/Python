import numpy as np

## 1 Introduction
# 1a : pour i != i0 : ri, pour i = i0 : xi0
# 1b : l'algorithme se terminera plus vite en se ramenant à des nombres les plus petits possibles, car cela réduira les restes

## 2 Test d'arrêt
def continuer(v):
    s=np.sum(v)
    c=True
    if s==0: # tous les éléments nuls
        c=False
    i=0
    while i<np.size(v) and c : # un seul élément non nul
        if v[i]==s:
            c=False
        i+=1
    return c

## 3 Localisation du pivot
def indice_min(v):
    longueur = np.size(v)
    i_min, min_non_nul = 0, v[0]
    for i in range(longueur):
        if v[i]!=0 and (v[i]<min_non_nul or min_non_nul==0) :
            i_min=i
            min_non_nul=v[i]
    return i_min

## 4 Blankinship
def blankinship(vl):
    v=[[i] for i in vl]
    nb_entiers = len(v)
    I = np.identity(nb_entiers)
    M = np.hstack((I,v)) # création du tableau de blankinship
    while continuer(M[:,-1]): # tant qu'il reste au moins 2 pivots non nuls
        j=indice_min(M[:,-1])
        xj=M[j,-1] # pivot
        lj=M[j,:] # ligne des coeffs du pivot
        for k in range(nb_entiers):
            if j!=k: # opérations sur les autres lignes
                q=int((M[k,-1])/xj) # quotient de la division euclidienne
                for muette in range(q):
                    M[k,:]-=lj # on retire la ligne du pivot autant de fois que nécessaire
    n=indice_min(M[:,-1])
    return (M[n,-1],M[n,:-1])