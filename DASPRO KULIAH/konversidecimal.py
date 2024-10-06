
#? mengonversikan bilangan desimal ke hexadecimal 
class Decihexa :
    def cihex (self,a) :
        x = a
        ans = []
        def hexa(a) :
            ans.append(a%16)
            if a // 16 != 0 :
                return hexa(a//16)
            else :
                return ans

        ans = hexa(x)
        ans.reverse()
        kamushex = {
            10 : 'A',
            11 : 'B',
            12 : 'C',
            13 : 'D',
            14 : 'E',
            15 : 'F'
        }
        answer = ''
        for i in ans:
             if (10 <= i <= 15) :
                i = kamushex.get(i,0)
             answer += str(i)

        return answer



#!mengonversikan bilangan decimal ke octal

class Decioctal :
    def decioc (self, a) :
        x = a
        ans = []

        def octal (a) :
            ans.append(a%8)
            if a//8 != 0 :
                return octal(a//8)
            else :
                return ans

        ans = octal(x)
        ans.reverse()
        answer = ''
        for i in ans:
            answer += str(i)

        return answer

#* pemilihan konversi decimal
butuh = ''
while (butuh.upper() != 'HEXADECIMAL') and (butuh.upper() != 'OCTAL')  :
    butuh = input('Ubah Decimal ke (hexadecimal / octal) : ')
    if (butuh.upper() != 'HEXADECIMAL') and (butuh.upper() != 'OCTAL') :
        print('maaf salah masukkan!')
        

if butuh.upper() == 'HEXADECIMAL' :
    operasi = Decihexa()
    y = int(input('>> Masukkan angka decimal : '))
    print('>> hasil : ',operasi.cihex(y))
else :
    operasi = Decioctal()
    y = int(input('>> Masukkan angka decimal : '))
    print('>> hasil : ',operasi.decioc(y))

