
def makePN(A,PN) :
    return [A,PN]

def akar(PN):
    return PN[0]

def anak(PN):
    return PN[1]

def IsTreeEmpty(PN):
    return PN == []

def IsOneELmtTree(PN):
    return (not IsTreeEmpty(PN)) and (IsTreeEmpty(anak(PN)))

def NbElmtTree(PN):
    if IsTreeEmpty(PN):
        return 0
    if IsOneELmtTree(PN):
        return 1
    else :
        return 1 + NbElmtTree(anak(PN)[0]) + NbElmtChild(anak[1:])

def NbElmtChild(PN):
    if IsTreeEmpty(PN):
        return 0
    else:
        return NbElmtTree(PN[0]) + NbElmtChild(PN[1:])
    
def NbDaun(PN):
    if IsTreeEmpty(PN):
        return 0
    elif IsOneELmtTree(PN) and IsTreeEmpty(anak(PN)):
        return 1
    else:
        return NbDaun(anak(PN))

def NbDaunChild(PN):
    if IsTreeEmpty(PN):
        return 0
    else:
        return NbDaun(PN[0]) + NbDaunChild(PN[1:])