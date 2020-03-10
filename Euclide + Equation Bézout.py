import numpy as np
def continuer(V):
	Compteur=0
	k=0
	n=len(V)
	while k<n and Compteur<2:
		if V[k]!=0:
			Compteur+=1
		k+=1
	return Compteur==2

def indice_min(V):
	longueur=V.size
	i_min=0
	debut=0

	while debut<longueur and V[debut]==0:
		debut+=1
	min_non_nul=V[debut]

	for k in range(debut+1,longueur):
		if 0<V[k] and V[k]<min_non_nul:
			min_non_nul=V[k]
			i_min=k
	return i_min

def Blankinship(V):
	nb_entiers=len(V)
	I=np.identity(nb_entiers)
	M=np.hstack((I,V))
	
	while continuer(M[:,-1]):
		indice=indice_min(M[:,-1])
		for i in range(nb_entiers):
			if i!=indice:
				q=M[i,-1]//M[indice,-1]
				M[i:]-=q*M[indice,:]
	
	ligne=indice_min(M[:,-1])
	return(M[ligne,:-1],M[ligne,-1])