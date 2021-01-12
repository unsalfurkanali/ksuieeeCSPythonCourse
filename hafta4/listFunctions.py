aylar = ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran"]
aySayilari = [1, 2, 3, 4, 5, 6, 7]

#zip fonksiyonu
sirali = zip(aylar, aySayilari)

for i in sirali:
    print(i)

en = enumerate(aylar)

for i in en:
    print(i)
