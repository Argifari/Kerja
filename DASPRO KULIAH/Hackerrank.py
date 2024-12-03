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
        
def kosong(a,b):
    return a + b

def penghitung(X,Y,e,tandaX,tandaY,b,cek):
    if is_empty(X):
        if e == 1:
            return [e]
        else:
            return []
    else:
        if tandaX == '-' and tandaY == '-' or (tandaX == '+' and tandaY == '+'):
            if last_elmt(X) + last_elmt(Y) + e > 9:
                return konsi(penghitung(head(X),head(Y),1,tandaX,tandaY,b,last_elmt(X) + last_elmt(Y) + e - 10), last_elmt(X) + last_elmt(Y) + e - 10)
            else :
                return konsi(penghitung(head(X),head(Y),0,tandaX,tandaY,b,(last_elmt(X) + last_elmt(Y) + e)), (last_elmt(X) + last_elmt(Y) + e))
        elif tandaX == '-' and tandaY == '+' or (tandaX == '+' and tandaY == '-'):
            if b:
                if last_elmt(X) >= last_elmt(Y):
                    return konsi(penghitung(head(X),head(Y),0,tandaX,tandaY,b,(last_elmt(X) - last_elmt(Y) + e) % 10), (last_elmt(X) - last_elmt(Y) + e) % 10)
                else:
                    return konsi(penghitung(head(X),head(Y),-1,tandaX,tandaY,b, 10 + last_elmt(X) - last_elmt(Y) + e), 10 + last_elmt(X) - last_elmt(Y) + e)
                
            else:
                if last_elmt(Y) >= last_elmt(X):
                    return konsi(penghitung(head(X),head(Y),0,tandaX,tandaY,b,(last_elmt(Y) - last_elmt(X) + e) % 10), (last_elmt(Y) - last_elmt(X) + e) % 10)
                else:
                    return konsi(penghitung(head(X),head(Y),-1,tandaX,tandaY,b,10 + last_elmt(Y) - last_elmt(X) + e), 10 + last_elmt(Y) - last_elmt(X) + e)



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
                             ,BesarX(first_elmt(Digit(tail(X),tail(Y))),tail(Digit(tail(X),tail(Y)))),last_elmt(X))
        
        elif first_elmt(X) == '-' and first_elmt(Y) != '-':
            return BesarMana(first_elmt(Digit(tail(X),Y)),tail(Digit(tail(X),Y)),'-','+') + hapus(penghitung(first_elmt(Digit(tail(X),Y)),tail(Digit(tail(X),Y)),0,'-','+'
                             ,BesarX(first_elmt(Digit(tail(X),Y)),tail(Digit(tail(X),Y))),last_elmt(X)))
        
        elif first_elmt(X) != '-' and first_elmt(Y) == '-':
            return BesarMana(first_elmt(Digit(X,tail(Y))),tail(Digit(X,tail(Y))),'+','-') + hapus(penghitung(first_elmt(Digit(X,tail(Y))),tail(Digit(X,tail(Y))),0,'+','-'
                              ,BesarX(first_elmt(Digit(X,tail(Y))),tail(Digit(X,tail(Y)))),last_elmt(X)))
        
        else:
            return BesarMana(first_elmt(Digit(X,Y)),tail(Digit(X,Y)),'+','+') + penghitung(first_elmt(Digit(X,Y)),tail(Digit(X,Y)),0,'+','+'
                            ,BesarX(first_elmt(Digit(X,Y)),tail(Digit(X,Y))),last_elmt(X))


# ===================================================== Geser List =================================================================


def GeserList(L):
    if IsEmpty(L):
        return []
    else:
        if IsAtom(FirstList(L)):
            return KonsLo(FirstList(L), GeserList(TailList(L)))
        elif IsList(FirstList(L)):
            return KonsLi(GeserList(TailList(L)), FirstList(L))

# ==================================================== Petualangan ======================================================================

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
print(shrimp(['-',1,3],[1,2]))