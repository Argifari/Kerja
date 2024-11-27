

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

# anak : PohonN-ner tidak kosong --> list of PohonN-ner
# {anak(PN) adalah list of pohon N-ner yang merupakan anak-anak (sub pohon) 
# dari PN. Jika PN adalah (A, P) maka anak PN adalah P}

# REALISASI

def anak(PN):
    return PN[1]

# saudara : PohonN-ner --> list of PohonN-ner
# {saudara(PN) mengembalikan list of pohon N-ner yang merupakan saudara atau yang 
#  selevel.}

# REALISASI

def saudara(PN):
    return PN[1:]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsTreeEmpty : PohonN-ner --> boolean
# {IsTreeEmpty(PN) bernilai benar jika PN kosong.}

# REALISASI

def IsTreeEmpty(PN):
    return PN == []

# IsOneElmtTree : PohonN-ner --> boolean
# {IsOneElmtTree(PN) bernilai benar jika PN hanya terdiri dari akar.}

# REALISASI

def IsOneELmtTree(PN):
    return (not IsTreeEmpty(PN)) and (IsTreeEmpty(anak(PN)))

# DEFINISI DAN SPESIFIKASI FUNGSI OPERATOR TERHADAP POHONN-NER
# NbNElmtTree : PohonN-ner --> integer >= 0 
# {NbNElmtTree(PN) memberikan banyaknya node dari pohon PN.}

# REALISASI

def NbNElmtTree(PN):
    if IsTreeEmpty(PN):
        return 0
    if IsOneELmtTree(PN):
        return 1
    else :
        return 1 + NbNElmtTree(akar(anak(PN))) + NbNElmtChild(saudara(anak(PN)))

# NbNElmtChild : PohonN-ner --> integer >= 0
# {NbNElmtChild(PN) menghitung jumlah elemen pada sisa anak PN.}

# REALISASI

def NbNElmtChild(PN): 
    if IsTreeEmpty(PN):
        return 0
    else:
        return NbNElmtTree(akar(PN)) + NbNElmtChild(saudara(PN))    


# NbNDaun : PohonN-ner --> integer >= 0
# {NbNDaun(PN) menghitung banyaknya daun pada pohon PN.}

# REALISASI

def NbNDaun(PN):
    if IsTreeEmpty(PN):
        return 0
    elif IsOneELmtTree(PN) and IsTreeEmpty(anak(PN)):
        return 1
    else:
        return NbNDaunChild(anak(PN))

# NbNDaunChild : PohonN-ner --> integer >= 0
# {NbNDaunChild(PN) menghitung jumlah daun pada sisa - sisa anak PN.}

# REALISASI

def NbNDaunChild(PN):
    if IsTreeEmpty(PN):
        return 0
    else:
        return NbNDaun(akar(PN)) + NbNDaunChild(saudara(PN)) 
    



# APLIKASI

print(IsTreeEmpty(makePN('A',[])))

print(IsOneELmtTree(makePN('A',[makePN('B',[])])))

print(NbNElmtTree(makePN('A',[makePN('B',[makePN('D',[]),makePN('E',[]),makePN('F',[])]),
                 makePN('C',[makePN('G',[]),makePN('H',[makePN('I',[])])])])))

print(NbNDaun(makePN('A',[makePN('B',[makePN('D',[]),makePN('E',[]),makePN('F',[])]),
                 makePN('C',[makePN('G',[]),makePN('H',[makePN('I',[])])])])))











