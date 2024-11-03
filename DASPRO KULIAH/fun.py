def IsEmpty(L):
    return L == []

def FirstElmt(L):
    return L[0]
def LastElmt(L):
    return L[-1]

def HeadTail(L):
    return L[1:-1]





def IsPalindrom(L):
    print(L)
    if not IsEmpty(L):
        if FirstElmt(L) != LastElmt(L):
            return False
        else:
            return IsPalindrom(HeadTail(L))
    else :
        return True


print(IsPalindrom("AYA"))