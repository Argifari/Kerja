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
  
# PRINT
print(eval(input()))


# Selamat Menikmati