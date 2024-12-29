

# ============================================= DUEL SIHIR =================================================================

# Nama : Muhammad Firdaus Argifari
# Tanggal : 3 Desember 2024

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def Konso(e, L):
    return [e] + L

def isEmpty(L):
    return L == []

def dimensi(L): # atau NbElmt()
    if isEmpty(L):
        return 0
    else:
        return 1 + dimensi(Tail(L))

# Skor : 2list, 2integer --> string
# {Skor(S,M,pointsS,pointsM) menghitung jumlah skor dan mengembalikan siapa pemenangnya.}


def Skor(S,M,pointS,pointM):
    if isEmpty(S):
        if pointM < pointS :
            return 'Snape Menang'
        elif pointM > pointS :
            return 'McGonagall Menang'
        elif pointS == pointM :
            return 'Keduanya Seri'
    elif FirstElmt(S) > FirstElmt(M):
        return Skor(Tail(S),Tail(M),pointS + 1, pointM)
    elif FirstElmt(S) < FirstElmt(M):
        return Skor(Tail(S),Tail(M),pointS, pointM + 1)
    elif FirstElmt(S) == FirstElmt(M):
        return Skor(Tail(S),Tail(M),pointS,pointM)
    
# DuelSihir : 2 list --> string 
# {DuelSihir(S,M) mengembalikan string sapa yang menang.}

def DuelSihir(S, M):
    if isEmpty(S):
        return 'Keduanya Seri'
    else:
        return Skor(S,M,0,0)



# ===================================================================== MATEMATIKA GURA ======================================================

# Nama File: matematika_gura.py
# Pembuat: 
# Tanggal: 
# Deskripsi: Mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.

# DEFINISI DAN SPESIFIKASI
# shrimp --> list: integer
# shrimp(X, Y) mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.

# REALISASI
def konso(e, L):
    return [e] + L
    
def konsi(L, e):
    return L + [e]
  
def first_elmt(L):
    return L[0]
  
def last_elmt(L):
    return L[-1]
  
def head(L):
    return L[:-1]
  
def tail(L):
    return L[1:]

def is_empty(L):
    return len(L) == 0

def IsOneElmt(L:list) -> bool:
    return head(L) == [] and tail(L) == []

def NbElmt(L:list) -> int:
    if is_empty(L):
        return 0
    else :
        return 1 + NbElmt(tail(L))


# ======================================================= MATEMATIKA GURA ===================================================

# Digit : 2list --> <list of list,list>
# fungsi digit berfungsi untuk membuat X dan Y memiliki digit yang sama. contoh [1,2] + [9] menjadi [1,2] + [0,9]

def Digit(X,Y):
    if is_empty(X) or is_empty(Y):
        return []
    else:
        if NbElmt(X) > NbElmt(Y):
            return Digit(X, konso(0,Y))
        elif NbElmt(X) < NbElmt(Y):
            return Digit(konso(0,X), Y)
        else:
            return [X] + Y
        
# BesarMana : 2 list, 2 character --> list
# fungsi BesarMana mngembalikan tanda dari bilangan antara positif atau negatif dan tanda mengeikuti bilangan yang paling besar antara X dan Y.

def BesarMana(X,Y,tandaX,tandaY):
    if is_empty(X):
        return []
    else:
        if first_elmt(X) > first_elmt(Y):
            if tandaX == '+':
                return []
            return [tandaX]
        elif first_elmt(Y) > first_elmt(X):
            if tandaY == '+':
                return []
            return [tandaY]
        else:
            return BesarMana(tail(X),tail(Y),tandaX,tandaY)

# BesarX : 2 list --> boolean
# fungsi BesarX mengembalikan boolean untuk mengetahui apakah X lebih dari Y agar pengurangan tidak ada yang menjadi negatif

def BesarX(X,Y):
    if is_empty(X):
        return False
    else:
        if first_elmt(X) > first_elmt(Y):
            return True
        elif first_elmt(Y) > first_elmt(X):
            return False
        else:
            return BesarX(tail(X),tail(Y))
        
# penghitung : 2list,integer,2 character, boolean --> list
# fungsi penghitung untuk menghitung X dan Y tergantung dari tanda X dan tanda Y. parameter b adalah boolean dari hasil BesarX(X,Y). parameter e berguna untuk carry menyimpan data sebelumnya.

def penghitung(X,Y,e,tandaX,tandaY,b):
    if is_empty(X):
        if e == 1:
            return [e]
        else:
            return []
    else:
        if tandaX == '-' and tandaY == '-' or (tandaX == '+' and tandaY == '+'):
            if last_elmt(X) + last_elmt(Y) + e > 9:
                return konsi(penghitung(head(X),head(Y),1,tandaX,tandaY,b), last_elmt(X) + last_elmt(Y) + e - 10)
            else :
                return konsi(penghitung(head(X),head(Y),0,tandaX,tandaY,b), (last_elmt(X) + last_elmt(Y) + e))
        elif tandaX == '-' and tandaY == '+' or (tandaX == '+' and tandaY == '-'):
            if b:
                if last_elmt(X) >= last_elmt(Y):
                    return konsi(penghitung(head(X),head(Y),0,tandaX,tandaY,b), (last_elmt(X) - last_elmt(Y) + e) % 10)
                else:
                    return konsi(penghitung(head(X),head(Y),-1,tandaX,tandaY,b), 10 + last_elmt(X) - last_elmt(Y) + e)
                
            else:
                if last_elmt(Y) >= last_elmt(X):
                    return konsi(penghitung(head(X),head(Y),0,tandaX,tandaY,b), (last_elmt(Y) - last_elmt(X) + e) % 10)
                else:
                    return konsi(penghitung(head(X),head(Y),-1,tandaX,tandaY,b), 10 + last_elmt(Y) - last_elmt(X) + e)

# hapus : list --> list
# fungsi hapus untuk menghapus angka 0 di awal list X. contoh [0,1,1] harusnya [1,1]

def hapus(X):
    if is_empty(X):
        return []
    elif first_elmt(X) != 0:
        return X
    else:
        if first_elmt(X) == 0 and is_empty(tail(X)):
            return X
        else:
            return hapus(tail(X))


# shrimp : 2 list --> list
# fungsi shrimp menghitung bilangan seperti representasi gura secara list.

def shrimp(X, Y):
    if is_empty(X) and is_empty(Y):
        return []
    elif is_empty(X) and not is_empty(Y):
        return Y
    elif is_empty(Y) and not is_empty(X):
        return X
    else:
        if first_elmt(X) == '-' and first_elmt(Y) == '-':
            return BesarMana(first_elmt(Digit(tail(X),tail(Y))),tail(Digit(tail(X),tail(Y))),'-','-') + penghitung(first_elmt(Digit(tail(X),tail(Y))),tail(Digit(tail(X),tail(Y))),0,'-','-'
                             ,BesarX(first_elmt(Digit(tail(X),tail(Y))),tail(Digit(tail(X),tail(Y)))))
        
        elif first_elmt(X) == '-' and first_elmt(Y) != '-':
            return BesarMana(first_elmt(Digit(tail(X),Y)),tail(Digit(tail(X),Y)),'-','+') + hapus(penghitung(first_elmt(Digit(tail(X),Y)),tail(Digit(tail(X),Y)),0,'-','+'
                             ,BesarX(first_elmt(Digit(tail(X),Y)),tail(Digit(tail(X),Y)))))
        
        elif first_elmt(X) != '-' and first_elmt(Y) == '-':
            return BesarMana(first_elmt(Digit(X,tail(Y))),tail(Digit(X,tail(Y))),'+','-') + hapus(penghitung(first_elmt(Digit(X,tail(Y))),tail(Digit(X,tail(Y))),0,'+','-'
                              ,BesarX(first_elmt(Digit(X,tail(Y))),tail(Digit(X,tail(Y))))))
        
        else:
            return BesarMana(first_elmt(Digit(X,Y)),tail(Digit(X,Y)),'+','+') + penghitung(first_elmt(Digit(X,Y)),tail(Digit(X,Y)),0,'+','+'
                            ,BesarX(first_elmt(Digit(X,Y)),tail(Digit(X,Y))))


# ===================================================== Geser List =================================================================

#NAMA: Muhammad Firdaus Argifari
#NIM : 24060124130107

#Konstruktor
# DEFINISI DAN SPESIFIKASI
# KonsLo(e, L): elemen, List of List --> List of List
# KonsLo(e, L) Menambahkan elemen di baris awal List of List
def KonsLo(e, L):
    return [e] + L

# DEFINISI DAN SPESIFIKASI
# KonsLi(L, e): List of List, elemen --> List of List
# KonsLi(L, e) Menambah6y5ukan elemen di baris akhir List of List
def KonsLi(L, e):
    return L + [e]

# Selektor

# DEFINISI DAN SPESIFIKASI
# FirstList(L): List of List --> elemen
# FirstList(L) Menampilkan elemen pertama dari List of List
def FirstList(L):
    return L[0]

# DEFINISI DAN SPESIFIKASI
# LastList(L): List of List --> elemen
# LastList(L) Menampilkan elemen terakhir dari List of List
def LastList(L):
    return L[-1]

# DEFINISI DAN SPESIFIKASI
# HeadList(L): List of List --> List of List
# HeadList(L) List of List dengan menghilangkan elemen terakhirnya
def HeadList(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI
# TailList(L): List of List --> List of List
# TailList(L) List of List dengan menghilangkan elemen pertamanya
def TailList(L):
    return L[1:]

# Predikat

# DEFINISI DAN SPESIFIKASI
# isEmpty(L): List of List --> boolean
# isEmpty(L) mengecek apakah List of List kosong
def IsEmpty(L):
    return L == []

# DEFINISI DAN SPESIFIKASI
# IsAtom: List of List --> boolean
# IsAtom Cek apakah S adalah atom atau bukan sebuah list
def IsAtom(S):
    return type(S) != list

# DEFINISI DAN SPESIFIKASI
# IsList: List of List --> boolean
# IsList Cek apakah S adalah List
def IsList(S):
    return type(S) == list

# DEFINISI DAN SPESIFIKASI
# GeserList: List of List --> List of List
# GeserList Fungsi merapikan perkakas milik Andi

def GeserList(L):
    if IsEmpty(L):
        return []
    else:
        if IsAtom(FirstList(L)):
            return KonsLo(FirstList(L), GeserList(TailList(L)))
        elif IsList(FirstList(L)):
            return KonsLi(GeserList(TailList(L)), FirstList(L))

# ==================================================== Petualangan Di Dunia Lumerion ======================================================================

# operator : list --> character
# {operator(L) mengembalikan operator dalam list.}
def operator(L):
    return L[0]
# operand1 : list -->  integer
# {operand1(L) mengembalikan elemen di dalam list pertama.}
def operand1(L):
    return L[1]
# operand2 : list --> integer
# {operand2(L) mengembalikan elemen di dalam list kedua.}
def operand2(L):
    return L[2]

# EvaluateExpression : list --> real
# {EvaluateExpression(L) menghitung elemen di dalam list sesuai dengan operatornya.}

def EvaluateExpression(L):
    if IsEmpty(L):
        return []
    else:
        if operator(L) == '+':
            return operand1(L) + operand2(L)
        elif operator(L) == '-':
            return operand1(L) - operand2(L)
        elif operator(L) == '*':
            return operand1(L) * operand2(L)
        elif operator(L) =='/':
            return (operand1(L) / operand2(L))
 
# ==================================================================== PERPUSTAKAAN AGUNG ================================================


def getTag(shelf):
    return FirstElmt(FirstList(shelf))

def getBooks(shelf):
    return LastElmt(FirstList(shelf))

# FUNGSI KHUSUS
# bersifat opsional, tidak harus digunakan
# boleh buat fungsi antara sendiri

# makeShelf: string, list -> shelf
# fungsi ini membuat sebuah shelf baru dengan komponen tag dan book
def makeShelf(tag, book):
    return [[tag] + [book]]

# AddToShelf: string, list -> shelf
# fungsi ini menambahkan buku ke sebuah shelf dengan tag tertentu
def AddToShelf(tag, book):
    return [tag] + [book]

# ----------------- FUNCTION ------------------------

# AddBooks: shelves, string, list -> shelves
# fungsi ini mengeluarkan shelves yang sudah ada dengan menambahkan buku ke sebuah shelf dengan tag tertentu

def AddBooks(shelves, tag, book):
    if IsEmpty(book):
        return shelves
    if IsEmpty(shelves):
        return makeShelf(tag,book)
    else:
        if getTag(shelves) == tag:
            return makeShelf(getTag(shelves), getBooks(shelves) + book) + TailList(shelves)
        else:
            return Konso(FirstList(shelves),AddBooks(TailList(shelves),tag,book))
