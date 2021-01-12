#Faktoriyel hesaplama fonksiyonu
#C(3,3)
def f(x):
    if x == 1:
        return 1
    elif x == 0: #0!=1
        return 1
    else:
        return x*f(x-1)

"""
C(n,r) = n!/(r!*(n-r)!)
P(n,r) = n!/(n-r)!
n>=r olmalı
"""

def combination(n, r):
    if n>=r:
        return f(n)/(f(r)*f(n-r))
    else:
        return -1

def permutation(n, r):
    return f(n)/f(n-r) if n >= 0 else -1

print(combination(10, 6))
print(permutation(10, 5))
