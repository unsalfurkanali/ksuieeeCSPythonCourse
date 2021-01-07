"""
x : 2->x
x%6 == 0
"""


def asal(x):
    for i in range(2, x//2+1):#2 3 4 5 6 7 ... x
        if x % i == 0:
            return False
    return True

#1-100 arası asal sayıları ekrana yazdırma:
for i in range(2,100):
    if asal(i):
        print("{} asal bir sayıdır".format(i))

#Sophie Germen Asalı bulma
# p asal iken 2p+1 'de asal ise p sayısı bir Sophie Asalıdır.
count = 0
"""
AND
0 False
1 True

0 and 0 = 0
0 and 1 = 0
1 and 0 = 0
1 and 1 = 1

"""

for p in range(2, 100000):

    if asal(p) and asal(2*p+1):
        count = count + 1
        print("{} sayısı bir Sophie Asalıdır".format(p))

print("1-100000 arası {} adet Sophie Asalı vardır.".format(count))




