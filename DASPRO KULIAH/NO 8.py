
# Nama file : NO 7.py
# Deskripsi : Menghitung deret geometri dengan rekursif
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107


# DEFINISI DAN SPESIFIKASI
# deretGeometri : integer > 0 --> integer
    # {deretGeometri(n) menghitung deret geometri dengan rasio 3, 1 + 3 + 9 + . . . }
# REALISASI

def deretGeometri (n) :
    if n == 1:
        return 1
    else :
        return deretGeometri(n - 1) + 1*3**(n-1)

# APLIKASI
print(deretGeometri(10)) # --> 29524
print(deretGeometri(14)) # --> 2391484
print(deretGeometri(2)) # --> 4