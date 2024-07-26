import os
from math import gcd


def find_primitive_roots(n):
    if n == 1:
        return []

    
    phi = n - 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            phi -= 1

    
    primitive_roots = []
    for g in range(1, n):
        powers = set()
        for k in range(1, n):
            powers.add(pow(g, k, n))
        if len(powers) == n - 1:
            primitive_roots.append(g)
    
    return primitive_roots

def shut_down_system():
    if os.name == 'nt':  
        os.system("shutdown /s /t 1")

def alert_and_confirm_shutdown():
    confirm = input("The number entered is between 1000 and 2000. Do you want to shut down the system? (yes/no): ").strip().lower()
    if confirm == "yes":
        print("Shutting down the system...")
        shut_down_system()
    else:
        print("Shutdown canceled.")


def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if 1000 <= number <= 2000:
        alert_and_confirm_shutdown()
    else:
        primitive_roots = find_primitive_roots(number)
        if primitive_roots:
            print(f"Primitive roots of {number} are: {primitive_roots}")
        else:
            print(f"No primitive roots for {number}.")

if __name__ == "__main__":
    main()
