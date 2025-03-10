import math

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1: return d
    return None

def is_prime(num):
    if num <= 1: return False
    if num <= 3: return True
    if num % 2 == 0 or num % 3 == 0: return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0: return False
        i += 6
    return True

def rsa():
    choice = int(input("Choose operation:\n1. RSA with custom values\n2. RSA with p=7, q=11, e=17, M=8\n"
                       "3. RSA with p=3, q=11, e=7, M=5\n4. Decrypt C=20 with e=13, n=77\nEnter choice (1-4): "))
    
    if choice == 1:
        p = int(input("Enter prime number p: "))
        q = int(input("Enter prime number q: "))
        e = int(input("Enter public exponent e: "))
        M = int(input("Enter message M: "))
    elif choice == 2:
        p, q, e, M = 7, 11, 17, 8
        print(f"Using p={p}, q={q}, e={e}, M={M}")
    elif choice == 3:
        p, q, e, M = 3, 11, 7, 5
        print(f"Using p={p}, q={q}, e={e}, M={M}")
    elif choice == 4:
        C, e, n = 20, 13, 77
        print(f"Attempting to decrypt C={C} with e={e}, n={n}")
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                p, q = i, n // i
                if is_prime(p) and is_prime(q): break
        
        print(f"Found factors: p={p}, q={q}")
        phi = (p - 1) * (q - 1)
        d = mod_inverse(e, phi)
        M = pow(C, d, n)
        print(f"Decrypted message: {M}")
        return
    else:
        print("Invalid choice")
        return
    
    if not (is_prime(p) and is_prime(q)):
        print("Both p and q must be prime numbers")
        return
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    if gcd(e, phi) != 1:
        print(f"Invalid e={e}. It must be coprime with phi={phi}")
        return
    
    d = mod_inverse(e, phi)
    C = pow(M, e, n)
    M_decrypted = pow(C, d, n)
    
    print(f"\nRSA Parameters:\np = {p}, q = {q}\nn = p * q = {n}\nphi(n) = (p-1) * (q-1) = {phi}")
    print(f"Public key (e, n) = ({e}, {n})\nPrivate key (d, n) = ({d}, {n})")
    print(f"\nOriginal message M = {M}\nEncrypted message C = M^e mod n = {M}^{e} mod {n} = {C}")
    print(f"Decrypted message = C^d mod n = {C}^{d} mod {n} = {M_decrypted}")
    
    print("\nDecryption successful: Original message recovered correctly!" if M == M_decrypted else "\nDecryption failed: Original message not recovered.")

if __name__ == "__main__":
    rsa()