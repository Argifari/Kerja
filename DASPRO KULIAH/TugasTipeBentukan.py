# NO 1 TIPE BENTUKAN PECAHAN CAMPURAN
# =================================================
# =================================================


def Bil(P) :
    return P[0]

def PembPecahanCampuran(P) :
    return P[1]

def PenyPecahanCampuran(P) :
    return P[2]

def PembPecahan(P) :
    return P[0]

def PenyPecahan(P):
    return P[1]

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
    return MakePecahan(
            PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)),
            PenyPecahan(KonversiPecahan(P1))*PembPecahan(KonversiPecahan(P2))
        )

def MulP(P1,P2) :
    return MakePecahan(
            PembPecahan(KonversiPecahan(P1))*PembPecahan(KonversiPecahan(P2)),
            PenyPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2))
        )

def EqP(P1,P2) :
    return (PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)) 
            == PembPecahan(KonversiPecahan(P2))*PenyPecahan(KonversiPecahan(P1)))

def LtP(P1,P2) :
    return (PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)) 
            < PembPecahan(KonversiPecahan(P2))*PenyPecahan(KonversiPecahan(P1)))

def GtP(P1,P2) :
    return (PembPecahan(KonversiPecahan(P1))*PenyPecahan(KonversiPecahan(P2)) 
            > PembPecahan(KonversiPecahan(P2))*PenyPecahan(KonversiPecahan(P1))) 

#print(EqP(MakePecahanCampuran(2,3,4), MakePecahanCampuran(2,3,4)))


# NO 2 TIPE BENTUKAN GARIS
# ==============================================
# ==============================================


def MakePoint(x,y):
    return [x,y]

def Absis(P) :
    return P[0]

def Ordinat(P):
    return P[1]

def MakeGaris(P1,P2) :
    return [P1,P2]

def GarisPoint1(L) :
    return L[0]

def GarisPoint2(L) :
    return L[1]

def Gradien(L) :
    if (Ordinat(GarisPoint1(L)) - Ordinat(GarisPoint2(L)) == 0) :
        if (Absis(GarisPoint1(L)) - Absis(GarisPoint2(L)) == 0) :
            return float('inf')
        else :
            return 0
    
    elif (Absis(GarisPoint1(L)) - Absis(GarisPoint2(L)) == 0) :
        return float('inf')
    
    else :
        return (    (Ordinat(GarisPoint1(L)) - Ordinat(GarisPoint2(L))) 
                                / 
                    (Absis(GarisPoint1(L)) - Absis(GarisPoint2(L)))
                )

def PanjangGaris(P1,P2) :
    return ((Absis(P1) - Absis(P2))**2 + (Ordinat(P1) - Ordinat(P2))**2)**0.5

def IsSejajar(L1,L2) :
    return Gradien(L1) == Gradien(L2)

def IsTegakLurus(L1,L2):
    if Gradien(L1) == float('inf') :
        if Gradien(L2) == 0 :
            return True
        else :
            return False
    elif Gradien(L2) == float('inf') :
        if Gradien(L1) == 0:
            return True
        else :
            return False
    else :
        return (Gradien(L1) * Gradien(L2) == -1)
        


print(Gradien(MakeGaris(MakePoint(1,2), MakePoint(2,1))))
print(IsSejajar(MakeGaris(MakePoint(1,2), MakePoint(3,2)), MakeGaris(MakePoint(1,2),MakePoint(2,2))))
print(IsTegakLurus(MakeGaris(MakePoint(0,0), MakePoint(5,0)), MakeGaris(MakePoint(1,0),MakePoint(1,-10))))





