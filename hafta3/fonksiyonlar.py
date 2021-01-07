def kare(x):
    return x*x

a = kare(5)

print(a)

for i in range(10):
    print(kare(i))


## Kapsam Kavramı
# Global Değişken Yerel Değişken

x = 5   #Global

def xKac():
    x = 8   #Local Variable
    y = 6
    print(x)

xKac()
print(x)
#print(y)    #Hata verir

def selamlama(isim = "Belirtilmedi", soyisim = "!Belirtilmedi"):
    print("Merhaba", isim, soyisim)

selamlama("Ali")
selamlama(soyisim="Ünsal")

