# Nama File : SetMhs.py
# Deskripsi : membuat tipe bentukan garis beserta konstruksi dan selektornya
# Pembuat   :
#             Muhammad Fikri - 24060124130069
#             Nawaal Hanif Mumtaz Arriye - 24060124120041
#             Muhammad Izzat Fauzan Putra Arya - 24060124130096
#             Muhammad Firdaus Argifari - 24060124130107
#             Rafa Azlan    - 24060124140126
# Tanggal   : 8 November 2024


# DEFINISI DAN SPESIFIKASI TYPE
# type Mhs: <nim: string, nama: string, kelas: character, nilai: list of integer>
# {type Mhs terdiri atas nim, nama, dan kelas mahasiswa, serta kumpulan nilai kuis yang pernah dikerjakan, dengan maksimal jumlah mengerjakan adalah 10 kali. Nilai mahasiswa memiliki rentang antara 0-100}
# type SetMhs: <mhs: list of Mhs>
# {type SetMhs terdiri atas kumpulan Mhs}


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso : elemen, list -> list
# Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e, L) :
    return [e] + L

# MakeMhs : 3 atom, list of integer -> list
# MakeMhs(e, L) menghasilkan sebuah tipe bentukan yang berisi nim, nama, kelas, dan nilai dengan banyak maksimal nilai 10
# Realisasi
def MakeMhs(nim, nama, kelas, nilai) :
    return [nim, nama, kelas, nilai]

# MakeSetMhs : list -> Set
# MakeSetMhs(e, L) : menghasilkan sebuah set berisi kumpulan tipe bentukan Mhs
# Realisasi
def MakeSetMHS(listOfMHS):
    return [listOfMHS]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt : list tidak kosong -> elemen
# FirstElmt(L) : menghasilkan elemen pertama dari list L
# Realisasi
def FirstElmt(L) :
    return L[0]

# Tail : list tidak kosong -> list
# Tail(L) : menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L) :
    return L[1:]

# getNIM : mhs -> string
# getNIM(mhs) : menghasilkan elemen nim dari tipe bentukan mhs
# Realisasi
def getNIM(mhs):
    return mhs[0]

# getNama : mhs -> string
# getNama(mhs) : menghasilkan elemen nama dari tipe bentukan mhs
# Realisasi
def getNama(mhs):
    return mhs[1]

# getKelas : mhs -> character
# getKelas(mhs) : menghasilkan elemen kelas dari tipe bentukan mhs
# Realisasi
def getKelas(mhs) :
    return mhs[2]

# getNilai : mhs -> list of integer
# getNilai(mhs) : menghasilkan list berisi nilai kuis yang sudah dikerjakan
# Realisasi
def getNilai(mhs):
    return mhs[3]


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : list -> boolean
# IsEmpty(L) -> benar jika list kosong
# Realisasi
def IsEmpty(L) :
    return L == []


# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN lIST
# NbElmt : list -> integer
# NbElmt(L) -> menghasilkan banyaknya elemen list, nol jika kosong
# Realisasi
def NbElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return 1 + NbElmt(Tail(L))

# SumElmt : list of integer -> integer
# SumElmt(L) : mengembalikan penjumlahan dari setiap elemen di list L
# Realisasi
def SumElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return FirstElmt(L) + SumElmt(Tail(L))

# AvgElmt : list of integer -> integer
# AvgElmt(L) : menghasilkan nilai rata rata
# Realisasi
def AvgElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return SumElmt(L) / NbElmt(L)

# max2 : 2 integer -> integer
# max2 : mengembalikan nilai terbesar dari 2 integer
# Realisasi
def max2(a, b) :
    if a > b :
        return a
    else :
        return b

# MaxElmt(L) : list of integer -> integer
# MaxElmt(L) : mengembalikan elemen maksimum dari list L
# Realisasi
def MaxElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return max2(FirstElmt(L), MaxElmt(Tail(L)))


# DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
# nilaiTertinggiKelas : character, setOfMhs -> integer
# nilaiTertinggiKelas(kelas, setOfMhs) : mengembalikan nilai rata rata dari suatu kelas
# Realisasi
def nilaiTertinggiKelas(kelas, setOfMhs) :
    if IsEmpty(setOfMhs):
        return 0
    else:
        if not IsEmpty(getNilai(FirstElmt(setOfMhs))) and getKelas(FirstElmt(setOfMhs)) == kelas :
            return max2(AvgElmt(getNilai(FirstElmt(setOfMhs))), nilaiTertinggiKelas(kelas, Tail(setOfMhs)))
        else :
            return nilaiTertinggiKelas(kelas, Tail(setOfMhs))

# mahasiswaTertinggiKelas : character, setOfMhs, integer -> setOfMhs
# mahasiswaTertinggiKelas(kelas, setOfMhs, nilaiTinggi) : menjadi fungsi antara yang akan digunakan pada fungsi utama yaitu himpunanMahasiswaTertinggi. Fungsi ini akan menghasilkan himpunan mahasiswa dengan rata rata nilai tertinggi di kelas. Nilai rata rata tidak akan berubah karena disimpan di parameter ketiga
# Realisasi
def mahasiswaTertinggiKelas(kelas, setOfMhs, nilaitinggi):
    if IsEmpty(setOfMhs):
        return []
    else:
        if getKelas(FirstElmt(setOfMhs)) == kelas and not IsEmpty(getNilai(FirstElmt(setOfMhs))):
            if AvgElmt(getNilai(FirstElmt(setOfMhs))) == nilaitinggi:
                return Konso(FirstElmt(setOfMhs), mahasiswaTertinggiKelas(kelas, Tail(setOfMhs), nilaitinggi))
            else:
                return mahasiswaTertinggiKelas(kelas, Tail(setOfMhs), nilaitinggi)
        else:
            return mahasiswaTertinggiKelas(kelas, Tail(setOfMhs), nilaitinggi)


# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN SET
# setMhs : Mhs, setOfMhs -> setOfMhs
# SetMhs(mhs, setOfMhs) : menambahkan mhs ke setOfMhs jika nim pada mhs belum ada pada setOfMhs
# Realisasi
def SetMhs(mhs, setOfMhs) :
    if IsEmpty(setOfMhs) :
        return Konso(mhs, setOfMhs)
    else :
        if getNIM(FirstElmt(setOfMhs)) == getNIM(mhs) :
            return setOfMhs
        else :
            return Konso(FirstElmt(setOfMhs), SetMhs(mhs, Tail(setOfMhs)))

# lulus : setOfMhs -> setOfMhs
# lulus(setOfMhs) : mengembalikan setOfMhs yang berisi Mhs yang rata rata nilai nya lebih dari sama dengan 70
# Realisasi
def lulus(setOfMhs):
    if IsEmpty(setOfMhs) :
        return []
    else:
        if AvgElmt(getNilai(FirstElmt(setOfMhs))) >= 70 :
            return Konso(FirstElmt(setOfMhs), lulus(Tail(setOfMhs)))
        else:
            return lulus(Tail(setOfMhs))

# tidakMengerjakanKuisKelas : character, setOfMhs -> setOfMhs
# tidakMengerjakanKuisKelas(kelas, setOfMhs) : mengembalikan setOfMhs yang berisi Mhs yang tidak mengerjakan kuis sama sekali
# Realisasi
def tidakMengerjakanKuisKelas(kelas, setOfMhs) :
    if IsEmpty(setOfMhs) :
        return []
    else:
        if (getKelas(FirstElmt(setOfMhs)) == kelas) and IsEmpty(getNilai(FirstElmt(setOfMhs))) :
            return Konso(FirstElmt(setOfMhs), tidakMengerjakanKuisKelas(kelas, Tail(setOfMhs)))
        else:
            return tidakMengerjakanKuisKelas(kelas, Tail(setOfMhs))

# nilaiTertinggi : setOfMhs -> real
# nilaiTertinggi(setOfMhs) : mengembalikan nilai tertinggi dari semua kelas
# Realisasi
def nilaiTertinggi(setOfMhs):
    if IsEmpty(setOfMhs):
        return 0
    else:
        if not IsEmpty(getNilai(FirstElmt(setOfMhs))):
            return max2(AvgElmt(getNilai(FirstElmt(setOfMhs))), nilaiTertinggi(Tail(setOfMhs)))
        else:
            return nilaiTertinggi(Tail(setOfMhs))

# himpunanMahasiswaTertinggi : character, setOfMhs -> setOfMhs
# himpunanMahasiswaTertinggi(kelas, setOfMhs) : mengembalikan setOfMhs yang berisi Mhs dengan rata rata nilai nya sama dengan rata rata tertinggi di kelas yang bersangkutan
# Realisasi
def himpunanMahasiswaTertinggi(kelas, setOfMhs):
    return mahasiswaTertinggiKelas(kelas, setOfMhs, nilaiTertinggiKelas(kelas, setOfMhs))

# jumlahTidakMengerjakanKuis : setOfMhs -> integer
# jumlahTidakMengerjakanKuis(setOfMhs) : mengembalikan jumlah Mhs yang tidak mengerjakan kuis sama sekali dari seluruh kelas
# Realisasi
def jumlahTidakMengerjakanKuis(setOfMhs) :
    if IsEmpty(setOfMhs) :
        return 0
    else:
        if IsEmpty(getNilai(FirstElmt(setOfMhs))) :
            return 1 + FirstElmt(setOfMhs), jumlahTidakMengerjakanKuis(Tail(setOfMhs))
        else :
            return jumlahTidakMengerjakanKuis(Tail(setOfMhs))

# jumlahLulus : setOfMhs -> integer
# jumlahLulus(setOfMhs) : mengembalikan jumlah Mhs yang lulus (rata rata nilai nya lebih dari sama dengan 70)
# Realisasi
def jumlahLulus(setOfMhs):
    return NbElmt(lulus(setOfMhs))