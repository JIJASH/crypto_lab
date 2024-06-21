def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def is_primitive_root(g, p):
    if gcd(g, p) != 1:
        return False
    required_set = {num for num in range(1, p)}
    actual_set = set()
    for power in range(1, p):
        actual_set.add(pow(g, power, p))
        if len(actual_set) == p - 1:
            break
    return required_set == actual_set

def find_primitive_roots(p):
    if not is_prime(p):
        return f"{p} is not a prime number."
    primitive_roots = []
    phi = p - 1
    prime_factors = find_prime_factors(phi)
    for g in range(2, p):
        flag = True
        for factor in prime_factors:
            if pow(g, phi // factor, p) == 1:
                flag = False
                break
        if flag:
            primitive_roots.append(g)
    return primitive_roots

p = 23  
primitive_roots = find_primitive_roots(p)
print(f"Primitive roots of {p}: {primitive_roots}")
