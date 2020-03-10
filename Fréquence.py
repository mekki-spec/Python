def Max(L):
    Top,ITop=L[0],0
    for k in range(len(L)):
        if L[k]>Top:
            Top=L[k]
            ITop=k
    return([Top,ITop])

def Inversion(t,a,b):
    c=t[a]
    t[a]=t[b]
    t[b]=c
    
def Tri(L):
    T=L[:]
    for i in range(len(L)): #Aspect Modulaire
        k=Max(T[:len(L)-i])[1]
        Inversion(T,k,len(L)-i-1)
    return(T)

def meilleure(tab):
    L= Tri(tab)
    max=0
    freq=0
    for k in range(len(L)-2):
        if L[k+1]-L[k]>max:
            max=L[k+1]-L[k]
            freq=(L[k+1]+L[k])/2
    return freq

def ecart(tab):
    L= Tri(tab)
    R=[]
    for k in range(len(L)-2):
        R.append(L[k+1]-L[k])
    return R