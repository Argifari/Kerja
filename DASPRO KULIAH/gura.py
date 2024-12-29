def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def list_ke_bilangan(l) :
    if IsEmpty(l) :
        return 0
    else :
        if IsOneElmt(l) :
            return FirstElmt(l)
        else :
            if type(FirstElmt(l)) != int :
                return -1 * (list_ke_bilangan(Tail(l)))
            else :
                return FirstElmt(l)*10**(NbElmt(l)-1) + list_ke_bilangan(Tail(l))
            
def bilangan_ke_list(l) :
    if l == 0:
        return []
    else:
        return bilangan_ke_list(l // 10) + [l % 10]

def shrimp(x,y) :
    if (list_ke_bilangan(x) + list_ke_bilangan(y)) <0 :
        return ['-'] + bilangan_ke_list((list_ke_bilangan(x) + list_ke_bilangan(y))*-1)
    elif (list_ke_bilangan(x) + list_ke_bilangan(y)) == 0 :
        return [0]
    else :
        return bilangan_ke_list(list_ke_bilangan(x) + list_ke_bilangan(y))
    
print(list_ke_bilangan([1,2,3]))