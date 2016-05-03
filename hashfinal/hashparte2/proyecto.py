#TODOKETE
'''Programadores: Juan Camilo Mantilla Rubio - Sebastian Camilo Reyes Villamil'''
from sys import stdin

class Node:
    """Nodo basico para construir las listas Lsec"""
    def __init__(self,val,next):
        self.value=val
        self.next=next

def makeEmpty():
    """Construye una Lsec vacia"""
    return Node(None,None)

def is_empty(list):
    """Decide si una Lsec es vacia"""
    return list.value is None and list.next is None

def printLsec(list):
    """Pre: list es una Lsec.
    Post: imprime el contenido de list, excluyendo el centinela,
    con las mismas convenciones de la ultima tarea."""
    if is_empty(list):
        print('NIL')
    else:
        list = list.next
        print('(',end='')
        print(list.value, end='')
        while list.next!=None:
            list=list.next
            print(' ',list.value,sep='',end='')
        print(')')

def hashcode(lon, lat):
    """Pre: lon es la longitud de la ciudad y lat la latitud
    post:retorna el hashcode de esa ciudad
    """
    code = ''
    a = lon + lat
    for i in a:
        if i.isalnum():
            code += i
    code = code.replace('N', str(ord('N')))
    code = code.replace('E', str(ord('E')))
    code = code.replace('S', str(ord('S')))
    code = code.replace('O', str(ord('O')))
    return int(code)

def compress(x, a, b, p, N):
    '''Pre: x,a,b,p,N son enteros
    Post: Retorna el valor comprimido de los valores'''
    return ((a * x + b) % p) % N

##def hashmake(pobla):
##    res=[]
##    for i in range(len(pobla)):
##        a=hashcode(pobla[i][1],pobla[i][2])
##        res.append(a)
##    return res


##def criba_eratostenes(n):
##    '''Pre: n es un entero
##    Post: retorna una lista con los numeros primos hasta n
##    Algoritmo tomado de wikibooks.org'''
##    l=[]
##    multiplos = set()
##    for i in range(2, n+1):
##        if i not in multiplos:
##            l.append(i)
##            multiplos.update(range(i*i, n+1, i))
##    return l


##def calcab(lista):
##    '''Pre: lista es una lista con los posibles valores de a y b
##    Post: retorna una lista con tuplas de cada combinacion a,b'''
##    res=[]
##    for i in range(len(lista)):
##        for j in range(len(lista)):
##            if lista[i]!=lista[j]:
##                a=(lista[i],lista[j])
##                if a not in res:
##                    res.append(a)
##    return res
##
##def calcab2(listaval,listatup):
##    '''Pre: lista es una lista con los posibles valores de a y b,
##    listatup es una lista con las tuplas posibles hasta el momento.
##    Post: retorna una lista con tuplas nuevas de cada combinacion a,b'''
##    for i in range(len(listaval)-1):
##        a=(listaval[i],listaval[-1])
##        b=(listaval[-1],listaval[i])
##        listatup.append(a)
##        listatup.append(b)
##    return listatup


##def compute(datos,N):
##    '''Pre: datos es la lista de hashcodes de las poblaciones, N es un entero
##    Calcula e imprime las tuplas para las cuales se dan las maximas y minimas
##    coliciones de compress'''
##    primos=criba_eratostenes(2*N)
##    cont=0
##    while primos[cont]<=N:
##        cont+=1
##    pval=primos[cont:]
##    abval=primos[0:cont]
##    maxi=0
##    mini=0
##    abtup=calcab(abval)
##    for i in range(len(pval)):
##        for j in range(len(abtup)):
##            coli=0
##            colist=[]
##            for k in range(len(datos)):
##                codigo=compress(datos[k],abtup[j][0],abtup[j][1],pval[i],N)
##                if codigo not in colist:
##                    colist.append(codigo)
##                else:
##                    coli+=1
##            if mini==0 and maxi==0:
##                mini,maxi=(N,abtup[j][0],abtup[j][1],pval[i],coli),(N,abtup[j][0],abtup[j][1],pval[i],coli)
##            else:
##                if coli < mini[4]:
##                    mini=(N,abtup[j][0],abtup[j][1],pval[i],coli)
##                elif coli == mini[4]:
##                    if (abtup[j][0] > mini[1]) or (abtup[j][0]==mini[1] and abtup[j][1] > mini[2]) or (abtup[j][0]==mini[1] and abtup[j][1]==mini[2] and pval[i]>mini[3]):
##                        mini=(N,abtup[j][0],abtup[j][1],pval[i],coli)
##                if coli > maxi[4]:
##                    maxi=(N,abtup[j][0],abtup[j][1],pval[i],coli)
##                elif coli == maxi[4]:
##                    if (abtup[j][0] > maxi[1]) or (abtup[j][0]==maxi[1] and abtup[j][1] > maxi[2]) or (abtup[j][0]==maxi[1] and abtup[j][1]==maxi[2] and pval[i]>maxi[3]):
##                        maxi=(N,abtup[j][0],abtup[j][1],pval[i],coli)
##        abval.append(pval[i])
##        abtup=calcab2(abval,abtup)
##    print(maxi,mini)

def main():
    datos = []
    a = stdin.readline().strip().split(": ")
    while a != ['']:
        datos.append(a)
        a = stdin.readline().strip().split(": ")
    for i in range(len(datos)):
        print(datos[i])
    pobla = []
    for i in range(len(datos)):
        lista = []
        lista.append(datos[i][0])
        a = lista[0].split(",")
        b = (a[1], a[2])
        lista.append(b)
        x = hashcode(b[0], b[1])
        c = compress(x, 67, 59, 73, 37)
        lista.append(c)
        pobla.append(lista)
    for i in pobla:
        print(i)















    #for i in range(len(pobla)):
        #a = pobla[i][0]
        ##print("a", a)
        #b = a.split(',')
        ##print("b", b)
        #c = (b[1], b[2])
        ##print("c", c)
        #d = hashcode(b[1], b[2])
        ##print("d", d)
        #e = compress(d, 67, 59, 73, 37)
        ##print("e", e)
        #pobla[i][0] = [c, e]
        ##print("pobla1", pobla)
        #try:
            #a = pobla[i][1]
            ##print("a", a)
            #b = a.split()
            ##print("b", b)
            #pobla[i][1] = b
            ##print("pobla", pobla)
        #except:
            #pass
    #for i in range(len(pobla)):
        #print(pobla[i])

main()
