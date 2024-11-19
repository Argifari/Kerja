
# Nama File : Set_24060124130107.py
# Deskripsi : berisi type dan operasi list of list
# Pembuat : Muhammad Firdaus Argifari _ 24060124130107
# Tanggal : 12 November 2024

from list import *
from Set_24060124130107 import *

# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST OF LIST
# isAtom? : list of list --> boolean 
# {IsAtom?(S) bernilai benar jika S adalah sebuah atom.}
# IsList? : list of list --> boolean
# {IsList?(S) bernilai benar jika S adalah sebuah list.}

# REALISASI

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# konslo : list, list of list --> list of list
# {konslo(L, S) membentuk list baru dengan list L sebagai 
# elemen pertama list of list S.}

# REALISASI

def konsLo(L,S) :
    return [L] + S

# konsli : list of list, list --> list of list
# {konsli(S,L) membentuk list baru dengan list L sebagai 
# elemen terakhir list of list S.}

# REALISASI

def konsLi(S,L):
    return S + [L]

# DEFINISI DAN SPESIFIKASI SELEKTOR 
# firstlist : list of list tidak kosong --> list
# {firstlist(S) menghasilkan elemen pertama list (
# mungkin sebuah atom atau list).}

# REALISASI

def firstList(S):
    return S[0]

# lastlist : list of list tidak kosong --> list
# {lastlist(S) menghasilkan elemen terakhir list 
# (mungkin sebuah list atau atom).}

# REALISASI

def lastList(S):
    return S[-1]

# tailist : list of list tidak kosong --> list of list
# {taillist(S) menghasilkann list of list S tanpa elemen pertamanya.}

# REALISASI

def tailList(S):
    return S[1:]

# headlist : list of list tidak kosong --> list of list
# {headlist(S) menghasilkan list of list S tanpa elemen terakhirnya.}

# REALISASI

def headList(S):
    return S[:-1]

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST OF LIST
# IsMemberLS? : list, list of list --> boolean
# {IsMemberLS?(L,S) mengembalikan true jika list L ada di dalam list of list S.}

# REALISASI

def IsMemberLS(L,S):
    if IsEmpty(S):
        return False
    else :
        if IsAtom(firstList(S)):
            return IsMemberLS(L,tailList(S))
        else:
            if IsEqualSetVersi1(firstList(S),L):
                return True
            else:
                return IsMemberLS(L,tailList(S))
            
# IsEqS? : 2 list of list --> boolean
# {IsEqS?(S1,S2) bernilai benar jika S1 memiliki elemen 
# dengan nilai dan urutan yang sama.}

# REALISASI

def IsEqS(S1,S2):
    if IsEmpty(S1) and IsEmpty(S2) :
        return True
    else :
        if IsAtom(firstList(S1)) and IsAtom(firstList(S2)):
            if firstList(S1) == firstList(S2):
                return IsEqS(tailList(S1), tailList(S2))
            else:
                return False
        elif IsList(firstList(S1)) and IsList(firstList(S2)):
            return IsEqS(firstList(S1),firstList(S2)) and IsEqS(tailList(S1),tailList(S2))
        else:
            return False
        
# IsMemberS? : elemen, list of list --> boolean
# {IsMemberS?(x,S) bernilai benar jika elemen x ada di dalam list of list S.}

# REALISASI
         
def IsMemberS(x,S):
    if IsEmpty(S):
        return False
    else :
        if IsAtom(firstList(S)):
            if x == firstList(S):
                return True
            else:
                return IsMemberS(x, tailList(S))
        else:
            return IsMemberS(x,firstList(S)) or IsMemberS(x,tailList(S))


# RemberLOL : elemen, list of list --> list of list
# {RemberLOL(x,S) menghapus semua elemen x yang ada di list of list S.} 

# REALISASI


def RemberLOL(x,S):
    if IsEmpty(S):
        return []
    else :
        if IsAtom(firstList(S)):
            if x == firstList(S):
                return RemberLOL(x,tailList(S))
            else:
                return konsLo(firstList(S),RemberLOL(x,tailList(S)))
        else:
            return konsLo(RemberLOL(x,firstList(S)), RemberLOL(x,tailList(S)))

# MaxLOL : list of list --> elemen
# {MaxLOL(S) mengembalikan elemen maksimum di dalam list of list S.}

# REALISASI

def MaxLOL(S):
    if IsOneElmt(S):
        if IsAtom(firstList(S)):
            return firstList(S)
        else:
            return MaxLOL(firstList(S))
    else:
        if IsAtom(firstList(S)):
            return max2(firstList(S), MaxLOL(tailList(S)))
        else:
            return max2(MaxLOL(firstList(S)), MaxLOL(tailList(S)))

# NBElmtAtom : list of list --> integer
# {NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom.}

# REALISASI  

def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(firstList(S)):
            return 1 + NBElmtAtom(tailList(S))
        else:
            return NBElmtAtom(tailList(S))

# NBElmtList : list of list --> integer
# {NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list.}

# REALISASI

def NBElmtList(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(firstList(S)):
            return 1 + NBElmtList(tailList(S))
        else:
            return NBElmtList(tailList(S))

# SumLOL : list of list --> integer
# {SumLOL(S) mengembalikan jumlah semua elemem dalam list of list S}

# REALISASI

def SumLOL(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(firstList(S)):
            return firstList(S) + SumLOL(tailList(S))
        else:
            return SumLOL(firstList(S)) + SumLOL(tailList(S))

# MaxNBElmtList : list of list --> integer
# {MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang 
# ada pada list of list S}

# REALISASI

def MaxNBElmtlist(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(firstList(S)):
            return max2(NbElmt(firstList(S)), MaxNBElmtlist(tailList(S)))
        else:
            return MaxNBElmtlist(tailList(S))
        
# MaxSumElmt : list of list --> integer
# {MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
# jika elemen berupa list, maka dihitung jumlahan elemen dalam list tersebut.}

# REALISASI

def MaxSumElmt(S):
    if IsOneElmt(S):
        if IsAtom(FirstElmt(S)):
            return firstList(S)
        else:
            return SumLOL(firstList(S))
    else:
        if IsAtom(firstList(S)):
            return max2(firstList(S), MaxSumElmt(tailList(S)))
        else:
            return max2(SumLOL(firstList(S)), MaxSumElmt(tailList(S)))

# APLIKASI

print(IsMemberLS([1,2],[1,2,[1,2]]))

print(IsMemberS(3,[1,2,[3,4,5]]))

print(RemberLOL(3,[1,2,3,[3,[3]]]))

print(MaxLOL([1,2,3,[4,3,[12]]]))

print(NBElmtAtom([1,2,3,[10,6,4,[8,9]]]))

print(NBElmtList([[1,2,3],[7,4],5,10]))

print(SumLOL([1,2,4,[5,[10,19]]]))

print(MaxNBElmtlist([1,2,4,9,[10,24,19],[12],[6,7]]))

print(MaxSumElmt([1,2,3,8,[10,11,12],[13,0]]))



