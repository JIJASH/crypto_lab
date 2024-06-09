import random

def miller_rabin(n, k):
    """
    Miller-Rabin primality test.

    Parameters:
    n : int
        The number to be tested for primality.
    k : int
        The number of rounds of testing to perform.

    Returns:
    bool
        True if n is probably prime, False if n is composite.
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Write n as d * 2^r + 1 with d odd (by factoring out powers of 2 from n - 1)
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

# Example usage:
n = 17  # Number to test
k = 5   # Number of iterations
if miller_rabin(n, k):
    print(f"{n} is probably prime.")
else:
    print(f"{n} is composite.")
