#Özyinelemeli Fonksiyonlar.
"""
Fonksiyonun içinde fonksiyonu tekrar çağırma işlemi
f f

"""
"""
5! = 5.4!
5! = 5.4.3!
5! = 5.4.3.2!
5! = 5.4.3.2.1!
1! = 1
x! = x*(x-1)!

"""

"""
F(n) = Eğer n = 0 F(0) = 0
F(n) Eğer n = 1 F(1) = 1
F(n) n>1 için F(n) = F(n-1) + F(n-2)
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

"""
n = 3
fib(3) = fib(2) + fib(1) [ 1 + 1]
fib(3-2) = 1
fib(3-1) = fib(2) [fib(1) + fib(0)] = [1+ 0] = 1

"""

for i in range(0, 10):
    print("{}.fibonacci terimi = {}".format(i, fib(i)))

#Ödev1 -----------------------------

x = int(input("Bir sayı giriniz : "))

sonuc = 1
for i in range(1,x+1): #[1 2 3 4 5]
    sonuc = sonuc * i
print(sonuc)

sonuc = x
for i in range(1, x):
    sonuc = sonuc * i
print(sonuc)

#Özyinelemeli fonksiyon (Recursive Function)

def f(x):
    if x == 1:
        return 1
    else:
        return x*f(x-1)

"""
5*f(4)->5*4*f(3)->5*4*3*f(2)->5*4*3*2*f(1)*5*4*3*2*1
"""
print(f(5))

#2.Yöntem

def g(x):
    return 1 if x == 1 else x*g(x-1)
print(g(5))

for i in range(1, 100):
    print(f"{i}! = {f(i)}")
