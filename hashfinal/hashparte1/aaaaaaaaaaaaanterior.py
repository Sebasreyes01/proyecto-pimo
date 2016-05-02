'''Programador: Juan Camilo Mantilla Rubio'''
import sys
import datetime

def hashcode(pobla):
    '''Pre: pobla es una lista con los datos de cada poblacion.
    Post: Retorna una lista con enteros, compuesta por los numeros
    de coordenadas y la direccion de cada poblacion'''    
    res=[]
    for case in pobla:
        a=case[1]+case[2]
##        a=a.replace('°','')
        a=a.replace('|','')
##        a=a.replace('′','')
        a=a.replace('/','')
##        a=a.replace('″','')
        a=a.replace('@','')
        a=a.replace('N','78')
        a=a.replace('S','83')
        a=a.replace('E','69')
        a=a.replace('O','79')
        a=a.strip()
        a=int(a)
        res.append(a)
    return res

##def primo(n):
##    pr=1
##    for i in range (1,a+1):
##        if (a%i==0):
##            if(i!=1 and (i+n-1)==a):
##                if(i!=a):
##                    pr=0
##            if(i==1 and (i+n-1)==a):
##                res=1
##        n=n-1
##    if(pr==0):
##        return False
##    else:
##        return True
    
def criba_eratostenes(n):
    '''Pre: n es un entero
    Post: retorna una lista con los numeros primos hasta n
    Algoritmo tomado de wikibooks.org'''
    l=[]
    multiplos = set()
    for i in range(2, n+1):
        if i not in multiplos:
            l.append(i)
            multiplos.update(range(i*i, n+1, i))
    return l

def compress(x,a,b,p,N):
    '''Pre: x,a,b,p,N son enteros
    Post: Retorna el valor comprimido de los valores'''
    return ((a*x+b)%p)%N

def calcab(lista):
    '''Pre: lista es una lista con los posibles valores de a y b
    Post: retorna una lista con tuplas de cada combinacion a,b'''
    res=[]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i]!=lista[j]:
                a=(lista[i],lista[j])
                if a not in res:
                    res.append(a)
    return res

def calcab2(listaval,listatup):
    '''Pre: lista es una lista con los posibles valores de a y b,
    listatup es una lista con las tuplas posibles hasta el momento.
    Post: retorna una lista con tuplas nuevas de cada combinacion a,b'''
    for i in range(len(listaval)-1): 
        a=(listaval[i],listaval[-1])
        b=(listaval[-1],listaval[i])
        listatup.append(a)
        listatup.append(b)
    return listatup
    

def compute(datos,N):
    primos=criba_eratostenes(2*N)
    cont=0
    while primos[cont]<=N:
        cont+=1
    pval=primos[cont:]
    abval=primos[0:cont]
    maxi=0
    mini=0
    abtup=calcab(abval)
    for i in range(len(pval)):
        for j in range(len(abtup)):
            coli=0
            colist=[]
            for k in range(len(datos)):
                codigo=compress(datos[k],abtup[j][0],abtup[j][1],pval[i],N)
                if codigo not in colist:
                    colist.append(codigo)
                else:
                    coli+=1
            if mini==0 and maxi==0:
                mini,maxi=(N,abtup[j][0],abtup[j][1],pval[i],coli),(N,abtup[j][0],abtup[j][1],pval[i],coli)
            else:
                if coli < mini[4]:
                    mini=(N,abtup[j][0],abtup[j][1],pval[i],coli)
                elif coli == mini[4]:
                    if (abtup[j][0] > mini[1]) or (abtup[j][0]==mini[1] and abtup[j][1] > mini[2]) or (abtup[j][0]==mini[1] and abtup[j][1]==mini[2] and pval[i]>mini[3]):
                        mini=(N,abtup[j][0],abtup[j][1],pval[i],coli)
                if coli > maxi[4]:
                    maxi=(N,abtup[j][0],abtup[j][1],pval[i],coli)
                elif coli == maxi[4]:
                    if (abtup[j][0] > maxi[1]) or (abtup[j][0]==maxi[1] and abtup[j][1] > maxi[2]) or (abtup[j][0]==maxi[1] and abtup[j][1]==maxi[2] and pval[i]>maxi[3]):
                        maxi=(N,abtup[j][0],abtup[j][1],pval[i],coli)
        abval.append(pval[i])
        abtup=calcab2(abval,abtup)
    print(maxi,mini)

def main():
    begin=datetime.datetime.now()
    sys.stdin=open('datos-2-1.in','r',encoding='utf-8')
    pobla=[]
    for line in sys.stdin:
        ln=line.split(',')
        pobla.append(ln)
    cases=pobla.pop()
    a=pobla.pop()
    hashing=hashcode(pobla)
    print(len(pobla))
    for i in range(len(cases)):
        compute(hashing,int(cases[i]))
    fin=datetime.datetime.now()
    print("DELTA:",str(fin-begin))
main()
