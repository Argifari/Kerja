
# Nama File : Set_24060124130107.py
# Deskripsi : berisi type dan operasi set yang menggunakan list
# Pembuat : Muhammad Firdaus Argifari _ 24060124130107
# Tanggal : 5 November 2024

# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah list dengan syarat setiap elemen harus unik 
# semua konstruktor, selektor, dan operasi yang telah didefinisikan
# untuk list juga berlaku untuk set

from list import*

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember : elemen, list --> list
# {Rember(x,L) menghapus sebuah elemen x dari list L
#   jika x ada di list L, maka elemen L berkurang 1.
#   jika x tidak ada di list L maka L tetap.
#   List kosong tetap menjadi list kosong.}

# REALISASI VERSI 1

def Rember(x,L):
    if IsEmpty(L):
        return []
    else :
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L),Rember(x,Tail(L)))

# REALISASI VERSI 2

def Rember2(x,L):
    if IsEmpty(L):
        return []
    else:
        if LastElmt(L) == x:
            return Head(L)
        else:
            return Konsi(Rember2(x,Head(L)),LastElmt(L))
        
print(Rember2(2,[2,2,3,4,5]))

# MultiRember : elemen, list -> list
# {MultiRember(x,L) menghapus semua kemunculan elemen x dari list L
#   List baru yang dihasilkan tidak lagi memiliki elemen x.
#   List kosong tetap menjadi list kosong.}

# REALISASI

def MultiRember(x,L):
    if IsEmpty(L):
        return []
    else: 
        if FirstElmt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x,Tail(L)))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET DARI LIST
# MakeSet : list --> set
# {MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan dari satu kali
#   list kosong tetap menjadi himpunan kosong.}

# REALISASI VERSI 1        

def MakeSetVersi1(L):
    if IsEmpty(L):
        return []
    else :
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSetVersi1(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSetVersi1(Tail(L)))

# REALISASI VERSI 2

def MakeSetVersi2(L):
    if IsEmpty(L):
        return []
    else :
        return Konso(FirstElmt(L),MakeSetVersi2(MultiRember(FirstElmt(L),Tail(L))))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET
# KonsoSet : elemen, set --> set
# {KonsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H
#   dengan syarat e belum ada di dalam himpunan H.}

# REALISASI

def KonsoSet(e,H):
    if IsMember(e,H):
        return H
    else:
        return Konso(e,H)

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet : list --> boolean
# {IsSet(L) bernilai benar jika L adalah sebuah set.}
# IsSubset : 2 set --> boolean
# {IsSubset(H1,H2) bernilai benar jika H1 merupakan subset dari H2.}
# IsEqualSet : 2 set --> boolean
# {IsEqualSet(H1,H2) bernilai benar jika H1 adalah set yang sama dengan H2.}
# IsIntersect : 2 set --> boolean
# {IsIntersect(H1,H2) bernilai benar jika H1 beririsan dengan H2.}

# REALISASI

def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)) :
            return False
        else:
            return IsSet(Tail(L))

def IsSubset(H1,H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1), H2):
            return IsSubset(Tail(H1), H2)
        else:
            return False

def IsEqualSetVersi1(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)

def IsEqualSetVersi2(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return True
    else :
        if IsMember(FirstElmt(H1), H2):
            return IsEqualSetVersi2(Tail(H1), Rember(FirstElmt(H1),H2))
        else:
            return False

def IsIntersect(H1,H2):
    if IsEmpty(H1):
        return False
    else:
        if IsMember(FirstElmt(H1),H2):
            return True
        else:
            return IsIntersect(Tail(H1),H2)
        
print(IsIntersect([6,9],[1,2,3]))

# DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# MakeIntersect : 2 set --> set
# {MakeIntersect(H1,H2) menghasilkan set baru yang merupakan irisan dari H1 dan H2.}
# MakeUnion : 2 set --> set
# {MakeUnion(H1,H2) menghasilkan set baru yang merupakan gabungan dari H1 dan H2.}
# NBintersect : 2 set --> integer
# {NBIntersect(H1,H2) menghitung jumlah elemen yang beririsan pada H1 dan H2.}
# NBUnion : 2 set --> integer
# {NBUnion(H1,H2) menghitung jumlah elemen hasil gabungan antara H1 dan H2.}

# REALISASI

def MakeIntersectVersi1(H1,H2):
    if IsEmpty(H1):
        return []
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1), 
                    MakeIntersectVersi1(Tail(H1),H2))
        else:
            return MakeIntersectVersi1(Tail(H1),H2)

print(MakeIntersectVersi1([1,2,3],[3,4,5]))

def MakeIntersectVersi2(H1,H2):
    if IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H2),H1):
            return Konso(FirstElmt(H2), 
                    MakeIntersectVersi1(H1,Tail(H2)))
        else:
            return MakeIntersectVersi1(H1,Tail(H2))

def MakeUnionVersi1(H1,H2):
    if IsEmpty(H1):
        return H2
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),
                    MakeUnionVersi1(Tail(H1),MultiRember(FirstElmt(H1),H2)))
        else:
            return Konso(FirstElmt(H1),MakeUnionVersi1(Tail(H1),H2))
        
print(MakeUnionVersi1([1,2,3],[1,3,4,5]))

def MakeUnionVersi2(H1,H2):
    if IsEmpty(H2):
        return H1
    else:
        if IsMember(FirstElmt(H2),H1):
            return Konso(FirstElmt(H2),
                    MakeUnionVersi1(MultiRember(FirstElmt(H2),H1),Tail(H2)))
        else:
            return Konso(FirstElmt(H1),MakeUnionVersi1(H1,Tail(H2)))
        
def NBIntersect(H1,H2):
    return NbElmt(MakeIntersectVersi1(H1,H2))

print(NBIntersect([1,2,3],[1,2,3,4]))

def NBUnion(H1,H2):
    return NbElmt(MakeUnionVersi1(H1,H2))

print(NBUnion([1,2,3],[4,5,1,2,3]))
        
