
from list import *
setOfMHS = [
    ['5', 'John Doe', 'A', [70, 20]],
    ['6', 'John Doe', 'A', [80, 80]],
    ['6', 'John Doe', 'D', [80, 45]],
    ['7', 'John Doe', 'A', [90, 1]],
    ['8', 'John Doe', 'A', []],
    ['9', 'John Doe', 'A', []],
]
def NIM(listOfMHS):
    return listOfMHS[0]

def Nama(listOfMHS):
    return listOfMHS[1]

def Kelas(listOfMHS):
    return listOfMHS[2]

def Nilai(listOfMHS):
    return listOfMHS[3]

def MakeMHS(a,b,c,d):
    return [a,b,c,d]

def MakeSetofMHS(listOfMHS):
    return [listOfMHS]

def AddMHS(Mhs,listOfMHS):
    if IsEmpty(listOfMHS):
        return Konso(Mhs,listOfMHS)
    else:
        if NIM(FirstElmt(listOfMHS)) == NIM(Mhs): 
            return listOfMHS
        else:
            return Konso(Mhs,listOfMHS)

def SetMHSLulus(listOfMHS):
    if IsEmpty(listOfMHS):
        return []
    else:
        if AvgElmt(Nilai(FirstElmt(listOfMHS))) >= 70:
            return Konso(FirstElmt(listOfMHS), SetMHSLulus(Tail(listOfMHS)))
        else:
            return SetMHSLulus(Tail(listOfMHS))
        
#print(SetMHSLulus(setOfMHS))

def SetMHSnoQuizinClass(kelas:chr, listOfMHS:List[list]) -> List[list]:
    if IsEmpty(listOfMHS):
        return []
    else:
        if (Kelas(FirstElmt(listOfMHS)) == kelas and 
            IsEmpty(Nilai(FirstElmt(listOfMHS)))) :
            return Konso(FirstElmt(listOfMHS), 
                    SetMHSnoQuizinClass(kelas,Tail(listOfMHS)))
        else:
            return SetMHSnoQuizinClass(kelas,Tail(listOfMHS))
#print(SetMHSnoQuizinClass('a',setOfMHS))

def HighessScoreAllClass(listOfMHS):
    if IsEmpty(listOfMHS):
        return 0
    else:
        if not IsEmpty(Nilai(FirstElmt(listOfMHS))):
            return max2(MaxElmt(Nilai(FirstElmt(listOfMHS))), HighessScoreAllClass(Tail(listOfMHS)))
        else:
            return HighessScoreAllClass(Tail(listOfMHS))

def HighessScore(kls,listOfMHS):
    if IsEmpty(listOfMHS):
        return 0
    else:
        if not IsEmpty(Nilai(FirstElmt(listOfMHS))) and Kelas(FirstElmt(listOfMHS)) == kls:
            return max2(MaxElmt(Nilai(FirstElmt(listOfMHS))), HighessScore(kls,Tail(listOfMHS)))
        else:
            return HighessScore(kls,Tail(listOfMHS))
        

#print(HighessScoreAllClass(setOfMHS))

def BesMHS(kls,listofMHS,highscore):
    if IsEmpty(listofMHS):
        return []
    else :
        if not IsEmpty(Nilai(FirstElmt(listofMHS))) :
            if (Kelas(FirstElmt(listofMHS)) == kls and 
                MaxElmt(Nilai(FirstElmt(listofMHS))) == highscore):
                return Konso(FirstElmt(listofMHS), BesMHS(kls,Tail(listofMHS), highscore))
            else:
                return BesMHS(kls,Tail(listofMHS),highscore)
        else:
            return BesMHS(kls,Tail(listofMHS),highscore)


def SetOfBestMHS(kls, listOfMHS):
    return BesMHS(kls,listOfMHS,HighessScore(kls,listOfMHS))

print(SetOfBestMHS('A',setOfMHS))

def SetMHSnoQuiz(listOfMHS:List[list]) -> List[list]:
    if IsEmpty(listOfMHS):
        return []
    else:
        if IsEmpty(Nilai(FirstElmt(listOfMHS))) :
            return Konso(FirstElmt(listOfMHS), 
                    SetMHSnoQuiz(Tail(listOfMHS)))
        else:
            return SetMHSnoQuiz(Tail(listOfMHS))
        
def NoquizMHS(listOfMHS):
    return NbElmt(SetMHSnoQuiz(listOfMHS))

def NiceGradeMHS(listOfMHS):
    return NbElmt(SetMHSLulus(listOfMHS))

print(NiceGradeMHS(setOfMHS))
