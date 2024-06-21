def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi_naive(n):
    count = 1  
    for i in range(2, n):
        if gcd(i, n) == 1:
            count += 1
    return count

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

n = 10
print(f"Euler's Totient function for {n} is {phi(n)}")
