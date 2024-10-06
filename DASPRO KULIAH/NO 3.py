
# Nama file : NO 3.py
# Deskripsi : Menghitung hasil pembagian dengan rekursif
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107


# DEFINISI DAN SPESIFIKASI 
# Pembagian : 2 integer > 0 --> integer
    # {Pembagian(x,y) fungsi pembagian x dan y, x / y}

# REALISASI 

def Pembagian(x, y) :
    if x <= 0 :
        return 0
    else:
        return Pembagian(x - y, y) + 1


# APLIKASI
print(Pembagian(14,7)) # --> 2
print(Pembagian(10,5)) # --> 2
print(Pembagian(6,3)) # --> 2