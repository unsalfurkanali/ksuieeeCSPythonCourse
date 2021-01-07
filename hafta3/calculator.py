#Fonksiyon tanımlamaları 


def menu():
    print("******Hesap Makinesi******")
    print("İşlemler")
    print("1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n5-Üs Alma")
    islem = int(input("Yapılacak İşlemi Seçiniz : "))
    return islem

def toplam(sayi1, sayi2):
    return sayi1+sayi2

def cikarma(x, y):
    return x-y

def carpma(x, y):
    return x*y

def bol(x, y):
    return x/y

def usAl(x, y):
    return x**y



i = menu()

x1 = int(input("Bir sayı giriniz : "))
x2 = int(input("Bir sayı giriniz : "))

if i == 1:
    print(toplam(x1, x2))
elif i == 2:
    print(cikarma(x1, x2))
elif i == 3:
    print(carpma(x1, x2))
elif i == 4:
    print(bol(x1, x2))
elif i == 5:
    print(usAl(x1, x2))

