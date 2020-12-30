#a = 5
#b = 6
# int a int b gibi veri tipi ile tanımlama yapılmaz
"""
Herhangi bir değişken tanımlamak istiyorsak ona göre atama yapabiliriz direkt olarak veya a = 0 veya b = 6.0 gibi
belirgin olacak şekilde tanımlarız.
Veya a ve b tanımlı iki sayı ise
c = a+b
şeklinde daha önceden tanımlanmamış bir değişken ismini kullanarak değişken oluşturabiliriz.

"""
# Yorum Satırı # işareti ile başlayan satırlar programın akışını etkilemez

#c = a + b

#format Değişken değerini ekrana bastırmak için kullanılır
#print  Ekrana yazı yazdırmak için

#print("a+b = {}".format(c))

#print("a-b = {}, a*b = {}".format(a-b, a*b))
"""
print("IEEE")
print("{}".format(5))
a = 10
print(a, "IEEE")
"""

#scanf("%d", &a)
#input() Kullanıcıdan bilgi almak için kullanılır.
#input ile kullanıcıdan bilgi alırken bir bilgilendirme mesajı yazmak için input("Mesaj") şeklinde kullanabilirsiniz
"""
input ile kullanıcıdan alınan tüm veriler öncelikle str yani string veri tipinde saklanır. Bu durumda bizim girilen
ifadeyi kullanacak olduğumuz veri tipine çevirmemiz gerekir. Bunu da tip dönüştürme ile yapabilir. 
Python'da tip dönüşümü oldukça basittir. Birbirine çevrilebilecek tipler arasında geçiş şu şekilde olur:
a bir str olsun ve içinde "5" olsun. Burada a bir sayı değil bir karakter dizisi olan strdir. Bunu işlemlerde kullanamayız
ancak bu a değişkenini şu şekilde tam sayıya çevirebiliriz; int(a) veya float veri tipine çevirmek istiyorsak; float(a)
kullanmamız yeterli.
"""

a = input()
#str çevirir.
print(a)
print(type(a))

#type fonksiyonu değişkeninin veri tipini ekrana yazdırmak için kullanılır (int, float, str, list vb)

""""
a = int(input())
"""
""""
a = input()
a = int(a)
c = a + 5
print(c)
"""

c = float(input("Bir sayı giriniz"))
print(c)