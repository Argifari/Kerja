

# Nama File : treeNaire_24060124130107.py
# Deskripsi : Berisi funsgi treeNaire
# Pembuat : Muhammad Firdaus Argifari _ 24060124130107
# Tanggal : 19 November 2024


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

def makePN(A,PN) :
    return [A,PN]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# akar : PohonN-ner tidak kosong --> elemen
# {akar(PN) adalah akar dari PN. Jika PN adalah (A,P) = akar(PN) adalah A.}

def akar(PN):
    return PN[0]

# anak : PohonN-ner tidak kosong --> elemen
# {anak(PN) adalah list of pohon N-ner yang merupakan anak-anak (sub pohon) 
# dari PN. Jika PN adalah (A, P) maka anak PN adalah P}

def anak(PN):
    return PN[1]

def saudara(PN):
    return PN[1:]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsTreeEmpty : PohonN-ner --> boolean
# {IsTreeEmpty(PN) bernilai benar jika PN kosong.}

def IsTreeEmpty(PN):
    return PN == []

# IsOneElmtTree : PohonN-ner --> boolean
# {IsOneElmt(PN) bernilai benar jika PN hanya terdiri dari akar.}

def IsOneELmtTree(PN):
    return (not IsTreeEmpty(PN)) and (IsTreeEmpty(anak(PN)))

# DEFINISI DAN SPESIFIKASI FUNGSI OPERATOR TERHADAP POHONN-NER
# NbElmtTree : PohonN-ner --> integer >= 0 
# {NbElmtTree(PN) memberikan banyaknya node dari pohon PN.}

def NbNElmtTree(PN):
    if IsTreeEmpty(PN):
        return 0
    if IsOneELmtTree(PN):
        return 1
    else :
        return 1 + NbNElmtTree(akar(anak(PN))) + NbNElmtChild(saudara(anak(PN)))

T2 = makePN('A',[makePN('B',[makePN('D',[]),makePN('E',[]),makePN('F',[])]),
                 makePN('C',[makePN('G',[]),makePN('H',[makePN('I',[])])])])

# NbElmtChild : PohonN-ner --> integer >= 0
# {NbElmtChild(PN)  }
def NbNElmtChild(PN): 
    if IsTreeEmpty(PN):
        return 0
    else:
        return NbNElmtTree(akar(PN)) + NbNElmtChild(saudara(PN))
    
print(NbNElmtTree(T2))
def NbNDaun(PN):
    if IsTreeEmpty(PN):
        return 0
    elif IsOneELmtTree(PN) and IsTreeEmpty(anak(PN)):
        return 1
    else:
        return NbNDaunChild(anak(PN))

def NbNDaunChild(PN):
    if IsTreeEmpty(PN):
        return 0
    else:
        return NbNDaun(akar(PN)) + NbNDaunChild(saudara(PN)) 
    
print(NbNDaun(T2))