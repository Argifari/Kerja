
# Nama file : NO 5.py
# Deskripsi : Menghitung fungsi perkalian n dengan rekursif
# Tanggal : 1 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107


# DEFINISI DAN SPESIFIKASI
# nthree : integer --> integer
    # {nthree(n) adalah fungsi perkalian 3 dan n, 3 * n}

# REALISASI 

def nthree(n):
    if n == 0:
        return 0
    else :
        return nthree(n - 1) + 3

# APLIKASI 
print(nthree(6)) # --> 18
print(nthree(10)) # --> 30
print(nthree(5)) # --> 15