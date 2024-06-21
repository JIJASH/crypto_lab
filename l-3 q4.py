import random

def is_prime(n):
    """ Check if a number is prime """
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

def find_primitive_root(p):
    """ Find a primitive root for prime p """
    if not is_prime(p):
        return None
    phi = p - 1
    prime_factors = find_prime_factors(phi)
    for g in range(2, p):
        flag = True
        for factor in prime_factors:
            if pow(g, phi // factor, p) == 1:
                flag = False
                break
        if flag:
            return g
    return None

def find_prime_factors(n):
    """ Find all prime factors of n """
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def diffie_hellman_key_exchange(p, g):
    """ Perform Diffie-Hellman Key Exchange """
    # Private keys (chosen randomly)
    a = random.randint(1, p-2)
    b = random.randint(1, p-2)
    
    # Public keys
    A = pow(g, a, p)
    B = pow(g, b, p)
    
    # Shared secret keys
    shared_key_A = pow(B, a, p)
    shared_key_B = pow(A, b, p)
    
    return a, A, b, B, shared_key_A, shared_key_B

# Example usage
p = 17  # This should be a large prime number in real applications
g = find_primitive_root(p)
if g is not None:
    a, A, b, B, shared_key_A, shared_key_B = diffie_hellman_key_exchange(p, g)
    print(f"Prime number (p): {p}")
    print(f"Primitive root (g): {g}")
    print(f"Private key of Alice (a): {a}")
    print(f"Public key of Alice (A): {A}")
    print(f"Private key of Bob (b): {b}")
    print(f"Public key of Bob (B): {B}")
    print(f"Shared secret key computed by Alice: {shared_key_A}")
    print(f"Shared secret key computed by Bob: {shared_key_B}")
else:
    print(f"Could not find a primitive root for the prime number {p}")
