
# Nama file : NO 6.py
# Deskripsi : menghitung deret aritmatika dengan beda 1 melalui cara rekursif
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107


# DEFINISI DAN SPESIFIKASI
# deret : integer > 0 --> integer
    # {deret(n) mengitung deret dari suku ke-1 sampai suku ke-n}

# REALISASI

def deret(n):
    if n == 1 :
        return 1
    else :
        return deret(n - 1) + n
    
# REALISASI
print(deret(10)) # --> 55
print(deret(12)) # --> 78
print(deret(100)) #--> 5050