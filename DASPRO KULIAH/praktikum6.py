#Nama File : rekursifB.py
#Pembuat   : Nadia Azura Nurhaniya
#NIM       : 24060124120019
#Tanggal   : 01 Oktober 2024

#LATIHAN B

#Menghitung perkalian dengan 3 f(n)= 3*n
def kalitiga(n):
    if n == 0:
        return 0
    else:
        return 3 + kalitiga(n-1) 

print(kalitiga(4))
print(kalitiga(9))
print(kalitiga(2))

#Menghitung deret bilangan integer: 1 + 2 + 3 + 4 + ...
def deret(n):
    if n == 1:
        return 1
    else:
        return n + deret(n-1)
    
print(deret(3))
print(deret(10))
print(deret(50))

#Menghitung deret arimatika: 3 + 6 + 9 + 12 + ...
def aritmatika(n):
    if n == 1:
        return 3
    else:
        return n * 3 + aritmatika(n-1)
    
print(aritmatika(2))
print(aritmatika(4))
print(aritmatika(10))

#Menghitung deret geometri: 1 + 3 + 9 + 27 + ...
def deretGeo(n):
    if n == 1:
        return 1
    else:
        return deretGeo(n-1) + (1*3**(n-1))

print(deretGeo(2))
print(deretGeo(5))
print(deretGeo(10))

#Menghitung deret persegi: 1 + 4 + 9 + 16 + ...
def deretPers(n):
    if n == 1:
        return 1
    else:
        return n**2 + deretPers(n-1)
    
print(deretPers(3))
print(deretPers(5))
print(deretPers(4))