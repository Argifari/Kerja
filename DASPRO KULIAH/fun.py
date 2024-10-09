

# # DEFINISI DAN SPESIFIKASI
# # tagihan : character, real --> real
#     # {tagihan(kode,m) menghitung biaya tagihan bulanan dari sebuah perusahaan air}
# #
# # REALISASI
# #   tagihan(kode,m) :
# #       depend on kode 
# #           kode = 'A' : 30000 + (m - 10)*2500
# #           kode = 'B' : 40000 + (m - 10)*3000
# #           kode = 'C" : 50000 + (m - 10)*3500
# #
# # APLIKASI
# # => tagihan('A', 25) --> 67500
# # => tagihan('B', 50) --> 160000
# # => tagihan('c', 30) --> 120000
# #
# #
# def tagihan(kode,m):
#     if kode == 'A' :
#         return 30000 + (m - 10)*2500
#     elif kode == 'B':
#         return 40000 + (m - 10)*3000
#     elif kode == 'C':
#         return 50000 + (m - 10)*3500


# # APLIKASI
# print(tagihan('A',25))
# print(tagihan('B',50))
# print(tagihan('C',30))


# # DEFINISI DAN SPESIFIKASI
# # IsTomorrowFriday? : integer[1..31], integer[1..12], integer > 0 --> boolean
# #     {IsTomorrowFriday?(d,m,y) bernilai benar jika esok hari adalah jumat}
# # dpm : integer[1..12] --> integer
# #     {dpm(m) memberikan jumlah hari di setiap bulan yang dihitung dari 1 Januari di tahun terkait}
# # IsKabisat? : integer > 0 --> boolean
# #     {IsKabisat?(y) bernilai benar jika y habis dibagi 4, tapi tidak habis dibagi 100, atau y habis dibagi 400}
# # JumlahHari : integer[1..31], integer[1..12], integer > 0 --> integer
# #     {JumlahHari(d,m,y) menghitung jumlah total hari dari 1 Januari di tahun terkait dengan memperhatikan tahun kabisat}

# # dpm(m) :
# #   depend on m
# #       m = 1 : 1
# #       m = 2 : 32
# #       m = 3 : 60
# #       m = 4 : 91
# #       m = 5 : 121
# #       m = 6 : 152
# #       m = 7 : 182
# #       m = 8 : 213
# #       m = 9 : 244
# #       m = 10 : 274
# #       m = 11 : 305
# #       m = 12 : 335
# # IsKabisat?(y): ((y mod 4) = 0 and (y mod 10 != 0)) or y mod 400 = 0
# # 
# # JumlahHari(d,m,y) :
# #   dpm(m) + d - 1 + if IsKabisat?(y) then 1 else 0
# #
# # IsTomorrowFriday(d,m,y):
# #   JumlahHari(d + 1,m,y) mod 7 = 5
# #
# #
# #

# # DEFINISI DAN SPESIFIKASI TYPE
# # type point : <x:real, y:real>
# #   {<x,y> adalah sebuah point dengan x adalah absis dan y adalah ordinat}
# # type line : <P1:point, P2:point>
# #   {<P1,P2> adalah sebuah garis dengan dua point}
# #
# # DEFINISI DAN SPESIFIKASI SELEKTOR
# # Absis : point --> real
# #   {Absis(P) memberikan absis x dari point, <x,y>}
# # Ordinat : point --> real
# #   {Ordinat(P) memberikan ordinat y dari point, <x,y>}
# # LinePoint1 : line --> point
# #   {LinePoint(L) memberikan point pertama(P1) dari line, <P1, P2>}
# # LinePoint2 : line --> point
# #   {LinePoint2(L) memberikan point kedua(P2) dari line, <P1, P2>}
# # 
# # DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# # MakePoint : 2 real --> point
# #   {MakePoint(x,y) membentuk sebuah point dengan x adalah absis dan y adalah ordinat}
# # MakeLine : 2 point --> line
# #   {MakeLine(P1,P2) membentuk sebuah line dengan point 1 dan point 2.}
# #
# # DEFINISI DAN SPESIFIKASI FUNGSI/OPERATOR TERHADAP LINE
# # PanjangGaris : line --> real
# #   {PanjangGaris(L) menghitung panjang garis dari 2 point.}
# # 
# # DEFINSI DAN SPESIFIKASI FUNGIS PREDIKAT
# # IsKuadran3? : line --> boolean
# #   {IsKuadran3?(L) bernilai benar saat keseluruhan line berasda di kuadran 3.}
# #     
# # REALISASI FUNGSI/OPERATOR TERHADAP LINE
# # PanjangGaris(L) : 
# #      sqrt((Absis(LinePoint1(L)) - Absis(LinePoint2(L))) * (Absis(LinePoint1(L)) - Absis(LinePoint2(L))) + 
# #      (Ordinat(LinePoint1(L)) - Ordinat(LinePoint2(L))) * (Ordinat(LinePoint1(L)) - Ordinat(LinePoint2(L)))
# #
# # REALISAIS FUNGSI PREDIKAT
# # IsKuadran3?(L) :
# #       Absis(LinePoint1(L)) < 0 and Absis(LinePoint2(L)) < 0 
# #       and Ordinat(LinePoint1(L)) < 0 and Ordinat(LinePoint2(L))
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #



# def MakePoint(x,y):
#     return [x,y]

# def MakeLine(P1,P2):
#     return [P1,P2]

# def Absis(P):
#     return P[0]

# def Ordinat(P):
#     return P[1]

# def LinePoint1(L) :
#     return L[0]

# def LinePoint2(L) :
#     return L[1]


# def kuadran3(L) :
#     return  Absis(
#             LinePoint1(L)) < 0 and Absis(
#             LinePoint2(L)) < 0 and (Ordinat(
#             LinePoint1(L)) < 0 and Ordinat(
#             LinePoint2(L)) < 0)


# print(kuadran3(MakeLine(MakePoint(-1,-2), MakePoint(-3,-5))))




# UTS 2022 DASPROOO


# HITUNG BIAYA PANGGILAN                                          BiayaPanggilan(kode,detik)

# DEFINISI DAN SPESIFIKASI 
# BiayaPanggilan : character, integer --> integer
#     {BiayaPemanggilan(kode, detik) mmenghitung biaya pemanggilan berdasarkan 
#     kode wilayah dan lama bicara dalam satuan detik}

# REALISASI
# BiayaPemanggilan(kode,detik) :
#     depend on kode 
#         kode = 'A' : if detik <= 30 then 200 else 200 + (detik - 30) * 10
#         kode = 'B' : if detik <= 30 then 300 else 300 + (detik - 30) * 20
#         kode = 'C' : if detik <= 30 then 350 else 350 + (detik - 30) * 25  


# TYPE DATE 

# DEFINISI DAN SPESIFIKASI TYPE

# type date : <d:integer[1..31], m:integer[1..12], y:integer > 0>
#     {<d, m, y> sebuah date dengan tanggal d, bulan m, tahun y}
# type diskonmaskapai : <kategori:string, diskon:real>
#     {<kategori, diskon> sebuah tipe bentukan berisi kategori dan diskon yang didapatkan penumpang}

# DEFINISI DAN SPESIFIKASI SELEKTOR

# Day : date --> integer[1..31]
#     {Day(D) memberikan tanggal d dari date D, <d,m,y>}
# Month : date --> integer[1..12]
#     {Month(D) memberikan bulan m dari date D, <d,m,y>}
# Year : date --> integer > 0
#     {Year(D) memberikan tahun y dari date D, <d,m,y>}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakeDate : integer[1..31], integer[1..12], integer > 0
#     {MakeDate(d,m,y) memebentuk sebuah date dari tanggal d, bulan m, dan tahun y}

# MakeDiskonMaskapai : string, real --> maskapai    
#     {MakeDiskonMaskapai(kategori, diskon) membentuk sebuah diskon maskapai dengan kategori dan diskon}

# DEFINISI DAN SPESIFIKASI FUNGSI/OPERATOR TERHADAP DATE

# DiskonUsia : 2 date --> diskonmaskapai
#     {DiskonUsia(D1,D2) memberikan diskon maspakai dari perhitungan tanggal lahir dengan tanggal keberangkatan}

# Usia : 2 date --> integer
#     {Usia(D1,D2) menghitung usia penumpang sampai date keberangkatan}

# REALISASI

# Usia(D1,D2) :
#     depend on D1, D2
#         Month(D1) <= Month(D2) and Day(D1) < Day(D2) : Year(D2) - Year(D1) - 1
#         Month(D1) >= Month(D2) and Day(D1) >= Day(D2) : Year(D2) - Year(D1)



# DiskonUsia(D1,D2): 
#     depend on D1,D2
#         Usia(D1,D2) <= 2 : MakeDiskonMaskapai("Infant", 75)
#         Usia(D1,D2) > 2 and Usia(D1,D2) <= 12 : MakeDiskonMaskapai("child", 25)
#         Usia(D1,D2) > 12 : MakeDiskonMaskapai("adult", 0)


# TYPE WAKTU

# DEFINISI DAN SPESIFIKASI TYPE

# type waktu : <h:integer >= 0, j:integer[0..23], m:integer[0..59], d:integer[0..59]>
#     {<h,j,m,d> sebuah tipe bentukan waktu yang terdiri dari hari, jam, menit, dan detik}

# DEFINISI DAN SPESIFIKASI SELEKTOR

# Hari : waktu --> integer
#     {Hari(W) memberikan hari h dari waktu W yang terdiri dari <h,j,m,d>}

# Jam : waktu --> integer
#     {Jam(W) memberikan jam j dari waktu W}

# Menit : waktu --> integer
#     {Menit(W) memberikan menit m dari waktu W}

# Detik : waktu --> integer
#     {Detik(W) memberikan detik d dari waktu W}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakeWaktu : integer >= 0, integer[0..23], integer[0..59], integer[0..59] --> waktu
#     {MakeWaktu(h,j,m,d) membentuk sebuah waktu dari hari h, jam j, menit m, dan detik d}

# DEFINISI DAN SPESIFIKASI TERHADAP WAKTU

# GetSelisih : 2 waktu --> integer 
#     {GetSelisih(W1,W2) menghitung selisih dari kedua waktu dalam satuan detik}

# KonversiKeDetik : waktu --> integer
#     {KonversiKeDetik(W) mengubah waktu menjadi satuan detik}


# REALISASI

# KonversiKeDetik(W) : Hari(W)*86400 + Jam(W)*3600 + Menit(W)*60 + Detik(W)

# GetSelisih(W1,W2) : if KonversiKeDetik(W1) >= KonversiKeDetik(W2) then KonversiKeDetik(W1) - KonversiKeDetik(W2) else KonversiKeDetik(W2) - KonversiKeDetik(W1)


# TYPE DATE 

# DEFINISI DAN SPESIFIKASI 

# type date : <d:integer[1..31],m:integer[1..12],y:integer >= 1900>
#     {<d,m,y> sebuah date dengan tanggal d, bulan m, dan tahun y}

# DEFINISI DAN SPESIFIKASI SELEKTOR

# Day : date --> integer
#     {Day(D) memberikan hari d dari date D yang terdiri dari <d,m,y>}

# Month : date --> integer
#     {Month(D) memberikan bulan m dari date D yang terdiri dari <d,m,y>}

# Year : date --> integer
#     {Year(D) memberikan tahun y dari date D yang terdiri dari <d,m,y>}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakeDate : integer[1..31], integer[1..12], integer > 1900 --> date
#     {MakeDate(d,m,y) membentuk sebuah date dengan tanggal d, bulan m, dan tahun y}

# DEFINISI DAN SPESIFIKASI FUNGSI/OPERATOR TERHADAP date

# Calender : date --> string
#     {Calender(D) memberikan kalimat sesuai dengan date D}

# REALISASI

# Calender(D) :
#     depend on Month(D)
#         Month(D) = 1 : IntToStr(Day(D)) + " Desember " + IntToStr(Year(D))
#         Month(D) = 2 :


# TYPE SQUARE

# DEFINISI DAN SPESIFIKASI TYPE

# type point : <x:real,y:real>
#     {<x,y> sebuah point dengan x adalah absis dan y adalah ordinat}

# type square : <P1:point,P3:point>
#     {<P1,P3> sebuah square dengan P1 adalah point diagonal atas dan 
#      P3 adalah point diagonal bawah}

# DEFINISI DAN SPESIFIKASI SELEKTOR

# Absis : point --> real
#     {Absis(P) memberikan absis dari point P, <d,m,y>}

# Ordinat : point --> real
#     {Ordinat(P) memberikan ordinat dari point P, <d,m,y>}

# SquareP1 : square --> point
#     {SquareP1(S) memberikan point diagonal atas dari square S, <P1,P3>}

# SquareP3 : squaree --> point
#     {SquareP3(S) memberikan point diagonal bawah dari square S, <P1,P3>}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR 

# MakePoint : 2 real --> point
#     {MakePoint(x,y) membentuk sebuah point}

# MakeSquare : 2 point --> square
#     {MakeSquare(P1,P3) membentuk sebuah square dengan 2 titk diagonal atas dan bawah}

# DEFINISI DAN SPESIFIKASI FUNGSI/OPERATOR TERHADAP SQUARE

# GetPanjang : square --> real
#     {GetPanjang(S) menghitung panjang sisi square}

# GetLebar : square --> real
#     {GetPanjang(S) menghitung lebar sisi dari square}

# GetDiagonal : square --> real
#     {GetDiagonal(S) menghitung panjang diagonal dari square}

# GetLuas : square --> real
#     {GetLuas(S) menghitung luas dari square}

# REALISASI

# GetPanjang(S): if Absis(SquareP1(S)) >= Absis(SquareP3(S)) then Absis(
#                     SquareP1(S)) - Absis(SquareP3(S))
#             else Absis(SquareP3(S)) - Absis(SquareP1(S))

# GetLebar(S) : if Ordinat(SquareP1(S)) >= Ordinat(SquareP3(S)) then Ordinat(
#                     SquareP1(S)) - Ordinat(SquareP3(S))
#             else Ordinat(SquareP3(S)) - Ordinat(SquareP1(S))

# GetDiagonal : sqrt((Absis(SquareP1(S)) - Absis(SquareP3(S)))*(Absis(
#                 SquareP1(S)) - Absis(SquareP3(S)))  + (Ordinat(SquareP1(S)) - Ordinat(
#                 SquareP3(S))) *(Ordinat(SquareP1(S)) - Ordinat(SquareP3(S))))

# GetLuas(S) : GetLebar(S) * GetPanjang(S)




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













