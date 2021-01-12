"""
İngilizce-Türkçe
key value
"key" = "anahtar"
"car" = "araba"
"araba" = 5.6

"key":value

"""
sozluk = {
    "one":1,
    "two":2,
    "three":3,
    "four":4
}

try: #Hata olabilecek kodlar
    print(5/0)
    print(sozluk["seven"])
    print("Merhaba")
except KeyError:    #Hata yakalama bloğu
    print("!!Bu şekilde bir anahtar sözcük yoktur")
except ZeroDivisionError:
    print("Matematik Hatası")

sozluk2 = {
    "aylar":{
        "kış":["aralık", "ocak", "şubat"],
        "yaz":["haz", "tem", "ağus"]
    },
    "günler":{
        "hi":["pzt", "salı", "çar", "per", "cum"],
        "hs":["paz", "cmt"]
    }
}

print(sozluk2["aylar"]["kış"][0])

sozluk["one"] = 2
print(sozluk)
sozluk2["aylar"]["kış"][0] = "mayıs"
print(sozluk2)

aylar = {
    "ocak":1,
    "şubat":2,
    "mart":3,
    "nisan":4,
    "mayıs":5,
    "haziran":6
}
#key bilgisine erişim
for i in aylar.keys():
    print(i)

#value bilgisine erişim
for i in aylar.values():
    print(i)

#ikisi birlikte
for i,j in aylar.items():
    print(i, j)
