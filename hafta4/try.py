sozluk = {
    "bir":1,
    "iki":2,
    "üç":3
}

dic = {
    "mevsimler":{
        "kış":"soğuk",
        "yaz":"sıcak"
    },
    "aylar":{
        "haziran":"yaz",
        "aralık":"kış"
    }
}

print(sozluk["bir"])
print(dic["aylar"]["haziran"])

for i,j in sozluk.items():
    print(i,j)


paragraph = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"""

words = paragraph.lower().split()

for i in words:
    print(i)

onlyWords = []
for i in words:
    i = i.strip("\n")
    i = i.strip(" ")
    i = i.strip(".")
    i = i.strip(",")

    onlyWords.append(i)

for i in onlyWords:
    print(i)

freq = {}
for i in onlyWords:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i,j in freq.items():
    print(f"{i} kelimesi {j} defa geçiyor")

def f(x):
    return 1 if x == 0 or x == 1 else x*f(x-1)

def comb(n,r):
    return f(n)/(f(r)*f(n-r)) if n >= r else -1 

print(comb(4,3))

