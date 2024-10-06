
# Nama file : NO 7.py
# Deskripsi : Menghitung deret aritmatika dengan rekursif
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107


# DEFINISI DAN SPESIFIKASI
# deretAritmatika : integer > 0 --> integer
    # {deretAritmatika(n) menghitung deret aritmatika dengan beda 3, 3 + 6 + ...}

# REALISASI

def deretAritmatika(n):
    if n == 1:
        return 3
    else :
        return deretAritmatika(n - 1) + n*3

# APLIKASI
print(deretAritmatika(4)) # --> 30
print(deretAritmatika(100)) # --> 15150
print(deretAritmatika(32)) # --> 1584