
# DEFINISI TYPE
# Type PohonBiner: <A: integer, L: PohonBiner, R: PohonBiner>
# Pohon Biner terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A, L, R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
# REALISASI
def MakePB(A, L, R):
    return [A, L, R]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar: PohonBiner --> integer
# Akar(P) mengembalikan akar dari sebuah PohonBiner
# REALISASI
def Akar(P):
    return P[0] 

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari sebuah PohonBiner
# REALISASI
def Left(P):
    return P[1] 

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari sebuah PohonBiner
# REALISASI
def Right(P):
    return P[2] 

def IsTreeEmpty(T):
    return T == []

def IsOneElmt(T):
    return not IsTreeEmpty(T) and IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T))
    

def NbElmt(P) :
    if IsTreeEmpty(P) :
        return 0
    else :
        return NbElmt(Left(P)) + 1 + NbElmt(Right(P))

    
def IsBiner(P) :
    return not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))

def IsUnerLeft(P) :
    return not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))
def IsUnerRight(P) :
    return not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))


#               O          Q    
#             P   -      -   I
#

def NbDaun(P) :
    if IsTreeEmpty(P) :
        return 0
    else :
        return NbDaun1(P)

def NbDaun1(P):
    if IsOneElmt(P) :
        return 1
    else :
        if (IsBiner(P)) :
            return NbDaun1(Left(P)) + NbDaun1(Right(P))
        
        elif (IsUnerLeft(P)) :
            return NbDaun1(Left(P))
        
        elif (IsUnerRight(P)) :
            return NbDaun1(Right(P))

#print(NbDaun1(MakePB('K',MakePB('J',[],MakePB('R',MakePB('D',MakePB('W',[],[]),[]),[])), MakePB('I',MakePB('Q',[],[]),[]))))
#print(NbElmt(MakePB('K',MakePB('J',[],MakePB('R',MakePB('D',MakePB('W',[],[]),[]),[])), MakePB('I',MakePB('Q',[],[]),[]))))
# 1 + 1 = 2

def NbElmt1(P) :
    if IsTreeEmpty(P) :
        return 0
    elif IsOneElmt(P) :
        return 1
    else :
        return 1 + NbElmt1(Left(P)) + NbElmt1(Right(P))
#        POHON        LEVEL
#          K           1
#      J       I       2
#   -    R   Q  -      3
#      D  -            4
#     W -              5
#   -  -
print(NbElmt1(MakePB('K',MakePB('J',[],MakePB('R',MakePB('D',MakePB('W',[],[]),[]),[])), MakePB('I',MakePB('Q',[],[]),[]))))

def RepPrefix(P):
    if IsOneElmt(P):  
        return [Akar(P)]  
    else:
        if IsBiner(P):  
            return [Akar(P), RepPrefix(Left(P)), RepPrefix(Right(P))]
        elif IsUnerLeft(P):  
            return [Akar(P), RepPrefix(Left(P)), []]
        elif IsUnerRight(P):  
            return [Akar(P), [], RepPrefix(Right(P))]

print(RepPrefix(MakePB('K',MakePB('J',[],MakePB('R',MakePB('D',MakePB('W',[],[]),[]),[])), MakePB('I',MakePB('Q',[],[]),[]))))




def NbElmtTree(T):
    if IsTreeEmpty(T):
        return 0
    else:
        return NbElmtTree(Left(T)) + 1 + NbElmtTree(Right(T))



# T = MakePB('Saburo', MakePB('Rendi', MakePB('Ruth', [], []), MakePB('Aqila', MakePB('Syifa', [], []), MakePB('Eko', [], []))), MakePB('Rayhan', MakePB('Silvani', [], []), []))
# PrintBinaryTree(T)
# T = MakePB('Saburo', [], [])
# print("Jumlah node di dalam Tree: ", IsOneElmt(T))

# 1 IsMember

def IsMember(P, X) :
    if IsTreeEmpty(P)  :
        return False
    elif Akar(P) == X :
        return True
    else :
        return IsMember(Left(P), X) or IsMember(Right(P),X)

print(IsMember(MakePB('K',MakePB('J',[],MakePB('R',MakePB('D',MakePB('W',[],[]),[]),[])), MakePB('I',MakePB('Q',[],[]),[])),'I'))

# 2 I

# 3 LevelOFX -- SALAH

def min2(a,b) :
    if a < b :
        return a
    else :
        return b
    
def LevelOfX(P, X) :
    if Akar(P) == X :
        return 0
    else :
        return 1 + min2(LevelOfX(Left(P), X), LevelOfX(Right(P), X))
    
print(LevelOfX(MakePB('K',MakePB('J',[],MakePB('R',MakePB('D',MakePB('W',[],[]),[]),[])), MakePB('I',MakePB('Q',[],[]),[])),'I'))
