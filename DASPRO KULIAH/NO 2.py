
# Nama File : NO 2.py
# Deskripsi : Operasi Aritmatika Perkalian
# Tanggal   : 1 Okotber 2024
# Pembuat   : Muhammad Firdaus Argifari 24060124130107


# DEFINISI DAN SPESIFIKASI 
# Perkalian : 2 integer --> integer
    # {Perkalian(x,y) perkalian x dan y, x * y}

# REALISASI

def Perkalian(x,y) :
    if y == 0 :
        return 0
    else :
        return x + Perkalian(x, y - 1)



# APLIKASI

print(Perkalian(5,4)) # --> 20
print(Perkalian(2,3)) # --> 6
print(Perkalian(4,5)) # --> 20