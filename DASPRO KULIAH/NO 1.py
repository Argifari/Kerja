# NAMA FILE : NO 1.py
# Deskripsi : berisi type dan operasi list
# Pembuat : Muhammad Firdaus Argifari
# Tanggal : 29 Oktober 2024

# DEFINISI DAN SPESIFIKASI TYPE
# Konstruktor menambahan elemen di awal, notasi prefix
# type List : [] atau [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfix
# type List : [] atau [List o e]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso : elemen, list --> List
#   {Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemn pertama}
# Konsi : List, elemen --> List
#   {Konsi(L,e) menghasilkan sebuah list dari e dan L dengan e sebagai elemen terakhir}

# REALISASI

def Konso(e,l):
    return [e] + l

def Konsi(L,e) :
    return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt : List tidak kosong --> elemen
#   {FirstElmt(L) menghasilkan elemen pertama dari L}
# LastElmt : List tidak kosong --> elemen
#   {LastElmt(L) menghasilkan elemen terakhir dari L}

# REALISASI

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

# Tail : List tidak kosong --> List
#   {Tail(L) menghasilkan list tanpa elemen pertama}
# Head : List tidak kosong --> List
#   {Head(L) menghasilkan list tanpa elemen terakhir}

# REALISASI

def Tail(L):
    return L[1:]

def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : List --> boolean
#   {IsEmpty(L) bernilai benar jika list kosong}
# IsOneElmt : List --> boolean
#   {IsOneElmt(L) bernilai benar jika L hanya punya satu elemen}

# REALISASI

def IsEmpty(L) :
    return L == []

def IsOneElmt(L):
    return Head(L) == [] and Tail(L) == []

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt : List --> integer
#   {NbElmt(L) menghasilkan banyaknya elemen di list}

# REALISASI

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else :
        return 1 + NbElmt(Tail(L))


# ElmtKeN : integer >= 0, List --> element
#   {ElmtKeN(N,L) mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N >= 0}

# REALISASI

def ElmtKeN(N,L):
    if N == 0:
        return L[0]
    else :
        return ElmtKeN(N - 1, Tail(L))
    

print(ElmtKeN(2,[1,2,3]))

# IsMember: elemen, List --> boolean
#   {IsMember(x,L) bernilai benar jika X adalah elemen list L}

# REALISASI

def IsMember(X,L):
    if IsEmpty(L) :
        return False
    else: 
        if X == FirstElmt(L):
            return True
        else :
            return IsMember(X,Tail(L))

print(IsMember(5,[1,3,4,5]))

# Copy : List --> List
#   {Copy(L) menghasilkan list yang identik dengan list asal}

# REALISASI

def Copy(L):
    if IsEmpty(L):
        return []
    else :
        return Konso(FirstElmt(L),Copy(Tail(L)))
    
print(Copy([1,2,3]))

# Inverse : List --> List
#   {Inverse(L) menghasilkan list L yang dibalik, yaitu urutan elemennya}

# REALISASI

def Inverse(L):
    if IsEmpty(L):
        return []
    else :
        return Konsi(Inverse(Tail(L)),FirstElmt(L))

print(Inverse([1,2,3]))

# Konkat: 2 List --> List
#   {Konkat(L1,L2) menghasilkan konkatenasi 2 buah list dengan list L2 sesudah list L1}

# REALISASI

def Konkat(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return []
    if not IsEmpty(L1) : 
        return Konso(FirstElmt(L1), Konkat(Tail(L1), L2))
    elif not IsEmpty(L2):
        return Konso(FirstElmt(L2), Konkat(L1,Tail(L2)))
    else :
        return []
    
print(Konkat([1,2,3],[4,5,6,7,8,9]))

# SumElmt : List of integer --> integer
#   {SumElmt(L) menghasilkan jumlahan dari setiap elemen di list}

# REALISASI

def SumElmt(L) :
    if IsEmpty(L):
        return 0
    else :
        return FirstElmt(L) + SumElmt(Tail(L))
    
print(SumElmt([1,1,1,1]))

# AvgElmt : List of integer --> integer
#   {AvgElmt(L) menghasilkan nilai rata - rata}

# REALISASI

def AvgElmt(L) :
    return SumElmt(L) // NbElmt(L)

print(AvgElmt([1,1,1,1]))

# MaxElmt : List of integer --> integer
#   {MaxElmt(L) mengembalikan elemen maksimum dari list}
# max2 : 2 integer --> integer
#   {max2(a,b) mengembalikan nilai maksimum dari 2 nilai}
# CountMax : integer, List of integer --> integer
#   {CountMax(x,L) mengembalikan jumlah banyaknya x dalam list L}

# REALISASI
#
def max2(a,b):
    if a > b:
        return a
    else :
        return b

def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        return max2(FirstElmt(L),MaxElmt(Tail(L)))

print(MaxElmt([1,7,3,4,5]))

# CountMax : integer, List of integer --> integer
#   {CountMax(x,L) menghitung jumlah banyaknya x yang muncul di list L}
# MaxNb : List of integer --> <integer, integer>
#   {MaxNb(L) menghasilkan <max, countmax>, 
#   dengan max adalah elemen maksimum list L
#   dan countmax adalah banyaknya kemunculan max di list L}

# REALISASI

def CountMax(x,L):
    if IsEmpty(L):
        return 0
    else:
        if x == FirstElmt(L) :
            return 1 + CountMax(x,Tail(L))
        else :
            return CountMax(x,Tail(L))

def MaxNb(L):
    return [MaxElmt(L), CountMax(MaxElmt(L),L)]
    
print(MaxNb([1,2,2,3,4,4,4]))

# AddList : 2 List of integer --> List of integer
#   {AddList(L1,L2) menghasilkan list baru yang setiap elemennya 
#   adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama}

# REALISASI

def AddList(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2) :
        return []
    else :
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

print(AddList([1,2,3],[1,1,1]))

# HeadTail : List --> List
#   {HeadTail(L) mengembalikan list dengan tanpa elemen pertama dan elemen terakhir}
# IsPalindrom : List of character --> boolean
#   {IsPalindrom(L) benar jika L merupakan kata palindrom, 
#   yaitu kata yang sama jika dibaca dari kiri atau kanan.}

def HeadTail(L):
    return L[1:-1]


def IsPalindrom(L):
    if not IsEmpty(L):
        if FirstElmt(L) != LastElmt(L):
            return False
        else:
            return IsPalindrom(HeadTail(L))
    else :
        return True

print(IsPalindrom(["a","a"]))
