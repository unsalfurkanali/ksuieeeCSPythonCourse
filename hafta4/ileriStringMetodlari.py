"""
upper : Bütük karakterleri büyük harfe çevirir
lower : Bütün karakterleri küçük harfe çevirir
split(x) : x değerine göre str'yi böler
strip(x) istrip rstrip : x değerini siler
count(x) : str içindeki x ifadelerinin sayar.

"""

a = "Hello World"
print(a, a.upper(), a.lower())
a = a.lower()
print(a.split())
print(a.split("l"))

print(a.strip("d"))




