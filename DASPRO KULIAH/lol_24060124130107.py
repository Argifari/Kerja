



from list import *
from Set_24060124130107 import *

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

def konsLo(L,S) :
    return [L] + S

def konsLi(S,L):
    return S + [L]

def firstList(S):
    return S[0]

def lastList(S):
    return S[-1]

def tailList(S):
    return S[1:]

def headList(S):
    return S[:-1]

def IsMemberLS(L,S):
    if IsEmpty(S):
        return False
    else :
        if IsAtom(firstList(S)):
            return IsMemberLS(L,tailList(S))
        else:
            if IsEqualSetVersi1(firstList(S),L):
                return True
            else:
                return IsMemberLS(L,tailList(S))
            
def IsEqS(S1,S2):
    if IsEmpty(S1) and IsEmpty(S2) :
        return True
    else :
        if IsAtom(firstList(S1)) and IsAtom(firstList(S2)):
            if firstList(S1) == firstList(S2):
                return IsEqS(tailList(S1), tailList(S2))
            else:
                return False
        elif IsList(firstList(S1)) and IsList(firstList(S2)):
            return IsEqS(firstList(S1),firstList(S2)) and IsEqS(tailList(S1),tailList(S2))
        else:
            return False
        
def IsMemberS(x,S):
    if IsEmpty(S):
        return False
    else :
        if IsAtom(firstList(S)):
            if x == firstList(S):
                return True
            else:
                return IsMemberS(x, tailList(S))
        else:
            return IsMemberS(x,firstList(S)) or IsMemberS(x,tailList(S))
# print(IsMemberS(3,[1,2,[3,4,5]]))

def RemberLOL(x,S):
    if IsEmpty(S):
        return []
    else :
        if IsAtom(firstList(S)):
            if x == firstList(S):
                return RemberLOL(x,tailList(S))
            else:
                return konsLo(firstList(S),RemberLOL(x,tailList(S)))
        else:
            return konsLo(RemberLOL(x,firstList(S)), RemberLOL(x,tailList(S)))

def MaxLOL(S):
    if IsOneElmt(S):
        if IsAtom(firstList(S)):
            return firstList(S)
        else:
            return MaxLOL(firstList(S))
    else:
        if IsAtom(firstList(S)):
            return max2(firstList(S), MaxLOL(tailList(S)))
        else:
            return max2(MaxLOL(firstList(S)), MaxLOL(tailList(S)))

def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(firstList(S)):
            return 1 + NBElmtAtom(tailList(S))
        else:
            return NBElmtAtom(tailList(S))
        
def NBElmtList(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(firstList(S)):
            return 1 + NBElmtList(tailList(S))
        else:
            return NBElmtList(tailList(S))

def SumLOL(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(firstList(S)):
            return firstList(S) + SumLOL(tailList(S))
        else:
            return SumLOL(firstList(S)) + SumLOL(tailList(S))

def MaxNBElmtlist(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(firstList(S)):
            return max2(NbElmt(firstList(S)), MaxNBElmtlist(tailList(S)))
        else:
            return MaxNBElmtlist(tailList(S))

def MaxSumElmt(S):
    if IsOneElmt(S):
        if IsAtom(FirstElmt(S)):
            return firstList(S)
        else:
            return SumLOL(firstList(S))
    else:
        if IsAtom(firstList(S)):
            return max2(firstList(S), MaxSumElmt(tailList(S)))
        else:
            return max2(SumLOL(firstList(S)), MaxSumElmt(tailList(S)))

