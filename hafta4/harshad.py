def rakamlarToplam(x):
    xStr = str(x)
    toplam = 0
    for i in range(len(xStr)):
        toplam = toplam + int(xStr[i])
    return toplam

def harshad(x):
    if x % rakamlarToplam(x) == 0:
        return True
    else:
        return False
toplam = 0
for i in range(1, 2000000):
    if harshad(i):
        print(f"{i} bir harsad sayısıdır")
        toplam += 1


print(f"0-200,000 arasında {toplam} kadar Harsad Sayısı Bulunmaktadır")





