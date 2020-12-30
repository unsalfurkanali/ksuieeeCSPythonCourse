hesapNo = 1234
sifre = 1234
para = 250
krediKartLimit = 100

girilenHesapNo = int(input("Hesap numaranızı giriniz : "))
girilenSifre = int(input("Şifrenizi giriniz : "))

#Bool True 1 False 0

if girilenHesapNo == hesapNo:
    while True:
        if girilenSifre == sifre:
            print("Bakiye = {}\nKredi Kart Limiti = {}".format(para, krediKartLimit))
            break
        else:
            print("Şifreniz yanlış!")
            girilenSifre = int(input("Şifrenizi giriniz : "))
else:
    print("Hesap numarası yanlış")




