def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi_naive(n):
    count = 1  # 1 is always relatively prime to any number
    for i in range(2, n):
        if gcd(i, n) == 1:
            count += 1
    return count

def phi(n):
    result = n
    p = 2
    # Check for all prime factors of n
    while p * p <= n:
        # Check if p is a prime factor
        if n % p == 0:
            # If yes, then update n and result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    # If n has a prime factor greater than sqrt(n)
    if n > 1:
        result -= result // n
    return result

# Test the function
n = 10
print(f"Euler's Totient function for {n} is {phi(n)}")
