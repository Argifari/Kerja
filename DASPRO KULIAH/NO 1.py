
# Nama File : NO 1.py
# Deskripsi : Operasi Aritmatika Pengurangan
# Tanggal   : 1 Oktober 2024
# Pembuat   : Muhammad Firdaus Argifari 24060124130107

# DEFINISI DAN SPESIFIKASI 
# AritmatikaPengurangan : 2 integer --> integer
    # {AritmatikaPengurangan(x,y) fungsi pengurangan x oleh y, x - y}

# REALISASI 

def AritmatikaPengurangan(x,y):
    if y == 0 :
        return x
    
    return AritmatikaPengurangan(x, y - 1) - 1


# APLIKASI
print(AritmatikaPengurangan(5,4)) # --> 1
print(AritmatikaPengurangan(5,3)) # --> 2
print(AritmatikaPengurangan(10,2)) # --> 8