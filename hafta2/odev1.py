a = int(input("Bir sayı giriniz")) #str
b = int(input("Bir sayı giriniz"))
c = int(input("Bir sayı giriniz"))

max = a
min = b


if b > max:
    max = b
if c > max:
    max = c

if a < min:
    min = a
if c < min:
    min = c

print("En büyük sayı {} \nEn küçük sayı {}".format(max, min))
