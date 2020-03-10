from math import *
from time import *
import numpy as np
## I
def puissance2(x,q):
	if q==0:
		return 1
	elif q%2==1:
		return x*puissance2(x*x,(q-1)%2)
	else:
		return puissance2(x*x,q%2)

## Question 3
def expo_it(x,n):
	res=1
	while n>0:
		if n%2==1:
			res*=x
		x*=x
		n//=2
	return res

## II
## Question 4.a
def fibo_suite(n,phi=(1+sqrt(5))/2,phi_tild=(1-sqrt(5))/2):
	A=(phi_tild-1)/(phi_tild-phi)
	B=1-A
	return A*expo_it(phi,n)+B*expo_it(phi_tild,n)

## Question 4.b
def Fib1(n):
	F=[1,1]
	debut=time()
	for k in range(n-1):
		F=[F[1],F[0]+F[1]]
	fin=time()
	return F[1],(fin-debut)

def Fib2(n):
	L=np.matrix([[0,1]])
	A=np.matrix([[0,1],[1,1]])
	B=expo_it(A,n-1)
	C=np.matrix([[1],[1]])
	return (L*B*C)[0,0]

## Question 4.d
def calculs_Fn(n,rep):
	temps=[]
	
	debut=time()
	for k in range(rep):
		un=fibo_suite(n)
	fin=time()
	temps.append(fin-debut)


	debut=time()
	for k in range(rep):
		deux=Fib1(n)
	fin=time()
	temps.append(fin-debut)

	debut=time()
	for k in range(rep):
		trois=Fib2(n)
	fin=time()
	temps.append(fin-debut)

	return un/deux,deux/trois,un,deux,trois,temps