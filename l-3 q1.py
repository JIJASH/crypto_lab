import random

def miller_rabin(n, k):
  
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

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

n= int(input('Enter the number : '))
k = int (input('Enter the number of iterations : '))
if miller_rabin(n, k):
    print(f"{n} is probably prime.")
else:
    print(f"{n} is composite.")
