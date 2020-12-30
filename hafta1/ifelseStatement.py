#Girilen bir sayının çift mi yoksa tek mi olduğunu bulan bir program:

sayi = input("Bir sayı giriniz : ")
sayi = int(sayi)
# sayi kullanıcıdan alındı ve int (tam sayı) değerine çevrildi

#Çift ise sayi mod 2 = 0  mod = %
#Tek ise sayi mod 2 = 1

"""
Mantıksal Operatörler
== eşit mi?
> Büyük mü?
< Küçük mü?
<= Küçük eşit mi?
>= büyük eşit mi?
"""

"""
if sayi % 2 == 0:
    print("{} sayısı çifttir.".format(sayi))
else:
    print("{} sayısı tektir.".format(sayi))

"""

if sayi < 0:
    print("{} sayısı negatiftir".format(sayi))
elif sayi == 0:
    print("{} sayısı sıfıra eşit".format(sayi))
elif sayi == 5:
    print("{} sayısı beştir".format(sayi))
else:
    print("{} sayısı pozitiftir".format(sayi))


"""
Vücüt kitle endeksi
vki = ağırlık / (boy**2)
if elif 
18>vki zayıf
18<vki<25 normal
25<vki<30 kilolu
30<vki aşırı kilolu

"""



