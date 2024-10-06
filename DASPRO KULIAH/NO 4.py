


# Nama file : NO 4.py
# Deskripsi : Operasi perpangkatan
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107

# DEFINISI DAN SPESIFIKASI
# Perpangkatan : integer, integer > 0 --> integer
    # {Perpangkatan(x,n) fungsi pangkat x, x pangkat n}


# REALISASI

def Perpangkatan(x, n) :
    if n == 0 :
        return 1
    else :
        return x * Perpangkatan(x, n - 1)
    
# APLIKASI

print(Perpangkatan(3,3)) # --> 27
print(Perpangkatan(8,2)) # --> 64
print(Perpangkatan(4,5)) # --> 1024