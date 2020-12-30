""""
öğrenci numarası int
öğrenci adı  str (string)
öğrenci soyadı str
öğrenci notu float
ders
ogr

"""
blank = []      #Boş Liste oluşturma

#       0      1       2       3
ogr = [1234, "Ali", "Ünsal", 10.5]      #Eleman ile liste oluşturma
print(ogr[1])   #ogr listesindeki 2.indexli elemanı ekrana bastırma
print(ogr[2])

ogr[1] = "Mehmet"       #Index numarası ile liste içerisindeki veriler değiştirilebilir.
print(ogr[1])

#Dizi Liste

ogr.append("Matematik")         #Listeye yeni eleman eklemek için .append metodu kullanılır.
print(ogr)

print(len(ogr))

ogr.pop(2)      #Listeden x.indexteki elemanı silmek için .pop(x) kullanılır
print(ogr)
ogr.pop()       #Listeye son eklenen elemanı silmek için pop kullanılır.
print(ogr)

a = [0, 8, 10, 65, 1, 3]


a.sort()        #Listedeki elemanlar küçükten büyüğe sıralanıyor
print(a)    
a.sort(reverse=True)    #Elemanlar büyükten küçüğe sıralanıyor
print(a)

#-----------------------

a.append(input("Bir sayı giriniz"))
print(a)

a.append(float(input("Bir sayı giriniz : ")))
print(a)


b = input("Bir yazı giriniz")
a.append(b)
print(a)


ogrenci = []
ogrenci.append(input("Adı"))
ogrenci.append(input("Soyadı"))
ogrenci.append(int(input("Numarası")))

for i in ogrenci:
    print(i)
