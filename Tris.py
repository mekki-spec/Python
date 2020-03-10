def insere(L,i,x):
	return L[:i]+[x]+L[i:]

def suppr_elt(L,i):
	return L[:i]+L[i+1:]

def echange(L,i,j):
	a=L[i]
	L[i]=L[j]
	L[j]=a
	return L

def tri_insertion(L):
	for i in range(1,len(L)):
		lieu=i-1
		while lieu>=0 and L[lieu]>L[lieu+1]:
			L=echange(L,lieu,lieu+1)
			lieu-=1
	return L

def tri_bulle(L):
	pastrié=True
	while pastrié:
		for i in range (len(L)-1):
			if L[i]>L[i+1]:
				L=echange(L,i,i+1)
				pastrié=True
			else :
				pastrié=False
	return L
L=[1,2,3,-6,-34,76]