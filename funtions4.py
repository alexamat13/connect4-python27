#coding: utf-8#
import string
import itertools

def creaTaulell(f,c):
    """
    """
    e=0
    i=0
    T=[]
    while i < f:
        F=[]
        e=0
        while e < c:
            F.append(0)
            e += 1
        if e == c:
            T.append(F)
            i+=1
    return T


def escriureTaulell(m):
    """
    >>> escriureTaulell([[1,2,3,7,9],[4,5,6,8,10]])
    None
    """
    r= len(m[0])
    NC=list(range(0,r))
    s= len(m)
    NF=list(range(0,s))
    NF = NF[::]
    T=m
    T=T[::-1]
    print "Taulell de Joc:"
    A="\t"
    for z in NC:
        A+="\t"+str(NC[z])
    print A
    print "-"*78
    i=0
    while i < s:
        j=0
        w=s-1
        o=w-i
        H= "\t"+str(o)+"-->"+"\t"+""
        while j < r:
            valuee=T[i][j]
            H+=str(valuee)+"\t"
            j+=1
        o-=1
        print H
        i+=1
    pass


def checkNumber(x):
    """
    Comprova que el numero no sigui ni una lletra, ni una paraula, ni una paraula buida.
    >>> comprovacioNumero('aaa')
    'Nombre mal introduit, ha de ser un nombre enter: '
    >>> comprovacioNumero('a2A')
    'Nombre mal introduit, ha de ser un nombre enter: '
    >>> comprovacioNumero('')
    'Nombre mal introduit, ha de ser un nombre enter: '
    >>> comprovacioNumero(22)
    22
    """
    t=False
    for c in x:
        a = c.isdigit()
        if a == True:
            t= True
        else:
            t=False
            break

    if t==False:
        print "[  X  ] Invalid number. Please, enter valid number."
        return False
    else:
        return True



def comprovaCord(x,m):
    y=len(m[0]) #numero de columnes
    z=len(m) #numero de files
    if x < 0 or x >= y:
        print "[  X  ] Invalid pos. Please, enter valid position."
        return False
    elif m[z-1][x] != 0:
        print "[  X  ] Invalid pos. Please, enter valid position."
        return False
    else:
        return True


def tirada(nplayer,m,x):
    """
    Demana columna al njugador en curs donat el taulell m.

    >>> tirada(1,[[2,1,0],[0,0,0]],1)
    """
    i=0
    while i < len(m):
        if m[i][x] == 0:
            m[i][x] += nplayer
            break
        else:
            i+=1
    return m


def quatrihor(m):
    """
    Retorna True si es connecta4 horitzontal.

    >>> quatrihor([[0,0,0,0,1,0],[1,2,1,1,1,1],[0,0,0,0,1,0],[1,2,1,1,1,1],[0,0,0,0,1,0],[1,2,1,1,1,1]])
    True
    >>> quatrihor([[0,0,0,0,1,0],[1,2,1,1,2,1],[0,0,0,0,1,0],[1,2,1,1,2,1],[0,0,0,0,1,0],[1,2,1,1,2,1]])
    False
    """
    h=len(m)
    i=len(m[0])
    q=0
    while q <= h-1:
        p=0
        while p < i-3 :
            if m[q][p] == m[q][p+1] == m[q][p+2] == m[q][p+3] != 0:
                return True
            p+=1
        q+=1
    return False


def quatriver(m):
    """
    Retorna True si es connecta4 vertical.

    >>> quatriver([[0,0,0,0,1,0],[0,2,1,1,1,1],[0,0,0,0,1,0],[0,2,1,1,1,1],[0,0,0,0,1,0],[1,2,1,1,1,1]])
    True
    >>> quatriver([[0,0,0,0,0,0],[1,2,1,1,2,1],[0,0,0,0,0,0],[1,2,1,1,2,1],[0,0,0,0,0,0],[1,2,1,1,2,1]])
    False
    """
    h=len(m)
    i=len(m[0])
    q=0
    while q < h-3:
        p=0
        while p <= i-1:
            if m[q][p] == m[q+1][p] == m[q+2][p] == m[q+3][p] != 0:
                return True
            p+=1
        q+=1
    return False


def quatridiagprinc(m,pn):
    """
    Retorna True si es connecta4 diagonal principal.

    >>> quatriver([[0,0,0,0,1,0],[0,2,1,1,1,1],[0,0,0,0,1,0],[0,2,1,1,1,1],[0,0,0,0,1,0],[1,2,1,1,1,1]])
    True
    >>> quatriver([[0,0,0,0,0,0],[1,2,1,1,2,1],[0,0,0,0,0,0],[1,2,1,1,2,1],[0,0,0,0,0,0],[1,2,1,1,2,1]])
    False
    """
    i=0
    while i < len(m)-3:
        j=0
        while j < len(m[0])-3:
            if [m[i][j], m[i+1][j+1], m[i+2][j+2], m[i+3][j+3]] == [pn,pn,pn,pn]:
                return True
            else:
                j+=1
        i+=1
    return False



def quatridiagsecun(m,pn):
    """
    Retorna True si es connecta4 diagonal segundaria.

    >>> quatriver([[0,0,0,0,1,0],[0,2,1,1,1,1],[0,0,0,0,1,0],[0,2,1,1,1,1],[0,0,0,0,1,0],[1,2,1,1,1,1]])
    True
    >>> quatriver([[0,0,0,0,0,0],[1,2,1,1,2,1],[0,0,0,0,0,0],[1,2,1,1,2,1],[0,0,0,0,0,0],[1,2,1,1,2,1]])
    False
    """
    i=0
    while i < len(m)-3:
        j=len(m[0])-1
        while j > 2:
            if [m[i][j], m[i+1][j-1], m[i+2][j-2], m[i+3][j-3]] == [pn,pn,pn,pn]:
                return True
            else:
                j-=1
        i+=1
    return False
