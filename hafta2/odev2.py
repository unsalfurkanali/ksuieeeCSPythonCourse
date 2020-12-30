puan = float(input("Notunuzu giriniz: "))
#dortluk = puan/25
puan = puan /25
if puan < 1:
    print("Başarısız")
elif puan>=1 and puan <2:
    print("daha çok çalışmalısın")
elif puan>=2 and puan<3:
    print("orta")
elif puan>=3 and puan<3.5:
    print("iyi")
elif puan>=3.5 and puan<=4:
    print("Çok iyi")


