
# i = 1
# while i <= 3 :
#     print("case",i)
#     hargaTahu = input("Harga tahu: ")
#     hargaTempe = input("Harga tempe: ")
#     hargaRoti = input("Harga roti: ")

#     TotalBiaya = int(hargaTahu)*4 + int(hargaTempe)*4 + int(hargaRoti)*5
#     BiayaAkhir = TotalBiaya - TotalBiaya*5/100


#     if len(str(TotalBiaya)) == 5:
#         jumlahPerDigit = (TotalBiaya % 10) + ((TotalBiaya//10) % 10) + ((TotalBiaya//100) % 10) + ((TotalBiaya//1000) % 10) + ((TotalBiaya//10000) % 10)
#         if jumlahPerDigit % 7 == 0 :
#             BiayaAkhir -= BiayaAkhir*10/100


#     print("Nona Deb perlu membayar sebesar",int(BiayaAkhir))
#     i += 1  



HargaAwal = int(input("Masukkan harga awal barang: "))
JumlahPenawaran = int(input("Masukkan jumlah penawaran: "))

if JumlahPenawaran == 1: 
    print("Total biaya yang harus dibayar adalah", int(HargaAwal))
elif JumlahPenawaran == 2:
    HargaAwal += HargaAwal*10/100
    if HargaAwal > 100000000 :
        HargaAwal -= 5000000
    print("Total biaya yang harus dibayar adalah", int(HargaAwal))
elif JumlahPenawaran == 3:
    HargaAwal += HargaAwal*10/100
    if HargaAwal > 100000000 :
        HargaAwal -= 5000000
    HargaAwal += HargaAwal*10/100
    if HargaAwal > 50000000 :
        HargaAwal -= HargaAwal*20/100
    print("Total biaya yang harus dibayar adalah", int(HargaAwal))

else:
    print("Total biaya yang harus dibayar adalah 0")








