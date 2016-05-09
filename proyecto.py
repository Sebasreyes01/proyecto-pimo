'''Programadores: Juan Camilo Mantilla Rubio - Sebastian Camilo Reyes Villamil'''
from sys import stdin
tabla = []
class ArrayQueue:
    CAPACITY = 1
    def __init__(self):
        self._data = [None] * ArrayQueue.CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('La Cola esta vacia')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('La Cola esta vacia')
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans

    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2* len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size +=1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

class Node:
    def __init__(self,val,next):
        self.value=val
        self.next=next
        
    def __len__(list):
        cont = 0
        while list is not None:
            cont += 1
            list = list.next
        return cont

def esta (a,b):
    """pre: a es un valor a buscar y b es un arreglo de listas encadenadas
    post: retorna la siguiente posicion si la encuentra y si no retorna una lista vacia
    """
    r = []
    for i in b:
        if a == i.value:
            i = i.next
            while i != None:
                r.append(i.value)
                i = i.next
            return r
    return []

def printList(lista):
    """pre: lista es una lista encadenada
    post: imprime la lista encadenada
    """
    line='('
    if lista != None:
        line=line+str(lista.value)
        lista=lista.next
        while lista != None:
            line=line+' '+str(lista.value)
            lista=lista.next
        line=line+')'
        print(line)
    else:
        print ('NIL')

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

def verifciudad(coord1):
    """pre: coord1 es la coordenada de la primera ciudad
    post: verifica si la ciudad en coord1 existe en el grafo
    """
    global tabla
    x = hashcode(coord1[0],coord1[1])
    c = compress(x, 67, 59, 73, 37)
    if tabla[c] is None:
        return False
    else:
        while tabla[c] != None:
            if tabla[c].value[1] == coord1:
                return True
            tabla[c] = tabla[c].next
        return False

def path(graph, start, end):
    """pre: graph es el grafo que se va a usar, start es la coordenada de inicio y end es la
                coordenada final
    post: retorna el nombre de las ciudades que conforman el camino mas corto o retorna no hay
    camino si no hay un camino entre las 2 ciudades o retorna no hay ciudad en coord1 si las
    coordenadas en start no existen
    """
    if verifciudad(start):
        queue = ArrayQueue()
        queue.enqueue([start])
        while queue:
            path = queue.dequeue()
            node = path[-1]
            if node == end:
                re = nombres(path)
                res = ", ".join(re)
                return res
            if len(path) > len(graph):
                return "No hay camino"
            for adjacent in esta(node,graph):
                new_path = list(path)
                new_path.append(adjacent)
                queue.enqueue(new_path)
    else:
        return "No hay ciudad en coord1"

def nombres(path):
    """pre: path es el camino entre 2 ciudades
    post: retorna el nombre de las ciudades que conforman a path
    """
    global tabla
    res = []
    for i in path:
        x = hashcode(i[0],i[1])
        c = compress(x, 67, 59, 73, 37)
        a = tabla[c]
        while a !=  None:
            if a.value[1] == i:
                z = a.value[0]
                z = z.split(",")
                res.append(z[0])
            a = a.next
    return res

def tablahash(pobla):
    """pre: pobla es una lista con la informacion de cada ciudad
    post: retorna la tabla de hash con las colisiones puestas como listas encadenadas
    """
    a = [None for x in range(37)]
    for i in range (len(pobla)):
        if a[pobla[i][2]] == None:
            b = Node(pobla[i],None)
            a[pobla[i][2]] = b
        else:
            b = Node(pobla[i],a[pobla[i][2]])
            a[pobla[i][2]] = b
    return a

def main():
    global tabla
    datos = []    
    a = stdin.readline().strip().split(": ")
    while a != ['']:
        if(len(a))==1:
            a.append(None)
        datos.append(a)
        a = stdin.readline().strip().split(": ")
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
        if datos[i][1]!=None:
            ciu = datos[i][1]
            ciu = ciu.split()
            for j in range(len(ciu)):
                c1 = ciu[j].replace('-', ' ')
                c1 = c1.replace('(', ' ')
                c1 = c1.replace(')', ' ')
                c2 = c1.split()
                ciu[j] = (c2[0], c2[1])
            lista.append(ciu)
        else:
            lista.append(None)
        pobla.append(lista)
    copia=pobla.copy()
    for i in range(len(copia)):
        if copia[i][3]!=None:
            for j in range(len(copia[i][3])):
                a=copia[i][3][j]
                b=copia[i][1]
                for k in range(len(copia)):
                    if copia[k][1]==a:
                        c=copia[k][3]
                        if c==None:
                            c=[b]
                        else:
                            c.append(b)
                        pobla[k][3]=c
    tabla = tablahash(pobla)
    tabladehash=[]
    for i in range(len(pobla)):
        nodo=None
        if pobla[i][3]!=None:
            for j in range(len(pobla[i][3])):
                nodo=Node(pobla[i][3][j],nodo)
        nodo=Node(pobla[i][1],nodo)
        tabladehash.append(nodo)
    r = path(tabladehash,('35|55/44@N', '14|24/08@E'),('35|53/45@N', '14|28/02@E'))
    if r is None:
        print("No hay camino")
    else:
        print(r)

main()
