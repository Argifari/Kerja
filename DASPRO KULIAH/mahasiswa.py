from list import *
from typing import List
def MakeMhs(nim: str, nama: str, kelas: chr, nilai: list) -> list : 
    return [nim, nama, kelas, nilai]

def MakeSetofMHS(listOfMHS:list) -> List[list]:
    return [listOfMHS]

def getNIM (mhs: list) -> str :
    return mhs[0]

def getNama(mhs: list) -> str :
    return mhs[1]

def getKelas(mhs: list) -> chr :
    return mhs[2]

def getNilai(mhs: list) -> list :
    return mhs[3]

setOfMhs = [
    ['5', 'John Doe', 'A', [70, 20]],
    ['6', 'John Doe', 'A', [80, 80]],
    ['6', 'John Doe', 'D', [80, 45]],
    ['7', 'John Doe', 'A', [90, 1]],
    ['8', 'John Doe', 'A', []],
    ['9', 'John Doe', 'A', []],
]

# fungsi untuk menambahkan mhs ketika tidak ditemukan nim mhs yang belum ada di list
def SetMhs(mhs, listMhs) : 
    if IsEmpty(listMhs) : 
        return Konso(mhs, listMhs)
    else : 
        if getNIM(FirstElmt(listMhs)) == getNIM(mhs) :
            return listMhs
        else : 
            return Konso(FirstElmt(listMhs), SetMhs(mhs, Tail(listMhs)))

# print(SetMhs(['7', 'John Doe', 'A', [90, 100]], setOfMhs))
            
def lulus(listMhs):
    if IsEmpty(listMhs) :
        return []
    else:
        if AvgElmt(getNilai(FirstElmt(listMhs))) >= 70 :
            return Konso(FirstElmt(listMhs), lulus(Tail(listMhs)))
        else:
            return lulus(Tail(listMhs))

# print(lulus(setOfMhs))

def tidakMengerjakanKuisKelas(kelas, listMhs) :
    if IsEmpty(listMhs) :
        return []
    else:
        if (getKelas(FirstElmt(listMhs)) == kelas) and IsEmpty(getNilai(FirstElmt(listMhs))) :
            return Konso(FirstElmt(listMhs), tidakMengerjakanKuisKelas(kelas, Tail(listMhs)))
        else:
            return tidakMengerjakanKuisKelas(kelas, Tail(listMhs))

# print(tidakMengerjakanKuisKelas("A", setOfMhs))

def nilaiTertinggi(listMhs):
    if IsEmpty(listMhs):
        return 0
    else:
        if not IsEmpty(getNilai(FirstElmt(listMhs))):
            return max2(MaxElmt(getNilai(FirstElmt(listMhs))), nilaiTertinggi(Tail(listMhs)))
        else:
            return nilaiTertinggi(Tail(listMhs))

print(nilaiTertinggi(setOfMhs))

# fungsi antara
def nilaiTertinggiKelas(kelas, listMhs) : 
    if IsEmpty(listMhs):
        return 0
    else:
        if not IsEmpty(getNilai(FirstElmt(listMhs))) and getKelas(FirstElmt(listMhs)) == kelas :
            return max2(MaxElmt(getNilai(FirstElmt(listMhs))), nilaiTertinggiKelas(kelas, Tail(listMhs)))
        else : 
            return nilaiTertinggiKelas(kelas, Tail(listMhs))

# print(nilaiTertinggiKelas("A", setOfMhs))

def mahasiswaTertinggiKelas(kelas, listMhs, nilaitinggi):
    if IsEmpty(listMhs):
        return []
    else:
        if getKelas(FirstElmt(listMhs)) == kelas and not IsEmpty(getNilai(FirstElmt(listMhs))): 
            if MaxElmt(getNilai(FirstElmt(listMhs))) == nilaitinggi:
                return Konso(FirstElmt(listMhs), mahasiswaTertinggiKelas(kelas, Tail(listMhs),nilaitinggi))
            else:
                return mahasiswaTertinggiKelas(kelas, Tail(listMhs),nilaitinggi)
        else:
            return mahasiswaTertinggiKelas(kelas, Tail(listMhs),nilaitinggi)


def himpunanMahasiswaTertinggi(kls, listOfMHS):
    return mahasiswaTertinggiKelas(kls,listOfMHS,nilaiTertinggiKelas(kls,listOfMHS))

print(himpunanMahasiswaTertinggi('A',setOfMhs))

def tidakMengerjakanKuis(listMhs) :
    if IsEmpty(listMhs) :
        return []
    else:
        if IsEmpty(getNilai(FirstElmt(listMhs))) :
            return Konso(FirstElmt(listMhs), tidakMengerjakanKuis(Tail(listMhs)))
        else : 
            return tidakMengerjakanKuis(Tail(listMhs))

def jumlahTidakMengerjakanKuis(listMhs) : 
    return NbElmt(tidakMengerjakanKuis(listMhs))
    
# print(jumlahTidakMengerjakanKuis(setOfMhs))

def jumlahLulus(listMhs): 
    return NbElmt(lulus(listMhs))

# print(jumlahLulus(setOfMhs))