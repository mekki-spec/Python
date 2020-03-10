import numpy as np
import matplotlib.pyplot as plt

## I. Permutation Limite/Intégrale et Intégrale de Gauss

def sommeN(n):
	S=0
	for k in range(n):
		S+=(-1)**k/((2*k+1)*(factorielle(k)))
	return S

# 3)
def factorielle(n):
	if n==0:
		return 1
	else:
		return n*factorielle(n-1)

# 4)
def ecart(seuil=10**-6):
	n=0
	truc=1/((2*n+3)*(factorielle(n+1)))
	while truc>seuil:
		truc*=(2*n+3)/((n+2)*(2*n+5))
		n+=1
	return n

## II. Notion de Polynôme Interpolateur

# 8)
def lagrange(x=[-1,0,1],y=[4,0,4],a=3):
	n=len(x)
	P=0
	for k in range(n):
		lk=1
		for i in range(n):
			if i!=k:
				lk*=(a-x[i])/(x[k]-x[i])
		P+=lk*y[k]
	return P

## Passage sur le Petit Sujet

## II. Interpolation de Lagrange

# 4.5)
def comparaison(n=75):
	x=np.linspace(-1,1,n)
	y=1/(1+x**2)

	T=np.linspace(-1.2,1.2,100)
	z=[lagrange(x,y,t) for t in T]

	plt.plot(x,y,'r',label='Le Vrai')
	plt.plot(T,z,'b',label='Lagrange')
	plt.xlim(-1.2,1.2)
	plt.ylim(0,1.5)
	plt.legend(loc='best')

## III. Polynômes de Legendre et Quadrature de Gauss

# 4)a)
def Xk(k):
	P=[0 for a in range(k+1)]
	P[-1]=1
	return P

# 4)b)
def produit(a=3,P=[0,1,0,2,3,4]):
	return [a*x for x in P]

def somme(P=[0,1,0,2,3,4],Q=[26,0,14,-2]):
	p=len(P)
	q=len(Q)
	if p<=q:
		P=P+[0 for a in range(q-p)]
		print(P)
	else:
		Q=Q+[0 for a in range(p-q)]
	return [P[k]+Q[k] for k in range(len(P))]

# 4)c)
def produit_poly(P=[0,1,0,2,3,4],Q=[26,0,14,-2]):
	n=len(P)+len(Q)
	M=[0 for a in range(n)]
	for m in range(n):
		for p in range(len(P)):
			for q in range(len(Q)):
				if p+q==m:
					M[m]+=P[p]*Q[q]
	return M

def evaluation(P,a):
	n=len(P)
	S=0
	for k in range(n):
		S+=P[k]*(a**k)
	return S


def ps(P=[0,1,0,2,3,4],Q=[26,0,14,-2]):
	M=produit_poly(P,Q)
	m=len(M)
	M=M+[0]
	Tab=np.copy(M)
	for k in range(m):
		Tab[k+1]=M[k]/(k+1)
	Tab[0]=0
	print(M)
	return evaluation(Tab,1)-evaluation(Tab,-1)