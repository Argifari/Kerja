
# Nama file : NO 5.py
# Deskripsi : Menghitung fungsi perkalian n dengan rekursif
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makePB : Elemen, 2PohonBiner --> PohonBiner
# {makePB(A,L,R) membentuk sebuah pohon biner dengan notasi prefix.}

# REALISASI

def makePB(A,L,R) :
    return [A,L,R]

def Konso(x,L):
    return x + L
 
# DEFIISI DAN SPESIFIKASI SELEKTOR
# Akar : PohonBiner --> Elemen
# {Akar(P) mengembalikan Akar dari P yang berupa elemen.}
# Left : PohonBiner --> PohonBiner
# {Left(P) mengembalikan anak kiri P yang berupa pohon biner.}
# Right : PohonBiner --> PohonBiner
# {Right(P) mengembalikan anak kanan yang berupa pohon biner.}

# REALISASI

def Akar(P):
    return P[0]

def Left(P):
    return P[1]

def Right(P):
    return P[2]

# DEFINISI DAN SPESIFIKASI PREDIKAT TERHADAP POHON BINER
# IsBiner : PohonBiner --> boolean
# {IsBiner(P) bernilai benar jika pohon biner P memiliki anak kanan dan kiri.}
# IsUnerLeft : PohonBiner --> boolean
# {IsUnerLeft(P) bernilai benar jika pohon biner P hanya memiliki anak kiri.}
# IsUnerRight : PohonBiner --> boolean
# {IsUnerRight(P) bernilai benar jika pohon biner hanya memiliki anak kanan.}
# IsTreeEmpty : PohonBiner --> boolean
# {IsTreeEmpty(P) bernilai benar jika pohon biner P kosong.}
# IsOneElmt : PohonBiner --> boolean
# {IsOneElmt(P) bernilai benar jika pohon biner hanya berupa akar, tidak memiliki anak kanan dan kiri.}

# REALISASI

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

# DEFINISI DAN SPESIFIKASI FUNGSI OPERATOR TERHADAP POHON BINER
# NbElmt : PohonBiner --> integer >= 0
# {NbElmt(P) memberikan banyaknya elemen dari pohon P.}
# NbElmt1 : PohonBiner --> integer >= 0
# {NbElmt1(P) memberikan banyaknya elemen dari pohon P basis 1.}
# NbDaun : PohonBiner --> integer >= 0 
# {NbDaun(P) memberikan banyaknya daun pada pohon P basis 0.}
# NBdaun1 : PohonBiner --> integer >= 0
# {NbDaun(P) memberikan banyaknya daun pada pohoon P basis 1.}
# RepPrefix : PohonBiner --> List of Elemen
# {RepPrefix(P) membentuk representasi pohon P menjadi list dengan penulisan secara prefix.}

# REALISASI

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
    
# DEFINISI DAN SPESIFIKASI FUNGSIONAL TERHADAP POHON BINER
# IsMember : PohonBiner, Elemen --> boolean
# {IsMember(P,X) bernilai benar jika ada node bernilai X pada pohon biner P.}
# IsSkewLeft : PohonBiner --> boolean
# {IsSkewLeft(P) bernilai benar jika P adalah pohon condong kiri.}
# IsSkewRight : PohonBiner --> boolean
# {IsSkewRight(P) bernilai benar jika P adalah pohon condong kanan.}
# LevelOfX : PohonBiner,Elemen --> integer
# {LevelOfX(P,X) mengembalikan level dari node X yang merupakan simpull pada pohon biner P.}
# Level : PohonBiner, Elemen, integer --> integer
# {Level(P,X,lvl) mengembalikan level dari node X pada pohon biner P.}
# AddDaunTerkiri : PohonBiner, Elemen --> PohonBiner
# {AddDaunTerkiri(P,X) mengembalikan pohon biner P dengan tambahan node X sebagai daun terkiri.}
# AddDaun : PohonBiner tidak kosong, Elemen, Eleemn, boolean --> PohonBiner
# {AddDaun(P,X,Y,Kiri) mengembalikan pohon biner P dengan Y sebagai anak kiri X(Kiri = true) atau 
# Y sebagai anak kanan X(Kiri = false). X adalah simpul di pohon biner P.}
# DelDaunTerkiri : PohonBiner tidak kosong --> <PohonBiner, Elemen>
# {DelDaunTerkiri(P) mengembalikan pohon biner P dengan menghapus daun terkiri dan daun terkiri yang dihapus.}
# Daun : PohobBiner --> PohonBiner
# {Daun(P) mengembalikan pohon biner P dengan menghapus daun terkirinya.}
# DaunTerkiri : PohonBiner --> Elemen
# {DaunTerkiri(P) mengembalikan elemen daun terkiri pada pohon biner P.}
# DelDaun : PohonBiner tidak kosong, elemen →  PohonBiner  
# { DelDaun(P,X) dengan X adalah salah satu daun , menghasilkan sebuah pohon tanpa X 
# yang semula adalah daun dari P} 
 
 
# MakeListDaun : PohonBiner  →list Of Node  
# {MakeListDaun(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong.  
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  daun  
# pohon P} 
 
# MakeListPreOrder :  PohonBiner) →list Of Node  
# {MakeListPreOrder(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P dengan urutan Preorder} 
 
# MakeListPostOrder :  PohonBiner →list Of Node  
# {MakeListPostOrder(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P dengan urutan PostOrder} 
 
# MakeListInOrder :  PohonBiner →list Of Node  
# {MakeListInOrder(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P dengan urutan InOrder} 
 
# MakeListLevel : PohonBiner, integer →list Of Node  
# {MakeListLevel(P,N) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P yang levelnya=N}
# ListLevel : PohonBiner, 2integer --> list 
# {ListLevel(P,N,lvl) mengembalikan list elemen dari pohon biner P yang levelnya sama dengan N.}

# REALISASI

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

# DEFINISI DAN SPESIFIKASI FUNGSI OPERATOR TERHADAP BINARY SEARCH TREEE
# BSearchX : BinSearchTree, Elemen --> boolean
# {BSeacrhX(P,X) bernilai benar jika node yang bernilai X ada pada Binary Search Tree P.}

# REALISASI

def BSearchX(P,X):
    if IsTreeEmpty(P):
        return False
    elif Akar(P) == X:
        return True
    elif Akar(P) > X:
        return BSearchX(Left(P),X)
    elif Akar(P) < X:
        return BSearchX(Right(P),X)

# AddX : BinSearchTree, Elemen --> BinSearchTree
# {AddX(P,X) menghasilkan sebuah pohon Binary Search Tree dengan tambahan node X. Belum ada 
# node bernilai X pada P.}

# REALISASI

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

# ListToBst : list of Elemen, BinSearchTree --> BinSearchTree
# {ListToBst(Ls,P) menghasilkan sebuah Pohon Binary Search Tree yang awalnya berupa list dengan setiap elemen 
# unik}

# REALISASI

def ListToBst(Ls,P):
    if IsEmpty(Ls):
        return P
    else:
        return ListToBst(Tail(Ls),AddX(P,FirstElmt(Ls)))

# MakeBinSearchTree : List of Elemen --> BinSearchTree
# {MakeBinSearchTree(Ls) membentuk Pohon Binary Search Tree yang awalnya berupa list dengan setiap elemennya 
# unik}

# REALISASI

def MakeBinSearchTree(Ls):
    if IsEmpty(Ls):
        return []
    else:
        return ListToBst(Tail(Ls),makePB(FirstElmt(Ls),[],[]))

# MinNode : BinSearchTree --> Elemen
# {MinNode(P) mengembalikan Akar P sebagai pengganti Akar sebelumnya yang dihilangkan.}

# REALISASI

def MinNode(P):
    if IsTreeEmpty(Left(P)):
        return Akar(P)
    else:
        return MinNode(Left(P))
# DelBtree : BinSearchTree, Elemen --> BinSearchTree
# {DelBtree(P,X) menghasilkan sebuah Pohon BInary Search Tree tanpa node yang bernilai X. 
# Node bernilai X pasti ada sebagai salah satu node P}

# REALISASI

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

# APLIKASI

Bst = [15,[14,[12,[],[]],[]],[19,[18,[17,[],[]],[]],[21,[],[22,[],[]]]]]

print(BSearchX(Bst,14))
print(AddX(Bst,30))
print(MakeBinSearchTree([12,23,13,5,9]))
print(DelBtree(Bst,15))






   