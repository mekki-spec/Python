from time import time 
def mesure(a,b):
        top=time()
        for j in range(a):
            s=0
            for i in range(b):
                s+=i**2
        print("Résultat obtenu en","%.3f"%(time()-top),"secondes")