kilo = int(input("Kilonuzu giriniz : "))
uzunluk = float(input("Boyunuzu giriniz : "))
"""
Vücüt kitle endeksi
vki = ağırlık / (boy**2)
if elif 
18>vki zayıf
18<vki<25 normal  vki>18 vki<25
25<vki<30 kilolu vki>25 and vki<30
30<vki aşırı kilolu

"""
vki = kilo / (uzunluk**2)

if vki<18:
    print("Zayıf {}".format(vki))
elif vki>18 and vki<25:
    print("Normal {}".format(vki))
elif vki>25 and vki<30:
    print("Kilolu {}".format(vki))
elif vki>30:
    print("Aşırı Kilolu {}".format(vki))
    

