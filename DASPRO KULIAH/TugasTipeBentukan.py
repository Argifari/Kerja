# Muhammad Firdaus Argifari




# NO 1 TIPE BENTUKAN PECAHAN CAMPURAN
# =================================================
# =================================================


# DEFINISI DAN SPESIFIKASI TYPE
# tpye pecahanCampuran : <bil: integer, n:integer >= 0, d:integer > 0 >
#   {<bil,n,d> adalah sebuah pecahan campuran dengan bil dapat bernilai positif, negatif, maupun nol, 
#       n selalu bernilai lebih kecil dari d, dengan d lebih dari nol.}
# type pecahan : <n:integer, d: integer > 0>
#   {<n,d> adalah pecahan biasa dengan n bisa bernilai negatif, nol, maupun positif, dan d lebih besar dari nol.}
#
# DEFINISI DAN SPESIFIKASI SELEKTOR
# Bil : pecahanCampuran --> integer
#   {Bil(P) memberikan bilangan bil dari pecahan campuran P, <bil,n,d>.}
# PembPecahanCampuran : pecahanCampuran --> integer >= 0
#   {PembPecahanCampuran(P) memberikan pembilang n dari pecahan campuran P, <bil,n,d>.}
# PenyPecahanCampuran : pecahanCampuran --> integer > 0
#   {PenyPecahanCampuran(P) memberikan penyebut d dari pecahan campuran P, <bil,n,d>.}
# PembPecahan : pecahan --> integer 
#   {PembPecahan(PB) memberikan pembilang n dari pecahan PB, <n,d>.}
# PenyPecahan : pecahan --> integer > 0
#   {PenyPecahan(PB) memberikan penyebut d dari pecahan PB, <n,d,>.}
#
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePecahanCampuran : integer, integer >= 0, integer > 0 --> pecahanCampuran
#   {MakePecahanCampuran(bil,n,d) membentuk pecahan campuran, <bil,n,d>.}
# MakePecahan : integer, integer > 0 --> pecahan
#   {MakePecahan(n,d) membentuk pecahan, <n,d>.}
#
# DEFINISI DAN SPESIFIKASI FUNGSI/OPERATOR TERHADAP PECAHAN CAMPURAN
# KonversiPecahan : pecahanCampuran --> pecahan
#   {KonversiPecahan(P) mengonversi sebuah pecahan campuran menjadi pecahan.}
# KonversiReal : pecahanCampuran --> real
#   {KonversiReal(P) mengonversi sebuah pecahan campuran menjadi bilangan real.}
# AddP : 2 pecahanCampuran --> pecahanCampuran
#   {AddP(P1,P2) menambahkan pecahan campuran P1 dengan pecahan campuran P2.}
# SubP : 2 pecahanCampuran --> pecahanCampuran
#   {SubP(P1,P2) mengurangi pecahan campuran P1 dengan pecahan campuran P2.}
# DivP : 2 pecahanCampuran --> pecahanCampuran
#   {DivP(P1,P2) membagi pecahan campuran P1 dengan pecahan campuran P2.}
# MulP : 2 pecahanCampuran --> pecahanCampuran
#   {MulP(P1,P2) mengalikan pecachan campuran P1 dengan pecahan campuran P2}
#
# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqP? : 2 pecahanCampuran --> boolean
#   {IsEqP?(P1,P2) bernilai benar jika pecahan campuran P1 sama dengan pecahan campuran P2.}
# IsLtP? : 2 pecahanCampuran --> boolean
#   {IsLtP?(P1,P2) bernilai benar jika pecahan campuran P1 kurang dari pecahan campuran P2.}
# IsGtP? : 2 pecahanCampuran --> boolean
#   {IsGtP?(P1,P2) bernilai benar jika pecahan campuran P1 lebih dari pecahan campuran P2.}
#
# REALISASI DALAM PYTHON

def Bil(P) :
    return P[0]

def PembPecahanCampuran(P) :
    return P[1]

def PenyPecahanCampuran(P) :
    return P[2]

def PembPecahan(PB) :
    return PB[0]

def PenyPecahan(PB):
    return PB[1]

def MakePecahanCampuran(bil,n,d) :
    return [bil,n,d]

def MakePecahan(n,d) :
    return [n,d]

def KonversiPecahan(P) :
    if Bil(P) < 0 :
        return MakePecahan(
                Bil(P)*PenyPecahanCampuran(P) - PembPecahanCampuran(P), 
                PenyPecahanCampuran(P)
            )
    else :
        return MakePecahan(
                Bil(P)*PenyPecahanCampuran(P) + PembPecahanCampuran(P), 
                PenyPecahanCampuran(P)
            )

def KonversiReal(P):
    if Bil(P) < 0:
        return Bil(P) - PembPecahanCampuran(P) / PenyPecahanCampuran(P)
    else :
        return Bil(P) + PembPecahanCampuran(P) / PenyPecahanCampuran(P) 

def AddP(P1,P2) :
    return MakePecahanCampuran(
            Bil(P1) + Bil(P2), 
            PembPecahanCampuran(P1)*PenyPecahanCampuran(P2) + PembPecahanCampuran(P2)*PenyPecahanCampuran(P1),
            PenyPecahanCampuran(P1)*PenyPecahanCampuran(P2)
        )

def SubP(P1,P2) :
    return MakePecahanCampuran(
            Bil(P1) - Bil(P2), 
            PembPecahanCampuran(P1)*PenyPecahanCampuran(P2) - PembPecahanCampuran(P2)*PenyPecahanCampuran(P1),
            PenyPecahanCampuran(P1)*PenyPecahanCampuran(P2)
        )

def DivP(P1,P2) :
    return MakePecahanCampuran( 
                PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2))// 
                (PenyPecahan(KonversiPecahan(P1))*PembPecahan(KonversiPecahan(P2))),
                PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)) % 
                (PenyPecahan(KonversiPecahan(P1))*PembPecahan(KonversiPecahan(P2))),
                PenyPecahan(KonversiPecahan(P1))*PembPecahan(KonversiPecahan(P2))

            )

def MulP(P1,P2) :
    return MakePecahanCampuran( 
                PembPecahan(KonversiPecahan(P1))*PembPecahan(KonversiPecahan(P2))// 
                (PenyPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2))),
                PembPecahan(KonversiPecahan(P1))*PembPecahan(KonversiPecahan(P2)) % 
                (PenyPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2))),
                PenyPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2))

            )
    
def IsEqP(P1,P2) :
    return (PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)) 
            == PembPecahan(KonversiPecahan(P2))*PenyPecahan(KonversiPecahan(P1)))

def IsLtP(P1,P2) :
    return (PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)) 
            < PembPecahan(KonversiPecahan(P2))*PenyPecahan(KonversiPecahan(P1)))

def IsGtP(P1,P2) :
    return (PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)) 
            > PembPecahan(KonversiPecahan(P2))*PenyPecahan(KonversiPecahan(P1))) 

# APLIKASI DALAM PYTHON
print(SubP(MakePecahanCampuran(1,1,2), MakePecahanCampuran(2,1,2)))
print(IsEqP(MakePecahanCampuran(2,3,4), MakePecahanCampuran(2,3,4)))
print(DivP(MakePecahanCampuran(2,1,2), MakePecahanCampuran(2,1,2)))
print(MulP(MakePecahanCampuran(2,1,2),MakePecahanCampuran(2,1,2)))







# NO 2 TIPE BENTUKAN GARIS
# ==============================================
# ==============================================

# DEFINISI DAN SPESIFIKASI TYPE
# type point : <x:real, y:real>
#   {<x,y> adalah sebuah point dengan x sebagai absis dan y sebagai ordinat.}
# type garis : <P1:point, P2:point> 
#   {<P1,P2> adalah sebuah garis dengan 2 point.}
#
# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis : point --> real
#   {Absis(P) memberikan nilai absis x dari point P, <x,y>.}
# Ordinat : point --> real
#   {Ordinat(P) memberikan nilai ordinat y dari point P, <x,y>.}
# GarisPoint1 : garis --> point
#   {GarisPoint1(G) memberikan point P1 dari garis G, <P1,P2>.}
# GarisPoint2 : garis --> point
#   {GarisPoint2(G) memberikan point P2 dari garis G, <P1,P2>.}
#
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint : 2 real --> point
#   {MakePoint(x,y) membentuk sebuah point.}
# MakeGaris : 2 point --> garis
#   {MakeGaris(P1,P2) membentuk sebuah garis.}
#
# DEFINISI DAN SPESIFIKASI FUNGSI/OPERATOR TERHADAP GARIS
# Gradien : garis --> real
#   {Gradien(G) menghitung gradien dari sebuah garis.}
# PanjangGaris : garis --> real
#   {PanjangGaris(G) menghitung panjang sebuah garis.}
#
# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSejajar? : 2 garis --> boolean
#   {IsSejajar?(G1,G2) bernilai benar jika kedua gradien bernilai sama.}
# IsTegakLurus? : 2 garis --> boolean
#   {IsTegakLurus?(G1,G2) bernilai benar jika perkalian kedua gradien sama dengan -1.}
#
# REALISASI DALAM PYTHON

def MakePoint(x,y):
    return [x,y]

def Absis(P) :
    return P[0]

def Ordinat(P):
    return P[1]

def MakeGaris(P1,P2) :
    return [P1,P2]

def GarisPoint1(G) :
    return G[0]

def GarisPoint2(G) :
    return G[1]

def Gradien(G) :
    if (Ordinat(GarisPoint1(G)) - Ordinat(GarisPoint2(G)) == 0) :
        if (Absis(GarisPoint1(G)) - Absis(GarisPoint2(G)) == 0) :
            return float('inf')
        else :
            return 0
    
    elif (Absis(GarisPoint1(G)) - Absis(GarisPoint2(G)) == 0) :
        return float('inf')
    
    else :
        return (    (Ordinat(GarisPoint1(G)) - Ordinat(GarisPoint2(G))) 
                                / 
                    (Absis(GarisPoint1(G)) - Absis(GarisPoint2(G)))
                )

def PanjangGaris(P1,P2) :
    return ((Absis(P1) - Absis(P2))**2 + (Ordinat(P1) - Ordinat(P2))**2)**0.5

def IsSejajar(G1,G2) :
    return Gradien(G1) == Gradien(G2)

def IsTegakLurus(G1,G2):
    if Gradien(G1) == float('inf') :
        if Gradien(G2) == 0 :
            return True
        else :
            return False
    elif Gradien(G2) == float('inf') :
        if Gradien(G1) == 0:
            return True
        else :
            return False
    else :
        return (Gradien(G1) * Gradien(G2) == -1)
        

# APLIKASI DALAM PYTHON

print(Gradien(MakeGaris(MakePoint(1,2), MakePoint(2,1))))

print(IsSejajar(MakeGaris(MakePoint(1,2), MakePoint(3,2)), 
                MakeGaris(MakePoint(1,2),MakePoint(2,2))))

print(IsTegakLurus(MakeGaris(MakePoint(0,0), MakePoint(5,0)), 
                    MakeGaris(MakePoint(1,0),MakePoint(1,-10))))





