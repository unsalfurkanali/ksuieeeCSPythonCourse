#Odev1
#------------------------------------------------------------------


x = int(input("Bir sayı giriniz : "))
tamBolenler = []

for i in range(2, x):
    if x % i == 0:
        for j in range(1, x):
            if x % j == 0:
                tamBolenler.append(j)
        print("Bu sayının tam bölenleri = ", tamBolenler)
        break
else:
    print("Bu sayı asaldır")


#Odev2
#------------------------------------------------------------------


while True:
    ogr = []
    ogr.append(input("Öğrencinin Adını Giriniz : "))
    ogr.append(input("Öğrencinin Soyadını Giriniz : "))
    ogr.append(int(input("Öğrencinin Numarasını Giriniz : ")))
    ogr.append(input("Öğrencinin Bölümünü Giriniz : "))
    ogr.append(int(input("Öğrencinin Sınıfını Giriniz : ")))
    ogr.append(float(input("Öğrencinin Not Ortalamasını Giriniz : ")))
    for i in ogr:
        print(i)

#Odev3
#------------------------------------------------------------------


a = []
size = 10
for i in range(size):
    a.append(int(input("{}.sayıyı giriniz : ".format(i+1))))

print("Sıralanmamış Liste : ", a)
#5, 3, 6, 10, 63, 56, 25, 15, 67, 32
#j = 0
for k in range(1, size):
    for j in range(0, size-1):
        # 1 3 6 2
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Sıralanmış Liste : ", a)


#Odev4
#------------------------------------------------------------------
a = []
size = 10

#Sayıları Klavyeden okunuyor
for i in range(size):
    a.append(int(input("{}.sayıyı giriniz : ".format(i+1))))

maxValue = 0    #Mod elemanı tutmak için
maxCount = 0    #Mod sayısını tutmak için kullanılacak
# a = 5 6 2 6 3
#i = 0
#j = 2
#count = 0

#Mod bulma
for i in range(0, size):
    count = 0
    for j in range(0, size):
        if a[j] == a[i]:
            count = count + 1

        if count > maxCount:
            maxCount, maxValue = count, a[i]

print("Mod = {}".format(maxValue))

total = 0
for i in range(size):
    total = total + a[i]
mean = total / size
print(mean)

for k in range(1, size):
    for j in range(0, size-1):
        # 1 3 6 2
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

#Median # 2 5 8 10 12 7//2=3
if len(a) % 2 == 0:
    median = (a[len(a)//2-1]+a[size//2+1])/2
else:
    median = a[size//2]
