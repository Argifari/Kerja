
# Nama file : NO 5.py
# Deskripsi : Menghitung fungsi perkalian n dengan rekursif
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107

def makePB(A,L,R) :
    return [A,L,R]

def Konso(x,L):
    return x + L
 
def Akar(P):
    return P[0]

def Left(P):
    return P[1]

def Right(P):
    return P[2]

def IsBiner(P):
    return not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))

def IsUnerLeft(P):
    return not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))

def IsUnerRight(P):
    return IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))

def IsTreeEmpty(P):
    return P == []

def IsOneELmt(P):
    return IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))

def NbElmt(P):
    if IsTreeEmpty(P):
        return 0 
    else:
        return NbElmt(Left(P)) + 1 + NbElmt(Right(P))

def NbElmt1(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneELmt(P):
        return 1
    else:
        return 1 + NbElmt1(Left(P)) + NbElmt1(Right(P))

def NbDaun(P):
    if IsTreeEmpty(P):
        return 0
    else :
        return NbDaun1(P)
    
def NbDaun1(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneELmt(P):
        return 1
    elif IsBiner(P):
        return NbDaun1(Left(P)) + NbDaun1(Right(P))
    elif IsUnerLeft(P):
        return NbDaun1(Left(P))
    elif IsUnerRight(P):
        return NbDaun1(Right(P))

def RepPrefix(P):
    if IsOneELmt(P):
        return [Akar(P), [], []]
    elif IsBiner(P):
        return [Akar(P), RepPrefix(Left(P)), RepPrefix(Right(P))]
    elif IsUnerLeft(P):
        return [Akar(P), RepPrefix(Left(P)), []]
    elif IsUnerRight(P):
        return [Akar(P), [], RepPrefix(Right(P))]
    


def IsMember(P,X): 
    if IsTreeEmpty(P):
        return False
    elif Akar(P) == X:
        return True
    else:
        return IsMember(Left(P),X) or IsMember(Right(P),X)

def IsSkewLeft(P):
    if IsTreeEmpty(P):
        return False
    elif IsOneELmt(P):
        return True
    elif IsUnerLeft(P):
        return True and IsSkewLeft(Left(P))
    else:
        return False
 
def IsSkewRight(P):
    if IsTreeEmpty(P):
        return False
    elif IsOneELmt(P):
        return True
    elif IsUnerRight(P):
        return IsSkewRight(Left(P)) and True
    else:
        return False
    
def max2(a,b):
    if a < b:
        return b
    else: return a



def Level(P,X,lvl):
    if IsTreeEmpty(P):
        return 0
    elif Akar(P) == X:
        return lvl
    else:
        return max2(Level(Left(P),X,lvl+1),Level(Right(P),X,lvl + 1))

def LevelOfX(P,X):
    if IsTreeEmpty(P):
        return 0
    elif Akar(P) == X :
        return 1
    else:
        return Level(P,X,0)

#                    a          1
#                b      d       2
#             c       e         3
#          f                    4
#             g                 5   


def AddDaunTerkiri(P,X):
    if IsTreeEmpty(P):
        return makePB(X,[],[])
    elif IsOneELmt(P):
        return makePB(Akar(P), makePB(X,[],[]), [])
    elif IsUnerRight(P):
        return makePB(Akar(P), makePB(X,[],[]), Right(P))
    else:
        return makePB(Akar(P),AddDaunTerkiri(Left(P),X),Right(P))

def AddDaun(P,X,Y,Kiri):
    if Akar(P) == X:
        if Kiri:
            return makePB(Akar(P),makePB(Y,[],[]),Right(P))
        else:
            return makePB(Akar(P),Left(P),makePB(Y,[],[]))
    elif IsBiner(P):
        return makePB(Akar(P),AddDaun(Left(P),X,Y,Kiri), AddDaun(Right(P),X,Y,Kiri))
    elif IsUnerLeft(P):
        return makePB(Akar(P),AddDaun(Left(P),X,Y,Kiri),[])
    elif IsUnerRight(P) :
        return makePB(Akar(P),[],AddDaun(Right(P),X,Y,Kiri))
    else:
        return makePB(Akar(P), Left(P), Right(P))
    
def Daun(P):
    if IsTreeEmpty(P):
        return []
    if IsOneELmt(P):
        return []
    if IsUnerLeft(P):
        return makePB(Akar(P), Daun(Left(P)), Right(P))
    if IsUnerRight(P):
        return makePB(Akar(P), Left(P), Daun(Right(P)))
    return makePB(Akar(P), Daun(Left(P)), Right(P))

def DaunTerkiri(P):
    if IsTreeEmpty(P):
        return []
    if IsOneELmt(P):
        return Akar(P)
    if IsUnerLeft(P):
        return DaunTerkiri(Left(P))
    if IsUnerRight(P):
        return DaunTerkiri(Right(P))
    return DaunTerkiri(Left(P))

def DelDaunTerkiri(P):
    return [Daun(P),DaunTerkiri(P)]

def DelDaun(P,X):
    if IsTreeEmpty(P):
        return []
    if Akar(P) == X:
        return []
    if IsUnerLeft(P):
        return makePB(Akar(P), DelDaun(Left(P),X), Right(P))
    if IsUnerRight(P):
        return makePB(Akar(P), Left(P), DelDaun(Right(P),X))
    return makePB(Akar(P), DelDaun(Left(P),X), DelDaun(Right(P),X))
    
def MakeListDaun(P):
    if IsTreeEmpty(P):
        return []
    if IsOneELmt(P):
        return [Akar(P)]
    if IsUnerLeft(P):
        return MakeListDaun(Left(P))
    if IsUnerRight(P):
        return MakeListDaun(Right(P))
    return Konso(MakeListDaun(Left(P)),MakeListDaun(Right(P)))    

def MakeListPreOrder(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneELmt(P):
        return [Akar(P),[],[]]
    elif IsBiner(P):
        return [Akar(P),MakeListPreOrder(Left(P)),MakeListPreOrder(Right(P))]
    elif IsUnerLeft(P):
        return [Akar(P),MakeListPreOrder(Left(P)),[]]
    elif IsUnerRight(P):
        return [Akar(P),[],MakeListPreOrder(Right(P))]

def MakeListPostOrder(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneELmt(P):
        return [[],[],Akar(P)]
    elif IsBiner(P):
        return [MakeListPostOrder(Right(P)),MakeListPostOrder(Left(P)),Akar(P)]
    elif IsUnerLeft(P):
        return [[],MakeListPostOrder(Left(P)),Akar(P)]
    elif IsUnerRight(P):
        return [MakeListPostOrder(Right(P)),[],Akar(P)]    


def MakeListInOrder(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneELmt(P):
        return [[],Akar(P),[]]
    elif IsBiner(P):
        return [MakeListInOrder(Left(P)),Akar(P),MakeListInOrder(Right(P))]
    elif IsUnerLeft(P):
        return [MakeListInOrder(Left(P)),Akar(P),[]]
    elif IsUnerRight(P):
        return [[],Akar(P),MakeListInOrder(Right(P))]   

def ListLevel(P,N,lvl):
    if IsTreeEmpty(P):
        return []
    elif lvl == N:
        return [Akar(P)]
    else:
        return ListLevel(Left(P),N,lvl+1) + ListLevel(Right(P),N,lvl + 1)
    
def MakeListLevel(P,N):
    if IsTreeEmpty(P):
        return []
    else:
        return ListLevel(P,N,0)

# ----------------------------- BST ----------------------------4
def IsEmpty(L):
    return L == []

def BSearchX(P,X):
    if IsTreeEmpty(P):
        return False
    elif Akar(P) == X:
        return True
    elif Akar(P) > X:
        return BSearchX(Left(P),X)
    elif Akar(P) < X:
        return BSearchX(Right(P),X)


def AddX(P,X):
    if IsTreeEmpty(P):
        return makePB(X,[],[])
    elif Akar(P) > X:
        return makePB(Akar(P),AddX(Left(P),X),Right(P))
    elif Akar(P) < X:
        return makePB(Akar(P),Left(P),AddX(Right(P),X))

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:]

def ListToBst(Ls,P):
    if IsEmpty(Ls):
        return P
    else:
        return ListToBst(Tail(Ls),AddX(P,FirstElmt(Ls)))

def MakeBinSearchTree(Ls):
    if IsEmpty(Ls):
        return []
    else:
        return ListToBst(Tail(Ls),makePB(FirstElmt(Ls),[],[]))

def MinNode(P):
    if IsTreeEmpty(Left(P)):
        return Akar(P)
    else:
        return MinNode(Left(P))

def DelBtree(P,X):
    if Akar(P) == X:
        if IsBiner(P):
            return makePB(MinNode(Right(P)),Left(P),DelBtree(Right(P),MinNode(Right(P))))
        elif IsUnerLeft(P):
            return makePB(Left(P),[],[])
        elif IsUnerRight(P):
            return makePB(Right(P),[],[])
        elif IsOneELmt(P):
            return []
    elif Akar(P) > X:
        return makePB(Akar(P),DelBtree(Left(P),X),Right(P))
    elif Akar(P) < X:
        return makePB(Akar(P),Left(P),DelBtree(Right(P),X))

Bst = [15,[14,[12,[],[]],[]],[19,[18,[17,[],[]],[]],[21,[],[22,[],[]]]]]
print(DelBtree(Bst,15))






   