
# Nama file : NO 9.py
# Deskripsi : menghitung deret aritmatika dua tingkat dengan rekursif
# Tanggal : 3 Oktober 2024
# Pembuat : Muhammad Firdaus Argifari 24060124130107

# DEFINISI DAN SPESIFIKASI
# deretdua : integer > 0 --> integer
    # {deretdua(n) menghitung deret aritmatika tingkat dua}

# REALISASI

def deretdua(n) :
    if n == 1:
        return 1
    else :
        return deretdua(n - 1) + n**2 
    
# APLIKASI    
print(deretdua(4)) # --> 30
print(deretdua(18)) # --> 2109
print(deretdua(31)) # --> 10416