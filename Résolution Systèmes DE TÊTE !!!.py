import numpy as np
from copy import *

def matrice_nulle(m,n):
	return np.array([[[0.]*n] for k in range(m)])

def matrice_identite(n):
	A=matrice_nulle(n):
	for k in range(n):
		A[k][k]=1
	return A

def pivot(A,colonne):
	i_pivot=colonne
	for k in range(colonne+1,len(A)):
		if abs(A[k][colonne])>abs(A[i_pivot][colonne]):
			i_pivot = k
	return i_pivot

def echange_lignes(A,ligne1,ligne2):
	save=A[ligne1]
	A[ligne1]=A[ligne2]
	A[ligne2]=save

def transvection_lignes(A,ligne1,ligne2,mu):
	A[ligne1]+=mu*A[ligne2]

def resolution(A0,Y0):
	A,Y=copy(A0),copy(Y0)
	for colonne in range(len(A)):
		i_pivot=pivot(A,colonne):
		if i_pivot>colonne:
			echange_lignes(A,colonne,i_pivot)
			echange_lignes(Y,colonne,i_pivot)
		for ligne in range(colonne+1,len(A)):
			mu=A[ligne][colonne]/A[colonne][colonne]
			transvection_lignes(A,ligne,colonne,-mu)
			transvection_lignes(B,ligne,colonne,-mu)
	X=matrice_nulle(len(A),1)
	for ligne in range(len(A)-1,-1,-1):
		S=0
		for col in range(ligne+1,len(A)):
			S+=A[ligne][col]*X[col]
		X[ligne]=(Y[ligne]-S)/A[ligne][ligne]
	return X