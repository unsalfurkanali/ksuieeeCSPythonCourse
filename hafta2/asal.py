"""
Klaveyeden bir sayı okunur
Girilen sayı asal ile ekran bu sayı asaldır.
while for
x x/2+1
kalan not == asal
"""

x = int(input("Bir sayı giriniz : "))

"""
2 - x/2 olan sayılara kalansız bölünüyor mu? 
"""

##1.Yöntem
"""
k = True
for i in range(2, x//2):
    if x % i == 0:
        print("Bu sayı asal değildir")
        k = False
        break
if k == True:
    print("Bu sayı asaldır.")

"""

##2.Yöntem
for i in range(2, x//2):
    if x % i == 0:
        print("Bu sayı asal değildir")
        break
else:
    print("Bu sayı asaldır")




